#===========================================================
# Programming Bootcamp 2015
#
# my_utils.py
# useful functions for DNA sequence data and files
# 
# Last updated 6/23/15
#===========================================================


# calculate fraction of a sequence that is G's and C's
def gc(seq):
	gcCount = seq.count("C") + seq.count("G")
	gcFrac = float(gcCount) / len(seq)
	
	return round(gcFrac,2)



# returns the reverse complement of a DNA sequence
def reverse_compl(seq):
	complements = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
	compl = ""
	for char in seq:
		compl = complements[char] + compl
	
	return compl



# assuming the indicated file is in fasta format, reads each entry
# into a dictionary using the header as the key and the concatenated 
# sequence as the value
def read_fasta(fileName):
	ins = open(fileName, 'r')
	seqDict = {}
	activeID = ""

	for line in ins:
		line = line.rstrip('\r\n')
		
		if line[0] == ">":
			activeID = line[1:] 
			if activeID in seqDict:
				print ">>> Warning: repeat id:", activeID, "-- overwriting previous ID."
			seqDict[activeID] = ""
			
		else:
			seqDict[activeID] += line 
	
	ins.close()	
	
	return seqDict


# a version of the fasta reader that is more robust to file IO problems
# (returns error if file is unreadable, instead of just crashing).
# usage (in main script): 
#	(seqs, error) = read_fasta2(myFile)
def read_fasta2(fileName):
	seqDict = {}
	error = False
	
	try:
		ins = open(fileName, 'r')
	except IOError:
		error = True
		print "Error: in read_fasta(): could not open", fileName
	else:
		currentKey = ""
		for line in ins:
			line = line.rstrip('\n') 
			if ">" == line[0]:
				currentKey = line[1:] 
				seqDict[currentKey] = ""
			else:
				seqDict[currentKey] += line.upper() 
		ins.close()	
	
	return (seqDict, error) #returns two values.


	

# returns a random string of nts of the specified length
def rand_seq(length, rna=False):
	import random
	
	if rna:
		nts = ['A','C','G','U']
	else:
		nts = ['A','C','G','T']
	seq = ""
	for i in range(length):
		seq += random.choice(nts)
	
	return seq




# returns a random permutation of the given sequence
def shuffle_nt(seq):
	import random
	
	strList = list(seq)
	random.shuffle(strList)
	shuffSeq = "".join(strList)
	
	return shuffSeq
