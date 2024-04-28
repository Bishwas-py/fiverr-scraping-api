import json
import bs4


def get_perseus_initial_props(soup: bs4.BeautifulSoup):
    perseus_initial_props_soup = soup.find('script', id='perseus-initial-props')
    try:
        perseus_initial_props = json.loads(perseus_initial_props_soup.contents[0].text) \
            if perseus_initial_props_soup and perseus_initial_props_soup.contents else {}
    except json.decoder.JSONDecodeError as e:
        print("JSONDecodeError: perseus_initial_props_soup.text")
        perseus_initial_props = {}
    return perseus_initial_props
