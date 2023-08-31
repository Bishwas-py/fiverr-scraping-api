import json
from bs4 import BeautifulSoup

from fiverr_api.utils.actions import actions
from fiverr_api.utils.scrape_utils import extract_text, extract_list_items, get_perseus_initial_props


def gig_scrape(gig_url: str):
    response = actions.request_session.get(gig_url)
    soup = BeautifulSoup(response.text, 'html5lib')

    main_soup = soup.find('div', class_='main')

    first_child_of_main_soup = main_soup.findChild()
    categories_breadcrumbs_links_soup = (
        first_child_of_main_soup.find_all('a', href=True)
    ) if first_child_of_main_soup else []
    categories_breadcrumbs = [category.text for category in categories_breadcrumbs_links_soup]
    if '' in categories_breadcrumbs:
        categories_breadcrumbs.remove('')

    gig_overview_soup = main_soup.find('div', class_='gig-overview')
    title = extract_text(gig_overview_soup.find('h1'))

    seller_overview_soup = main_soup.find('div', class_='seller-overview')
    rating = extract_text(seller_overview_soup, class_name='rating-score')
    ratings_count = extract_text(seller_overview_soup, class_name='ratings-count')
    if ratings_count:
        ratings_count = ratings_count.replace(")", '').replace("(", '')

    gig_gallery_soup = main_soup.find('section', class_='gig-gallery-component')
    gig_images_list = gig_gallery_soup.find_all('img', src=True)
    images = [image['src'] for image in gig_images_list]

    about_this_gig_soup = main_soup.find(text=lambda text: text and 'about this gig' in text.lower())

    description = extract_text(about_this_gig_soup.next_element if about_this_gig_soup else None)

    metadata_soup = main_soup.find('ul', class_='metadata')
    metadata_attributes = metadata_soup.find_all('li', class_='metadata-attribute') if metadata_soup else []
    meta_data = {attribute.find('p').text: [value.text for value in attribute.find('ul').find_all('li')]
                 for attribute in metadata_attributes}

    seller_card_soup = main_soup.find('div', class_='seller-card')
    seller_bio = extract_text(seller_card_soup.find('p', class_='one-liner'))
    profile_photo_img_soup = seller_card_soup.find('img')
    profile_photo = profile_photo_img_soup['src'] if profile_photo_img_soup else None
    user_name = profile_photo_img_soup['alt'] if profile_photo_img_soup else None

    user_stats_soup = seller_card_soup.select('ul.user-stats > li')
    user_stats = {stat.find(text=True): stat.find('strong').text for stat in user_stats_soup} if user_stats_soup else {}

    user_description = extract_text(seller_card_soup.find('article', class_='seller-desc'))
    if user_description:
        user_description = user_description.replace('+ See More', '')

    # gig_tags_container = main_soup.find('div', class_='gig-tags-container').find('ul').find_all('li')
    gig_tags_container = main_soup.select('div.gig-tags-container > ul > li')
    gig_tags = [tag.text for tag in gig_tags_container] if gig_tags_container else []

    perseus_initial_props = get_perseus_initial_props(soup)

    return {
        'user_name': user_name,
        'title': title,
        'categories_breadcrumbs': categories_breadcrumbs,
        'rating': rating,
        'ratings_count': ratings_count,
        'images': images,
        'description': description,
        'meta_data': meta_data,
        'seller_bio': seller_bio,
        'profile_photo': profile_photo,
        'user_stats': user_stats,
        'user_description': user_description,
        'gig_tags': gig_tags,
        'perseus_initial_props': perseus_initial_props
    }


if __name__ == "__main__":
    import json

    scrape = gig_scrape(
        'https://www.fiverr.com/bishwasbh/do-web-scraping-in-python-with-requests-and-beautifulsoup4')
    print(json.dumps(scrape, indent=4))
