'''
[image no] [x y w h] [confidence value] [nth bb in image]
'''
image = []
confidence = []

acc = []

with open('reorder.txt', 'r') as file:
  for line in file:
    '''
    w = line.split()
    image.append(w[0])
    confidence.append(w[1])
    bb.append(w[2])
    print w
    '''
    #a = tuple(int(x.strip()) for x in raw_input().split(','))
    #a = tuple(int(x.strip()) for x in line.split(','))
    a = line.split()
    b = []
    b.append(int(a[0]))
    b.append(float(a[1]))
    b.append(int(a[2]))
    #c = sorted(b,key=itemgetter(1))
    acc.append(b)
    #print b
#c = sorted(acc, key=lambda x: x[1])
c = sorted(acc, key=lambda x:(-x[1], x[0], x[2]))
#print c
final = []
for tup in c:
  temp = []
  temp.append(tup[0])
  temp.append(tup[2])
  final.append(temp)
print "The final sorted files in decreasing order : "
print final
print len(final)