#Find the difference between the sum of squares of 1-100 and the square of sum 1-100
sum1=0
sum2=0

for i in range(1,101):
    sum1+=i**2

for j in range (1,101):
    sum2+=j




diff=sum1-(sum2**2)
print diff
