import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Dict
from scripts.analysis.preprocess_nlp import preprocess_reviews

themes: Dict[str, List[Dict[str, str]]] = {
    "Commercial Bank of Ethiopia": [
        {"name": "Account Access", "keywords": ["login", "access", "sign", "account", "authentication"]},
        {"name": "Transactions", "keywords": ["transfer", "payment", "withdraw", "deposit", "send"]},
        {"name": "Customer Support", "keywords": ["help", "support", "service", "assist", "call"]},
    ],
    "Bank of Abyssinia": [
        {"name": "Digital Banking", "keywords": ["app", "mobile", "online", "digital", "internet"]},
        {"name": "Service Fees", "keywords": ["charge", "fee", "cost", "price", "expensive"]},
        {"name": "ATM Availability", "keywords": ["atm", "cash", "machine", "withdraw", "terminal"]},
    ],
    "Dashen Bank": [
        {"name": "Online Banking", "keywords": ["internet", "online", "web", "digital", "e-banking"]},
        {"name": "Loan Services", "keywords": ["loan", "credit", "finance", "borrow", "mortgage"]},
        {"name": "Branch Services", "keywords": ["branch", "office", "teller", "queue", "counter"]},
    ]
}

def assign_themes(text: str, bank: str) -> List[str]:
    """Assign themes based on keywords for a specific bank."""
    if not isinstance(text, str) or not text.strip():
        return []
    assigned_themes = []
    bank_themes = themes.get(bank, [])
    for theme in bank_themes:
        if any(keyword in text.lower() for keyword in theme["keywords"]):
            assigned_themes.append(theme["name"])
    return assigned_themes if assigned_themes else ["General"]

def thematic_analysis(df: pd.DataFrame, text_column: str = "review") -> pd.DataFrame:
    """Apply thematic analysis to DataFrame."""
    df = df.copy()
    df["themes"] = df.apply(lambda x: assign_themes(x[text_column], x["bank"]), axis=1)
    return df

def aggregate_themes(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate themes by bank."""
    exploded = df.explode("themes")
    return exploded.groupby(["bank", "themes"]).size().reset_index(name="count")

if __name__ == "__main__":
    input_csv = "data/processed/sentiment_reviews.csv"
    output_csv = "data/processed/thematic_reviews.csv"
    df = pd.read_csv(input_csv)  # Full data
    # df = pd.read_csv(input_csv).head(400)  # Uncomment for testing
    df = thematic_analysis(df)
    df.to_csv(output_csv, index=False)
    print(f"Saved thematic analysis for banks: {df['bank'].unique().tolist()} to {output_csv}")
    aggregates = aggregate_themes(df)
    aggregates.to_csv("data/processed/theme_aggregates.csv", index=False)
    print(f"Saved theme aggregates to data/processed/theme_aggregates.csv")