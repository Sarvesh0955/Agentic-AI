import os
from dotenv import load_dotenv
from google import genai
from models import get_gemini_model

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ Error: GEMINI_API_KEY is not set in .env file.")
    print("Please add your key to Cloud LLM/.env")
    exit(1)

client = genai.Client(api_key=api_key)

model = get_gemini_model()
print(f"🚀 Sending request to Google Gemini ({model})...")

try:
    response = client.models.generate_content(
        model=model,
        contents="Explain AI agents in 2 concise sentences."
    )
    print("\n--- Gemini Response ---")
    print(response.text)
except Exception as e:
    print(f"❌ Error communicating with Gemini: {e}")

