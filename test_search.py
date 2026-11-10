
from tools.web_search import search_web

query = "AI adoption in Indian hospitals"

results = search_web(query)

print("\nSEARCH RESULTS")
print("=" * 60)

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("Title:", result["title"])
    print("URL:", result["url"])
    print("Content:", result["content"])
