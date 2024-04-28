from fiverr_api.utils.req import session


def profile_scrape(profile_url: str):
    response = session.get(profile_url)
    js_main_content = response.props_json()
    print("js_main_content", json.dumps(js_main_content, indent=4))


if __name__ == "__main__":
    import json
    from env import SCRAPER_API_KEY

    session.set_scraper_api_key(SCRAPER_API_KEY)
    scrape = profile_scrape('https://www.fiverr.com/bishwasbh')
    print(json.dumps(scrape, indent=4))
