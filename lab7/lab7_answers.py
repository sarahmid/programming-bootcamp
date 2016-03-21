#===========================================================
# Programming Bootcamp 2015
# Lab 7 answers
# 
# Last updated 7/1/15
#===========================================================


### 1a

import sys
import os

# read in command line args
if len(sys.argv) == 3:
	inputFile = sys.argv[1]
	outputFolder = sys.argv[2]
else:
	print ">>Error: Incorrect args. Please provide an input file name and an output folder. Exiting."
	sys.exit()

# check if input file / output directory exist
if not os.path.exists(inputFile):
	print ">>Error: input file (%s) does not exist. Exiting." % inputFile
	sys.exit()
	
if not os.path.exists(outputFolder):
	print "Creating output folder (%s)" % outputFolder
	os.mkdir(outputFolder)



	
	
### 1b

import sys
import os
import my_utils

# read in command line args
if len(sys.argv) == 3:
	inputFile = sys.argv[1]
	outputFolder = sys.argv[2]
else:
	print ">>Error: Incorrect args. Please provide an input file name and an output folder. Exiting."
	sys.exit()

# check if input file / output directory exist
if not os.path.exists(inputFile):
	print ">>Error: input file (%s) does not exist. Exiting." % inputFile
	sys.exit()
	
if not os.path.exists(outputFolder):
	print "Creating output folder (%s)" % outputFolder
	os.mkdir(outputFolder)
	
# read in sequences from fasta file & print to separate output files
# you'll get an error for one of them because there's a ">" in the sequence id,
# which is not allowed in a file name. you can handle this howevere you want.
# here I used a try-except statement and just skipped the problematic file (with a warning message)
seqs = my_utils.read_fasta(inputFile)
for seqID in seqs:
	outFile = "%s/%s.fasta" % (outputFolder, seqID)
	outStr = ">%s\n%s\n" % (seqID, seqs[seqID])
	
	try:
		outs = open(outFile, 'w')
		outs.write(outStr)
		outs.close()
	except IOError:
		print ">>Warning: Could not print (%s) file. Skipping." % outFile
	


### 1c

import sys
import glob
import os

# read in command line args
if len(sys.argv) == 2:
	folderName = sys.argv[1]
else:
	print ">>Error: Incorrect args. Please provide an folder name. Exiting."
	sys.exit()

fastaList = glob.glob(folderName + "/*.fasta")
for filePath in fastaList:
	print os.path.basename(filePath)




### 2

import optparse
import random
import my_utils 

msg = "Usage: %prog OUTFILE [options]"
parser = optparse.OptionParser(usage=msg)

parser.add_option("--num", action="store", type='int', default=1, dest="NUM_SEQS", help="Number of sequences to create. Default is %default.")
parser.add_option("--len-min", action="store", type='int', default=100, dest="MIN_LEN", help="Minimum sequence length")
parser.add_option("--len-max", action="store", type='int', default=100, dest="MAX_LEN", help="Maximum sequence length")
parser.add_option("--rna", action="store_true", default=False, dest="RNA", help="Replace T's with U's?")
parser.add_option("--prefix", action="store", dest="ID_PREFIX", default="seq", help="Prefix to be added to the beginning of each sequence ID. Default is %default")

# parse args
(opts, args) = parser.parse_args()
outFile = args[0]

# generate and print sequences
outs = open(outFile, 'w')

for i in range(opts.NUM_SEQS):
	
	if opts.RNA:
		newSeq = my_utils.rand_seq(random.randint(opts.MIN_LEN, opts.MAX_LEN), rna=True)
	else:
		newSeq = my_utils.rand_seq(random.randint(opts.MIN_LEN, opts.MAX_LEN), rna=False)
	
	newID = opts.ID_PREFIX + str(i)
	outputStr = ">%s\n%s\n" % (newID, newSeq)
	outs.write(outputStr)
	
outs.close()






### 3a

import time
import my_utils

seqs = my_utils.read_fasta("fake.fasta")

# test manual replacement
startManual = time.time()

