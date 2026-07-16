import asyncio

from app.graph.graph import research_graph


async def main():

    result = await research_graph.ainvoke(
        {
            "query": "Latest developments in Artificial Intelligence",
            "context": "",
            "report": "",
        }
    )

    print("\n========== RESULT ==========\n")

    print(result["report"])


if __name__ == "__main__":
    asyncio.run(main())