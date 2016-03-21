fileName = "sequences.txt"
totalLen = 0
numSeqs = 0

ins = open(fileName, 'r')
for line in ins:
	line = line.rstrip('\r\n')
	print len(line)
	
	totalLen = totalLen + len(line)
	numSeqs = numSeqs + 1
ins.close()

print ""
print "Avg len:", float(totalLen) / numSeqs