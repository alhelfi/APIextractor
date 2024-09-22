# API and Token Extractor

This Python script extracts API URLs and tokens from a given webpage. It utilizes the `requests` library to fetch the page content, `BeautifulSoup` for parsing HTML, and regular expressions for matching patterns.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage 

1. Run the script in your terminal:
```bash
python main.py
```
2. When prompted, enter the URL of the webpage you want to analyze (make sure to include the protocol, e.g., `https://google.com`).
3. The script will create a folder named `targets` (if it doesn't already exist) and save two files:

-   `apis.txt`: Contains all extracted API URLs.
-   `tokens.txt`: Contains all extracted tokens.
4. You will see a message indicating that the information has been saved.
## Note

-   Ensure that the URL you provide is publicly accessible.
-   The script may not capture all APIs or tokens depending on their structure and encoding.
