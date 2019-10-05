from gameObject import GameObject, add, game_objects
from vector import Vector
from boxCollider import BoxCollider
import pygame


class Line(GameObject):
    def __init__(self, x1, y1, x2, y2, length):
        GameObject.__init__(self, 0, 0)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.length = length
        self.collider = False
    def render(self, canvas):
        # YELLOW = (255, 255, 0)
        # line = (self.x1, self.y1, self.x2, self.y2)
        # pygame.draw.line(canvas, YELLOW, (self.x1, self.y1),(self.x2, self.y2), 1)
        pass
        
    def overlap(self, other):
        denominator = ((self.x2 - self.x1) * (other.y2 - other.y1)) - ((self.y2 - self.y1) * (other.x2 - other.x1))
        numerator1 = ((self.y1 - other.y1) * (other.x2 - other.x1)) - ((self.x1 - other.x1) * (other.y2 - other.y1));
        numerator2 = ((self.y1 - other.y1) * (self.x2 - self.x1)) - ((self.x1 - other.x1) * (self.y2 - self.y1));

        if (denominator == 0):
            return (numerator1 == 0 and numerator2 == 0)
        r = numerator1 / denominator;
        s = numerator2 / denominator;
        return (r >= 0 and r <= 1) and (s >= 0 and s <= 1)

    def updateLine(self,v, s):
        self.x1 = v.x
        self.y1 = v.y
        sT = s.unit()
        self.x2 = self.x1 + sT.x*self.length
        self.y2 = self.y1 + sT.y*self.length
    def overlapBox(self, b):
        left = False
        if(not self.collider):
            if(self.x1 - self.length < b.x < self.x1 + self.length):
                if(self.y1 -self.length < b.y < self.y1+self.length):
                    left = self.overlap(Line(b.x-b.width/2, b.y-b.height/2, b.x-b.width/2, b.y+b.height/2, 100))
                    if(left):
                        self.collider = True
        return left


def createLine(x1, y1, v, length):
    v = v.unit()
    l = Line(x1, y1, (x1+v.x*length), (y1+v.y*length), length)
    add(l)
    return l


        








