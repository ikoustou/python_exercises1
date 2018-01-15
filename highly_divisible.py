goal = 500
count = 1
current_triangle = 1
max_divisors=0

while max_divisors<goal:
    divisors=0
    for i in xrange(1,current_triangle+1):
        if current_triangle%i==0:
            divisors +=1

    if divisors>max_divisors:
        max_divisors = divisors

    count +=1

    current_triangle += count

print 'number : ', count-1
print 'current triangle : ', current_triangle-count
print 'divisors ', max_divisors