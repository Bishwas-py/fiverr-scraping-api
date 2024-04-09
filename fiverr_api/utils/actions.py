import requests


class Session(requests.Session):
    def __init__(self):
        super().__init__()
        self.SCRAPER_API_KEY = None
        self.SCRAPER_API = "https://api.scraperapi.com/"
        self.country_code = "us"
        self.device_type = "desktop"
        self.session_number = 1

    def request(
            self,
            method,
            url,
            *args,
            **kwargs,
    ):
        if self.SCRAPER_API_KEY:
            print("Using Scraper API")
            kwargs["params"] = {
                "api_key": self.SCRAPER_API_KEY,
                "url": url,
                "country_code": self.country_code,
                "device_type": self.device_type,
                "session_number": self.session_number,
            }
            url = self.SCRAPER_API
        return super().request(method, url, *args, **kwargs)


class Actions:

    def __init__(self):
        self.unique_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                                 "(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        self.headers = {
            'authority': 'fiverr.com',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'user-agent': self.unique_user_agent
        }
        self.request_session = Session()

        self.request_session.headers = self.headers

    def set_headers(self, headers: dict):
        self.headers = headers

    def set_user_agent(self, user_agent: str):
        self.headers['user-agent'] = user_agent

    def set_proxy(self, proxy: dict):
        self.request_session.proxies = proxy

    def set_scraper_api_key(self, api_key: str):
        self.request_session.SCRAPER_API_KEY = api_key


actions = Actions()
