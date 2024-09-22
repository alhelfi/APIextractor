import os
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urljoin


def extract_page_content(url):
    response = requests.get(url)
    return response.content



def extract_apis_and_tokens(content, js_scripts):
    api_pattern = r'https?://[^\s/$.?#].[^\s]*'
    all_matches = re.findall(api_pattern, content) + re.findall(api_pattern, str(js_scripts))

    token_pattern = r'[a-zA-Z0-9]{16,}'
    all_tokens = re.findall(token_pattern, content) + re.findall(token_pattern, str(js_scripts))

    return all_matches, all_tokens


def save_to_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(data)


def main():
    target_url = input("Enter URL : ") #with protocol like : https://google.com
    target_domain = urlparse(target_url).netloc

    page_content = extract_page_content(target_url)

    site_folder = os.path.join("targets", target_domain)
    os.makedirs(site_folder, exist_ok=True)


    soup = BeautifulSoup(page_content, "html.parser")

    js_scripts = soup.find_all("script")
    html_content = soup.get_text()

    all_matches, all_tokens = extract_apis_and_tokens(html_content, js_scripts)
    apis_data = "\n".join(all_matches)
    tokens_data = "\n".join(all_tokens)
    apis_file = os.path.join(site_folder, "apis.txt")
    tokens_file = os.path.join(site_folder, "tokens.txt")
    save_to_file(apis_file, apis_data)
    save_to_file(tokens_file, tokens_data)

    print("Information saved in website's files.")

if __name__ == "__main__":
    main()
