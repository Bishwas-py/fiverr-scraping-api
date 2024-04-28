from fiverr_api.utils.req import session


class ScrapeAPI:
    def __init__(self, api_key):
        session.set_scraper_api_key(api_key)

    def get_props_json(self):
