#Sum of numbers under 1000 which are multipliers of 3 or 5

sum=0
for i in range(1000):
    if i%3==0 or i%5==0:
        sum+=i
print sum