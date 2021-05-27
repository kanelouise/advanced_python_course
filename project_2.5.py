import sqlite3
import json

db_name = 'session_2.db'
table_name = 'revenue'
fname = 'revenue.json'

conn = sqlite3.connect(f'../{db_name}')
c = conn.cursor()

dod = {}

query = 'SELECT *  from revenue;'
table = c.execute(query)
header = ("name", "state", "cost")

for row in table:
    name = row[0]
    state = row[1]
    cost = row[2]

    inner = dict(zip(header, row))

    dod[inner['name']] = inner


output = json.dumps(dod, indent=4)

with open(f'../{fname}', 'w') as outfile:
    json.dump(output, outfile)
