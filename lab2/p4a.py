dnaSeq = raw_input("Enter a DNA sequence: ")
motif = raw_input("Enter a motif to search for: ")

if len(motif) > len(dnaSeq):
	print "Error: motif sequence is longer than DNA sequence."