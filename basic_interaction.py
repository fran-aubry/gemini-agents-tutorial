from dotenv import load_dotenv
from google import genai

# Load secure environment variables
load_dotenv()

# Initialize the GenAI Client
client = genai.Client()

# Create a basic interaction with a managed agent
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Install the matplotlib package, verify its version, and report back.",
    environment="remote"
)

# Output the status of the agent
print(f"Status: {interaction.status}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output:\n{interaction.output_text}")
