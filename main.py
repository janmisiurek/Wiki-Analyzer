from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

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

@app.get("/analyze_links/")
async def analyze_links(url: Optional[str] = None):
    if url is not None:
        links = scrape_links(url)
        return {"links": links}
    else:
        return {"message": "No URL provided"}

@app.get("/analyze_content/")
async def analyze_content(url: Optional[str] = None):
    if url is not None:
        content = scrape_content(url)
        return {"content": content}
    else:
        return {"message": "No URL provided"}
