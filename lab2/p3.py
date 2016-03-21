a = float(raw_input("a = "))
b = float(raw_input("b = "))
c = float(raw_input("c = "))

underRoot = b**2 - 4*a*c
if underRoot < 0:
	print "Non-real answer"
else:
	x1 = ( (-b) + underRoot ** (0.5) ) / float(2*a)
	x2 = ( (-b) - underRoot ** (0.5) ) / float(2*a)
	print "x =", x1, "or", x2