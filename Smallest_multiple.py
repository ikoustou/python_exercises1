#Smallest multiple


#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
number=100000
max=0
for i in range(number):
	flag=False
	for j in range(1,21):
		
		if (i/j)%2==0:
			if j==20:
				flag=True
			continue
		else:
			break
	
	if flag and i>max:
		max=i

print max