# GCD of Two Numbers in Python using While loop
p, q = None, None

# p & q - denotes the two positive numbers

print ("-----Enter the two positive integer numbers-----")
p = int (input ())
q = int (input ())

while p != q:
	if p > q:
		p -= q
	else:
		q -= p

print ("\nThe GCD number is: ", p)