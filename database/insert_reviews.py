import cx_Oracle
import pandas as pd

# Connection details for XEPDB1
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
connection = cx_Oracle.connect(user="bank_reviews", password="Biruk1221", dsn=dsn)
cursor = connection.cursor()

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_reviews.csv")

# Map bank names to bank_ids
bank_mapping = {
    'Commercial Bank of Ethiopia': 1,
    'Bank of Abyssinia': 2,
    'Dashen Bank': 3
}
df['bank_id'] = df['bank'].map(bank_mapping)

# Insert data
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reviews (review_id, bank_id, review_text, rating, review_date, created_date)
        VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), SYSDATE)
    """, (index + 1, row['bank_id'], row['review'], row['rating'], row['date']))
connection.commit()

# Close connection
cursor.close()
connection.close()

print(f"Inserted {len(df)} reviews into Oracle database.")