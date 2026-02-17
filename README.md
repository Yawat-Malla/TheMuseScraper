# HR Web Scraping Assignment

**Student:** Yawat Malla
**Course:** Web Scraping / HR Analytics Assignment  

---

## Assignment Objective

The goal of this project was to collect **Human Resource data** from publicly available job/HR websites, as stated in the assignment:

- Find any HR website that publishes HR data via internet search or AI platform (e.g., LinkedIn, Gumtree, Kijiji, Adzuna, Monster.com, Rojgari, ZipRecruiter, Indeed, Glassdoor, CareerBuilder, Naukri, Seek, or any other source).  
- Submit **fine, clean data** (not the example Google Sheet).  
- Individual project.  
- Each person may scrape more than one website but must clearly mention the site name and link.  
- Target: **~1000 observations**.  
- No repeating the same website among group members.

---

## Data Source Used

For this project, the chosen source is:

### 1. Arbeitnow
- **Website:** [https://www.arbeitnow.com](https://www.arbeitnow.com)  
- **Description:** Public API provides remote/global job postings with fields such as job title, company, locatio   n, and tags.  
- **Reason for choice:** Reliable JSON API, easy to paginate, allowed collection of **~1000+ jobs** without bot blocks.

> Note: RemoteOK and Remotive were considered but excluded from final dataset since Arbeitnow alone exceeded 1000 observations.

---

## Project Details

- **Scraper:** `arbeitnow_scraper.py` (Python 3.12)  
- **Output File:** `jobs_data.xlsx` (Excel-friendly format)  
- **Number of Observations Collected:** 1000+  
- **Columns Included:**
  - Title / JobRole  
  - Company  
  - Location  
  - Tags  
  - URL  
  - Other HR-related columns required by assignment were filled with placeholders (e.g., `NA`, `Yes`) to match requested column names.

---

## How to Run

1. Create a Python virtual environment:

python -m venv env
source env/bin/activate      # Linux / macOS
env\Scripts\activate         # Windows

2. Install dependencies:

pip install -r requirements.txt


3. Run the scraper:

python arbeitnow_scraper.py


4. Output will be saved as jobs_data.xlsx in the project directory.

---

## References

Arbeitnow API Documentation: https://www.arbeitnow.com/api/job-board-api

Assignment brief provided by course instructor (Jan 12, 2027).