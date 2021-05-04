from this import s

from bs4 import BeautifulSoup
import requests

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

user_agent = user_agent_rotator.get_random_user_agent()

unique_user_agent = False




class Scrape:

    while not unique_user_agent:
        file = open('last_user_agent.txt', mode='w+')
        if str(user_agent) != str(file.read()):
            file.write(str(user_agent))
            user_agent = user_agent
            unique_user_agent = True

    @staticmethod
    def scrape(url):
        headers = {
            'authority': 'fiverr.com',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

        data = {}
        session = requests.Session()
        response = session.get(url, headers=headers)
        fiv_soup = BeautifulSoup(response.text, 'html5lib')

        gig_overview = fiv_soup.find('div', {'class': 'gig-overview'})
        categories_breadcrumbs_html = gig_overview.find('nav', {'class':'categories-breadcrumbs'}).find_all('span')

        categories_breadcrumbs = list() #imp

        for category in categories_breadcrumbs_html:
            if category.text != '':
               categories_breadcrumbs.append(category.text)

        title = gig_overview.find('h1').text #imp

        seller_overview_html = fiv_soup.find('div', {'class' : "seller-overview"})
        user_name = seller_overview_html.find("a", {"class":"seller-link"}).text #imp
        rating = seller_overview_html.find("b", {'class':'rating-score'}).text #imp
        ratings_count = seller_overview_html.find("span", {'class':'ratings-count'}).text #imp

        description = seller_overview_html.find("span", {'class':'description-content'}).text #imp
        cooked_data = {
            "title": title,
            "rating": rating,
            "ratings_count":ratings_count.replace(")",'').replace("(",''),
            "categories_breadcrumbs": categories_breadcrumbs,
            'user_name':user_name,
        }

        data.update(cooked_data)

        print(f"{data}")

        return str(response.text)


scrapper = Scrape()
content = scrapper.scrape('https://www.fiverr.com/tripchoni/make-seo-tools-website-with-49-tools')
f = open('new.html', mode='w+', encoding="utf-8")
f.write(str(content))