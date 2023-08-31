import requests


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
        self.request_session = requests.Session()
        self.request_session.headers = self.headers

    def set_headers(self, headers: dict):
        self.headers = headers

    def set_user_agent(self, user_agent: str):
        self.headers['user-agent'] = user_agent

    def set_proxy(self, proxy: dict):
        self.request_session.proxies = proxy


actions = Actions()
