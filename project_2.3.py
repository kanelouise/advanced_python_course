import sqlite3
import csv

db_name = 'session_2.db'
fname = 'weather_newyork.csv'

f = open(f"../{fname}")
reader = csv.reader(f)
header_row = next(reader)

conn = sqlite3.connect(f'../{db_name}')
c = conn.cursor()

rows = csv.reader(f)

q1 = 'DROP TABLE IF EXISTS weather_newyork;'
q2 = 'CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT);'
q3 = 'INSERT INTO weather_newyork (date, mean_temp, precip, events) VALUES (?, ?, ?, ?);'

c.execute(q1)
c.execute(q2)
for row in reader:
    date = row[0]
    mean_temp = row[1]
    precip = row[17]
    events = row[19]

    if precip == "T":
        precip = None

    new_row = [date, mean_temp, precip, events]

    c.execute(q3, new_row)

conn.commit()

c.close()
