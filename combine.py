import os
import json

files = os.listdir("leads")

all_leads = []

for file in files:
    with open(f"leads/{file}", "r") as f:
        leads = json.load(f)
        for lead in leads:
            if lead not in all_leads:
                all_leads.append(lead)

with open("all_leads.json", "w") as f:
    json.dump(all_leads, f, indent=2)