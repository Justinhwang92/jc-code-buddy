from dotenv import load_dotenv
from linkedIn import scrape_linkedin_profile

load_dotenv()

data = scrape_linkedin_profile()
print(data)
