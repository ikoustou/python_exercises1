#takes a list and returns a list with unique values as elements
l1=[1,2,1,1,2,2,3,4,50]

def unique_list(l):
    l_out=[]
    for item in l:
        for i in l_out:
            if i==item:
                break
        else:
            l_out.append(item)
    return l_out

l2 = unique_list(l1)
print l2

#second version with set
l3 = set(l1)
print l3

#third version with in
def unique2(l):
    lout=[]
    for item in l:
        if item in lout:
            pass
        else:
            lout.append(item)
    return lout

print 'third version '
print unique2(l1)
