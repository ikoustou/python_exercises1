#Prime numbers in range 1-100

prime=[]
for i in range(1,10000):
    flag=True
    for j in range(2, i):
        if i%j==0 :
            flag=False
            break
    if flag:   
        prime.append(i)
print prime