import os
from dotenv import load_dotenv
from google import genai
import utils

# Load secure environment variables
load_dotenv()

# Initialize the GenAI Client
client = genai.Client()

inter = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Add all the numbers in the `/workspace/numbers.txt` file.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                # The file where to store the data in the agent environment
                "target": "/workspace/numbers.txt",
                # Assumes that the file data/numbers.txt exists
                "content": utils.read_text_file("data/numbers.txt")
            }
        ]
    }
)

print(f"Status: {inter.status}")
print(f"Environment ID: {inter.environment_id}")
print(f"Output:\n{inter.output_text}")