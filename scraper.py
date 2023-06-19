from bs4 import BeautifulSoup
import requests

def scrape_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for a in soup.find_all('a', href=True):
        links.append(a['href'])

    return links

def scrape_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.get_text()
