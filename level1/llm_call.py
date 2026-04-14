import os
import dotenv
import google.genai

dotenv.load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")
client = google.genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)

print(response.text) 
