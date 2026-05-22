import requests
from dotenv import load_dotenv
import os
import tarfile


load_dotenv()


def read_text_file(path):
  with open(path, "rt") as f:
    return f.read() 
  

def download_env(env_id):
    download_url = f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download"
    try:

        request_params = {"alt": "media"}  # Retrieves raw media binary
        request_headers = {"x-goog-api-key": os.environ.get("GEMINI_API_KEY")}

        # Perform the direct GET download request
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
        with open(archive_name, "wb") as archive_file:
            archive_file.write(response.content)
        print(f"Successfully downloaded workspace snapshot archive: {archive_name}")
        
    except requests.exceptions.RequestException as error:
        print(f"Failed to download sandbox workspace via HTTP request: {error}")
    except tarfile.TarError as archive_error:
        print(f"Failed to unpack download tarball: {archive_error}")


if __name__ == "__main__":
    env_id = "529b3af5-31de-4027-b393-0b709106db0e"
    download_env(env_id)