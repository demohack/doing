2021-09-17 01:03 am, start at part 1

answering conceptual questions


2021-09-17 02:27 am, finished with Part 1


2021-09-18 10:06 am


CREATE TABLE movies
(
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  release_year INTEGER NOT NULL,
  runtime INTEGER NOT NULL,
  rating TEXT NOT NULL
);

CREATE TABLE studios
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  start_date DATE
);

CREATE TABLE roles
(
  id SERIAL PRIMARY KEY,
  movie_id INTEGER REFERENCES movies (id) ON DELETE CASCADE,
  star_id INTEGER REFERENCES stars (id) ON DELETE CASCADE
);

CREATE TABLE stars
(
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT,
  birth_date DATE NOT NULL
);
