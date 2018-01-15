goal=2000000
def is_prime(num):
    flag=True
    for i in xrange(2,num):
        if num%i==0 :
            flag=False
            break
    return flag

sum=5947727884
count=383420

while count<goal:
    if is_prime(count):

        sum+=count

        print count, sum

    count+=1

print sum