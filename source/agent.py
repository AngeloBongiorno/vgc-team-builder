from typing import Any
import dotenv 
import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageToolCall, ChatCompletionUserMessageParam
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
            response = client.chat.completions.create(
                model="nvidia/nemotron-3-super-120b-a12b:free",
                messages=[{"role": "system", "content": load_system_prompt("source/prompts/system_prompt.md", team=str(current_team), regulation=regulation, tools_usage_guidelines_list=available_tools_guidance)}, *messages],
                tools=tools
            )
            assistant_message = response.choices[0].message
            messages.append(assistant_message)

            tool_calls = response.choices[0].message.tool_calls
            if not tool_calls:
                print(f"\n- Assistant: {assistant_message.content}")
                break
            for tool_call in tool_calls:
                if not isinstance(tool_call, ChatCompletionMessageToolCall):
                    print("\n- Received tool call that is not of type ChatCompletionMessageToolCall, skipping...")
                    continue
                function_name = tool_call.function.name
                arguments = tool_call.function.arguments
                current_team, tool_call_response = dispatch_tool_call(function_name, arguments, current_team)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_call_response
                })
        
        print("*** CUURRENT TEAM STATE ***")
        print(current_team)
        print("**************************")

if __name__ == "__main__":
    initial_messages: list[Any] = []
    ask_agent(initial_messages)
