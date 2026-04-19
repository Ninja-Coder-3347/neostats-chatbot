from duckduckgo_search import DDGS


def web_search(query):

    try:

        results = []

        with DDGS() as ddgs:

            for r in ddgs.text(query, max_results=5):

                results.append(r["body"])

        return " ".join(results)

    except Exception as e:
        print(e)