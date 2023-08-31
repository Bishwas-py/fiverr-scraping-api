Fiverr API Scraper is a Python library that allows you to extract detailed information from Fiverr gig pages and user
profiles. This tool can be used to programmatically gather data from Fiverr gigs and profiles, facilitating analysis and
automation of tasks related to Fiverr.

## Features

- Extract detailed information from Fiverr gig pages and user profiles.
- Dynamic scraping of Fiverr pages, also includes the initial props of the page.
- Proxy support.
- Change user-agent or other headers.

## Installation

You can install the Fiverr API Scraper using pip:

```bash
pip install fiverr-api
```

## Usage

Below are examples of how to use the Fiverr API Scraper to extract data from Fiverr gig pages and user profiles.

### Gig Scrape Example

```python
from fiverr_api.scrapers import gig_scrape

# URL of the Fiverr gig you want to scrape
gig_url = "https://www.fiverr.com/some-seller/some-gig-title"

# Scrape gig data
gig_data = gig_scrape(gig_url)

# Print the scraped gig data
print(gig_data)
```

### Profile Scrape Example

```python
from fiverr_api.scrapers import profile_scrape

# URL of the Fiverr profile you want to scrape
profile_url = "https://www.fiverr.com/some-seller"

# Scrape profile data
profile_data = profile_scrape(profile_url)

# Print the scraped profile data
print(profile_data)
```

## Proxy Support

You can use the Fiverr API Scraper with a proxy by setting via `actions.set_proxy()`:

```python
from fiverr_api.utils.actions import actions

# Set proxy
actions.set_proxy({
    "http": "http://username:password@proxy:port",
    "https": "http://username:password@proxy:port"
})
```

## Changing User-Agent or Other Headers

You can change the user-agent or other headers by setting via `actions.set_headers()`:

```python
from fiverr_api.utils.actions import actions

# Set headers
actions.set_headers({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,"
              "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.fiverr.com",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
})

# Set user-agent specifically
actions.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")

# Get headers with actions.headers
print(actions.headers)
```

## Project Structure

The Fiverr API Scraper is organized into several modules to enhance code readability and maintainability:

- `fiverr_api`
    - `gig_scrape.py`: Contains functions to scrape gig-related information.
    - `profile_scrape.py`: Contains functions to scrape user profile information.
- `fiverr_api.utils`
    - `scrape_utils.py`: Contains utility functions for extracting information from HTML elements.
    - `actions.py`: Defines the Actions class responsible for handling HTTP requests.

`scraper.py` gives you a function named `get_perseus_initial_props()` which returns the initial props of
the Fiverr page. This function is used by the other modules to extract initial `JSON` data from the page, and
is also used by `gig_scrape.py` and `profile_scrape.py` to extract data from the page.

## License

[GPL](https://choosealicense.com/licenses/gpl-3.0/)

## Contributing

[Pull requests](https://github.com/Bishwas-py/fiverr-scraping-api) are welcome.
For major changes, please open an issue first to discuss what you would like to change.

## Author

Check more [my projects](https://bishwas.net/projects).