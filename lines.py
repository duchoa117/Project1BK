
from point import Point
from gameObject import GameObject
from vector import Vector
from lineCollider import Line, createLine
from boxes import Boxes
import math
lines = []
class Lines():
    def __init__(self, boxes):
        self.boxes = boxes
        self.line1 = createLine(self.boxes.player.center.x, self.boxes.player.center.y, self.boxes.player.speed, 200)
        self.line2 = createLine(self.boxes.player.center.x, self.boxes.player.center.y, self.boxes.player.speed.rotateNew(math.pi/2,"l"), 100)
        self.line3 = createLine(self.boxes.player.center.x, self.boxes.player.center.y, self.boxes.player.speed.rotateNew(math.pi/4, "l"), 100)
        self.line4 = createLine(self.boxes.player.center.x, self.boxes.player.center.y, self.boxes.player.speed.rotateNew(math.pi/2, "r"), 100)
        self.line5 = createLine(self.boxes.player.center.x, self.boxes.player.center.y, self.boxes.player.speed.rotateNew(math.pi/4, "r"), 100)
    def update(self):
        self.line1.updateLine(self.boxes.player.center, self.boxes.player.speed)
        self.line2.updateLine(self.boxes.player.center, self.boxes.player.speed.rotateNew(math.pi/2,"l"))
        self.line3.updateLine(self.boxes.player.center, self.boxes.player.speed.rotateNew(math.pi/4, "l"))
        self.line4.updateLine(self.boxes.player.center, self.boxes.player.speed.rotateNew(math.pi/2, "r"))
        self.line5.updateLine(self.boxes.player.center, self.boxes.player.speed.rotateNew(math.pi/4, "r"))
        self.line1.collider = False
        self.line2.collider = False
        self.line3.collider = False
        self.line4.collider = False
        self.line5.collider = False

    def render(self, canvas):
        # self.line1.render(canvas)
        # self.line2.render(canvas)
        # self.line3.render(canvas)
        # self.line4.render(canvas)
        # self.line5.render(canvas)
        pass
