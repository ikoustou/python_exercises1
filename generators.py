def fibo(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        c = a #temp variable
        a = b
        b = c+b

for item in fibo(10):
    print item

#-----Create a generator that generates the squares of numbers up to some number N.
def gen_sqr(n):
    for i in xrange(n+1):
        yield i**2

for item in gen_sqr(10):
    print item

print
#----Create a generator that yields "n" random numbers between a low and high number (that are inputs)
import random
def rand_num(low,high,n):
    for i in xrange(1,n+1):
        yield random.randint(low, high)

for item in rand_num(50,70,5):
    print item