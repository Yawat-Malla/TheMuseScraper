import requests
import pandas as pd

OUTPUT = "jobs_data.xlsx"  
all_jobs = []

def fetch_arbeitnow():
    print("Fetching Arbeitnow jobs...")
    page = 1
    headers = {"User-Agent": "Mozilla/5.0"}

    while True:
        url = f"https://www.arbeitnow.com/api/job-board-api?page={page}"
        try:
            r = requests.get(url, headers=headers, timeout=15)
        except Exception as e:
            print("Request failed:", e)
            break

        if r.status_code == 429:
            print("Rate limit hit — stopping.")
            break
        elif r.status_code != 200:
            print("Non-200 response:", r.status_code)
            break

        try:
            data = r.json()
        except:
            print("Non-JSON response — stopping.")
            break

        jobs = data.get("data", [])
        if not jobs:
            print("No more jobs found — finished pagination.")
            break

        for job in jobs:
            all_jobs.append({
                "Title": job.get("title"),
                "Company": job.get("company_name"),
                "Location": job.get("location"),
                "Tags": "; ".join(job.get("tags", [])), 
                "URL": job.get("url")
            })

        # Pagination 
        if not data.get("links", {}).get("next"):
            break

        page += 1

    print(f"Collected {len(all_jobs)} jobs from Arbeitnow.")
    return all_jobs


if __name__ == "__main__":
    fetch_arbeitnow()

    # Deduplicate by URL
    df = pd.DataFrame(all_jobs)
    df.drop_duplicates(subset=["URL"], inplace=True)

    print("Total after dedupe:", len(df))

    # Save 
    df.to_excel(OUTPUT, index=False)
    print(f"Saved data to '{OUTPUT}'")
