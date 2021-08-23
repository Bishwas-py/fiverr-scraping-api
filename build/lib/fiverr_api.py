from bs4 import BeautifulSoup
import json
import requests

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value,
                     OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(
    software_names=software_names, operating_systems=operating_systems, limit=100)

user_agent = user_agent_rotator.get_random_user_agent()

unique_user_agent = False

headers = {
    'authority': 'fiverr.com',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}


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
    headers.update({'user-agent': user_agent})

    @staticmethod
    def gig_scrape(url):
        data = {}
        session = requests.Session()
        response = session.get(url, headers=headers)
        fiv_soup = BeautifulSoup(response.text, 'html5lib')

        gig_overview = fiv_soup.find('div', {'class': 'gig-overview'})
        try:
            categories_breadcrumbs_html = gig_overview.find(
                'nav', {'class': 'categories-breadcrumbs'}).find_all('span')
        except:
            categories_breadcrumbs_html
            
        categories_breadcrumbs = list()  # imp

        for category in categories_breadcrumbs_html:
            if category.text != '':
                categories_breadcrumbs.append(category.text)

        try:
            title = gig_overview.find('h1').text  # imp
        except:
            title = ''
        seller_overview_html = fiv_soup.find(
            'div', {'class': "seller-overview"})
        user_name = seller_overview_html.find(
            "a", {"class": "seller-link"}).text  # imp
        rating = seller_overview_html.find(
            "b", {'class': 'rating-score'}).text  # imp
        ratings_count = seller_overview_html.find(
            "span", {'class': 'ratings-count'}).text  # imp
        ratings_count = ratings_count.replace(")", '').replace(
            "(", '')  # removing unnecessary brackets

        # Getting gig images
        gig_gallery_component = fiv_soup.find(
            "section", {"class": "gig-gallery-component"})
        gig_images_list = gig_gallery_component.find_all("img", {'src': True})
        images = [image['src'] for image in gig_images_list]

        # Getting gig description
        description = fiv_soup.find(
            "div", {'class': 'description-content'}).text  # imp

        metadata = fiv_soup.find("div", {"class": "metadata"})

        metadata_attributes = fiv_soup.find_all("li", {"metadata-attribute"})

        # Getting all the meta data below discription
        meta_data = dict()  # imp
        for metadata_attribute in metadata_attributes:
            attribute = metadata_attribute.find("p").text
            meta_values = metadata_attribute.find("ul").find_all("li")

            values = [value.text for value in meta_values]

            meta_data.update({
                attribute: values
            })

        # Getting profile information
        seller_card = fiv_soup.find("div", {"class": "seller-card"})
        try:
            seller_bio = seller_card.find(
                "p", {"class": "one-liner"}).text  # add this
        except:
            seller_bio = None
        profile_photo = seller_card.find("img")["src"]  # imp

        user_stats_soups = seller_card.find(
            "ul", {"class": "user-stats"}).find_all("li")
        user_stats = dict()
        for stat in user_stats_soups:
            stat_topic = stat.find(text=True)
            stat_value = stat.find("strong").text
            user_stat = {
                stat_topic: stat_value
            }
            user_stats.update(user_stat)

        # Getting user discription from  seller card
        user_discription = seller_card.find(
            "article", {"class": "seller-desc"}).text.replace("+ See More", "")

        # Prices Ranges
        packages_tabs = fiv_soup.find("div", {"class": "packages-tabs"})
        try:
            labels = packages_tabs.find_all("label")
        except:
            labels = []
        forms = packages_tabs.find_all("form")
        price_and_features = dict()  # imp
        for index in range(len(labels)):
            label = labels[index]
            form = forms[index]
            title = form.find("b", {"class": "title"}).text
            price = form.find("span", {"class": "price"}).text
            try:
                discription = form.find("p").text
            except:
                discription = ""
                
            try:
                delivery_days = form.find(
                    "b", {"class": "delivery"}).text.replace(" Day Delivery", "")
            except:
                delivery_days = ''
            try:
                revisions = form.find(
                    "b", {"class": "revisions"}).text.replace(" Revisions", "")
            except:
                revisions = ''
            feature_soups = form.find("ul", {"class": "features"}).find_all(
                "li", {"class": "feature"})
            features = [feature.text for feature in feature_soups]
            features_data = {
                label.text: {
                    "price": price,
                    "discription": discription,
                    "features": features
                }
            }
            price_and_features.update(features_data)

        # Get Tags
        gig_tags_container = fiv_soup.find(
            "div", {"class": "gig-tags-container"}).find("ul").find_all("li")
        gig_tags = [tag.text for tag in gig_tags_container]

        cooked_data = {
            'user_name': user_name,
            "title": title,
            "categories_breadcrumbs": categories_breadcrumbs,
            "rating": rating,
            "ratings_count": ratings_count,
            "images": images,
            "description": description,
            "meta_data": meta_data,
            "seller_bio": seller_bio,
            "profile_photo": profile_photo,
            "user_stats": user_stats,
            "user_discription": user_discription,
            "price_and_features": price_and_features,
            "gig_tags": gig_tags,
            "delivery_days": delivery_days,
            "revisions": revisions
        }

        data.update(cooked_data)
        return json.dumps(data, indent=4)

    @staticmethod
    def profile_scrape(url):
        data = {}
        session = requests.Session()
        response = session.get(url, headers=headers)
        fiv_soup = BeautifulSoup(response.text, 'html5lib')
        profile = fiv_soup.find('div', {'class': 'grid-12'})

        user_area = profile.find('img', {'class': 'profile-pict-img'})
        user_name, user_photo = user_area['alt'], user_area['src']

        try:
            user_level = profile.find(
                'a', {'class': 'user-badge-round'})['class'][-1]
        except:
            user_level = ''

        oneliner = profile.find('div', {'class': 'oneliner-wrapper'})
        bio = oneliner.find('small', {'class': 'oneliner'}).text

        user_stats = profile.find('ul', {'class': 'user-stats'})
        user_from = user_stats.find('li', {'class': 'location'}).find('b').text
        member_since = user_stats.find(
            'li', {'class': 'member-since'}).find('b').text
        response_time = user_stats.find(
            'li', {'class': 'response-time'}).find('b').text
        recent_delivery = user_stats.find('li', {'class': 'recent-delivery'}).find(
            'strong').text.split('<!-- -->')[0].replace('\xa0', ' ')

        seller_profile = profile.find('div', {'class': 'seller-profile'})
        description = seller_profile.find('div', 'description').find('p').text

        # Language gets scraped here
        languages_soap = seller_profile.find(
            'div', {'class': 'languages'}).find('ul').find_all('li')
        languages = []
        for language in languages_soap:
            laguage_data = language.text.split(
                '<!-- -->')[0].replace('\xa0', '').split('- ')
            languages.append((laguage_data[0], laguage_data[1]))

        # Skills sets gets scraped here
        skills_area = seller_profile.find(
            'div', {'class': 'skills'}).find('ul').find_all('li')
        skill_set = []
        for skill in skills_area:
            skill_set.append(skill.text)

        """ this part needs to be developed
        # Education/Certifications gets scraped here
        education_list = seller_profile.find(
            'div', {'class': 'education-list'}).find('ul').find_all('li')
        educations = []
        for education in education_list:
            print('s12')
            educations.append(education.getText())
        """

        gig_listings = profile.find_all(
            'div', {'class': 'gig-wrapper-impressions'})
        gigs = []
        for gig_card in gig_listings:
            headings = gig_card.find(
                'h3', {'class': 'text-display-7'}).find('a')
            heading = headings['title']
            gig_link = headings['href']
            gigs.append((heading, gig_link))

        gigs_reviews = profile.find('div', {'class': 'gigs-reviews-panel'})
        header_stars = gigs_reviews.find(
            'ul', {'class': 'header-stars'}).find_all('span', {'class': 'total-rating-out-five'})
        seller_communication_level = header_stars[0].text
        recommended_to_friend = header_stars[0].text
        service_as_described = header_stars[0].text
        profile_ratings = {
            'seller_communication_level':seller_communication_level,
            'recommended_to_friend': recommended_to_friend,
            'service_as_described': service_as_described
        }
        reviews_list = gigs_reviews.find('ul', {'class':'review-list'})
        reviews_list = reviews_list.find_all('span', recursive=False)
        print(len(reviews_list))
        
        reviews = []
        for review in reviews_list:
            review_li = review.find('li', class_='review-item', recursive=False)
            buyer_name = review_li.find('h5').text
            given_rating = review_li.find('span', {'class': 'total-rating-out-five'}).text
            country_name = review_li.find('div', {'class': 'country-name'}).text
            review_description = review_li.find(
                'div', {'class': 'review-description'}).find('p', {'class': 'text-body-2'}).text
            reviews.append(
                {
                    'buyer_name': buyer_name,
                    'given_rating': given_rating,
                    'country_name': country_name,
                    'review_description': review_description
                }
            )

        # header-total-rating
        return json.dumps({
            'user': {
                'name': user_name,
                'photo': user_photo,
                'level': user_level,
                'bio': bio,
                'from': user_from,
                'member_since': member_since,
                'response_time': response_time,
                'recent_delivery': recent_delivery,
                'description': description,
                'languages': languages,
                'skill_set': skill_set,
            },
            'gig_info': {
                'gigs': gigs,
                'profile_ratings': profile_ratings,
                'reviews': reviews
            }
        }, indent=4) 


if __name__ == "__main__":
    scrape = Scrape().gig_scrape('https://www.fiverr.com/deesmithvo/provide-high-quality-voice-overs-to-help-bring-life-to-your-projects')
    print(scrape)
