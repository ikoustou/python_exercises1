prime=[]
for i in range(2,100000):
    flag=True
    for j in range(2, i):
        if i%j==0 :
            flag=False
            break
    if flag:   
        prime.append(i)


number = 600851475143
max=0
for item in prime:
	if number%item==0:
		max=item

print max