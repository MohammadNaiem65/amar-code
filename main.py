import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')

if not api_key:
    raise RuntimeError("`GEMINI_API_KEY` is not found.")

# Create genai client
client = genai.Client(api_key=api_key)

# Setup argparse
arg_parser = argparse.ArgumentParser(description="Amar Code CLI")

# Set arguments
arg_parser.add_argument("prompt", type=str, help="User prompt.")
arg_parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

# Parse arguments
args = arg_parser.parse_args()

prompt = args.prompt
verbose = args.verbose

# Messages
messages: list[types.Content] = [
    types.Content(role="user", parts=[types.Part(text=prompt)])
]

response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

if response.usage_metadata is None:
    raise RuntimeError("Request failed as `usage_metadata` not found.")

prompt_token = response.usage_metadata.prompt_token_count
response_token = response.usage_metadata.candidates_token_count

if verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {prompt_token}")
    print(f"Response tokens: {response_token}")
    
print(response.text)
