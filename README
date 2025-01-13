# Fetch Titles Script

## Overview
This script fetches the titles of webpages from a list of URLs provided in a text file or through standard input. Titles are processed to remove unwanted strings (defined in a blacklist) and are saved to an output file while also being printed to the standard output.

## Features
- Fetches webpage titles using `curl`-like functionality.
- Cleans titles by removing unwanted strings based on a blacklist.
- Supports input from a file or standard input.
- Saves titles to a new file named `<input_file>_titles` or `output_titles.txt` if the input is from standard input.

## Requirements
- Python 3.6+
- `requests` library
- `beautifulsoup4` library

Install required packages using:
```bash
pip install requests beautifulsoup4
```

## Usage

### Input File
The script reads a list of URLs from a text file. Each URL should be on a separate line.

Example file `urls.txt`:
```
https://www.example.com
https://www.google.com
https://nonexistent.url
```

### Running the Script
#### Using a File
Run the script with input redirection:
```bash
python fetch_titles.py < urls.txt
```
This will save the titles in a file named `urls.txt_titles`.

#### Entering the File Path
Run the script and manually provide the file path:
```bash
python fetch_titles.py
```
Then enter the file path when prompted.

#### Using Standard Input
You can also provide URLs directly through standard input:
```bash
echo -e "https://www.example.com\nhttps://www.google.com" | python fetch_titles.py
```
This will save the titles in a file named `output_titles.txt`.

### Output Format
- The titles are printed to the standard output in the same order as the URLs.
- They are also saved to a file (e.g., `urls.txt_titles`).

Example output for the input file `urls.txt`:
```
Example Domain
Google
Error: HTTPSConnectionPool(host='nonexistent.url', port=443): Max retries exceeded with url: /
```

## Configuration
The blacklist for removing unwanted strings from titles can be modified by editing the `blacklist` variable in the script:
```python
blacklist = ["| Spotify", "song by"]
```

## Error Handling
If a URL cannot be accessed, the script will output an error message indicating the issue (e.g., timeout or connection error).

## License
This script is provided under the MIT License. Use it freely and modify as needed.

