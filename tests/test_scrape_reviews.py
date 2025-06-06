import pytest
import pandas as pd
import os
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from scripts.task1_data_collection.scrape_reviews import scrape_reviews

def test_scrape_reviews():
    """Test the scrape_reviews function for CBE."""
    print("Testing scraping for Commercial Bank of Ethiopia...")
    bank_name = "Commercial Bank of Ethiopia"
    app_id = "com.combanketh.mobilebanking"  # Commercial Bank of Ethiopia app ID
    reviews_data = scrape_reviews(bank_name, app_id, count=10)  # Small count for testing
    assert isinstance(reviews_data, list), f"Expected list of reviews, got {type(reviews_data)}"
    assert len(reviews_data) > 0, f"No reviews scraped for {bank_name}; check app ID or network"
    assert all(
        key in reviews_data[0] for key in ["bank", "review", "rating", "date", "source"]
    ), f"Review data missing required fields: {reviews_data[0].keys()}"
    assert all(
        isinstance(r["rating"], int) and 1 <= r["rating"] <= 5 for r in reviews_data
    ), f"Invalid ratings found in {bank_name} reviews: {[r['rating'] for r in reviews_data]}"
    print(f"Success: Scraped {len(reviews_data)} test reviews for {bank_name}")

def test_raw_files():
    """Test raw CSV files for all banks."""
    banks = [
        "commercial_bank_of_ethiopia",
        "bank_of_abyssinia",
        "dashen_bank"
    ]
    for bank in banks:
        file = f"data/raw/{bank}_reviews_raw.csv"
        if os.path.exists(file):
            print(f"Checking raw file for {bank.replace('_', ' ').title()}...")
            df = pd.read_csv(file)
            assert len(df) >= 400, f"{file} has {len(df)} reviews, expected at least 400"
            assert all(
                col in df.columns for col in ["bank", "review", "rating", "date", "source"]
            ), f"{file} missing columns: {set(['bank', 'review', 'rating', 'date', 'source']) - set(df.columns)}"
            print(f"Success: {file} valid with {len(df)} reviews")
        else:
            pytest.skip(f"Raw file {file} not found; run scrape_reviews.py first")

def test_cleaned_file():
    """Test the cleaned CSV output for all banks."""
    output_file = "data/processed/cleaned_reviews.csv"
    if os.path.exists(output_file):
        print("Checking cleaned CSV...")
        df = pd.read_csv(output_file)
        assert len(df) >= 1200, f"Cleaned CSV has {len(df)} reviews, expected at least 1200"
        assert df.isnull().sum().sum() / len(df) < 0.05, f"Missing data rate {(df.isnull().sum().sum() / len(df)):.2%} exceeds 5% limit"
        assert all(
            col in df.columns for col in ["bank", "review", "rating", "date", "source"]
        ), f"Cleaned CSV missing columns: {set(['bank', 'review', 'rating', 'date', 'source']) - set(df.columns)}"
        assert df["rating"].between(1, 5).all(), f"Invalid ratings found: {df['rating'].unique()}"
        bank_counts = df.groupby("bank").size().to_dict()
        assert bank_counts.get("Commercial Bank of Ethiopia", 0) >= 400, f"CBE has {bank_counts.get('Commercial Bank of Ethiopia', 0)} reviews, expected 400+"
        assert bank_counts.get("Bank of Abyssinia", 0) >= 400, f"BOA has {bank_counts.get('Bank of Abyssinia', 0)} reviews, expected 400+"
        assert bank_counts.get("Dashen Bank", 0) >= 400, f"Dashen has {bank_counts.get('Dashen Bank', 0)} reviews, expected 400+"
        print(f"Success: Cleaned CSV valid with {len(df)} reviews: {bank_counts}")
    else:
        pytest.skip("Cleaned CSV not found; run preprocess_reviews.py first")