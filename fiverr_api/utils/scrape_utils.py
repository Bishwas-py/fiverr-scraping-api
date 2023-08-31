import json
from typing import Optional

import bs4


def extract_text(element: bs4.Tag, class_name=None) -> Optional[str | None]:
    if element:
        if class_name:
            found_element = element.find(class_=class_name)
            return found_element.text if found_element else None
        return element.text
    return None


def extract_list_items(element: bs4.Tag, class_name=None):
    if element:
        if class_name:
            return [item.text for item in element.find_all(class_=class_name)]
        return [item.text for item in element.find_all('li')]
    return []


def get_perseus_initial_props(soup: bs4.BeautifulSoup):
    perseus_initial_props_soup = soup.find('script', id='perseus-initial-props')
    try:
        perseus_initial_props = json.loads(perseus_initial_props_soup.contents[0].text) \
            if perseus_initial_props_soup and perseus_initial_props_soup.contents else {}
    except json.decoder.JSONDecodeError as e:
        print("JSONDecodeError: perseus_initial_props_soup.text")
        perseus_initial_props = {}
    return perseus_initial_props
