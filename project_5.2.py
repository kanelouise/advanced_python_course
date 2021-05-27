#commented out the function and keys variable in exchange for lambda
#curious: could the key for loop be written as a lambda as well?

import json

fh = open('../weny_dod_tiny.json')
dod = json.load(fh)

keys = sorted(dod, key = lambda i: dod[i]['date'])

# def by_date(arg):
#     return dod[arg]['date']

# keys = sorted(dod, key=by_date)

for key in keys:
    print(f'{key}:  {dod[key]}')
