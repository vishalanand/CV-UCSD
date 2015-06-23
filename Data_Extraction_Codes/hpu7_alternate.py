'''
[image no] [x y w h] [confidence value] [nth bb in image]
'''
acc = []

with open('reorder.txt', 'r') as file:
  for line in file:
    a = line.split()
    b = []
    #b.append(int(a[0]))
    b.append(int(a[0]))
    b.append(float(a[1]))
    b.append(int(a[2]))
    acc.append(b)
    #print b
#c = sorted(acc, key=lambda x: x[1])
c = sorted(acc, key=lambda x:(-x[1], x[0], x[2]))
#print c
count = len(c)
count_2 = count / 2
d = []
for i in range(count_2):
  #print c[i]
  #print c[count - i - 1]
  d.append(c[i])
  d.append(c[count - i - 1])
if count%2==1:
  #print c[count/2]
  d.append(c[count/2])
  #print "Middle element"
print d
final = []
for tup in d:
  temp = []
  temp.append(tup[0])
  temp.append(tup[2])
  final.append(temp)
print "The final sorted files in alternating(max, min) order : "
print final
print len(final)