import sqlite3
db_name = 'session_2.db'

conn = sqlite3.connect(f'../{db_name}')
c = conn.cursor()

q1 = 'DROP TABLE IF EXISTS weather_newyork'
q2 = 'CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT)'

c.execute(q1)

c.execute(q2)


c.close()

