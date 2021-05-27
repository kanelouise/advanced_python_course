fname = '../revenue.csv'

fh = open(fname)
next(fh)

total = 0.00

mysum = 0.00


for line in fh:
   line = line.rstrip()
   items = line.split(',')
   if items[1] == 'NY':
      revenue = float(items[-1])
      mysum = mysum + revenue
      print(round(revenue, 2))

mysum = round(mysum,2)
print(f"\nsum: {mysum}")

