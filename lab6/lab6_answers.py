#===========================================================
# Programming Bootcamp 2015
# Lab 6 answers
# 
# Last updated 6/23/15
#===========================================================



#-------------------------------------------------------
# Problem 3 - functions
#-------------------------------------------------------


### (a) 
# calculate fraction of a sequence that is G's and C's
def gc(seq):
	gcCount = seq.count("C") + seq.count("G")
	gcFrac = float(gcCount) / len(seq)
	
	return round(gcFrac,2)


### (b)
# returns the reverse complement of a DNA sequence
def reverse_compl(seq):
	complements = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
	compl = ""
	for char in seq:
		compl = complements[char] + compl
	
	return compl


### (c)
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


	
### (d)
# returns a random string of nts of the specified length
def rand_seq(length):
	import random
	
	nts = ['A','C','G','T']
	seq = ""
	for i in range(length):
		seq += random.choice(nts)
	
	return seq



### (e)	
# returns a random permutation of the given sequence
def shuffle_nt(seq):
	import random
	
	strList = list(seq)
	random.shuffle(strList)
	shuffSeq = "".join(strList)
	
	return shuffSeq
	






#-------------------------------------------------------
# Problem 4 - command args
#-------------------------------------------------------

### (a) quadratic formula
import sys

if len(sys.argv) == 4:
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	c = float(sys.argv[3])
else:
	print "Please specify three numbers. Exiting."
	sys.exit()

underRoot = (b**2) - (4*a*c)
if underRoot < 0:
	print "Non-real answer."
else:
	x1 = (-b + (underRoot ** 0.5)) / (2*a)
	x2 = (-b - (underRoot ** 0.5)) / (2*a)
	print "x equals", x1, "or", x2





### (b) file reading and writing
import sys
import my_utils

if len(sys.argv) == 3:
	inFile = sys.argv[1]
	outFile = sys.argv[2]
else:
	print "Please specify an input and output file. Exiting."
	sys.exit()

seqs = my_utils.read_fasta(inFile)

outs = open(outFile, 'w')
outs.write("SeqID\tLen\tGC\n") #print header to file

for (id,seq) in seqs.items():
	gcCont = my_utils.gc(seq)
	length = len(seq)
	outs.write(id + "\t" + str(length) + "\t" + str(gcCont) + "\n")

outs.close()



"""
Note on printing:
If this:
   
   outs.write(id + "\t" + str(length) + "\t" + str(gcCont) + "\n") 

seems clunky to you, you can try some more advanced string formatting:
   
   outString = "%s\t%s\t%s\n" % (id, length, gcCont)
   outs.write(outString)

This is harder to read, but much easier to write. Basically, each '%s' 
gets subbed in with one of the variables listed on the right, in 
order of appearance.
"""









#-------------------------------------------------------
# Problem 5 - kmer generation
#-------------------------------------------------------

### Several possibilities:



# Method 1
# Generic kmer generation for any k and any alphabet (default is DNA nt)
# Pretty fast
def get_kmers1(k, letters=['A','C','G','T']):
	kmers = []
	choices = len(letters)
	finalNum = choices ** k
	
	# initialize to blank strings
	for i in range(finalNum):
		kmers.append("")
	
	# imagining the kmers lined up vertically, generate one "column" at a time
	for i in range(k): 
		consecReps = choices ** (k - (i + 1))   #number of times to consecutively repeat each letter
		patternReps = choices ** i #number of times to repeat pattern of letters
		
		# create the current column of letters
		index = 0
		for j in range(patternReps):
			for m in range(choices):
				for n in range(consecReps):
					kmers[index] += letters[m]
					index += 1
			
	return kmers


	
	
# Method 2 
# Generate numbers, discard any that aren't 1/2/3/4's, convert to letters. 
# Super slow~
def get_kmers2(k):
	discard = ["0", "5", "6", "7", "8", "9"]
	convert = {"1": "A", "2": "T", "3": "G", "4": "C"}
	min = int("1" * k)
	max = int("4" * k)
	kmers = []
	tmp = []
	for num in range(min, (max + 1)): # generate numerical kmers
		good = True
		for digit in str(num):
			if digit in discard:
				good = False
				break
		if good == True:
			tmp.append(num)		
	for num in tmp: # convert numerical kmers to ATGC
		result = ""
		for digit in str(num):
			result += convert[digit]
		kmers.append(result)
	
	return kmers



	
	
# Method 3 (by Nate)
# A recursive solution. Fast!
# (A recursive function is a function that calls itself)
def get_kmers3(k):
	nt = ['A', 'T', 'G', 'C']
	k_mers = []

	if k == 1:
		return nt

	else:
		for i in get_kmers3(k - 1):
			for j in nt:
				k_mers.append(i + j)
	return k_mers



	
	
# Method 4 (by Nate)
# Fast
def get_kmers4(k):
	nt = ['A', 'T', 'G', 'C']
	k_mers = []
	total_kmers = len(nt)**k

	# make a list of size k with all zeroes. 
	# this keeps track of which base we need at each position 
	pointers = []
	for p in range(k):
		pointers.append(0)

	for k in range(total_kmers):

		# use the pointers to generate the next k-mer
		k_mer = ""
		for p in pointers:
			k_mer += nt[p]
		k_mers.append(k_mer)

		# get the pointers ready for the next k-mer by updating them left to right
		pointersUpdated = False
		i = 0
		while not pointersUpdated and i < len(pointers):
			if pointers[i] < len(nt) - 1:
				pointers[i] += 1
				pointersUpdated = True
			else:
				pointers[i] = 0
				i += 1
	
	return k_mers

	
	

