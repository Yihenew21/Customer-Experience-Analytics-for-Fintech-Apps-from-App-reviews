# Customer Experience Analytics for Fintech Apps

This project provides a comprehensive analysis of customer experiences for the fintech applications of Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank, leveraging Google Play Store reviews. The workflow covers data collection, preprocessing, sentiment and thematic analysis, database integration, and the generation of actionable insights and recommendations.

---

## 🚀 Project Overview

**Objective:**  
Extract actionable insights and recommendations to enhance user experience for CBE, BOA, and Dashen Bank apps.

**Key Tasks:**

- **Task 1:** Collect and explore review data.
- **Task 2:** Perform sentiment and thematic analysis.
- **Task 3:** Store cleaned data in Oracle XE.
- **Task 4:** Generate insights, recommendations, and a final report.

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8+
- Oracle XE 21c (with `bank_reviews` user and password `Biruk1221`)
- Virtual environment tool (e.g., `venv`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/customer-experience-analytics.git
   cd customer-experience-analytics
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Oracle XE:**
   - Install Oracle XE and configure the XEPDB1 service.
   - Create the `bank_reviews` user with password `Biruk1221` via SQL Developer or command line.

---

## 📁 Project Structure

```
customer-experience-analytics/
├── data/
│   ├── raw/           # Raw review data (e.g., sentiment_reviews.csv, thematic_reviews.csv)
│   └── processed/     # Cleaned data (e.g., cleaned_reviews.csv)
├── reports/           # Reports and documentation (e.g., final_report.docx)
├── figures/           # Visualization outputs (e.g., sentiment_trends.png)
├── database/
├── notbooks/
│   ├── data_exploration/
│   ├── task2_analysis/
│   └── task4_analysis/ # Jupyter notebook for Task 4 analysis
├── scripts/
│   ├── task1_data_collection/ # Data collection scripts
│   ├── analysis/             # Sentiment and thematic analysis scripts
│   ├── database/             # Database integration scripts
│   └── task4_analysis/       # Insight generation and reporting scripts
├── requirements.txt          # Python dependencies
├── tests/
│   ├── test_scrape_reviews/
│   ├── test_sentiment_analysis/
│   └── test_thematic_analysis/
└── README.md                 # This file
```

---

## 📋 Task Details

### Task 1: Data Collection

- **Purpose:** Gather Google Play Store reviews for CBE, BOA, and Dashen Bank.
- **Output:** Raw data files in `data/raw/`.
- **Steps:** Use web scraping or API calls to collect >1,000 reviews, stored as CSV files.

### Task 2: Sentiment and Thematic Analysis

- **Purpose:** Analyze sentiment and identify themes in reviews.
- **Tools:** Python, pandas, NLTK (VADER), wordcloud.
- **Output:** Visualizations in `figures/` (e.g., `sentiment_trends.png`, `keyword_cloud.png`).

**Workflow:**

1. Preprocess data (clean text, handle missing values).
2. Apply VADER for sentiment scores.
3. Generate word clouds for themes.
4. Save cleaned data to `data/processed/cleaned_reviews.csv`.

### Task 3: Store Cleaned Data in Oracle XE

- **Purpose:** Efficiently store preprocessed data in a database.
- **Tools:** Oracle XE, cx_Oracle.

**Scripts:**

- `scripts/task3_database/database_setup.sql`: Creates banks and reviews tables and inserts sample data.
- `scripts/task3_database/insert_reviews.py`: Dynamically inserts all reviews from `cleaned_reviews.csv`.
- `scripts/task3_database/generate_sql_inserts.py`: Generates `inserts.sql` for bulk data loading.

**Workflow:**

1. Run `database_setup.sql` to set up the schema.
2. Use `generate_sql_inserts.py` to create `inserts.sql` from `cleaned_reviews.csv`.
3. Execute `insert_reviews.py` or append `inserts.sql` to populate the database.
4. Verify with `SELECT COUNT(*) FROM reviews;` (>1,000 rows).

### Task 4: Insights and Recommendations

- **Purpose:** Derive insights, propose improvements, and document findings.
- **Output:** `docs/final_report.docx` with visualizations and analysis.

**Workflow:**

1. Analyze visualizations (e.g., rating and sentiment distributions).
2. Identify drivers (e.g., fast transactions for CBE) and pain points (e.g., crashes for Dashen).
3. Recommend stability improvements and a budgeting tool.
4. Address ethical concerns (e.g., negative skew bias).
5. Compile a 4+ page Word document with images from `figures/`.

---

## ▶️ Usage

1. Collect data and run preprocessing scripts in `scripts/analysis/`.
2. Store data using scripts in `scripts/task3_database/`.
3. Perform analysis in `notbooks/task4_analysis/` and generate the report in `reports/`.
4. Commit changes and push to the repository.

---

## 📦 Dependencies

See `requirements.txt` for the full list. Key packages include:

- `pandas==2.2.2`
- `numpy==1.26.4`
- `matplotlib==3.8.4`
- `seaborn==0.13.2`
- `wordcloud==1.9.3`
- `cx_Oracle==8.3.0`
- `nltk==3.8.1`

---

## 🤝 Contributing

We welcome contributions! To get started:

1. **Fork** this repository.
2. **Create a feature branch:**
   ```bash
   git checkout -b my-feature
   ```
3. **Commit your changes** with a clear message:
   ```bash
   git commit -m "Add my feature"
   ```
4. **Push to your fork:**
   ```bash
   git push origin my-feature
   ```
5. **Open a Pull Request** describing your changes and their purpose.

Please ensure your code follows the project’s style guidelines and passes all tests before submitting a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Special thanks to [10 Academy](https://www.10academy.org/) for providing the project framework and guidance.
- Appreciation to xAI for their support and assistance during development.

---
