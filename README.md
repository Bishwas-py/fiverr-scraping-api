# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install fiverr-api.

```bash
pip install fiverr-api
```

## Usage

```python
from fiverr_api import Scrape

# returns 'words'
url = "https://www.fiverr.com/otem_global/your-kajabi-teachable-web
site-expert-fix-your-pipeline-set-up-online-courses"

# initialize fiverr scrapper
scraper = Scrape()

# returns the scraped data in dictory or json format
data = scraper.gig_scrape(url)

# print data or do what ever you want to do with it
print(data)
```

### Result
```json
{
    "user_name": "otem_global",
    "title": "MEMBERSHIP WEBSITE",
    "categories_breadcrumbs": [
        "Programming & Tech",
        "Website Builders & CMS",
        "Full Website Creation"
    ],
    "rating": "4.9",
    "ratings_count": "24",
    "images": [
        "https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/185639232/original/2e1b0f882eb8f14aba30dee8f2c30b19beb880b4/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.jpg",
        "https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs2/185639232/original/22703c2453d6b56d800fd7b0a3f7e41f11e5d8cf/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.jpg",
        "https://fiverr-res.cloudinary.com/images/t_thumbnail3_3,q_auto,f_auto/gigs/185639232/original/2e1b0f882eb8f14aba30dee8f2c30b19beb880b4/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.jpg",
        "https://fiverr-res.cloudinary.com/images/t_thumbnail3_3,q_auto,f_auto/gigs2/185639232/original/22703c2453d6b56d800fd7b0a3f7e41f11e5d8cf/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.jpg",
        "https://fiverr-res.cloudinary.com/images/t_thumbnail3_3,q_auto,f_auto/gigs3/185639232/original/e0ccd7f99ec328d0ca169b84b15f8919ae096ecd/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.jpg",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/a2f81b45b8eac37972a07bbf7be51ebc-1625667569/screencapture-mindirosser-mykajabi-LinkedIn-Profile-Mini-Training-Opt-In-Page-2021-07-07-15_17_03/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/4f27179e071e327dfd1cb1dd5b4a3c7b-1624107456/screencapture-freedomjoiross-morning-routine-pdf-2021-06-19-13_56_55/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/14fb953d5ea836f43395502dde039952-1623466136/screencapture-millennialhomeinvestor-2021-06-12-03_48_05/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/085627c842912c6889a0da552132816f-1622257065/screencapture-joiross-2021-05-27-13_46_26/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/ab6fa82339999a3b5e7b902314cab5fb-1621556283/screencapture-newagetalks-servicess-2021-05-20-20_40_41/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/33573d07ff305348e2b5ef0118773828-1621173138/screencapture-credit-360-group-mykajabi-optin-page-2021-05-16-11_56_03/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/7b065b4300ef902ca5ffa68b2c30bc4e-1619606557/screencapture-benedita-sousa-mykajabi-stackingjoints-2021-04-27-18_19_24/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.jpg",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/aebf8e8171b8c66b04446e311e2b513c-1619443045/screencapture-app-kartra-pages-sites-preview-3-2021-04-26-14_03_12/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/9f142a47b0826c931df20caf44dc8ddd-1616899170/screencapture-freedomjoiross-download-essential-Growth-Mindsets-to-Experience-Freedom-2021-03-28-04_37_39/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/5e4dbf2846e809081e26281e143ab378-1616720810/screencapture-onlydo-online-2021-03-25-23_46_30/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/f2fbb5acdca2aa749496773b714a0cca-1616632175/screencapture-joiross-2021-03-24-18_48_07%20(1)/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/5e9aa003f64ec09bb55574ecaee1f800-1616586256/screencapture-trupro-kartra-page-comingsoon-2021-03-24-12_43_01/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/4c4d66306dd9e10eb075b035605e1457-1616016584/screencapture-educatorsforchange2008-about-founder-2021-03-17-22_29_24/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/d74f75b2e9427f552a3778fb126e9143-1615168725/sales%20page_%20landing%20page_%20converting%20landing%20page_%20kajabi%20expert_%20kajabi%20website/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.jpg",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/10dfbcef3ec512a28f557c0bd65a440a-1613857929/screencapture-the-collar-club-mykajabi-admin-index-preview-2021-02-20-22_09_20/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/af7fe111ddddf78fc74f6a84de1d0bdf-1611433996/screencapture-websites-godaddy-en-GB-editor-7c131a20-a79c-43e1-b6f3-bd3e11e2e558-f2fd5e3c-9bb7-4c00-837b-68475e3418bc-2021-01-23-16_55_44/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png",
        "https://fiverr-res.cloudinary.com/images/t_smartwm/t_delivery_thumb,q_auto,f_auto/attachments/delivery/asset/7b68358143f75fdc37bc63681c903f6f-1611063140/consultation-page-updated/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses.png"
    ],
    "description": "About This GigHi, welcome to “ i will be your kajabi website expert, coaching website expert, fix your pipeline, set up online courses“ gigAre you looking for:A HIGH CONVERTING Kajabi websiteA Kajabi online course web-site using THINKIFIC/KARTRAA Kajabi landing page or sales funnelOr looking to transfer your current website to Kajabi?You’ve just landed on the right gig. We can help you with any Kajabi task. We have a flexible schedule and We are easy to work with. If you’re looking for a team of seller who’ll deliver high quality services with all transparency, you are on the right gig.\xa0WHAT WE PROVIDEFull Kajabi website creationProfessional Kajabi landing pageHigh converting Kajabi sales funnel, pipelineOnline course web-site, membership web sites (Kajabi, Thinkfic, Teachable)Ecommerce FunctionalitySEO OptimizationOn-Page SEO and moreWHY ME?Quality ServiceQuick and professional100% satisfactory work.Effective customer services.If you’re looking for a sales funnel on Clickfunnels, Kartra, Getresponse or click funnel, feel free to check out my other gigs. CONTACT ME NOW to get your KAJABI tasks done for you by an expert. I hope to hear from you.R",
    "meta_data": {
        "Platform": [
            "Wix"
        ],
        "Specialization": [
            "Blog",
            "Business",
            "Education",
            "Portfolio",
            "Entertainment",
            "Non-profit",
            "Wedding",
            "Podcasting",
            "Online Communities",
            "Forms",
            "Crowdfunding",
            "Wiki /Knowledge",
            "SaaS",
            "Job Board",
            "Portal",
            "Brochure"
        ],
        "Supported plugin types": [
            "Marketing",
            "Payment",
            "Forum",
            "Social Media",
            "Customer Support",
            "Shipping",
            "Inventory",
            "Analytics",
            "Video",
            "Form",
            "Events",
            "Music",
            "Chat ",
            "Membership",
            "Map",
            "FAQ",
            "Gallery"
        ]
    },
    "seller_bio": None,
    "profile_photo": "https: //fiverr-res.cloudinary.com/t_profile_original,q_auto,f_auto/attachments/profile/photo/61cf220c614f3e5bba7cd3d05e9a0c59-1627605699698/34ee6407-f943-451d-aab1-66abcbcc9ed3.jpg",
    "user_stats": {
        "From": "Nigeria",
        "Member since": "Nov 2020",
        "Avg. response time": "1 hour",
        "Last delivery": "4 days"
    },
    "user_discription": "I Help People to Create Successful Sales Funnels and fast Websites\n\nAs a Sales Funnel Hacker and Designer, I help passionate coaches, consultants, and small businesses improve their marketing, conversion, and sales by designing high-converting funnels that appeal to their target audience.\n\nHere’s how I can help you. My areas of expertise include following, but are not limited to:\n\n--- Clickfunnels,  Building high converting sales funnels & product creation, landing page design & integration. SalesFunnels by using ClickFunnels. Sales Pages, Checkouts, Upsells Downsells and much more.\nThank you.",
    "price_and_features": {
        "Basic": {
            "price": "$25",
            "discription": "Fully Responsive one page Kajabi website with Optin form",
            "features": [
                "Design Customization",
                "Content Upload",
                "Responsive Design",
                "E-Commerce Functionality"
            ]
        },
        "Standard": {
            "price": "$150",
            "discription": "3 Pages kajabi  website + ecommerce functionality",
            "features": [
                "Design Customization",
                "Content Upload",
                "Responsive Design",
                "E-Commerce Functionality"
            ]
        },
        "Premium": {
            "price": "$250",
            "discription": "Fully converting kajabi website + ecommerce functionality + membership setup",
            "features": [
                "Design Customization",
                "Content Upload",
                "Responsive Design",
                "E-Commerce Functionality"
            ]
        }
    },
    "gig_tags": [
        "membership funnel",
        "kajabi website",
        "kajabi pipeline",
        "online course",
        "kajabi expert"
    ]
}

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPL](https://choosealicense.com/licenses/gpl-3.0/)