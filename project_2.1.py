import sqlite3
import csv

db_name = 'session_2.db'
table_name = 'revenue'
csv_filename = 'revenue_from_db_csv'

def sql_to_csv(db_filename, table_name,csv_filename):
    conn = sqlite3.connect(f'../{db_name}')
    c = conn.cursor()
    query = f'SELECT * from {table_name}'
    c.execute(query)

    newfile = open(f'../{csv_filename}','w',newline = '')
    writer = csv.writer(newfile)
    for row in c:
        writer.writerow(row)
    newfile.close()



sql_to_csv(db_name, table_name, csv_filename)
