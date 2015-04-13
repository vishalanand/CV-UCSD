import os, glob
path = "./"
filenames = next(os.walk(path))[2]
print filenames

#for filename in glob.iglob(os.path.join('Test', '*', '*.txt')):
for filename in filenames:
	f=open(filename, 'r');
	f.readline();
	print filename
	for line in f:
		print line,