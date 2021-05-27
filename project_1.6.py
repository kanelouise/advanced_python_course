import csv

fname = 'revenue.csv'

f = open(f"../{fname}")
reader = csv.reader(f)
header_row = next(reader)

rev = []
rev.append(header_row)

for row in reader:
    company = row[0]
    state = row[1]
    price = row[2]

    new_row = [company, state, price]

    if state == 'NY':
        rev.append(new_row)

f.close()

rny = open('revenue_ny.csv ', 'w', newline='')
writer = csv.writer(rny)
writer.writerows(rev)

rny.close()





