#the if statement for the precip == 'T' isn't working as expected. any insight?

import sqlite3
import json

db_name = 'session_2.db'
fname = 'weather_newyork_dod.json'

f = open(f"../{fname}")
dod = json.load(f)
nlist = []
print(dod)

conn = sqlite3.connect(f'../{db_name}')
c = conn.cursor()

q1 = 'DROP TABLE IF EXISTS weather_newyork;'
q2 = 'CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT);'
q3 = 'INSERT INTO weather_newyork (date, mean_temp, precip, events) VALUES (?, ?, ?, ?);'

c.execute(q1)
c.execute(q2)
for ikey in dod:
    idict = dod[ikey]
    date = idict['date']
    mean_temp = idict['mean_temp']
    precip = idict['precip']
    events = idict['events']

    if precip == "T":
        precip = None

    new_row = [date, mean_temp, precip, events]

    c.execute(q3, new_row)

conn.commit()

c.close()

