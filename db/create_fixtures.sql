CREATE TABLE IF NOT EXISTS news (
    id TEXT NOT NULL,
    title TEXT NOT NULL,
    release_date DATE NOT NULL,
    release_time FLOAT,
    link TEXT,
    description TEXT
);
CREATE TABLE IF NOT EXISTS users (
    id BIGINT,
    time_created FLOAT,
    status TEXT,
    last_seen FLOAT
);