import os
from dotenv import load_dotenv
from groq import Groq
from models import get_groq_model

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("❌ Error: GROQ_API_KEY is not set in .env file.")
    print("Please add your key to Cloud LLM/.env")
    exit(1)

client = Groq(api_key=api_key)

model = get_groq_model()
print(f"🚀 Sending request to Groq ({model})...")

try:
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Explain AI agents in 2 concise sentences."
            }
        ]
    )
    print("\n--- Groq Response ---")
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"❌ Error communicating with Groq: {e}")


