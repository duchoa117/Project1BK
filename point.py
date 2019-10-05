from gameObject import GameObject, game_objects
from vector import Vector
from random import choice
from boxCollider import BoxCollider
from renderers.image_renderer import ImageRenderer
f = open("map.txt", "r")
pData = []
data = f.readlines()
len = len(data)
for i in range(0, len, 2):
    v = Vector(float(data[i]), float(data[i+1]))
    pData.append(v)
f.close()
class Point(GameObject):
    def __init__(self): 
        t = choice(pData)
        GameObject.__init__(self, t.x, t.y)
        self.box_collider = BoxCollider(20, 20)
        self.renderer = ImageRenderer("/Users/apple/Desktop/ai:mlPr/carDrive/assets/images/point.png")
    def update(self):
        GameObject.update(self)
        if not self.is_active:
            p = choice(pData)
            self.x = p.x
            self.y = p.y
            self.is_active = True
    def render(self, canvas):
        GameObject.render(self, canvas)







