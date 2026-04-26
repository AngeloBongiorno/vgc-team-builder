import dotenv 
import os
from openai import OpenAI

dotenv.load_dotenv()

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
