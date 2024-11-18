import duckdb
import pandas as pd

conn = duckdb.connect('c:/GAVB/Neogrid/duckDB/learning_sql.db')

conn.sql('select Location from location_data limit 3')
conn.sql('show databases')

print(conn.sql('from location_data limit 3'))
