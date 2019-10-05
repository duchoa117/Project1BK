import pygame
import math
from gameObject import GameObject, game_objects
from point import Point
from vector import Vector
# from lineCollider import Line, createLine, overlapBox

class Player(GameObject):
    def __init__(self, inputManganer):
        GameObject.__init__(self, 200, 100)
        self.width = 24
        self.height = 12
        self.speed = Vector(3,0)
        self.inputManganer = inputManganer
        self.center = Vector(200, 100)
        self.check = True 
        
        self.a = None
        self.b = None
        self.mid = self.center.addNew(self.speed.unit().mul(self.width/2))
        self.run = True
       
        


    def render(self, canvas):
        t1 = Vector(-self.speed.y, self.speed.x).unit()
        t2 = Vector(self.speed.y, -self.speed.x).unit()
        s1 = Vector(-self.speed.x, -self.speed.y)

        a = self.center.addNew(self.speed.unit().mul(self.width/2)).addNew(t1.mul(self.height/2))
        b = self.center.addNew(self.speed.unit().mul(self.width/2)).addNew(t2.mul(self.height/2))
        d = self.center.addNew(s1.unit().mul(self.width/2)).addNew(t1.mul(self.height/2))
        c = self.center.addNew(s1.unit().mul(self.width/2)).addNew(t2.mul(self.height/2))
        self.a = a
        self.b = b 
       

        if self.is_active:
            pygame.draw.polygon(canvas, (255, 255, 255), [(a.x, a.y), (b.x, b.y), (c.x, c.y), (d.x, d.y)])
           
    def update(self):

        a = math.sqrt(self.speed.x*self.speed.x + self.speed.y*self.speed.y)
        if self.inputManganer.right_pressed:
            self.speed.rotate(math.pi/(125/a), 'r')
            self.run = True
        elif self.inputManganer.left_pressed:
            self.run = True
            self.speed.rotate(math.pi/(125/a), 'l')
        if self.run:
            self.center.add(self.speed)
        
        


        