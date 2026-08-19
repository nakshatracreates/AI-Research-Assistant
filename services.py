import requests
from bs4 import BeautifulSoup


def fetch_webpage(url: str):
    headers = {
        "User-Agent": "AIResearchAssistant/1.0"
    }
    response = requests.get(url,
        headers=headers, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")

    article = soup.find("article")

    if article:
        return article.get_text("", strip=True)

    return soup.get_text("", strip=True)


def search_topics(topic: str):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": topic,
        "format": "json"
    }

    headers = {
        "User-Agent": "AIResearchAssistant/1.0"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )

    return response.json()

def chunk_text(text:str,chunksize:int=1000):
    chunks=[]
    for i in range(0,len(text),chunksize):
        chunk=text[i:i+chunksize]
        chunks.append(chunk)
    return chunks

#'''search_sources() = FIND the sources
#fetch_webpage() = READ the source''' 