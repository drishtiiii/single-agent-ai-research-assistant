from app.tools.search import SearchTool

search = SearchTool()

results = search.search(
    "Latest AI research trends 2026",
    max_results=5,
)

print("\nSEARCH RESULTS\n")

for i, result in enumerate(results, start=1):
    print("=" * 80)
    print(f"Result {i}")
    print(f"Title : {result['title']}")
    print(f"URL   : {result['url']}")
    print(f"Body  : {result['body']}")