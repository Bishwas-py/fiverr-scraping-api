import json
from bs4 import BeautifulSoup
from fiverr_api.utils.actions import actions
from fiverr_api.utils.scrape_utils import extract_text, extract_list_items


def profile_scrape(profile_url: str):
    response = actions.request_session.get(profile_url)
    soup = BeautifulSoup(response.text, 'html5lib')
    user_page_soup = soup.find('div', class_='user-page-perseus')

    user_area = user_page_soup.find('img', class_='profile-pict-img')
    user_name, user_photo = user_area['alt'], user_area['src']

    user_level = user_page_soup.find('a', class_='user-badge-round')['class'][-1] if user_page_soup.find('a',
                                                                                                         class_='user-badge-round') else ''

    oneliner = user_page_soup.find('div', class_='oneliner-wrapper')
    bio = extract_text(oneliner.find('span', class_='oneliner'))

    user_stats = user_page_soup.find('ul', class_='user-stats')
    user_from = extract_text(user_stats.find('li', class_='location').find('b'))
    member_since = extract_text(user_stats.find('li', class_='member-since').find('b'))
    response_time = extract_text(user_stats.find('li', class_='response-time').find('b'))
    recent_delivery = extract_text(user_stats.find('li', class_='recent-delivery').find('strong')).split('<!-- -->')[
        0].replace('\xa0', ' ')

    seller_profile = user_page_soup.find('div', class_='seller-profile')
    description = extract_text(seller_profile.find('div', class_='description').find('p'))

    languages_soup = seller_profile.find('div', class_='languages')
    languages = []
    if languages_soup:
        languages_list = languages_soup.find('ul').find_all('li')
        for lang_item in languages_list:
            lang_text = lang_item.text.strip()
            lang_parts = lang_text.split('-')
            if len(lang_parts) >= 2:
                language = lang_parts[0].strip()
                proficiency = lang_parts[1].strip()
                languages.append((language, proficiency))

    skills_area = seller_profile.find('div', class_='skills')
    skill_set = extract_list_items(skills_area.find('ul')) if skills_area else []

    gig_listings = user_page_soup.find_all('div', class_='gig-wrapper-impressions')
    gigs = []
    for gig in gig_listings:
        gig_title_elem = gig.find('h3')
        if gig_title_elem:
            gig_title = gig_title_elem.find('a')['title']
            gig_href = gig_title_elem.find('a')['href']
            rating_wrapper_soup = gig.find('div', class_='rating-wrapper')
            gig_rating_soup = rating_wrapper_soup.find('span', class_='gig-rating')
            """html
            <span class="gig-rating text-body-2">
            <svg xmlns="...></svg>
            5.0
            <span>(20)</span></span>
            """
            gig_rating = gig_rating_soup.contents[1] if gig_rating_soup else None
            gig_rating = gig_rating.text if gig_rating else None
            gig_rating_count_soup = gig_rating_soup.find('span')
            gig_rating_count = gig_rating_count_soup if gig_rating_count_soup else None
            gig_rating_count = gig_rating_count.text.strip('()') if gig_rating_count else None
            gigs.append((gig_title, gig_href, gig_rating, gig_rating_count))
        else:
            print("Gig title element not found for a listing.")

    gigs_review_soup = user_page_soup.find('div', class_='reviews-wrapper')

    ranking_soup = user_page_soup.find('div', class_='ranking')
    ranking_list_soup = ranking_soup.find('ul').find_all('li') if ranking_soup else []
    rating_breakdown = {
        'seller_communication_level': 0,
        'recommend_to_a_friend': 0,
        'service_as_described': 0
    }
    for ranking_soup in ranking_list_soup:
        ranking_soup_text = str(ranking_soup.find(text=True, recursive=False))
        if ranking_soup_text == "Seller communication level":
            rating_breakdown['seller_communication_level'] = ranking_soup.find('b', class_='rating-score').text
        elif ranking_soup_text == "Recommend to a friend":
            rating_breakdown['recommend_to_a_friend'] = ranking_soup.find('b', class_='rating-score').text
        elif ranking_soup_text == "Service as described":
            rating_breakdown['service_as_described'] = ranking_soup.find('b', class_='rating-score').text

    rating_rows = soup.find_all('tr')
    starers_rating = {
        'five_starers_rating_count': 0,
        'four_starers_rating_count': 0,
        'three_starers_rating_count': 0,
        'two_starers_rating_count': 0,
        'one_starers_rating_count': 0
    }
    for rating_row in rating_rows:
        rating_label = rating_row.find('button').text.strip()
        rating_count = rating_row.find('td', class_='star-num').text.strip('()')
        if rating_label == "5 Stars":
            starers_rating['five_starers_rating_count'] = rating_count
        if rating_label == "4 Stars":
            starers_rating['four_starers_rating_count'] = rating_count
        if rating_label == "3 Stars":
            starers_rating['three_starers_rating_count'] = rating_count
        if rating_label == "2 Stars":
            starers_rating['two_starers_rating_count'] = rating_count
        if rating_label == "1 Stars":
            starers_rating['one_starers_rating_count'] = rating_count

    reviews_list = gigs_review_soup.find('ul', class_='review-list')
    seller_reviews = []

    for review_item_soup in reviews_list.find_all('li', class_='review-item'):
        review_data = {}

        # Extract user details
        user_profile_icon_soup = review_item_soup.find('div', class_='user-profile-image')
        user_profile_img_soup = user_profile_icon_soup.find('img')
        if user_profile_img_soup:
            user_photo = user_profile_img_soup['src']
        else:
            user_photo = None

        reviewer_details_soup = review_item_soup.find('div', class_='reviewer-details')
        buyer_user_name = reviewer_details_soup.find('b').text.strip() if reviewer_details_soup else '<unknown>'
        buyer_user_country = review_item_soup.find('div', class_='country-name').text.strip()

        # Extract review details
        review_details_soup = review_item_soup.find('div', class_='review-details')
        rating = review_details_soup.find('b', class_='rating-score').text.strip()
        review_date = review_details_soup.find('time', class_='text-body-2').text.strip()
        review_text = review_details_soup.find('div', class_='review-description').p.text.strip()

        # Extract gig details
        gig_link = review_details_soup.find('a', class_='gig-link review-gig-info-link')['href']

        # Append data to the reviews list
        review_data['user_name'] = buyer_user_name
        review_data['user_country'] = buyer_user_country
        review_data['rating'] = rating
        review_data['review_date'] = review_date
        review_data['review_text'] = review_text
        review_data['gig_link'] = gig_link

        seller_reviews.append(review_data)

    return {
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
            'rating_breakdown': rating_breakdown,
            'starers_rating': starers_rating,
            'seller_reviews': seller_reviews
        }
    }


if __name__ == "__main__":
    import json

    scrape = profile_scrape('https://www.fiverr.com/torokcsaba')
    print(json.dumps(scrape, indent=4))
