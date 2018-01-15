
st = 'Print only the words that start with s in this sentence'

l1= st.split(' ')
for item in l1:
    if item[0]=='s':
        print item

#Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
l_div3=[num for num in xrange(1,51) if num%3==0]

print l_div3


#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
l2=st.split()
for item in l2:
    if len(item)%2==0:
        print item

