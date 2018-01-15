l1 = [x**2 for x in xrange(11)]

print l1

#nested comprehension list
l2 = [x**2 for x in [x**2 for x   in xrange(11)]]

print l2