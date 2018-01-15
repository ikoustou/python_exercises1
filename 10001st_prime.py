goal=10001

def is_prime(num):
    flag=True
    for i in xrange(2,num):
        if num%i==0 :
            flag=False
            break
    return flag

count=1
i=2

while count<=goal:
    if is_prime(i):
      #  print count, i
        count += 1
    i+=1
print count-1, i-1