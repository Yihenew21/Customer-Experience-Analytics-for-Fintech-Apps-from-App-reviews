import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import pytest
from scripts.analysis.sentiment_analysis import analyze_sentiment

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "bank": ["Commercial Bank of Ethiopia"],
        "review": ["Great service and fast transactions"],
        "rating": [5]
    })

def test_analyze_sentiment(sample_df):
    df = analyze_sentiment(sample_df)
    assert "vader_label" in df.columns
    assert "vader_score" in df.columns
    assert "distilbert_label" in df.columns
    assert "distilbert_score" in df.columns
    assert df["vader_label"].iloc[0] in ["positive", "negative", "neutral"]
    assert df["distilbert_label"].iloc[0] in ["positive", "negative"]