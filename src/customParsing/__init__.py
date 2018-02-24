import linecache

def read():

	fileName = "/home/lvuser/auto.txt"
	
	timeLine = [""]	
	with open(fileName) as file:
		for line in file:
			if "[" in line:
				timeLine.append(line)
				
	linecache.clearcache()
	
	return timeLine