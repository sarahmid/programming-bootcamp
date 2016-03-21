dnaSeq = raw_input("Enter a DNA sequence: ")
motif = raw_input("Enter a motif to search for: ")

if len(motif) > len(dnaSeq):
	print "Error: motif sequence is longer than DNA sequence."
else:
	if motif in dnaSeq:
		print "Found the motif in the sequence."
	else:
		print "Did not find the motif in the sequence."