for seq in seqs.values():
	newSeq = ""
	for nt in seq:
		if nt == "T":
			newSeq += "U"
		else:
			newSeq += nt
			
print "Manual replacement:", time.time() - startManual

# test built-in replacement
startBuiltIn = time.time()

for seq in seqs.values():
	newSeq = seq.replace("T", "U")
			
print "Built-in replacement:", time.time() - startBuiltIn


# Answer: The built-in method should be much faster! Most built in functions are pretty well optimized, so they will often (but not always) be faster.



### 3b

import time
import my_utils

seqs = my_utils.read_fasta("fake.fasta")

# test manual replacement
startManual = time.time()

count = 0
for seq in seqs.values():
	for nt in seq:
		if nt == "A":
			count += 1
			
print "Manual replacement:", time.time() - startManual

# test built-in replacement
startBuiltIn = time.time()

count = 0
for seq in seqs.values():
	count += seq.count("A")
			
print "Built-in replacement:", time.time() - startBuiltIn


# Answer: Again, the built in function should be quite a bit faster.



### 3c

import time
import my_utils

seqs = my_utils.read_fasta("fake.fasta")

# test list as lookup table
startList = time.time()

seenIdList = []
for seqID in seqs:
	if seqID not in seenIdList:
		seenIdList.append(seqID)
			
print "List:", time.time() - startList

# test built-in replacement
startDict = time.time()

seenIdDict = {}
for seqID in seqs:
	if seqID not in seenIdDict:
		seenIdDict[seqID] = 0
			
print "Dictionary:", time.time() - startDict


# Answer: Dictionary should be faster. When you use a dictionary, Python jumps directly to where the requested key *should* be, if it were in the dictionary. This is very fast (it's an O(1) operation, for those who are familiar with the terminology). With lists, on the other hand, Python will scan through the whole list until it finds the requested element (or until it reaches the end). This gets slower and slower on average as you add more elements (it's an O(n) operation). Just something to keep in mind if you start working with very large datasets!



### 4a


# command-running function
# if verbose=True, prints output of the command to the screen
def run_command(command, verbose=False):
	import subprocess
	error = False
	
	if verbose == True: 
		print command
		print ""
	
	job = subprocess.Popen(command, bufsize=0, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	jobOutput = []
	if verbose == True:
		for line in job.stdout:
			print "   ", line,
			jobOutput.append(line)
	else:
		jobOutput = job.stdout.readlines()
	result = job.wait()
	if result != 0:
		error = True
	
	return (jobOutput, result, error)

# run the command
command = "ls -l"
(output, result, error) = run_command(command, verbose=True)
if error:
	print ">>Error running command:\n    %s\n" % command




# 4b

import sys

# command-running function
# if verbose=True, prints output of the command to the screen
def run_command(command, verbose=False):
	import subprocess
	error = False
	
	if verbose == True: 
		print command
		print ""
	
	job = subprocess.Popen(command, bufsize=0, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	jobOutput = []
	if verbose == True:
		for line in job.stdout:
			print "   ", line,
			jobOutput.append(line)
	else:
		jobOutput = job.stdout.readlines()
	result = job.wait()
	if result != 0:
		error = True
	
	return (jobOutput, result, error)

# file names
seqOutFile = "new_fake.fasta"
seqInfoFile = "new_fake.seq_info.txt"
	
# generate random sequence file
command = "python lab7_sequence_generator.py %s --num=10000 --len-min=500 --len-max=5000" % seqOutFile
(output, result, error) = run_command(command, verbose=True)
if error:
	print ">>Error running command:\n%s\nExiting." % command
	sys.exit()

# get stats about sequences
command = "python lab6_get_seq_info.py %s %s" % (seqOutFile, seqInfoFile)
(output, result, error) = run_command(command, verbose=True)
if error:
	print ">>Error running command:\n%s\nExiting." % command
	sys.exit()

# graph statistics (prints to a pdf)
command = "Rscript graph_gc.r %s" % seqInfoFile
(output, result, error) = run_command(command, verbose=True)
if error:
	print ">>Error running command:\n%s\nExiting." % command
	sys.exit()




















