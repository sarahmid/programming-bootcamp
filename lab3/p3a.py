fileName = "sequences.txt"
ins = open(fileName, 'r')
for line in ins:
	line = line.rstrip('\r\n') #\r is another potential line ending. I check for it just in case. 
	print line
ins.close()