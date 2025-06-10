import cx_Oracle
import pandas as pd

def insert_reviews():
    """Insert cleaned review data into Oracle XE database.

    This script connects to the Oracle XE database (XEPDB1), creates 'banks' and 'reviews' tables if
    they don't exist, and inserts data from 'cleaned_reviews.csv'. It dynamically maps bank names to IDs,
    handles errors, and commits changes.

    Requirements:
    - Oracle XE with 'bank_reviews' user and password 'Biruk1221'.
    - 'cleaned_reviews.csv' with columns: bank, review, rating, review_date.

    Raises:
    - cx_Oracle.Error: If database operations fail.
    """
    # Database connection details
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
    connection = cx_Oracle.connect(user="bank_reviews", password="Biruk1221", dsn=dsn)
    cursor = connection.cursor()

    try:
        # Create tables if they don't exist
        cursor.execute("""
            CREATE TABLE banks (
                bank_id NUMBER GENERATED ALWAYS AS IDENTITY,
                bank_name VARCHAR2(100) NOT NULL,
                created_date DATE DEFAULT SYSDATE,
                PRIMARY KEY (bank_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE reviews (
                review_id NUMBER GENERATED ALWAYS AS IDENTITY,
                bank_id NUMBER,
                review_text VARCHAR2(1000),
                rating NUMBER,
                review_date DATE,
                created_date DATE DEFAULT SYSDATE,
                PRIMARY KEY (review_id),
                FOREIGN KEY (bank_id) REFERENCES banks(bank_id)
            )
        """)

        # Load cleaned data
        df = pd.read_csv("data/processed/cleaned_reviews.csv")

        # Insert unique banks dynamically
        banks = df['bank'].drop_duplicates()
        for bank in banks:
            cursor.execute("INSERT INTO banks (bank_name) VALUES (:1)", (bank,))
        connection.commit()

        # Map bank names to bank_ids dynamically
        cursor.execute("SELECT bank_id, bank_name FROM banks")
        bank_mapping = {row[1]: row[0] for row in cursor.fetchall()}
        df['bank_id'] = df['bank'].map(bank_mapping)

        # Validate and insert reviews
        successful_inserts = 0
        for index, row in df.iterrows():
            try:
                cursor.execute("""
                    INSERT INTO reviews (bank_id, review_text, rating, review_date)
                    VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'))
                """, (row['bank_id'], row['review'], row['rating'], row['review_date']))
                successful_inserts += 1
            except cx_Oracle.Error as e:
                print(f"Error inserting review {index}: {e}")
        connection.commit()

        print(f"Successfully inserted {successful_inserts} out of {len(df)} reviews into Oracle database.")

    except cx_Oracle.Error as error:
        print(f"Database error: {error}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    insert_reviews()