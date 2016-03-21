import random

secretNum = random.randint(1,20)
quitLoop = False

while (quitLoop == False):
	guess = int(raw_input("Guess a number between 1 and 20 (enter 0 to quit): "))
	
	if guess == 0:
		print "I win!"
		quitLoop = True
	
	elif guess == secretNum:
		print "You got it!"
		quitLoop = True
	
	elif guess > secretNum:
		print "Lower..."
	
	elif guess < secretNum:
		print "Higher..."
		
	