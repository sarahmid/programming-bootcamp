a = int(raw_input("a = "))
b = int(raw_input("b = "))
c = int(raw_input("c = "))

x1 = ( (-b) + (b**2 - 4*a*c) ** (0.5) ) / float(2*a)
x2 = ( (-b) - (b**2 - 4*a*c) ** (0.5) ) / float(2*a)

print "x =", x1, "or", x2