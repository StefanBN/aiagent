import os
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    print("Hello from aiagent!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("API key is empty...")

    parser = argparse.ArgumentParser(description='Chatbot')
    parser.add_argument('prompt', type=str, help='User prompt')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.prompt)])
    ]

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model='gemini-3.1-flash-lite', contents=messages)

    if args.verbose:
        print(f'User prompt: {args.prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    else:
        print(response.text)

if __name__ == "__main__":
    main()
