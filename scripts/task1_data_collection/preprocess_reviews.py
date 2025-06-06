import pandas as pd
import os

# Directories
RAW_DATA_DIR = "data/raw" #
PROCESSED_DATA_DIR = "data/processed"
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

def preprocess_reviews():
    """Preprocess raw review data and save as a single cleaned CSV."""
    # List of raw CSV files
    bank_files = [
        f"{RAW_DATA_DIR}/{bank}_reviews_raw.csv"
        for bank in [
            "commercial_bank_of_ethiopia",
            "bank_of_abyssinia",
            "dashen_bank"
        ]
    ]

    # Load and combine raw CSVs
    dfs = []
    for file in bank_files:
        if os.path.exists(file):
            df = pd.read_csv(file)
            dfs.append(df)
            print(f"Loaded {len(df)} reviews from {file}")
        else:
            print(f"File not found: {file}")

    if not dfs:
        print("No data files found. Please run scrape_reviews.py first.")
        return

    combined_df = pd.concat(dfs, ignore_index=True)

    # Remove duplicates based on review text, date, and bank
    initial_count = len(combined_df)
    combined_df = combined_df.drop_duplicates(subset=["review", "date", "bank"], keep="first")
    print(f"Removed {initial_count - len(combined_df)} duplicates")

    # Handle missing data
    combined_df = combined_df.dropna(subset=["review", "rating"])
    print(f"Removed {initial_count - len(combined_df)} rows with missing review or rating")

    # Normalize dates to YYYY-MM-DD
    combined_df["date"] = pd.to_datetime(combined_df["date"]).dt.strftime("%Y-%m-%d")

    # Ensure rating is integer
    combined_df["rating"] = combined_df["rating"].astype(int)

    # Verify data quality
    print(f"\nProcessed Data Info:")
    print(f"Total reviews: {len(combined_df)}")
    print(f"Missing values:\n{combined_df.isnull().sum()}")
    print(f"Reviews per bank:\n{combined_df.groupby('bank').size()}")

    # Save cleaned data
    output_path = f"{PROCESSED_DATA_DIR}/cleaned_reviews.csv"
    combined_df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    preprocess_reviews()