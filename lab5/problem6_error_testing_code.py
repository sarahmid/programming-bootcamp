infile = "horrible.fasta"
inFile = open(infile, 'r')
seqDict = {}
all = []
keys = []
values = []
n = 0
a = 0
keynumber = []
for line in inFile:
	line = line.rstrip('\n')
	data = line.split()
	n += 1
	all.append(line)
	seq = ""
	nonew = True
	if ">" in line:
		keys.append(line.lstrip(">"))
		keynumber.append(n)
	else:
		seq = seq+line
		values.append(seq)
# when I correctly concatenate the value list, 
# it will have the same number of elements as in the keys list
# and I can use the same index to link the two together for dictionary
for i in range(len(keys)):
	for key in keys: #iterating in the same order as i for values
		seqDict[key] = values[i]


for seqid in seqDict:
	print seqDict[seqid]

# error testing code
error = False
if ">varlen2_uc001pmn.3_3476" in seqDict:
	print "Remove > chars from headers!"
	error = True
elif "varlen2_uc001pmn.3_3476" not in seqDict:
	print "Something's wrong with your dictionary: missing keys"
	error = True
if "varlen2_uc021qfk.1>2_1472" not in seqDict:
	print "Only remove the > chars from the beginning of the header!"
	error = True
if len(seqDict["varlen2_uc009wph.3_423"]) > 85:
	if "\n" in seqDict["varlen2_uc009wph.3_423"]:
		print "Remove newline chars from sequences"
		error = True
	else:
		print "Length of sequences longer than expected for some reason"
		error = True
elif len(seqDict["varlen2_uc009wph.3_423"]) < 85:
	print "Length of sequences shorter than expected for some reason"
	error = True
	
if error == False:
	print "Congrats, you passed all my tests!"