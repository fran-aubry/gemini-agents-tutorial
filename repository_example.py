import os
from dotenv import load_dotenv
from google import genai
import utils

# Load secure environment variables
load_dotenv()

# Initialize the GenAI Client
client = genai.Client()

inter1 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Add all the numbers in the `/workspace/repository/numbers.txt` file.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/fran-aubry/gemini-agents-tutorial",
                "target": "/workspace/repository"
            }
        ]
    }
)

print(f"Status: {inter1.status}")
print(f"Environment ID: {inter1.environment_id}")
print(f"Output:\n{inter1.output_text}")