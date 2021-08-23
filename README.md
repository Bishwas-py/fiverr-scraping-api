# Fiverr API v0.0.8 - Scrapes Fiverr profile

Fiverr API (Newer Version) - This Fiverr scrapping API is capable of getting all the info from a gig in Fiverr.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install fiverr-api.

```bash
pip install fiverr-api
```

## Essential Links
[GitHub Repo](https://github.com/Bishwas-py/fiverr-scraping-api), [Issue A Bug](https://github.com/Bishwas-py/fiverr-scraping-api/issues) and ask for help in [Webmatrices Forum](http://webmatrices.com/)!

## Usage

```python
from fiverr_api import Scrape

# the gig you wanna scrape
gig_url = "https://www.fiverr.com/otem_global/your-kajabi-teachable-"\
    "website-expert-fix-your-pipeline-set-up-online-courses"

# the profile you wanna scrape
profile_url = "https://www.fiverr.com/otem_global/"

# initialize fiverr scrapper
scraper = Scrape()

# returns the scraped gig's data in dictory or json format
gig_data = scraper.gig_scrape(gig_url)

# returns the scraped profile's data in dictory or json format
profile_data = scraper.profile_scrape(profile_url)

# print data or do what ever you want to do with it
print(gig_data)
print(profile_data)
```

### Result: GIG_SCRAPE
```json
{
    "user_name": "deesmithvo",
    "title": "Voiceover",
    "categories_breadcrumbs": [
        "Music & Audio",
        "Voice Over"
    ],
    "rating": "5",
    "ratings_count": "292",
    "images": [
        "https://fiverr-res.cloudinary.com/videos/so_74.656115,t_main1,q_auto,f_auto/vr222n7r11jhrypou4tw/provide-high-quality-voice-overs-to-help-bring-life-to-your-projects.png",
        "..."
    ],
    "description": "... HIGHEST QUALITY voice over recordings on FIVERR! Please read full description before submitting an order.ELITE talent and SUPERIOR customer service.With over 13 years of experience in vocal recording and engineering, your words are in good hands, Let me tell your story and add a little magic to your next project.As a dynamic African American male voice ...",
    "meta_data": {
        "Gender": [
            "Male"
        ],
        "Language": [
            "English"
        ],
        "Purpose": [
            "Video Narration",
            "TV",
            "eLearning"
        ],
        "Accent": [
            "English - American"
        ],
        "Age Range": [
            "Adult"
        ],
        "Tone": [
            "Calming",
            "Casual",
            "Corporate",
            "Dramatic",
            "Energetic"
        ]
    },
    "seller_bio": "Unique and dynamic voice overs that bring life to any project!",
    "profile_photo": "https://fiverr-res.cloudinary.com/t_profile_original,q_auto,f_auto/attachments/profile/photo/092096782fcd79252a1c8bce84951a81-1616396583081/ae9bdd13-6917-4a93-80bb-d3623ab533bc.png",
    "user_stats": {
        "From": "United States",
        "Member since": "Jan 2021",
        "Avg. response time": "1 hour",
        "Last delivery": "1 day"
    },
    "user_discription": "A refreshing African American millennial male voice over artist ready to help you tell your story and bring your project to life.\n",
    "price_and_features": {
        "Number of words": {
            "price": "$50",
            "discription": "",
            "features": [
                "HQ Audio File (WAV format))"
            ]
        }
    },
    "gig_tags": [
        "male voice over",
        "audio recording",
        "narration",
        "voice acting",
        "voice talent"
    ],
    "delivery_days": "3 Days Delivery",
    "revisions": "1 Revision"
}

```

### Result: PROFILE_SCRAPE
```json
{
  "user": {
      "name": "bishwasbh",
      "photo": "https://fiverr-res.cloudinary.com/t_profile_original,q_auto,f_auto/attachments/profile/photo/602e60b8e98a3d98ebf47508e874051e-1619826399837/c9ce5be4-1cd8-4a3d-abba-323b3096c69a.jpg",
      "level": "",
      "bio": "Fiverr software developer for python, django, automation, webscraping",
      "from": "Nepal",
      "member_since": "Jul 2018",
      "response_time": "6 hours",
      "recent_delivery": "1 month",
      "description": "Hello, I am the best fiverr Django Python developer, Web Scrapping and Automation Expert. I have huge expertise in frontend and backend (Django) development. We have completed 174+ projects with different clients at various marketplaces since 2016, we have proficiency in the feild of Python Django Web Development and, Web Scrapping and Automation feild. We have 2+ years of hands on experience in Django Web Development and our team has 3.7+ experience in Django.",
      "languages": [
          [
              "English",
              "Basic"
          ],
          [
              "Nepali(\u0928\u0947\u092a\u093e\u0932\u0940)",
              "Native/Bilingual"
          ],
          [
              "Hindi(\u0939\u093f\u0902\u0926\u0940)",
              "Conversational"
          ],
          [
              "Polish(polski)",
              "Basic"
          ]
      ],
      "skill_set": [
          "Python programming",
          "Python django",
          "Javascript",
          "Web application",
          "Wordpresss",
          "Bootstrap",
          "Web development",
          "Wordpress",
          "Django",
          "Mysql",
          "Postgresql",
          "Cpanel",
          "Heroku",
          "Python programmer",
          "Jquery"
      ]
  },
  "gig_info": {
      "gigs": [
          [
              "I will install, setup or update flarum on cpanel, cloud server",
              "/bishwasbh/install-setup-or-configure-flarum-on-cpanel-cloud-server?context_referrer=user_page&ref_ctx_id=37227c7bbf14f51135f6ad8bef05d80c&pckg_id=1&pos=1&seller_online=true"
          ],
          [
              "I will deploy django in cpanel server",
              "/bishwasbh/deploy-django-in-cpanel-server?context_referrer=user_page&ref_ctx_id=37227c7bbf14f51135f6ad8bef05d80c&pckg_id=1&pos=2&seller_online=true"
          ],
          [
              "I will develop bots, web scraping, automation, and custom scripts",
              "/bishwasbh/do-web-scraping-in-python-with-requests-and-beautifulsoup4?context_referrer=user_page&ref_ctx_id=37227c7bbf14f51135f6ad8bef05d80c&pckg_id=1&pos=3&seller_online=true"
          ],
          [
              "I will deploy django in heroku or pythonanywhere",
              "/bishwasbh/deploy-django-in-pythonanywhere?context_referrer=user_page&ref_ctx_id=37227c7bbf14f51135f6ad8bef05d80c&pckg_id=1&pos=4&seller_online=true"
          ],
          [
              "I will python programming articles and seo",
              "/bishwasbh/python-programming-articles-and-seo?context_referrer=user_page&ref_ctx_id=37227c7bbf14f51135f6ad8bef05d80c&pckg_id=1&pos=5&seller_online=true"
          ],
          [
              "I will develop django forum, tool web, portal, django blog and cms",
              "/bishwasbh/develop-a-django-website?context_referrer=user_page&ref_ctx_id=37227c7bbf14f51135f6ad8bef05d80c&pckg_id=1&pos=6&seller_online=true"
          ],
          [
              "I will develop tool website and web apps",
              "/bishwasbh/develop-tool-website-and-web-apps?context_referrer=user_page&ref_ctx_id=37227c7bbf14f51135f6ad8bef05d80c&pckg_id=1&pos=7&seller_online=true"
          ]
      ],
      "profile_ratings": {
          "seller_communication_level": "5",
          "recommended_to_friend": "5",
          "service_as_described": "5"
      },
      "reviews": [
          {
              "buyer_name": "wesleyboy245",
              "given_rating": "5",
              "country_name": "United States"
          },
          {
              "buyer_name": "wesleyboy245",
              "given_rating": "5",
              "country_name": "United States"
          },
          {
              "buyer_name": "zoleoab",
              "given_rating": "5",
              "country_name": "Sweden"
          },
          {
              "buyer_name": "nftprotocol",
              "given_rating": "5",
              "country_name": "United States"
          },
          {
              "buyer_name": "zoleoab",
              "given_rating": "5",
              "country_name": "Sweden"
          }
      ]
  }
}

```

### Precautions
Please follow these precautions while using the fiverr api:
- Try not to scrape the same url frequently without any break
- Try to scrape multiple url in some time internal/break 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPL](https://choosealicense.com/licenses/gpl-3.0/)