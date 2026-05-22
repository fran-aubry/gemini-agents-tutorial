from dotenv import load_dotenv
from google import genai
import utils

load_dotenv()
client = genai.Client()

# 1. Register the Agent
# The agent will automatically detect the /.agents/ folder inside the repository
data_analyst = utils.load_or_create_agent(client, "data-analyst-agent")

print(f"Agent '{data_analyst.id}' initialized.")

# 2. Interact
inter1 = client.interactions.create(
    agent=data_analyst.id,
    input="Install the `matplotlib` package.",
    environment="remote"
)

env_id = inter1.environment_id

# The agent will automatically recognize and use the netflix-viz skill
# from the repository for this request.
inter2 = client.interactions.create(
    agent=data_analyst.id,
    input="Use the csv-aggregator to plot the top 10 genres from `/workspace/repository/data/netflix.csv` in terms of viwership",
    environment=env_id
)

print(f"Status: {inter2.status}")
print(f"Output:\n{inter2.output_text}")

inter3 = client.interactions.create(
    agent=data_analyst.id,
    input="""
    Execute the `genres.py` script using python.
    """,
    environment=env_id
)

utils.download_env(inter3.environment_id)