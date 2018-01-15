names = ['Giannis', 'Stelios', 'Panagiotis']
ages = [42, 39, 38]
print zip(names, ages)
lista = zip(names, ages)
print lista
#---------------
print
lista2 = [i**2 for i in range(5)]
print lista2
#--------------
print
lista3 =[x for x in range(1,11)]
lista_sqr= map(lambda x:x**2 , lista3)
print lista3
print lista_sqr
#------------------------
print
a=10
b=25
c= a if a>b else b
print c
#------------------------reduce
lista4=[12, 10, 100, 24, 4000, 350]
megistos= reduce(lambda a,b: a if a>b else b , lista4)
print megistos

#------------------------------------filter
def protos(num):
    for i in range(2,num):
        if num%i == 0:
            return False
            break
    else:
        return True

protoi_ekato= filter(protos, range(1,101))
print protoi_ekato
#-----------------------------------------enumerate
print
for i,item in enumerate(names):
    print i, item

#--------------------------any
lista5 = [0 , 1, False, False]
if all(lista5):
    print 'ola'

if any(lista5):
    print 'toulaxiston'
