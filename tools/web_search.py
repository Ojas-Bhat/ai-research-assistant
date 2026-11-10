
from tavily import TavilyClient


# Initialise the search client
search_client = TavilyClient()


def search_web(query: str) -> list:
    """
    Search the web and return relevant results.
    """

    response = search_client.search(
        query=query,
        max_results=5,
        topic="general"
    )

    results = []

    for item in response["results"]:
        results.append({
            "title": item["title"],
            "url": item["url"],
            "content": item["content"]
        })

    return results
