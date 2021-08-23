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
    """
    Scape Fiverr data with this function.
    """
    while not unique_user_agent:
        file = open('last_user_agent.txt', mode='w+')
        if str(user_agent) != str(file.read()):
            file.write(str(user_agent))
            user_agent = user_agent
            unique_user_agent = True

    @staticmethod
    def gig_scrape(url):
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
        ratings_count = ratings_count.replace(")",'').replace("(",'') #removing unnecessary brackets

        # Getting gig images
        gig_gallery_component = fiv_soup.find("section", {"class":"gig-gallery-component"})
        gig_images_list = gig_gallery_component.find_all("img", {'src': True})
        images = [image['src'] for image in gig_images_list]

        # Getting gig description
        description = fiv_soup.find("div", {'class':'description-content'}).text #imp

        metadata = fiv_soup.find("div", {"class":"metadata"})
        
        metadata_attributes = fiv_soup.find_all("li", {"metadata-attribute"})

        # Getting all the meta data below discription
        meta_data = dict() # imp
        for metadata_attribute in metadata_attributes:
            attribute = metadata_attribute.find("p").text
            meta_values = metadata_attribute.find("ul").find_all("li")

            values = [value.text for value in meta_values]

            meta_data.update({
                attribute: values
            })

        # Getting profile information
        seller_card = fiv_soup.find("div", {"class":"seller-card"})
        try:
            seller_bio = seller_card.find("p", {"class":"one-liner"}).text #add this
        except:
            seller_bio = None
        profile_photo = seller_card.find("img")["src"] #imp
        
        user_stats_soups = seller_card.find("ul", {"class":"user-stats"}).find_all("li")
        user_stats = dict()
        for stat in user_stats_soups:
            stat_topic = stat.find(text=True)
            stat_value = stat.find("strong").text
            user_stat = {
                stat_topic:stat_value
            }
            user_stats.update(user_stat)

        # Getting user discription from  seller card
        user_discription = seller_card.find("article", {"class":"seller-desc"}).text.replace("+ See More","")

        # Prices Ranges
        packages_tabs = fiv_soup.find("div", {"class":"packages-tabs triple"})
        labels = packages_tabs.find_all("label")
        forms = packages_tabs.find_all("form")
        price_and_features = dict() #imp
        for index in range(len(labels)):
            label = labels[index]
            form = forms[index]
            title = form.find("b", {"class":"title"}).text
            price = form.find("span", {"class":"price"}).text
            discription = form.find("p").text
            delivery_days = form.find("b", {"class":"delivery"}).text.replace(" Day Delivery","")
            revisions = form.find("b", {"class":"revisions"}).text.replace(" Revisions","")
            feature_soups = form.find("ul", {"class":"features"}).find_all("li", {"class":"feature"})
            features = [feature.text for feature in  feature_soups]
            features_data = {
                label.text : {
                    "price": price,
                    "discription": discription,
                    "features": features
                }
            }
            price_and_features.update(features_data)

        # Get Tags
        gig_tags_container = fiv_soup.find("div",{"class":"gig-tags-container"}).find("ul").find_all("li")
        gig_tags = [tag.text for tag in gig_tags_container]

        cooked_data = {
            'user_name':user_name,
            "title": title,
            "categories_breadcrumbs": categories_breadcrumbs,
            "rating": rating,
            "ratings_count":ratings_count,
            "images":images,
            "description":description,
            "meta_data": meta_data,
            "seller_bio":seller_bio,
            "profile_photo":profile_photo,
            "user_stats":user_stats,
            "user_discription":user_discription,
            "price_and_features":price_and_features,
            "gig_tags":gig_tags
            
        }

        data.update(cooked_data)
        return data