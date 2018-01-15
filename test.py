l = ['Giannis', 'Stelios', 'Panagiotis']
ages = [42, 39, 38]
for x, y in zip(l, ages):
    print x, y

#--------------
products = [
{'sku': '1', 'expiration_date': 'today', 'price': 100.0},
{'sku': '2', 'expiration_date': 'tomorrow', 'price': 50},
{'sku': '3', 'expiration_date': 'today', 'price': 20},
]

print
print products[0]['sku']
print products[0]['expiration_date']

for item in products:
    if item['expiration_date'] == 'today':
        item['price'] *= 0.8

print products

#----test the [2,2) range
for i in range(2,2):
    print 'not printed'

#----------------------
discounts = {
'F20': (0.0, 20.0), # each value is (percent, fixed)
'P30': (0.3, 0.0),
'P50': (0.5, 0.0),
'F15': (0.0, 15.0),
}
for item in discounts:
    x, y = discounts.get(item)
    print x, ' ', y

#--------------------------iterators  -----------
from itertools import count
for n in count(100, 10):
    if n>300:
        break
    print n

#-------------  function keyword arguments  ----
def func(a, b, c):
    print a, b, c

func(c=3, a=1, b=2)

#-----------------------
a=3
b=2
print a//b
#---------------------------BUILT-IN --------
# ---  id ---
print id(a)
print id(b)
print id(func)

#-----  any -----
list1=[2, 3, 4, 'mitsos', False]
print any(list1)