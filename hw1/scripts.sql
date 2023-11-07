CREATE DATABASE homework1;

CREATE TABLE IF NOT EXISTS authors (
    id integer UNIQUE, 
    full_name varchar(255), 
    sex boolean, 
    birth_date date, 
    avatar bytea
);

CREATE TABLE IF NOT EXISTS books (
    id integer UNIQUE, 
    title varchar(255), 
    is_published boolean, 
    created_at date,
    author_id integer REFERENCES authors(id)
);

