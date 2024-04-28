import json
from bs4 import BeautifulSoup
from fiverr_api.utils.req import session
from fiverr_api.utils.scrape_utils import extract_text, extract_list_items, get_perseus_initial_props


def profile_scrape(profile_url: str):
    response = session.get(profile_url)
    soup = BeautifulSoup(response.text, 'html5lib')
    js_main_content = get_perseus_initial_props(soup)
    print("js_main_content", json.dumps(js_main_content, indent=4))


if __name__ == "__main__":
    import json
    from env import SCRAPER_API_KEY

    session.set_scraper_api_key(SCRAPER_API_KEY)
    scrape = profile_scrape('https://www.fiverr.com/bishwasbh')
    print(json.dumps(scrape, indent=4))
