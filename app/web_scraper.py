import requests
from bs4 import BeautifulSoup

def fetch_website_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_elements(html):
    soup = BeautifulSoup(html, 'html.parser')
    meta_tags = soup.find_all('meta')
    images = soup.find_all('img')
    links = soup.find_all('a')
    return meta_tags, images, links
