-- database_setup.sql
-- Script to set up and populate the Oracle XE database for fintech app reviews

-- Drop tables if they exist (for reset purposes)
DROP TABLE reviews CASCADE CONSTRAINTS;
DROP TABLE banks CASCADE CONSTRAINTS;

-- Create banks table
CREATE TABLE banks (
    bank_id NUMBER GENERATED ALWAYS AS IDENTITY,
    bank_name VARCHAR2(100) NOT NULL,
    created_date DATE DEFAULT SYSDATE,
    PRIMARY KEY (bank_id)
);

-- Create reviews table
CREATE TABLE reviews (
    review_id NUMBER GENERATED ALWAYS AS IDENTITY,
    bank_id NUMBER,
    review_text VARCHAR2(1000),
    rating NUMBER,
    review_date DATE,
    created_date DATE DEFAULT SYSDATE,
    PRIMARY KEY (review_id),
    FOREIGN KEY (bank_id) REFERENCES banks(bank_id)
);

-- Insert sample bank data
INSERT INTO banks (bank_name) VALUES ('Commercial Bank of Ethiopia');
INSERT INTO banks (bank_name) VALUES ('Bank of Abyssinia');
INSERT INTO banks (bank_name) VALUES ('Dashen Bank');
COMMIT;

-- Insert sample review data (replace with full dataset)
INSERT INTO reviews (bank_id, review_text, rating, review_date) VALUES 
(1, 'Great app, fast transactions!', 5, TO_DATE('2025-06-01', 'YYYY-MM-DD'));
INSERT INTO reviews (bank_id, review_text, rating, review_date) VALUES 
(2, 'User-friendly but crashes sometimes.', 3, TO_DATE('2025-06-02', 'YYYY-MM-DD'));
INSERT INTO reviews (bank_id, review_text, rating, review_date) VALUES 
(3, 'Easy access, needs updates.', 4, TO_DATE('2025-06-03', 'YYYY-MM-DD'));
-- Add more INSERT statements for all >1,000 reviews from cleaned_reviews.csv
-- Example generation: Use a script to convert CSV to INSERT statements
COMMIT;

-- Verify data
SELECT b.bank_name, COUNT(r.review_id) as review_count
FROM banks b
LEFT JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_name;