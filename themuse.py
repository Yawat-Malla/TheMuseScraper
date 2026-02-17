import requests
import pandas as pd

all_jobs = []
page = 1

while True:
    url = f"https://www.themuse.com/api/public/jobs?page={page}"
    r = requests.get(url)

    if r.status_code != 200:
        break

    data = r.json()
    jobs = data.get("results", [])
    if not jobs:
        break

    for j in jobs:
        locations = j.get("locations", [])
        categories = j.get("categories", [])
        levels = j.get("levels", [])

        description = j.get("contents", "")

        all_jobs.append({
            "ID": j.get("id"),
            "Title": j.get("name"),
            "ShortName": j.get("short_name"),
            "Type": j.get("type"),
            "ModelType": j.get("model_type"),

            "Company": j.get("company", {}).get("name"),
            "CompanyID": j.get("company", {}).get("id"),
            "CompanyShort": j.get("company", {}).get("short_name"),

            "Locations": ", ".join(l.get("name") for l in locations),
            "LocationCount": len(locations),

            "Categories": ", ".join(c.get("name") for c in categories),
            "CategoryCount": len(categories),

            "Levels": ", ".join(l.get("name") for l in levels),
            "LevelCount": len(levels),

            "PublicationDate": j.get("publication_date"),

            # Derived / useful features
            "DescriptionLength": len(description),
            "HasDescription": bool(description),

            # URLs
            "LandingURL": j.get("refs", {}).get("landing_page"),
            "DetailURL": j.get("refs", {}).get("detail"),
        })

    print(f"Page {page} collected")
    page += 1


df = pd.DataFrame(all_jobs)
df.drop_duplicates(subset=["ID"], inplace=True)

df.to_excel("muse_jobs.xlsx", index=False)
print("Saved rows:", len(df))
