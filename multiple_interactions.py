from dotenv import load_dotenv
from google import genai

# Load secure environment variables
load_dotenv()

# Initialize the GenAI Client
client = genai.Client()

# Create a basic interaction with a managed agent

# First interaction
inter1 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script `sum.py` that adds all integers from 1 to 100.",
    environment="remote"
)

# Second interaction
inter2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=inter1.id, # Passes the conversation history
    environment=inter1.environment_id, # Keeps the exact same filesystem state
    input="Execute 'sum.py' using Python and display the standard output."
)

# Output the status of the agent
print(f"Output:\n{inter2.output_text}")
