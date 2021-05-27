import re

fname = '../access_log.txt'
f = open(fname)


bytes_count = {}
for line in f:
    matchobj1 = re.search(r'(~([A-Za-z]{2,3}\d+))', line)
    matchobj2 = re.search(r'(\d{3}\s+(\d+)$)', line)
    if not matchobj1 or not matchobj2:
        continue
    nyu_id = matchobj1.group(2)
    bytes = matchobj2.group(2)  # or group(0) if you're pulling the entire match
    bytes = int(bytes)
    if nyu_id not in bytes_count:
        bytes_count[nyu_id] = 0
    bytes_count[nyu_id] = bytes_count[nyu_id] + bytes

#print(bytes_count)

count = 0
sorted_keys = sorted(bytes_count, key = bytes_count.get)
for key in sorted_keys:
    if bytes_count[key] > 10000000:
        print(f'{key}: {bytes_count[key]}')
        count += len(bytes_count)
print(f'{count} users found')




# for line in f
#     search for nyu id
#     extract nyu id from line (assign to nyu_id)
#     search for bytes
#     extract bytes from line (assign to bytes)
#     if nyu_id not in bytes_count:
#         bytes_count[nyu_id] = 0
#     bytes_count[nyu_id] = bytes_count[nyu_id] + bytes






