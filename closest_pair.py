points = 5
lst = []
for i in range(5):
    print ('{} point'.format(i+1) )
    x = int( raw_input('Give me the x :'))
    y = int( raw_input('Give me the y :'))
    lst.append((x,y))

def closest_pair(lista):
    num = len(lista)
    min = 1000000
    pair=[]
    for i,item1 in enumerate(lista):
        x1 = item1[0]
        y1 = item1[1]
        for j in range(i+1,num):
            item2 = lista[j]
            x2 = item2[0]
            y2 = item2[1]
            dist = ( (x1-x2)**2 +(y1-y2)**2 )**0.5
            if dist < min:
                min = dist
                pair=[]
                pair.append(item1)
                pair.append(item2)
    return pair



print 'the closest pair of points is: ' , closest_pair(lst)