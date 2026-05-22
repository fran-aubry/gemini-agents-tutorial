import requests
from dotenv import load_dotenv
import os
import tarfile


load_dotenv()


def read_text_file(path):
  with open(path, "rt") as f:
    return f.read() 
  

def download_env(env_id, path="environments"):
    download_url = f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download"
    try:
        request_params = {"alt": "media"}  # Retrieves raw media binary
        request_headers = {"x-goog-api-key": os.environ.get("GEMINI_API_KEY")}
        # Download the environment
        print(f"Downloading enviroment: {env_id}")
        response = requests.get(
            download_url,
            params=request_params,
            headers=request_headers,
            allow_redirects=True
        )
        response.raise_for_status()
        # Save the compressed workspace archive locally
        archive_name = f"{env_id}.tar"
        output_path = os.path.join(path, archive_name)
        with open(output_path, "wb") as archive_file:
            archive_file.write(response.content)
        print(f"Successfully downloaded workspace snapshot archive: {output_path}")     
    except requests.exceptions.RequestException as error:
        print(f"Failed to download sandbox workspace via HTTP request: {error}")
    except tarfile.TarError as archive_error:
        print(f"Failed to unpack download tarball: {archive_error}")


def load_or_create_agent(client, agent_id):
    try:
        # Try to retrieve the existing agent
        agent = client.agents.get(id=agent_id)
        print("Found existing agent.")
    except:
        # If not found, create it
        agent = client.agents.create(
            id=agent_id,
            base_agent="antigravity-preview-05-2026",
            base_environment={
                "type": "remote",
                "sources": [
                    # Explicitly load the persona
                    {
                        "type": "inline", 
                        "target": ".agents/AGENTS.md", 
                        "content": read_text_file(".agents/AGENTS.md")
                    },
                    # Explicitly load the skill
                    {
                        "type": "inline", 
                        "target": ".agents/skills/csv-aggregator/SKILL.md", 
                        "content": read_text_file(".agents/skills/csv-aggregator/SKILL.md")
                    },
                    {
                        "type": "repository",
                        "source": "https://github.com/fran-aubry/gemini-agents-tutorial",
                        "target": "/workspace/repository"
                    }
                ]
            }
        )
    return agent
