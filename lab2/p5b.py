password = "Mittens123"
guess = raw_input("Enter the password: ")

if guess == password:
	print "Correct!"
else:
	guess = raw_input("Incorrect password. Try again: ")
	if guess == password:
		print "Correct!"
	else:
		guess = raw_input("Incorrect password. Try again: ")
		if guess == password:
			print "Correct!"
		else:
			print "Incorrect password. Access denied."