#stuck on the extra credit, created a dictionary, but can't get the sort yet. will revisit
import re

fname = '../market_discussion.txt'
f = open(fname)
f = f.read()

find = re.findall(r'([A-Z]+)\,\s([\+\-]\d+)', f)
find = sorted(find)
tot = len(find)

find = dict(find)

#sorted_find = sorted(find.items(), reverse = True)

print(find)
print(f'found {tot} Stock Symbols and price mentions in this article')


