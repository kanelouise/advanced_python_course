import csv

fname = 'weather_newyork_tiny.csv'

f = open(f"../{fname}")
reader = csv.reader(f)
header_row = next(reader)

nlist = []


for row in reader:
    date = row[0]
    mean_temp = row[1]
    precip = row[17]
    events = row[19]

    new_row = [date, mean_temp, precip, events]

    nlist.append(new_row)

f.close()

narrow = open('weather_newyork_narrow.csv', 'w', newline='')
writer = csv.writer(narrow)
writer.writerows(nlist)

narrow.close()

