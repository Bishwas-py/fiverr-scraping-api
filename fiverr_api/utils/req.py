import re

import requests
from bs4 import BeautifulSoup

from fiverr_api.utils.scrape_utils import get_perseus_initial_props

SCRAPER_API_URL = "https://api.scraperapi.com/"
SCRAPER_API_REF = "https://www.scraperapi.com/?fp_ref=enable-fiverr-api"


class Response(requests.Response):
    soup: 'BeautifulSoup'

    def set_soup(self):
        self.soup = BeautifulSoup(self.text, 'html5lib')

    def props_json(self) -> dict:
        return get_perseus_initial_props(self.soup)


class Session(requests.Session):
    def __init__(self):
        super().__init__()
        self.SCRAPER_API_KEY = None
        self.USE_SCRAPER_API = True
        self.country_code = "us"
        self.device_type = "desktop"
        self.session_number = 1

    def request(
            self,
            method,
            url: str = '',
            self_: 'Session' = None,
            *args,
            **kwargs,
    ) -> Response:
        if not re.match(r"https://(www\.)?fiverr\.com/", url):
            raise ValueError(
                f"Invalid URL: {url}, must be a Fiverr URL.")
        if self_ is None:
            self_ = self
        if self_.USE_SCRAPER_API and not self_.SCRAPER_API_KEY:
            raise ValueError(
                f"No Scraper API key found, please get one from {SCRAPER_API_REF}, and "
                f"use `set_scraper_api_key(` to set it.")
        if self_.SCRAPER_API_KEY and self_.USE_SCRAPER_API:
            kwargs["params"] = {
                "api_key": self_.SCRAPER_API_KEY,
                "url": url,
                "country_code": self_.country_code,
                "device_type": self_.device_type,
                "session_number": self_.session_number,
            }
            url = SCRAPER_API_URL
        response = super().request(method, url, *args, **kwargs)
        response.__class__ = Response
        response.set_soup()
        return response

    def set_scraper_api_key(self, api_key: str):
        self.SCRAPER_API_KEY = api_key

    def set_session_number(self, session_number: int):
        self.session_number = session_number


session = Session()
