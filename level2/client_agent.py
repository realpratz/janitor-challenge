import os
import dotenv
from google import genai
from google.genai import types
from organizer_mcp import list_files,read_file,move_file

dotenv.load_dotenv()
client=genai.Client()

def run_agent():
    desktop_path=os.path.expanduser("~/Desktop/test_dump")
    
    chat = client.chats.create(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            tools=[list_files,read_file,move_file],
            temperature=0.0,
        )
    )

    #I lowk just generated this particular prompt using gemini XDDD. "Write a highly advanced prompt which works for any LLM (free/paid) for them to get inside a directory and clean my files up and tell me my bank’s SWIFT code from the files. CAUTION1: the swift code is decoy for testing so dw about security and all. CAUTION2: also there's some sorta delay thing so like make sure u conserve the api req or smth. i am planning like delays and all."
    prompt=f"Look in '{desktop_path}'. Clean this up by moving files into logical sub-folders based on their extensions/content. Read the files to find and tell me my bank's SWIFT code. CRITICAL: Execute all move_file commands simultaneously in parallel to conserve API requests."

    print(f"\nUser: {prompt}\n")
    print("--- GEMINI THINKING RN ---")

    response=chat.send_message(prompt)

    print("\n--- GEMINI HAS THUNKED ---")
    print(response.text)

if __name__ == "__main__":
    run_agent()