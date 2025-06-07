import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import pytest
from scripts.analysis.thematic_analysis import thematic_analysis

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "bank": ["Commercial Bank of Ethiopia"],
        "review": ["Login issues with the app"],
        "rating": [3]
    })

def test_thematic_analysis(sample_df):
    df = thematic_analysis(sample_df)
    assert "themes" in df.columns
    assert isinstance(df["themes"].iloc[0], list)
    assert "Account Access" in df["themes"].iloc[0]