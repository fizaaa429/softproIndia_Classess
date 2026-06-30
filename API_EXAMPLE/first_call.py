from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant"
        },
        {
            "role": "user",
            "content": "Explain what an API is in 1 line"
        }
    ]
)

print(response.choices[0].message)

#once client ob that tails to the API
client = Groq(api_key=api_key)

client.chat.completions.create(
    model = "llama-3.1-8b-instant",
    messages = [
        {"role":"user","contant":"explain what is full stack devlopement"}
    ]
)

print("model's response")
print(response.choice[0].message.content)

