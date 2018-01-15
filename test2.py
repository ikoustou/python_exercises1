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
#------------------------
lista4=[12, 10, 100, 24, 4000, 350]
megistos= reduce(lambda a,b: a if a>b else b , lista4)
print megistos

#------------------------------------

