CREATE TABLE banks (
    bank_id NUMBER PRIMARY KEY,
    bank_name VARCHAR2(100) NOT NULL,
    created_date DATE DEFAULT SYSDATE
);

CREATE TABLE reviews (
    review_id NUMBER PRIMARY KEY,
    bank_id NUMBER NOT NULL,
    review_text VARCHAR2(1000),
    rating NUMBER(1) CHECK (rating BETWEEN 1 AND 5),
    review_date DATE,
    created_date DATE DEFAULT SYSDATE,
    FOREIGN KEY (bank_id) REFERENCES banks(bank_id)
);