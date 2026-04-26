import dotenv 
import os
from openai import OpenAI
from utils import load_system_prompt
from tools import available_tools_guidance

dotenv.load_dotenv()


regulation = "this is a mock regulation, for testing purposes only, the system is not in prod yet"

system_prompt = load_system_prompt(
    "system_prompt.md",
    tools_usage_guidelines_list=available_tools_guidance,
    regulation=regulation
)


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
completion = client.chat.completions.create(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    messages=[
      {
        "role": "user",
        "content": "Pick a color, green or blue?"
      }
    ]
)

print(completion.choices[0].message.content)
