from boxCollider import BoxCollider
from vector import Vector
from gameObject import game_objects
from point import Point
bs = []
class Boxes():
    def __init__(self, player):

        self.boxa = BoxCollider(1,1)
        self.boxb = BoxCollider(1,1)
        self.boxmid = BoxCollider(1,1)
        self.a = 1
        self.b = 1
        self.player = player
    def render(self, canvas):
        
        if self.player.is_active:
            self.boxa.render(canvas)
            self.boxb.render(canvas)
            self.boxmid.render(canvas)
    def update(self):
    
        t1 = Vector(-self.player.speed.y, self.player.speed.x).unit()
        t2 = Vector(self.player.speed.y, -self.player.speed.x).unit()
        s1 = Vector(-self.player.speed.x, -self.player.speed.y)

        a = self.player.center.addNew(self.player.speed.unit().mul(self.player.width/2)).addNew(t1.mul(self.player.height/2))
        b = self.player.center.addNew(self.player.speed.unit().mul(self.player.width/2)).addNew(t2.mul(self.player.height/2))
        d = self.player.center.addNew(s1.unit().mul(self.player.width/2)).addNew(t1.mul(self.player.height/2))
        c = self.player.center.addNew(s1.unit().mul(self.player.width/2)).addNew(t2.mul(self.player.height/2))
        self.a = a
        self.b = b 
        self.mid = self.player.center.addNew(self.player.speed.unit().mul(self.player.width/2))
        self.boxa.x = self.a.x
        self.boxa.y = self.a.y
        self.boxb.x = self.b.x
        self.boxb.y = self.b.y
        self.boxmid.x = self.mid.x
        self.boxmid.y = self.mid.y
        for game_object in game_objects:
            if type(game_object) == Point:
                        overlapPoint = BoxCollider.overlap(self.boxa, game_object.box_collider) or BoxCollider.overlap(self.boxb, game_object.box_collider) or BoxCollider.overlap(self.boxmid, game_object.box_collider)
                        if(overlapPoint):
                            game_object.is_active = False
                            # overlapPoint = False
                            self.player.speed.add(self.player.speed.unit().mul(0.1))
        
