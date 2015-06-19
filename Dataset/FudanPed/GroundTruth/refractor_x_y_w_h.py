#Run it in the folder to be converted; i.e. the 1_FudanPed_xmin_ymin_xmax_ymax folder
import os, glob
path = "./"
filenames = next(os.walk(path))[2]
#print filenames

for filename in filenames:
	if not(filename.endswith('.dat')):
		continue
	#if(filename=="refractor_x_y_w_h.py"):
	#	continue;
	f=open(filename, 'r');
	print filename
	text=f.read();
	text2 = text.split("\n")
	x_min = []
	y_min = []
	x_max = []
	y_max = []
	iterate=0
	for line in text2:
		if(line==''):
			continue
		#print ":D",line
		numbers = line.split();
		x_min.append(int(numbers[0]))
		y_min.append(int(numbers[1]))
		x_max.append(int(numbers[2]))
		y_max.append(int(numbers[3]))
		print x_min[iterate], y_min[iterate], x_max[iterate], y_max[iterate]
		print x_min[iterate], y_min[iterate], x_max[iterate]-x_min[iterate], y_max[iterate]-y_min[iterate]
		
		dir_path = os.path.join("new")  # will return 'feed/address'
		
		try:
			os.makedirs(dir_path)                             # create directory [current_path]/feed/address
		except OSError:
			pass # already exists
		f1 = open(os.path.join(dir_path, filename), 'a')
		f1.write(str(x_min[iterate])+" "+str(y_min[iterate])+" "+str(x_max[iterate]-x_min[iterate])+" "+str(y_max[iterate]-y_min[iterate])+"\n")
		iterate=iterate+1