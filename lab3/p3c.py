fileName = "sequences.txt"
totalGC = 0
numSeqs = 0

ins = open(fileName, 'r')
for line in ins:
	line = line.rstrip('\r\n')
	
	seqGC = 0 #this needs to be reset to 0 for each sequence
	for nt in line:
		if (nt == "G") or (nt == "C"):
			seqGC = seqGC + 1
	
	fractGC = float(seqGC) / len(line)
	print fractGC
	
	# add this fraction to the running total so we can compute the avg
	totalGC = totalGC + fractGC
	numSeqs = numSeqs + 1
ins.close()

print ""
print "Avg GC:", float(totalGC) / numSeqs