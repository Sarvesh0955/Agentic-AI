import os
from dotenv import load_dotenv
from openai import OpenAI

# Paid

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain what an API is in simple terms."}
    ]
)

print(response.choices[0].message.content)