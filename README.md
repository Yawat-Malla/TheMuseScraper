# HR Web Scraping Assignment

**Student:** Yawat Malla
**Course:** Web Scraping / HR Analytics Assignment

---

## Assignment Objective

The objective of this project was to collect **Human Resource–related data** from publicly accessible job platforms using automated scraping techniques. The assignment required:

* Identification of a site providing HR/job-related data
* Extraction of real structured data
* Individual implementation
* Clear documentation of source and method
* Target of approximately **1000 observations**

This project satisfies the requirements through the development of a Python-based scraper that collects structured job data suitable for HR analytics exploration.

---

## Data Source Used

### TheMuse Job API

* Website: https://www.themuse.com
* API Endpoint: https://www.themuse.com/api/public/jobs
* Access Method: Public JSON API

### Description

TheMuse provides structured job listings including company information, job classification, experience levels, and location metadata. The API supports pagination, enabling large-scale data collection.

### Reason for Selection

* Reliable structured JSON output
* Richer metadata compared to many job boards
* Pagination support enabling **1000+ observations**
* Includes job classification fields useful for HR-oriented analysis

---

## Project Implementation

* Language: Python 3.12
* Scraper Script: `themuse_scraper.py`
* Output Format: Excel (`.xlsx`)
* Final Dataset Size: **1000+ job records**

---

## Extracted Dataset Attributes

The dataset contains fields directly obtained or derived from the API:

### Core Job Information

* Job ID
* Job Title
* Job Type
* Model Type
* Short Name

### Company Information

* Company Name
* Company ID
* Company Short Name

### Classification Metadata

* Categories
* Category Count
* Levels
* Level Count

### Location Metadata

* Locations
* Location Count

### Posting Information

* Publication Date

### Derived Analytical Features

* Description Length
* Description Presence Indicator

### Reference Links

* Landing Page URL
* Detail Page URL

All attributes were derived from actual API responses without introducing artificial placeholder data.

---

## How to Run

### 1. Create Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

(Windows)

```bash
env\Scripts\activate
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Execute Scraper

```bash
python themuse_scraper.py
```

---

### 4. Output

The dataset is saved as:

```
muse_jobs_expanded.xlsx
```

Ready for inspection or further HR analytics processing.

---

## References

TheMuse Public API
https://www.themuse.com/api/public/jobs

Assignment brief provided by course instructor.
