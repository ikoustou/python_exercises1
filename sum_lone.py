
l=[1,3,80,6,4,14, 5, 5, 80]
l.sort()

meion=0
sum1=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            meion+=l[j]
    sum1 += l[i]
	
sum1+=l[-1]
sum1-=meion
print sum1