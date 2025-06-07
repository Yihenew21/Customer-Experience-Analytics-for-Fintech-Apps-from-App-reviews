import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pandas as pd
import spacy
import re
from deep_translator import GoogleTranslator
from typing import List, Tuple

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
translator = GoogleTranslator(source='am', target='en')

AMHARIC_REGEX = re.compile(r'[\u1200-\u137F]')  # Ge'ez script range
TRANSLITERATED_KEYWORDS = ["selam", "betam", "amasegnallo", "yene", "kefel"]  # Common transliterated Amharic

def is_amharic(text: str) -> bool:
    """Detect Amharic script or transliterated Amharic."""
    if not isinstance(text, str):
        return False
    if AMHARIC_REGEX.search(text):
        return True
    if any(keyword in text.lower() for keyword in TRANSLITERATED_KEYWORDS):
        return True
    return False

def translate_to_english(text: str) -> Tuple[str, bool]:
    """Translate Amharic to English, return translated text and success flag."""
    try:
        translation = translator.translate(text)
        return translation, True
    except Exception as e:
        print(f"Translation error: {e}")
        return text, False

def preprocess_text(text: str) -> List[str]:
    """Tokenize, remove stopwords, and lemmatize text using Spacy."""
    if not isinstance(text, str) or not text.strip():
        return []
    doc = nlp(text.lower())
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

def preprocess_reviews(df: pd.DataFrame, text_column: str = "review") -> pd.DataFrame:
    """Apply preprocessing to a DataFrame's text column, handling Amharic."""
    df = df.copy()
    amharic_reviews = []

    # Detect and translate Amharic
    df["is_amharic"] = df[text_column].apply(is_amharic)
    for idx, row in df.iterrows():
        if row["is_amharic"]:
            translated_text, success = translate_to_english(row[text_column])
            if success:
                df.at[idx, text_column] = translated_text
            else:
                amharic_reviews.append(row.to_dict())
    
    # Save Amharic reviews (failed translations)
    if amharic_reviews:
        pd.DataFrame(amharic_reviews).to_csv("data/processed/amharic_reviews.csv", index=False)
        print(f"Saved {len(amharic_reviews)} Amharic reviews to data/processed/amharic_reviews.csv")

    # Fallback: Filter Amharic if no translations
    # df = df[~df["is_amharic"]]  # Uncomment to filter instead of translate

    # Preprocess text
    df["tokens"] = df[text_column].apply(preprocess_text)
    return df.drop(columns=["is_amharic"])

if __name__ == "__main__":
    input_csv = "data/processed/cleaned_reviews.csv"
    output_csv = "data/processed/preprocessed_reviews.csv"
    df = pd.read_csv(input_csv)  # Full data
    # df = pd.read_csv(input_csv).head(400)  # Uncomment for testing
    df = preprocess_reviews(df)
    df.to_csv(output_csv, index=False)
    print(f"Preprocessed {len(df)} reviews for banks: {df['bank'].unique().tolist()}, saved to {output_csv}")