fileName = "sequences.txt"

ins = open(fileName, 'r')
for line in ins:
	line = line.rstrip('\r\n')
	
	# Here I am reversing and complementing at the same time.
	# You could also do it as separate steps, it will just be 
	# less efficient (not a big deal on a small dataset).
	revCompl = ""
	for nt in line:
		if nt == "A":
			revCompl = "T" + revCompl
		elif nt == "T":
			revCompl = "A" + revCompl
		elif nt == "G":
			revCompl = "C" + revCompl
		elif nt == "C":
			revCompl = "G" + revCompl
		else:
			# The below isn't strictly necessary, but it makes for more robust code.
			# A good warning/error message should state: (1) the problem, (2) the data that 
			# caused the problem, and (3) what the code will do about the problem.
			print ">> Warning: Encountered unknown nt:", nt
			print "	Keeping unknown nt as-is."
			revCompl = nt + revCompl 
			
	# We don't want to print until we've looped through the whole sequence.
	# So this print statement should be outside of the sequence for-loop
	# (but NOT outside the file for-loop)
	print revCompl 
	
ins.close()