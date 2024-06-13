from bs4 import BeautifulSoup
import json
from requests import get
import re

bas_url = "https://www.yellowpages.com/search?search_terms=financial%20adviser&geo_location_terms=florida&page="

def get_info(lead):
    try:
        return {
            "business_name": lead.find("a", class_="business-name")["href"],
            "phone": lead.find("div", class_=re.compile(r'phone')).text,
        }
    except:
        return None

def main():
    for page in range(1, 101):
        url = bas_url + str(page)
        response = get(url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        leads = soup.find_all("div", class_="info")
        leads_info = [get_info(lead) for lead in leads if get_info(lead) is not None]
        with open(f"./leads/leads_{page}.json", "w") as f:
            json.dump(leads_info, f, indent=2)
        print("Finished page {}".format(page))

main()

