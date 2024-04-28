Fiverr API Scraper is a Python library that allows you to extract detailed information from Fiverr fluently without
any restriction. It returns `JSON` responses and `BS4-HTML-SOUP` according to your will.

## Features

- Extract detailed information from Fiverr; gig, recommendations, profiles, bios and all.
- No restrictions
- ScraperAPI supported

## Installation

You can install the Fiverr API Scraper using pip:

```bash
pip install fiverr-api
```

## Usage

Below are examples of how to use the Fiverr API Scraper to extract data from Fiverr gig pages and user profiles.

### Scrape Example

```python
from fiverr_api import session

session.set_scraper_api_key("XYZ-SCRAPER_API_KEY")
response = session.get("https://www.fiverr.com/username/your-gig-slug") # your fiverr url should be here
json_data = response.props_json() # gives you JSON
print(response.soup) # gives you beautiful soup instance
# You can use `response.soup` to further extract your information. 
```
> Get your ScraperAPI key [here](https://www.scraperapi.com/?fp_ref=enable-fiverr-api).

## Project Structure

The Fiverr API Scraper is organized into several modules to enhance code readability and maintainability:

- `fiverr_api`
  - `__init__.py`: For exporting `session`
- `fiverr_api.utils`
  - `req.py`: Extending requests for Fiverr scraping
  - `scrape_utils.py`: Utilities for scraping

`scraper.py` gives you a function named `get_perseus_initial_props()` which returns the initial props of
the Fiverr page. This function is used by the modules to extract initial `JSON` data.

## License

[GPL](https://choosealicense.com/licenses/gpl-3.0/)

## Contributing

New [pull requests](https://github.com/Bishwas-py/fiverr-scraping-api) are welcome.
For major changes, please open an issue first to discuss what you would like to change.

## Author

Check more of [my projects](https://bishwas.net/projects).