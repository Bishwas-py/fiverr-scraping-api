from fiverr_api import Scrape


url = "https://www.fiverr.com/otem_global/your-kajabi-teachable-website-expert-fix-your-pipeline-set-up-online-courses"
scraper = Scrape()
data = scraper.gig_scrape(url)

print(f"{data}")
