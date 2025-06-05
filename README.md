# Customer Experience Analytics for Fintech Apps

## Overview

This repository contains code and deliverables for the B5W2 challenge, analyzing Google Play Store reviews for three Ethiopian banks (CBE, BOA, Dashen) to improve mobile apps.

## Folder Structure

- `data/`: Raw and processed datasets, SQL scripts.
- `scripts/`: Python scripts for scraping, analysis, database, and insights.
- `tests/`: Unit tests for scripts.
- `reports/`: Interim and final reports.

## Setup

1. Clone the repository: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Oracle XE or PostgreSQL (see `data/sql/` for schema).
4. Run scripts in `scripts/` (e.g., `python scripts/task1_data_collection/scrape_reviews.py`).

## Methodology

- **Task 1**: Scraped 1,200+ reviews using `google-play-scraper`, cleaned data with `pandas`.
- **Task 2**: Performed sentiment analysis with DistilBERT, thematic analysis with TF-IDF and manual clustering.
- **Task 3**: Stored data in Oracle XE with `oracledb`.
- **Task 4**: Generated insights and visualizations using `matplotlib` and `seaborn`.

## Challenges

- Handled scraping rate limits by batching requests.
- Used PostgreSQL as a fallback for Oracle XE setup issues.
