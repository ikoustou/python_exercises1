class Circle(object):
    pi=3.14

    #constructor with default radius=1
    def __init__(self, radius=1):
        # type: (object) -> object
        self.radius= radius

    #method area
    def area(self):
        return self.radius * self.radius * Circle.pi

    #method for resetting Radius
    def setRadius(self, radius):
        self.radius= radius

    #method for returning Radius
    def getRadius(self):
        return self.radius


cyclos= Circle()
print 'Radius is: ', cyclos.getRadius()
cyclos.setRadius(5)
print 'Now raidus is: ', cyclos.getRadius()
print 'Area is: ', cyclos.area()

print 'Class Circle attribute pi: ', Circle.pi
print 'Class Circle attribute pi: ', cyclos.pi 