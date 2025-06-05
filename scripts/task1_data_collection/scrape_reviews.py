from google_play_scraper import reviews, Sort
import pandas as pd
import os

# Define banks and their app IDs 
banks = [
    {"name": "Commercial Bank of Ethiopia", "app_id": "com.combanketh.mobilebanking"},
    {"name": "Bank of Abyssinia", "app_id": "com.boa.boaMobileBanking"},
    {"name": "Dashen Bank", "app_id": "com.dashen.dashensuperapp"}
]

# Directory to save raw data
RAW_DATA_DIR = "data/raw" # Define the directory for raw data
os.makedirs(RAW_DATA_DIR, exist_ok=True) # Create the directory if it doesn't exist

# Function to scrape reviews from Google Play Store
def scrape_reviews(bank_name, app_id, count=400):
    """Scrape reviews for a given app from Google Play Store."""
    try: # Attempt to scrape reviews
        result = reviews(
            app_id,
            lang="en",
            country="et",
            sort=Sort.NEWEST,
            count=count
        )[0]
        reviews_data = [
            {
                "bank": bank_name,
                "review": review["content"],
                "rating": review["score"],
                "date": review["at"],
                "source": "Google Play"
            }
            for review in result
        ]
        return reviews_data
    except Exception as e:
        print(f"Error scraping {bank_name}: {e}")
        return []
# Main function to scrape reviews for all banks and save to CSV
def main():
    """Scrape reviews for all banks and save to CSV."""
    all_reviews = []
    for bank in banks: # Iterate through each bank
        print(f"Scraping reviews for {bank['name']}...") # Log the bank being processed
        reviews_data = scrape_reviews(bank["name"], bank["app_id"], count=400) # Scrape reviews for the bank
        if reviews_data: # If reviews were successfully scraped
            df = pd.DataFrame(reviews_data) # Convert to DataFrame
            df.to_csv(f"{RAW_DATA_DIR}/{bank['name'].lower().replace(' ', '_')}_reviews_raw.csv", index=False) # Save individual bank reviews to CSV
            all_reviews.extend(reviews_data) # Add to combined list
            print(f"Saved {len(reviews_data)} reviews for {bank['name']}") # Log the number of reviews saved
        else:
            print(f"No reviews scraped for {bank['name']}") # If no reviews were scraped, log it

    # Save combined raw reviews
    if all_reviews: # If there are any reviews collected
        combined_df = pd.DataFrame(all_reviews) # Convert to DataFrame
        combined_df.to_csv(f"{RAW_DATA_DIR}/all_reviews_raw.csv", index=False) # Save all reviews to a combined CSV
        print(f"Saved {len(all_reviews)} total reviews") # Log the total number of reviews saved
# Run the main function
if __name__ == "__main__":
    main()