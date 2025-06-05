# Customer Experience Analytics for Fintech Apps

This repository contains the solution for the "Customer Experience Analytics for Fintech Apps" challenge, part of the 10Academy Kaim Week 5 training program. The project analyzes Google Play Store reviews for three Ethiopian banks—Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank—to derive insights for improving their mobile apps.

## Project Overview

The challenge comprises two tasks:

1. **Task 1: Data Collection and Preprocessing** (Completed): Scrape 1,200+ reviews (400+ per bank), preprocess them, and validate data quality.
2. **Task 2: Sentiment and Thematic Analysis** (Pending): Perform sentiment analysis and identify key themes in reviews.

The repository uses Git branches (`task-1`, `task-2`) and includes scripts, tests, notebooks, visualizations, and documentation.

## Task 1: Data Collection and Preprocessing

### Objectives

- Scrape at least 400 reviews per bank (1,200+ total) from the Google Play Store.
- Preprocess reviews into `cleaned_reviews.csv` with columns: `bank`, `review`, `rating`, `date`, `source`.
- Ensure <5% missing data and validate with unit tests.

### Deliverables

- **Scripts**:
  - `scripts/task1_data_collection/scrape_reviews.py`: Scrapes reviews using `google-play-scraper`, with empty review handling and rate limit delays.
  - `scripts/task1_data_collection/preprocess_reviews.py`: Combines raw CSVs, removes duplicates, normalizes dates, and saves `cleaned_reviews.csv`.
- **Tests**:
  - `tests/test_scrape_reviews.py`: Validates scraping (CBE), raw CSVs (400+ reviews per bank), and cleaned CSV (1,200+ reviews, <5% missing data).
- **Notebook**:
  - `scripts/notebooks/task1_exploration.ipynb`: Performs exploratory data analysis (EDA), generating plots in `figures/` (e.g., rating distributions).
- **Visualizations**:
  - `figures/rating_distribution.png`: Overall rating histogram.
  - `figures/avg_rating_per_bank.png`: Average ratings per bank.
  - `figures/review_length_distribution.png`: Review length histogram.
- **Data** (Ignored in Git):
  - `data/raw/*.csv`: Raw reviews per bank.
  - `data/processed/cleaned_reviews.csv`: Cleaned dataset.
- **Documentation**:
  - This README and commit history.

### Results

- Scraped 1,200+ reviews (400+ per bank for CBE, BOA, Dashen).
- Generated `cleaned_reviews.csv` with <5% missing data, valid ratings (1–5), and dates (YYYY-MM-DD).
- Passed all unit tests with descriptive messages.
- Conducted EDA, confirming data quality and generating insights (e.g., rating distributions, review lengths) for Task 2.
- **Challenges**:
  - Resolved CBE scraping failure (`com.cbe.birr` app ID) by adding empty review handling and delays.
  - Fixed Matplotlib style error in Notebook (replaced `seaborn` with `sns.set_theme()`).

### Setup Instructions

1. **Clone Repository**:

```bash
   git clone <repository-url>
   cd Customer-Experience-Analytics-for-Fintech-Apps-from-App-reviews
```

2. **Set Up Virtual Environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. **Install Dependencies**:

```bash
   pip install -r requirements.txt
```

4. **Run Scripts**:

```bash
python scripts/task1_data_collection/scrape_reviews.py
python scripts/task1_data_collection/preprocess_reviews.py
```

5. **Run Tests**:

```bash
pytest tests/test_scrape_reviews.py -vs
```

6. **Run Notebook**:

```bash
jupyter notebook
# Open scripts/notebooks/task1_exploration.ipynb
```

## Directory Structure

```
Customer-Experience-Analytics-for-Fintech-Apps-from-App-reviews/
├── data/
│ ├── raw/ # Ignored: raw CSVs per bank
│ ├── processed/ # Ignored: cleaned_reviews.csv
├── scripts/
│ ├── task1_data_collection/
│ │ ├── scrape_reviews.py
│ │ ├── preprocess_reviews.py
├── notebooks/
│ │ ├── data_exploration.ipynb
├── tests/
│ ├── test_scrape_reviews.py
├── figures/ # EDA plots
├── .gitignore
├── README.md
├── requirements.txt

```
