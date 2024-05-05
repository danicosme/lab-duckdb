CREATE TABLE IF NOT EXISTS coffee_shop.{table} AS
SELECT *
FROM '{abs_path}\{table}.csv'