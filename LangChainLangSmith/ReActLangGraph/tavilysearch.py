from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()

def get_profile_url_tavily(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]
    # return res

if __name__ == "__main__":
    print(get_profile_url_tavily("Sandeep Puttur linkedin"))