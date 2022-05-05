CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question TEXT,
    correct TEXT,
    wrong1 TEXT,
    wrong2 TEXT,
    wrong3 TEXT
);

CREATE TABLE advanced_questions (
    id SERIAL PRIMARY KEY,
    question TEXT,
    correct TEXT,
    wrong1 TEXT,
    wrong2 TEXT,
    wrong3 TEXT
);

CREATE TABLE hard_questions (
    id SERIAL PRIMARY KEY,
    question TEXT,
    correct TEXT,
    wrong1 TEXT,
    wrong2 TEXT,
    wrong3 TEXT
);

CREATE TABLE millionaires (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    username TEXT
);

CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    username TEXT,
    comment TEXT
);

