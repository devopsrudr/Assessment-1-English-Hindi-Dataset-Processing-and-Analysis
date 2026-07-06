"""
download_dataset.py
--------------------
Downloads the gated Hugging Face dataset `ainlpml/english-hindi` into
./data/ (eng.txt, hin.txt). This is the same script used to originally
obtain the raw data for this project — included here so the pipeline is
fully reproducible from scratch.

SETUP (one time):
1. Log in / sign up: https://huggingface.co/join
2. Visit https://huggingface.co/datasets/ainlpml/english-hindi and click
   "Agree and access repository"
3. Create a Read token: https://huggingface.co/settings/tokens
4. Open the ".env" file in this folder and paste your token there, replacing
   "paste_your_token_here".

HOW TO RUN:
    pip install huggingface_hub python-dotenv
    python download_dataset.py
"""

import os
import sys
from dotenv import load_dotenv
from huggingface_hub import snapshot_download, login

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

REPO_ID = "ainlpml/english-hindi"
REPO_TYPE = "dataset"
LOCAL_DIR = os.path.join(PROJECT_ROOT, "data")


def main():
    load_dotenv(os.path.join(SCRIPT_DIR, ".env"))
    token = os.environ.get("HF_TOKEN")

    if not token or token == "paste_your_token_here":
        print("ERROR: No valid HF_TOKEN found.")
        print("Open the '.env' file in this folder and paste your Hugging "
              "Face token there.")
        sys.exit(1)

    print("Logging in to Hugging Face...")
    login(token=token)

    print(f"Downloading '{REPO_ID}' into {LOCAL_DIR} ...")
    try:
        local_path = snapshot_download(
            repo_id=REPO_ID, repo_type=REPO_TYPE, local_dir=LOCAL_DIR,
        )
        print(f"Done! Files downloaded to: {local_path}")
    except Exception as e:
        print(f"DOWNLOAD FAILED: {e}")
        print(
            "Make sure you clicked 'Agree and access repository' on the "
            "dataset page (same account as your token)."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
