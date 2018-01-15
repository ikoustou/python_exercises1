class Line(object):
    def __init__(self, coor1, coor2):
        self.coordinate1 = coor1
        self.coordinate2 = coor2

    def distance(self):
        return abs(self.coordinate1[0] - self.coordinate2[0]) + abs(self.coordinate1[1] - self.coordinate2[1])

    def slope(self):
        return float(self.coordinate2[1] - self.coordinate1[1]) / (self.coordinate2[0] - self.coordinate1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print li.distance()
print li.slope()
