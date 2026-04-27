from typing import Any
import dotenv 
import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageToolCall, ChatCompletionUserMessageParam
from logger import logger
from utils import load_system_prompt
from tools import tools, available_tools_guidance, dispatch_tool_call
from team import Team

dotenv.load_dotenv()
regulation = "this is a mock regulation, for testing purposes only, the system is not in prod yet"
current_team: Team = Team(format=regulation)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def ask_agent(messages: list[Any]) -> None:
    global current_team
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        user_message: ChatCompletionUserMessageParam = {
            "role": "user",
            "content": user_input
        }
        messages.append(user_message)

        while True: 

            try:
                response = client.chat.completions.create(
                    model="google/gemma-4-26b-a4b-it:free",
                    messages=[
                        {
                            "role": "system",
                            "content": load_system_prompt(
                                "source/prompts/system_prompt.md",
                                team=str(current_team),
                                regulation=regulation,
                                tools_usage_guidelines_list=available_tools_guidance
                                )
                        },
                        *messages],
                    tools=tools
                )
                logger.debug(f"API call | model={response.model} | tokens={response.usage}")
                if not response.choices:
                    logger.error(f"Empty response from API: {response}")
                assistant_message = response.choices[0].message
            except Exception as e:
                logger.error(f"API call failed: {e}")
                break

            messages.append(assistant_message)
            logger.info(f"Assistant response | length={len(assistant_message.content or '')}")

            tool_calls = response.choices[0].message.tool_calls
            if not tool_calls:
                print(f"\n- Assistant: {assistant_message.content}")
                break
            for tool_call in tool_calls:
                if not isinstance(tool_call, ChatCompletionMessageToolCall):
                    logger.error(f"Received tool call that is not of type ChatCompletionMessageToolCall: ({tool_call}), skipping...")
                    continue
                function_name = tool_call.function.name
                arguments = tool_call.function.arguments
                logger.info(f"Tool call name: {function_name} | args: {arguments}")
                current_team, tool_call_response = dispatch_tool_call(function_name, arguments, current_team)
                logger.debug(f"Tool result | {tool_call_response[:200]}")
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_call_response
                })
        
        print("*** CURRENT TEAM STATE ***")
        print(current_team)
        print("**************************")
        print("\n")

if __name__ == "__main__":
    initial_messages: list[Any] = []
    ask_agent(initial_messages)
