d = []
file_name = 1


with open('try.txt') as f:
	for lines in f:
		if lines == '\n':
			f1.close()
			file_name += 1
		else:
			if file_name in d:
			    f1.write(lines)              
			else:
			    d.append(file_name)
			    f1 =  open("{}.txt".format(file_name), "w")
			    f1.write(lines)
