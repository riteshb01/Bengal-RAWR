from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="How does api work"
)

print(response.text)