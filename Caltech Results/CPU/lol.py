for i in range (1, 739):
	g = open("filename",'a')
	string= "cut -d \" \" -f 1-4 test-" + str(i).zfill(3) + ".dat > pro/test-" + str(i).zfill(3) + ".dat\n"
	g.write(string)