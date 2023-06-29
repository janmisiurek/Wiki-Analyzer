# Wiki Analyzer

Wiki Analyzer is a simple tool developed to analyze webpage contents. It's written in Python using the FastAPI framework and utilizes BeautifulSoup for web scraping. 
Primary focus of Wiki Analyzer is on Wikipedia pages, but it can be used with various other webpages as well.

## What does it do?

Wiki Analyzer provides two primary analyses:
1. **Link Analysis**: Analyzes the number of internal and external links on a given webpage.
2. **Content Analysis**: Analyzes the most common words in the content of a given webpage.



## How to use it?

Wiki Analyzer provides two endpoints for its analyses:

1. **/analyze_links/**: Requires a URL parameter. Returns the number of internal and external links.
2. **/analyze_content/**: Requires a URL parameter. Returns the ten most common words in the webpage content.

For example, to analyze the links of the Wikipedia page for "Le Corricolo", you would use the following URL:

```
http://localhost:8000/analyze_links/?url=https://en.wikipedia.org/wiki/Le_Corricolo
```

## Local Setup

You'll need Python 3.10 or higher. Follow these steps to set up Wiki Analyzer locally:

1. Clone this repository.
2. Install the requirements using pip:
    ```
    pip install -r requirements.txt
    ```
3. Run the FastAPI server:
    ```
    uvicorn main:app --reload
    ```

## Docker Setup

Alternatively, you can use Docker to avoid installing Python and the necessary packages locally.

1. Build the Docker image:
    ```
    docker build -t wiki-analyzer .
    ```
2. Run the Docker image:
    ```
    docker run -p 8000:8000 wiki-analyzer
    ```

Now you should be able to access the FastAPI server at http://localhost:8000.

## Documentation

For detailed information about the API endpoints and their usage, navigate to `/docs` after running the server. FastAPI provides a user-friendly interface to interact with the API.
