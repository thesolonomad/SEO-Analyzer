import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

def fetch_website_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # If authentication is required, add username and password
    username = "your_username"
    password = "your_password"
    
    try:
        response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text
    
    except requests.exceptions.HTTPError as err:
        if response.status_code == 403:
            return "Access forbidden: You do not have permission to access this resource."
        else:
            return f"HTTP error occurred: {err}"
    except Exception as err:
        return f"An error occurred: {err}"

def extract_elements(html):
    soup = BeautifulSoup(html, 'html.parser')
    meta_tags = soup.find_all('meta')
    images = soup.find_all('img')
    links = soup.find_all('a')
    return meta_tags, images, links


if __name__ == "__main__":
    url = "https://www.vargasinsurance.com/"
    content = fetch_website_html(url)
    print(content)
