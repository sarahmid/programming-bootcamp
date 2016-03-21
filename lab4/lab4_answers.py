#===========================================================
# Programming Bootcamp 2015
# Lab 4 answers
# 
# Last updated 6/16/15
#===========================================================




#-------------------------------------------------------
# Problem 2
#-------------------------------------------------------


# (a) print only IDs that contain "uc007"
inFile = "genes.txt"
ins = open(inFile, 'r')
for line in ins:
	line = line.rstrip('\n')
	if "uc007" in line:
		print line
ins.close()



# (b) print only unique ids
inFile = "genes.txt"
geneList = []
ins = open(inFile, 'r')
for line in ins:
	line = line.rstrip('\n')
	if line not in geneList: #keep track of what we've already seen using a list
		geneList.append(line)
		print line
ins.close()


# (c) print unique ids after removing .X suffix
inFile = "genes.txt"
geneList = []
ins = open(inFile, 'r')
for line in ins:
	line = line.rstrip('\n')
	splitLine = line.split(".") #could also do this using string slicing: line[:-2]
	geneID = splitLine[0] #the splitting returns a list, and the geneID should be the first part
	if geneID not in geneList: 
		geneList.append(geneID)
		print geneID
ins.close()















#-------------------------------------------------------
# Problem 3
#-------------------------------------------------------


### (a) compute average CDS length
fileName = "init_sites.txt"
totalLen = 0
numLines = 0
ins = open(fileName, 'r')
ins.readline()
for line in ins:
	line = line.rstrip('\n')
	lineParts = line.split()
	totalLen = totalLen + int(lineParts[6]) #all file input is read as string; must convert to int
	numLines = numLines + 1
print float(totalLen)/numLines
ins.close()



### (b) print 6th column iff 12th column == "aug"
fileName = "init_sites.txt"
ins = open(fileName, 'r')
for line in ins:
	line = line.rstrip('\n')
	lineParts = line.split()
	if lineParts[11] == "aug":
		print lineParts[5]
ins.close()



















#-------------------------------------------------------
# Problem 4
#-------------------------------------------------------

initFile = "init_sites.txt"
exprFile = "gene_expr.txt"

# create a list of "high expression" genes
highExpr = []
ins = open(exprFile)
ins.readline() #skip header
for line in ins:
	line = line.rstrip('\n')
	lineParts = line.split()
	if float(lineParts[1]) >= 50:
		highExpr.append(lineParts[0])
ins.close()

# average the peak scores for high vs low genes
highExprTotal = 0
highExprCount = 0
lowExprTotal = 0
lowExprCount = 0

ins = open(initFile, 'r')
ins.readline() #skip header
for line in ins:
	line = line.rstrip('\n')
	lineParts = line.split()
	if lineParts[0] in highExpr:
		print lineParts[1], "\t", lineParts[10]
		highExprTotal = highExprTotal + float(lineParts[10])
		highExprCount = highExprCount + 1
	else:
		lowExprTotal = lowExprTotal + float(lineParts[10])
		lowExprCount = lowExprCount + 1
ins.close()

print ""
print "Avg PeakScore high expression genes:", float(highExprTotal) / highExprCount
print "Avg PeakScore low expression genes:", float(lowExprTotal) / lowExprCount














#-------------------------------------------------------
# Problem 5
#-------------------------------------------------------


### (a) print a distance matrix for a list of same-length strings

things = ["bear", "pear", "boar", "tops", "bops"]
for i in range(len(things)):
	for j in range(len(things)):
		str1 = things[i]
		str2 = things[j]
		diffs = 0
		for k in range(len(str1)):
			if str1[k] != str2[k]:
				diffs += 1
		print round(float(diffs)/len(str1),2), "\t",
	print "" 

	
	

### (b) print distance matrix for a list of sequences read in from a file

# create list of sequences
things = []
ins = open("sequences2.txt", 'r')
for line in ins:
	line = line.rstrip('\n')
	things.append(line)
ins.close()

# create distance matrix
for i in range(len(things)):
	for j in range(len(things)):
		str1 = things[i]
		str2 = things[j]
		diffs = 0
		for k in range(len(str1)):
			if str1[k] != str2[k]:
				diffs += 1
		print round(float(diffs)/len(str1),2), "\t",
	print "" 



	
	
### (c) avoid unecessary calcs
### METHOD #1

print ""
print "METHOD 1: lower triangle"
print ""

things = []
ins = open("sequences2.txt", 'r')
for line in ins:
	line = line.rstrip('\n')
	things.append(line)
ins.close()

for i in range(len(things)):
	for j in range(0,i): #<-- this is the only change we need to make
		str1 = things[i]
		str2 = things[j]
		diffs = 0
		for k in range(len(str1)):
			if str1[k] != str2[k]:
				diffs += 1
		print round(float(diffs)/len(str1),2), "\t",
	print "" 




### METHOD #2
# note that the way it prints will look weird! see below for another example that fixes this

print ""
print "METHOD 2: upper triangle, messed up format"
print ""

things = []
ins = open("sequences2.txt", 'r')
for line in ins:
	line = line.rstrip('\n')
	things.append(line)
ins.close()

for i in range(len(things)):
	for j in range(i+1,len(things)): #<-- 
		str1 = things[i]
		str2 = things[j]
		diffs = 0
		for k in range(len(str1)):
			if str1[k] != str2[k]:
				diffs += 1
		print round(float(diffs)/len(str1),2), "\t",
	print "" 



### METHOD #3
# similar to above, but fixed output formatting to be more easily interpreted

print ""
print "METHOD 3: upper triangle with formatting"
print ""

things = []
ins = open("sequences2.txt", 'r')
for line in ins:
	line = line.rstrip('\n')
	things.append(line)
ins.close()

for i in range(len(things)):
	for j in range(len(things)):
		if j > i:
			str1 = things[i]
			str2 = things[j]
			diffs = 0
			for k in range(len(str1)):
				if str1[k] != str2[k]:
					diffs += 1
			print round(float(diffs)/len(str1),2), "\t",
		else:
			print " - \t",
	print "" 










