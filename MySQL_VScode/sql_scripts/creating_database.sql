-- This script will create the database in which we will be working

CREATE DATABASE IF NOT EXISTS ratings; -- ignore this warning
USE ratings;
CREATE TABLE ratings (
    name VARCHAR(256),
    rating VARCHAR(120),
    region VARCHAR(256));