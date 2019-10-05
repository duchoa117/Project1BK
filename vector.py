
import math
class Vector():
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    def unit(self):
        x = self.x/math.sqrt(self.x*self.x + self.y*self.y)
        y = self.y/math.sqrt(self.x*self.x + self.y*self.y)
        return Vector(x, y)
    def mul(self, a):
        return Vector(self.x*a, self.y*a)
    def rotate(self, a, nav):
        if nav == 'l':
            a = 2*math.pi - a
        xT = self.x 
        yT = self.y
        self.x = xT*math.cos(a) - yT*math.sin(a)
        self.y = xT*math.sin(a) + yT*math.cos(a)
    def add(self, v):
            self.x += v.x
            self.y += v.y
    def addNew(self, v):
        if v != None:
            return Vector(self.x + v.x, self.y+ v.y)
    def rotateNew(self, a, nav):
        if nav == 'l':
            a = 2*math.pi - a
        xT = self.x
        yT = self.y
        x = xT*math.cos(a) - yT*math.sin(a)
        y = xT*math.sin(a) + yT*math.cos(a)
        return Vector(x, y)

