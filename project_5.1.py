#commented out a lambda that worked as well
import json

fh = open('../weny_lod_tiny.json')   # 'file' object
lod = json.load(fh)


#print(sorted(lod, key = lambda i: int(i['mean_temp'])))


def by_mean_temp(arg):
    return int(arg['mean_temp'])

sorted_dicts = sorted(lod, key=by_mean_temp)

for idict in sorted_dicts:
   print(idict)
