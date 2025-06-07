import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline
from typing import Tuple

analyzer = SentimentIntensityAnalyzer()
pipe = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_vader_sentiment(text: str) -> Tuple[str, float]:
    """Compute VADER sentiment label and score."""
    if not isinstance(text, str) or not text.strip():
        return "neutral", 0.0
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]
    if compound >= 0.05:
        return "positive", compound
    elif compound <= -0.05:
        return "negative", compound
    return "neutral", compound

def get_distilbert_sentiment(text: str) -> Tuple[str, float]:
    """Compute DistilBERT sentiment label and score."""
    if not isinstance(text, str) or not text.strip():
        return "neutral", 0.0
    result = pipe(text, truncation=True, max_length=512)[0]
    label = result["label"].lower()
    score = result["score"]
    return label, score

def analyze_sentiment(df: pd.DataFrame, text_column: str = "review") -> pd.DataFrame:
    """Apply VADER and DistilBERT sentiment analysis to DataFrame."""
    df = df.copy()
    df[["vader_label", "vader_score"]] = df[text_column].apply(
        lambda x: pd.Series(get_vader_sentiment(x))
    )
    df[["distilbert_label", "distilbert_score"]] = df[text_column].apply(
        lambda x: pd.Series(get_distilbert_sentiment(x))
    )
    return df

def aggregate_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sentiment by bank and rating."""
    return df.groupby(["bank", "rating"]).agg({
        "vader_label": lambda x: x.value_counts().to_dict(),
        "distilbert_label": lambda x: x.value_counts().to_dict(),
        "vader_score": ["mean", "count"],
        "distilbert_score": "mean"
    }).reset_index()

if __name__ == "__main__":
    input_csv = "data/processed/preprocessed_reviews.csv"
    output_reviews_csv = "data/processed/sentiment_reviews.csv"
    output_aggregates_csv = "data/processed/sentiment_aggregates.csv"
    df = pd.read_csv(input_csv)  # Full data
    # df = pd.read_csv(input_csv).head(400)  # Uncomment for testing
    df = analyze_sentiment(df)
    df.to_csv(output_reviews_csv, index=False)
    print(f"Saved sentiment analysis for banks: {df['bank'].unique().tolist()} to {output_reviews_csv}")
    aggregates = aggregate_sentiment(df)
    aggregates.to_csv(output_aggregates_csv, index=False)
    print(f"Saved sentiment aggregates to {output_aggregates_csv}")