try:
    for i in ['a', 'b', 'c']:
        print i**2
except:
    print 'An error occured'

#-------------------
print '2'
x = 5
y = 0
try:
    z = x/y
except:
    print 'Error'
finally:
    print 'All done'

#----------------------
print '3'
def giveInteger():
    try:
        i = int( )