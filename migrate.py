import os
import sys
import requests
from bs4 import BeautifulSoup

# Define a blacklist of strings to remove from titles
blacklist = ["| Spotify", "abc"]

def get_file_content():
    """Fetches the content of the file containing a list of URLs."""
    if not sys.stdin.isatty():
        return sys.stdin.read().strip().splitlines()
    else:
        file_path = input("Enter the path to the file containing URLs: ").strip()
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            sys.exit(1)
        with open(file_path, 'r') as file:
            return file.read().strip().splitlines()

def clean_title(title):
    """Removes unwanted strings from the title based on the blacklist."""
    for blacklisted in blacklist:
        title = title.replace(blacklisted, "")
    return title.strip()

def fetch_title(url):
    """Fetches the title of the webpage at the given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "(no title)"
        return clean_title(title)
    except requests.RequestException as e:
        return f"Error: {e}"

def main():
    """Main function of the script."""
    if not sys.stdin.isatty():
        input_file = "stdin"
        urls = sys.stdin.read().strip().splitlines()
    else:
        input_file = input("Enter the path to the file containing URLs: ").strip()
        if not os.path.exists(input_file):
            print(f"File {input_file} does not exist.")
            sys.exit(1)
        with open(input_file, 'r') as file:
            urls = file.read().strip().splitlines()

    output_file = f"{input_file}_titles" if input_file != "stdin" else "output_titles.txt"

    with open(output_file, 'w') as out_file:
        for url in urls:
            if not url.strip():
                continue
            title = fetch_title(url)
            print(title)
            out_file.write(title + "\n")

if __name__ == "__main__":
    main()
