# notes.py
import os
from dotenv import load_dotenv

def load_folders_from_env():
    """Loads the directory from .env and returns list of folder names."""
    load_dotenv()

    directory_path = os.getenv('DIRECTORY_PATH')
    if directory_path and os.path.isdir(directory_path):
        return [name for name in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, name))]
    else:
        return []

if __name__ == "__main__":
    # For testing purposes
    print("Folders in Notes:")
    print(load_folders_from_env())
