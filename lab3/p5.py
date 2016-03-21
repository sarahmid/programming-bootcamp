import random

# By convention, variables with a set, pre-defined value ("constants")
# are indicated by ALL_CAPS variable names and are defined at the top.
# It's not really necessary to define GIRL = 1, but it will make
# the code easier to read and understand, so it's considered good form.
NUM_FAMS = 10000 
GIRL = 1

# regular variables, like this counter, are lower case/camelCase
totalKidsAllFams = 0

for i in range(NUM_FAMS):
	
	numKids = 0
	hadGirl = False
	
	while not hadGirl:
		numKids = numKids + 1
		gender = random.randint(0,1) #the miracle of birth
		if gender == GIRL:
			hadGirl = True
		
	# once we exit the while loop, we must have had a girl.
	# so add the number of kids this fam had to the running total, and
	# move on to the next family
	totalKidsAllFams = totalKidsAllFams + numKids

# finally, divide the total number of kids by the number of families to get the avg
print "Avg kids per fam:", float(totalKidsAllFams) / NUM_FAMS