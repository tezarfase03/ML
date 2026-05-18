import json
import os
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

def download_notebook_from_github(github_url, output_dir=None):
    """
    Download a Jupyter notebook from GitHub and save it locally.

    Args:
        github_url: URL to the notebook on GitHub (e.g.,
                   https://github.com/user/repo/blob/main/notebook.ipynb)
        output_dir: Directory to save the notebook (default: current directory)

    Example:
        download_notebook_from_github(
            'https://github.com/anthropics/anthropic-sdk-python/blob/main/example.ipynb'
        )
    """

    # Convert GitHub web URL to raw content URL
    # https://github.com/user/repo/blob/main/path/notebook.ipynb
    # becomes
    # https://raw.githubusercontent.com/user/repo/main/path/notebook.ipynb

    if 'github.com' not in github_url:
        print("❌ Error: Please provide a valid GitHub URL")
        return

    # Extract parts from URL
    try:
        parts = github_url.replace('https://github.com/', '').split('/')
        username = parts[0]
        repo = parts[1]
        # Skip 'blob' at parts[2]
        branch = parts[3]
        notebook_path = '/'.join(parts[4:])

        raw_url = f"https://raw.githubusercontent.com/{username}/{repo}/{branch}/{notebook_path}"

    except IndexError:
        print("❌ Error: Invalid GitHub URL format")
        print("Expected: https://github.com/user/repo/blob/branch/path/notebook.ipynb")
        return

    # Download the notebook
    print(f"📥 Downloading from: {raw_url}")

    try:
        with urlopen(raw_url) as response:
            notebook_data = json.loads(response.read().decode('utf-8'))
    except URLError as e:
        print(f"❌ Error downloading: {e}")
        return
    except json.JSONDecodeError:
        print("❌ Error: Downloaded file is not a valid Jupyter notebook")
        return

    # Get filename from URL
    filename = notebook_path.split('/')[-1]

    # Create output directory if specified
    if output_dir:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        filepath = os.path.join(output_dir, filename)
    else:
        filepath = filename

    # Save the notebook
    try:
        with open(filepath, 'w') as f:
            json.dump(notebook_data, f, indent=1)
        print(f"✅ Notebook saved to: {filepath}")
    except IOError as e:
        print(f"❌ Error saving file: {e}")
        return

    return filepath


if __name__ == "__main__":
    # Get input from user
    url = input("📌 Enter GitHub notebook URL: ").strip()

    output_dir = input("📁 Enter output directory (press Enter for current dir): ").strip()
    if not output_dir:
        output_dir = None

    download_notebook_from_github(url, output_dir)
