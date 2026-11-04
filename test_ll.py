
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Send a message to the LLM
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Explain what an AI research agent is in simple terms."
        }
    ]
)

# Extract and print the response
answer = response.choices[0].message.content

print(answer)
