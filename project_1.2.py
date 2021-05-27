#would love to go over the challenge program in class, time permitting

import statistics

def collect_mean_temps(filename, column_name):
    fh = open(filename)
    headers = next(fh)
    meantemps = []
    for line in fh:
        line = line.rstrip()
        items = line.split(',')
        meantemp = int(items[1])
        meantemps.append(meantemp)
    return meantemps

avg = sum(meantemps)/len(meantemps)

m = statistics.mean(meantemps)
md = statistics.median(meantemps)
stdev = statistics.stdev(meantemps)



