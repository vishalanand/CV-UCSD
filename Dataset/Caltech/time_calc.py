f = open("hpu5.data", 'r')
sums=0
for line in f:
    lines = line.split()
    sums = sums + float(lines[2])
print sums
print sums/366