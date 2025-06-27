# IRS Credentialed Professional Scraper

A fully automated, cross-platform web scraper that extracts credentialed tax professionals from the official [IRS Return Preparer Office](https://irs.treasury.gov/rpo/rpo.jsf) site based on dynamic user input. Designed with clean modular architecture and robust input validation, this project utilizes Selenium, pandas, and Python 3 to efficiently collect and export structured data into CSV format.

[Watch Demo Video](https://pranavvadd.github.io/IRS-Scraper-Backend/demo.mp4) *(Outdated: Same functionality, but current CSV styled differently: will update soon)*
---

## Key Highlights

- Modular Design: Separated logic into validation, scraping, and utility components for scalability and readability.
- User-Centric Input Flow: Validates and guides user input interactively with intuitive prompts.
- Real Data Pipeline: Collects credentialed tax professional data across multiple pages and outputs a clean, structured CSV.
- Cross-Platform File Access: Automatically opens the output file regardless of OS (macOS, Windows, Linux).
- Fast and Scalable: Designed to handle multiple pages of results and custom filtering across six credential categories.

---

## Tech Stack

- Language: Python 3.11
- Libraries: selenium, pandas
- Browser Automation: ChromeDriver
- Environment: Cross-platform (tested on macOS and Windows)

---

## Why This Project?

I built this to explore how automation and clean code principles could be applied to real-world datasets provided by government portals. The IRS RPO database offered a complex structure that required form interaction, conditional filtering, and pagination — the perfect challenge for testing my Selenium and data processing skills.

---

## Features in Detail

| Feature               | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| Input Validation       | Ensures users provide valid integers, ZIP codes, and boolean responses     |
| IRS Website Automation | Interacts with dropdowns, checkboxes, and navigates multiple pages         |
| Credential Filtering   | Filters by Attorney, CPA, Enrolled Agent, Actuary, and more                |
| CSV Export             | All results are saved to `contacts.csv` with structured columns            |
| File Launcher          | Automatically opens the result in your system’s default CSV viewer         |

---

## 🆕 New CSV Format Enhancements *(Updated June 27th, 2025)*

These improvements make the CSV easier to use, more structured, and ready for manual enrichment.

- **Separated Name Columns**: Full names are now split into distinct **First Name** and **Last Name** columns. The script automatically detects the comma in names like `"Doe, Jane"` and separates them accordingly.
- **Manual Entry Fields**: Added two new columns — `Email` and `Phone Number` — which are left **blank** for users to fill out manually. These details are often unavailable or unreliable from the IRS database, making manual entry more practical.
- **Other Info Consolidation**: Details such as **City**, **Distance**, and other location-related metadata are now grouped into a single column called `Other Info`. This provides helpful context for users while completing contact fields like `Email` and `Phone Number`.

---
## Run It Yourself

Requirements:  
`pip install selenium pandas`

---

## Run Script:

`python main.py`

---

## You’ll be prompted for:

- ZIP Code  
- Search distance (in miles)  
- Number of pages to scrape  
- Which credential types to include (yes/no)  

---

## Code Architecture

- `irs-credential-scraper/`  
- `main.py` — Orchestrates the workflow from input to output  
- `input_validation.py` — Handles user interaction and sanitization  
- `web_scraping.py` — Core Selenium scraping logic  
- `utils.py` — OS-aware utility for opening CSV  
- `contacts.csv` — Exported results (generated after run)  
- `README.md` — This documentation file  

---

## Lessons and Takeaways

- Learned how to automate interaction with complex web forms using Selenium, including dropdowns, checkboxes, and pagination.  
- Developed strong input validation techniques to ensure robust user interaction and prevent invalid data entry.  
- Gained experience structuring a modular Python project for clarity, maintainability, and scalability.  
- Improved skills in data extraction, cleaning, and exporting to CSV format using pandas.  
- Learned to handle cross-platform compatibility for launching files in different operating systems.  

---

## Future Enhancements

- Improve the scraper’s resilience by implementing robust error handling to better manage website load delays, unexpected changes in the IRS site structure, and element availability issues.
- Explore replacing Selenium with direct API calls or alternative data sources where possible to increase reliability, reduce maintenance, and speed up data extraction.
- Add support for exporting data in additional formats such as Excel or JSON to increase flexibility for end users.
- Implement multi-threading or asynchronous scraping techniques to improve performance and reduce runtime.
- Enhance filtering options with more detailed credential categories and geographic search parameters to provide more precise results.

---

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/irs-credential-scraper.git  
cd irs-credential-scraper
