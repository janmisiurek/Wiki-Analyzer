from fastapi import FastAPI
from typing import Optional
from scraper import scrape_links, scrape_content
from analysis import analyze_links_data, analyze_content_data

app = FastAPI()


@app.get("/analyze_links/")
async def analyze_links(url: Optional[str] = None):
    if url is not None:
        links = scrape_links(url)
        link_data = analyze_links_data(links, url)
        return {"link_analysis": link_data}
    else:
        return {"message": "No URL provided"}
    
@app.get("/analyze_content/")
async def analyze_content(url: Optional[str] = None):
    if url is not None:
        content = scrape_content(url)
        content_data = analyze_content_data(content)
        return {"content_analysis": content_data}
    else:
        return {"message": "No URL provided"}

