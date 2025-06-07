# Customer Experience Analytics for Fintech Apps

This project analyzes user reviews of mobile banking apps for three Ethiopian banks: **Commercial Bank of Ethiopia**, **Bank of Abyssinia**, and **Dashen Bank**. The goal is to extract customer experience insights through data collection, preprocessing, sentiment analysis, and thematic analysis, meeting KPIs of 90%+ sentiment score coverage and identifying 3+ themes per bank.

## Project Structure

- `data/raw/`: Raw scraped reviews.
- `data/processed/`: Cleaned and processed CSVs (e.g., `cleaned_reviews.csv`, `sentiment_reviews.csv`).
- `figures/`: Visualization PNGs (e.g., `sentiment_distribution.png`).
- `scripts/task1_data_collection/`: Task 1 scripts for scraping and preprocessing.
- `scripts/data/`: Task 2 scripts for analysis and visualization.
- `scripts/notebooks/`: Jupyter notebooks for exploration (e.g., `task2_analysis.ipynb`).
- `tests/`: Unit tests for Task 2.
- `docs/`: Documentation, including LaTeX report (`report.tex`).
- `requirements.txt`: Python dependencies.
- `.github/workflows/`: CI/CD configuration for GitHub Actions.

## Prerequisites

- **Python**: 3.13
- **OS**: Windows (adaptable to Linux/macOS)
- **Virtual Environment**: Recommended
- **Dependencies**: Listed in `requirements.txt`
- **Spacy Model**: `en_core_web_sm`

## Setup

1. **Clone Repository**:

   ```bash
   git clone https://github.com/Yihenew21/Customer-Experience-Analytics-for-Fintech-Apps-from-App-reviews.git
   cd Customer-Experience-Analytics-for-Fintech-Apps-from-App-reviews
   ```

2. **Create Virtual Environment**:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download Spacy Model**:

   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **Create Directories**:
   ```bash
   mkdir -p data/raw data/processed figures scripts/task1_data_collection scripts/notebooks docs
   ```

## Task 1: Data Collection and Preprocessing

Collects and cleans Google Play Store reviews for the three banks’ mobile apps.

### Scripts

- `scripts/task1_data_collection/scrape_reviews.py`: Scrapes reviews using `google-play-scraper`.
- `scripts/task1_data_collection/preprocess_reviews.py`: Cleans reviews (removes duplicates, nulls).

### Run Task 1

1. Update `scrape_reviews.py` with correct app IDs (e.g., `com.cbe.mobilebanking`).
2. Execute:
   ```bash
   python scripts/task1_data_collection/scrape_reviews.py
   python scripts/task1_data_collection/preprocess_reviews.py
   ```

### Outputs

- `data/raw/reviews.csv`: Raw scraped reviews.
- `data/processed/cleaned_reviews.csv`: Cleaned reviews with columns `bank`, `review`, `rating`, `date`.

### Verify

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/cleaned_reviews.csv'); print(df.groupby('bank').size())"
```

Expected: Counts for Commercial Bank of Ethiopia, Bank of Abyssinia, Dashen Bank.

## Task 2: Sentiment and Thematic Analysis

Analyzes reviews for sentiment and themes, handling Amharic reviews via translation.

### Scripts

- `scripts/data/preprocess_nlp.py`: Preprocesses reviews with Spacy, translates Amharic using `deep-translator`.
- `scripts/data/sentiment_analysis.py`: Applies VADER and DistilBERT sentiment analysis.
- `scripts/data/thematic_analysis.py`: Identifies 3+ themes per bank using TF-IDF.
- `scripts/data/visualize_results.py`: Generates sentiment and theme visualizations.

### Run Task 2

1. Ensure `cleaned_reviews.csv` contains all three banks.
2. Execute:
   ```bash
   python scripts/data/preprocess_nlp.py
   python scripts/data/sentiment_analysis.py
   python scripts/data/thematic_analysis.py
   python scripts/data/visualize_results.py
   ```

### Outputs

- `data/processed/preprocessed_reviews.csv`: Preprocessed reviews with tokens.
- `data/processed/sentiment_reviews.csv`: Review-level sentiment scores.
- `data/processed/sentiment_aggregates.csv`: Aggregated sentiment by bank and rating.
- `data/processed/thematic_reviews.csv`: Review-level themes.
- `data/processed/theme_aggregates.csv`: Aggregated theme counts by bank.
- `data/processed/amharic_reviews.csv`: Untranslated Amharic reviews.
- `figures/sentiment_distribution.png`: Sentiment distribution by bank.
- `figures/theme_counts.png`: Theme counts by bank.

### Verify

- Check banks:
  ```bash
  python -c "import pandas as pd; df = pd.read_csv('data/processed/sentiment_reviews.csv'); print(df['bank'].unique())"
  ```
  Expected: `['Commercial Bank of Ethiopia', 'Bank of Abyssinia', 'Dashen Bank']`
- Check sentiment coverage:
  ```bash
  python -c "import pandas as pd; df = pd.read_csv('data/processed/sentiment_reviews.csv'); print(f'Coverage: {len(df.dropna(subset=[\"vader_label\", \"distilbert_label\"]))/len(df):.2%}')"
  ```
  Expected: ≥90%
- Check themes:
  ```bash
  python -c "import pandas as pd; df = pd.read_csv('data/processed/theme_aggregates.csv'); print(df.groupby('bank')['themes'].nunique())"
  ```
  Expected: ≥3 per bank

## Tests

Run unit tests for Task 2:

```bash
pytest tests/ -v
```

- `tests/test_sentiment_analysis.py`: Tests sentiment analysis.
- `tests/test_thematic_analysis.py`: Tests thematic analysis.

## Exploratory Analysis

Explore results in:

- `scripts/notebooks/task2_analysis.ipynb`: Visualizes sentiment, themes, and provides insights.

Run:

```bash
jupyter notebook
```

## Documentation

- `docs/report.tex`: LaTeX report summarizing methodology, results, and recommendations.
  - Compile with a LaTeX editor (e.g., Overleaf) or `pdflatex docs/report.tex`.

## Deliverables

- **Task 1**:
  - `data/processed/cleaned_reviews.csv`
- **Task 2**:
  - CSVs: `sentiment_reviews.csv`, `sentiment_aggregates.csv`, `thematic_reviews.csv`, `theme_aggregates.csv`, `amharic_reviews.csv`
  - Plots: `sentiment_distribution.png`, `theme_counts.png`
  - Notebook: `task2_analysis.ipynb`
  - Report: `report.tex`
  - Pull Request URL

## CI/CD

- GitHub Actions runs linting (`flake8`) and tests on push/PR.
- Fix linting issues:
  ```bash
  pip install flake8 autopep8
  flake8 . --max-line-length=88 --extend-ignore=E203,E501
  autopep8 --in-place --aggressive --max-line-length=88 --ignore=E203,E501 scripts/**/*.py tests/*.py
  ```

## Contributing

1. Create a branch (e.g., `task-2`).
2. Commit changes with clear messages.
3. Push and create a PR to `main`.
4. Ensure CI passes.

## License

[Add license, e.g., MIT]
