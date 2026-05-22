from dotenv import load_dotenv
from google import genai
import utils

load_dotenv()
client = genai.Client()

# Load the agent
data_analyst = utils.load_or_create_agent(client, "data-analyst-agent")
print(f"Agent '{data_analyst.id}' initialized.")

# Install matplotlib package
inter1 = client.interactions.create(
    agent=data_analyst.id,
    input="Install the `matplotlib` package.",
    environment="remote"
)

# Ask to use the skill to get the top 10 genres
inter2 = client.interactions.create(
    agent=data_analyst.id,
    input="Use the csv-aggregator to plot the top 10 genres from `/workspace/repository/data/netflix.csv` in terms of viewership",
    environment=inter1.environment_id
)

print(f"Status: {inter2.status}")
print(f"Output:\n{inter2.output_text}")

inter3 = client.interactions.create(
    agent=data_analyst.id,
    input="Execute the `genres.py` script using python.",
    environment=inter2.environment_id
)

utils.download_env(inter3.environment_id)