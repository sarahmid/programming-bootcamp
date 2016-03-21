#===========================================================
# Programming Bootcamp 2015
# Lab 5 answers
# 
# Last updated 6/18/15
#===========================================================

'''



#-------------------------------------------------------
# Problem 2 - simple file writing
#-------------------------------------------------------

### (a) print "hello world" to a file
outFile = "hello.txt"
outs = open(outFile, 'w')
outs.write("Hello world")
outs.close()


### (b) printing formatted text
outFile = "meow.txt"
outs = open(outFile, 'w')
outs.write("Dear Mitsworth,\n\n\tMeow, meow meow meow.\n\nSincerely,\nA friend")
outs.close()


### (c) reading and printing
inFile = "genes.txt"
outFile = "genes_unique.txt"
unique = []
ins = open(inFile, 'r')
outs = open(outFile, 'w')
for line in ins:
    line = line.rstrip('\n')
    if line not in unique:
        outs.write(line + "\n")
        unique.append(line)
outs.close()
ins.close()




#-------------------------------------------------------
# Problem 3 - simple dictionaries
#-------------------------------------------------------


### (a) hard-coded dictionary
hash = {'Wilfred': '555-1234', 'Manfred': '555-3939', 'Wadsworth': '555-8765', 'Jeeves': '555-1001', 'Mitsworth': '555-5555'}
name = raw_input("Welcome to the Phone Book. Who do you want to look up? ")
if name in hash:
    print "The number for", name, "is", hash[name]
else:
    print "Sorry, I don't know that person."

    
### (b) print all entries to screen
hash = {'Wilfred': '555-1234', 'Manfred': '555-3939', 'Wadsworth': '555-8765', 'Jeeves': '555-1001', 'Mitsworth': '555-5555'}
for name in hash:
    print name, "'s number is", hash[name]
    
    # other ways to print (just FYI):
    
    #if you don't like the space between the name and 's
    print (name + "'s number is " + hash[name]) 
    
    #a fancy way of doing the same thing. the variables at the end are inserted in place of the %s characters
    print "%s's number is %s" % (name, hash[name]) 

    
### (c) print just the names in alphabetical order
hash = {'Wilfred': '555-1234', 'Manfred': '555-3939', 'Wadsworth': '555-8765', 'Jeeves': '555-1001', 'Mitsworth': '555-5555'}
for name in sorted(hash.keys()):
    print name

    
### (d) print just the names sorted by phone number
hash = {'Wilfred': '555-1234', 'Manfred': '555-3939', 'Wadsworth': '555-8765', 'Jeeves': '555-1001', 'Mitsworth': '555-5555'}
for name in sorted(hash, key=hash.get):
    print name


### (e) thinkin' question
# Keys in a dictionary must be unique. If we were to add a new person to the dict 
# with the same name as someone else, we would end up overwriting the information
# of the person who was already in there.
# The best way to handle this is to just use a key that is unique in the first place.
# If that isn't possible, you could try storing a list of values instead of a single
# value for each hash key. This would still present the problem of not being able
# to associate the name with a single correct value, but sometimes this is ok, depending
# on what the purpose of the dict is. It wouldn't be very good for our phonebook example, though,
# unless you're ok with calling all 5 of the "Wilfred"s that you know to find the right one.











#-------------------------------------------------------
# Problem 4 - many counters problem
#-------------------------------------------------------


inFile = "sequences3.txt"
lenDict = {}
ins = open(inFile, 'r')
for line in ins:
    line = line.rstrip('\n') #important to do here, since '\n' counts as a character and thus increases the length of the sequence by 1
    seqLen = len(line)
    if seqLen not in lenDict:
        lenDict[seqLen] = 1
    else:
        lenDict[seqLen] += 1
ins.close()

# print all tallies for informational purposes
for name in sorted(lenDict.keys()):
    print name, ":", lenDict[name]

# now to get the max length, we can sort the keys by value
sortedLens = sorted(lenDict, key=lenDict.get) #this returns a list of the keys sorted by value

# this sorts from smallest to largest, so we take the last element
mostCommon = sortedLens[-1]
print "Most common length is", mostCommon, "nts"











#-------------------------------------------------------
# Problem 5 - codon table
#-------------------------------------------------------

### (a) thinkin' question
# Codons should be the keys, since we are starting with nucleotide sequence. 
# That is the info we'll want to use to retrieve the amino acid.
# If you were instead going from protein --> nucleotide, then you'd want the 
# amino acids to be the keys. (But as discussed in problem 3e, that can be 
# problematic because a single amino acid usually maps to more than one codon) 


### (b) create codon dict and translate a user-supplied codon

inFile = "codon_table.txt"
codon2aa = {}
ins = open(inFile, 'r')
ins.readline() #skip header
for line in ins:
    line = line.rstrip('\n')
    
    # since I know there are exactly 2 values on every line, I can use this shorthand 
    # notation to automatically "unpack" the returned list into named variables.
    (codon, aa) = line.split() 
    if codon not in codon2aa:
        codon2aa[codon] = aa
    else:
        print "Warning! Multiple entries found for the same codon (" + codon + "). Skipping."
ins.close()

# get user input
request = raw_input("Codon to translate: ").upper() #read & covert to uppercase
if request in codon2aa:
    print request, "-->", codon2aa[request]
else:
    print "Did not recognize that codon."


    
    
### (c) translate a whole sequence

inFile = "codon_table.txt"
codon2aa = {}
ins = open(inFile, 'r')
ins.readline() #skip header
for line in ins:
    line = line.rstrip('\n')
    (codon, aa) = line.split() 
    if codon not in codon2aa:
        codon2aa[codon] = aa
    else:
        print "Warning! Multiple entries found for the same codon (" + codon + "). Skipping."
ins.close()

# get user input
request = raw_input("Sequence to translate (multiple of 3): ").upper()
protSeq = ""
if (len(request) % 3) == 0:
    
    # this indexing/slicing is tricky! definitely try this sort of thing out in the 
    # interpreter to make sure you get it right.
    for i in range(0,len(request),3):
        codon = request[i:i+3]
        if codon in codon2aa:
            protSeq += codon2aa[codon]
        else:
            print "Warning! Unrecognized codon ("+codon+"). Using X as a place holder."
            protSeq += "X"
    print "Your protein sequence is:", protSeq
else:
    print "Please enter a sequence length that is a multiple of 3."

    
    
### (d) translate many sequences from a file

inFile = "codon_table.txt"
codon2aa = {}
ins = open(inFile, 'r')
ins.readline() #skip header
for line in ins:
    line = line.rstrip('\n')
    (codon, aa) = line.split() 
    if codon not in codon2aa:
        codon2aa[codon] = aa
    else:
        print "Warning! Multiple entries found for the same codon (" + codon + "). Skipping."
ins.close()

# read file of sequences
inFile = "sequences3.txt"
outFile = "proteins.txt"
ins = open(inFile, 'r')
outs = open(outFile, 'w')
lineNum = 1 #just used for nicer error message
for line in ins:
    line = line.rstrip('\n')
    protSeq = "" #best to define this with the loop so it's re-created for each separate sequence.
    if (len(line) % 3) == 0:
        for i in range(0,len(line),3):
            codon = line[i:i+3]
            if codon in codon2aa:
                protSeq += codon2aa[codon]
            else:
                print "Warning! Unrecognized codon ("+codon+"). Using X as a place holder."
                protSeq += "X"
        outs.write(protSeq + '\n') # write to output file
    else:
        print "Line "+lineNum+" - Encountered sequence length that is not a multiple of 3. Skipping."
    lineNum += 1
outs.close()
ins.close()
    
    

    
    
    
    




#-------------------------------------------------------
# Problem 6 - fasta reader
#-------------------------------------------------------
'''

ins = open("horrible.fasta", 'r')
seqDict = {}
activeID = ""

for line in ins:
    line = line.rstrip('\r\n')
    
    # if the first character is >, this line is a header.
    if line[0] == ">":
        activeID = line[1:] 
        
        if activeID in seqDict:
            print ">>> Warning: repeat id:", activeID, "-- overwriting previous ID."
        seqDict[activeID] = ""
        
    # otherwise, this is a sequence line--add it to the activeID entry
    else:
        seqDict[activeID] += line 
        
ins.close()   
 

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





