#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#the secret is that str1[half::-1]-> 900 mismatch with 90

max=0
arr=[]
for i in range(90,1000):
    for j in range(90,1000):
        result = i*j
        #print result
        str1=str(result)
        half= len(str1)/2
        end=str1[half:]
        anapodo=end[::-1]
        #print str1[:half]
        #print anapodo
        if str1[:half]== anapodo:
            arr.append(str1)
            palidrome=int(str1)
            if palidrome>max :
                max=palidrome

print max
#print arr