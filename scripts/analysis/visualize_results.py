import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(df: pd.DataFrame):
    """Plot sentiment distribution by bank."""
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x="bank", hue="distilbert_label")
    plt.title("Sentiment Distribution by Bank")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("figures/sentiment_distribution.png")
    plt.close()

def plot_theme_counts(df: pd.DataFrame):
    """Plot theme counts by bank."""
    plt.figure(figsize=(12, 8))
    sns.barplot(data=df, x="count", y="themes", hue="bank")
    plt.title("Theme Counts by Bank")
    plt.tight_layout()
    plt.savefig("figures/theme_counts.png")
    plt.close()

if __name__ == "__main__":
    sentiment_csv = "data/processed/sentiment_reviews.csv"
    theme_csv = "data/processed/theme_aggregates.csv"
    df_sentiment = pd.read_csv(sentiment_csv)
    df_themes = pd.read_csv(theme_csv)
    print(f"Visualizing data for banks: {df_sentiment['bank'].unique().tolist()}")
    plot_sentiment_distribution(df_sentiment)
    plot_theme_counts(df_themes)
    print("Saved plots to figures/")