CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
);

CREATE TABLE money (
    id SERIAL PRIMARY KEY,
    amount INTEGER
);

CREATE TABLE questions (
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

CREATE TABLE highscores (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    score INTEGER
);