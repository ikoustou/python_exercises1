
class Animal(object):
    def __init__(self):
        print 'Animal created'

    def whoAmI(self):
        print 'Animal'

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print 'Dog created'

    def whoAmI(self):
        print 'Dog'

d = Dog()
d.whoAmI()