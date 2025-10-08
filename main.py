import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
]
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if sys.argv[1] == None:
    
    print("Prompt is missing.")
    sys.exit(1)


response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)

if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
    print(f"User prompt: {sys.argv[1]}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    print(response.text)
