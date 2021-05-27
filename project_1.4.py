import csv

filename = 'nyse-listed_csv_tiny.csv'

tickerco = {}
def get_lookup(filename):
    tickerco = {}

    f = open(f"../{filename}")

    for row in f:
        items = row.split(',')
        name = items[1]
        ticker = items[0]
        tickerco[ticker] = name
    return tickerco