# Method 5 (by Justin Becker, bootcamp 2013)
# Fast!
def get_kmers5(k):   #function requires int as an argument
	kmers = [""]
	for i in range(k):   #after each loop, kmers will store the complete set of i-mers
		currentNumSeqs = len(kmers)
		for j in range(currentNumSeqs): #each loop takes one i-mer and converts it to 4 (i+1)=mers
			currentSeq = kmers[j]
			kmers.append(currentSeq + 'C')
			kmers.append(currentSeq + 'T')
			kmers.append(currentSeq + 'G')
			kmers[j] += 'A'
	return kmers


	
	
# Method 6 (by Nick)
# Convert to base-4
def get_kmers6(k):
	bases = ['a', 'g', 'c', 't']
	kmers = []

	for i in range(4**k):
		digits = to_base4(i, k)
		mystr = ""
		for baseidx in digits:
			mystr += bases[baseidx]

		kmers.append(mystr)

	return kmers

# convert num to a k-digit base-4 int
def to_base4(num, k):

	digits = []

	while k > 0:

		digits.append(num/4**(k-1))

		num %= 4**(k-1)
		k -= 1

	return digits

	
	
	

# Below: more from Nate
# see also separate script
import random
import time
alphabet = ['A', 'C', 'G', 'T']

## Modulus based
def k_mer_mod(k):
	k_mers = []
	for i in range(4**k):
		k_mer = ''
		for j in range(k):
			k_mer = alphabet[(i/4**j) % 4]+ k_mer
		k_mers.append(k_mer)
	return k_mers


## maybe the range operator slows things down by making a big tuple
def k_mer_mod_1(k):
	k_mers = []
	total = 4**k
	i = 0
	while i < total:
		k_mer = ''
		for j in range(k):
			k_mer = alphabet[(i/4**j) % 4]+ k_mer
		k_mers.append(k_mer)
		i += 1
	return k_mers



## Does initializing the list of k_mers help?
def k_mer_mod_2(k):
	k_mers = [''] * 4**k
	for i in range(4**k):
		k_mer = ''
		for j in range(k):
			k_mer = alphabet[(i/4**j) % 4] + k_mer
		k_mers[i] = k_mer
	return k_mers


## What's faster? element assignment or hashing?
def k_mer_mod_set(k):
	k_mers = set() 
	for i in range(4**k):
		k_mer = ''
		for j in range(k):
			k_mer = alphabet[(i/4**j) % 4] + k_mer
		k_mers.add(k_mer)
	return list(k_mers)


## does creating the string up front help?
#def k_mer_mod_3(k):
#n	k_mers = []
#	k_mer = "N" * k	
#	for i in range(4**k):
#		for j in range(k):
#			k_mer[j] = alphabet[(i/4**j) % 4]
#		k_mers.append(k_mer)
#	return k_mers
# Nope! String are immutable, dummy!


# maybe we can do something tricky with string substitution
def k_mer_mod_ssub(k):
	template = "\%s" * k
	k_mers = []

	for i in range(4**k):
		k_mer = []
		for j in range(k):
			k_mer.append(alphabet[(i/4**j) % 4])
		k_mers.append(template % k_mer)
	return k_mers


# what about using a list?
def k_mer_mod_4(k):
	k_mers = [''] * 4**k
	k_mer = [''] * k
	
	for i in range(4**k):
		for j in range(k):
			k_mer[j] = alphabet[(i/4**j) % 4]
		k_mers[i] = "".join(k_mer)
	return k_mers

## recursive version
def k_mer_recursive(k):
	if k == 0:
		return ['']
	else:
		k_mers = []
		for k_mer in k_mer_recursive(k-1):
			for n in alphabet:
				k_mers.append("%s%s" % (k_mer, n))
		return k_mers

			 
## That works, but what I wanted to be like, really obnoxious about it
def k_mer_recursive_2(k):
	if k == 0:
		return ['']
	else:
		k_mers = []
		[[k_mers.append("%s%s" % (k_mer, n)) for n in alphabet] for k_mer in k_mer_recursive_2(k-1)]
		return k_mers

 # using list instead of strings to store the k_mers
def k_mer_recursive_3(k, j = False):
	if k == 0:
		return [[]]
	else:
		k_mers = []
		[[k_mers.append((k_mer + [n])) if j else k_mers.append("".join(k_mer + [n])) for n in alphabet] for k_mer in k_mer_recursive_3(k-1, True)]
		return k_mers

## stochastic (I have a good feeling about this one!)
def k_mer_s(k):
	s = set()
	i = 0
	while i < 4**k:
		k_mer = ''
		for j in range(k):
			k_mer = k_mer + random.choice(alphabet)
		if k_mer not in s:
			s.add(k_mer)
			i += 1
	return list(s)


## I sure hope this works because now we're pretty much cheating
import array
def k_mer_mod_array(k):

	k_mers = [] 
	k_mer = array.array('c', ['N'] * k)
	
	for i in range(4**k):
		for j in range(k):
			k_mer[j] = alphabet[(i/4**j) % 4]
		k_mers.append("".join(k_mer))
	return k_mers
## That could have gone better. 



























