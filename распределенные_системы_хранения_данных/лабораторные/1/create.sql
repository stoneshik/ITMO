CREATE TABLE IF NOT EXISTS lab1_first (
    id serial,
    column1 int,
    column2 int,
    column3 int
);
CREATE TABLE IF NOT EXISTS lab1_second (
    id serial,
    "column1'" int,
    "'column2'" int,
    "column3'''" int
);
CREATE TABLE IF NOT EXISTS lab1_third (
    id serial,
    "col""""umn1" int,
    "co""lumn2" int,
    "column''3" int
);
