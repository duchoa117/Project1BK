import pygame
from gameObject import game_objects, GameObject, add
import json
from addict import Dict
from renderers.image_renderer import ImageRenderer
from boxCollider import BoxCollider
# from createPlayer import playerL
from boxes import bs
from lines import lines

class Tree(GameObject):
    def __init__(self, x, y, path):
        GameObject.__init__(self, x, y)
        self.box_collider = BoxCollider(5,5)
    def render(self, canvas):
        # GameObject.render(self, canvas)
        for l in lines:
            if(l.line1.overlapBox(self.box_collider)):
                pygame.draw.circle(canvas, (255,255,0), (self.x, self.y), 5)
            if(l.line2.overlapBox(self.box_collider)):
                pygame.draw.circle(canvas, (255,255,0), (self.x, self.y), 5)
            if(l.line3.overlapBox(self.box_collider)):
                pygame.draw.circle(canvas, (255,255,0), (self.x, self.y), 5)
            if(l.line4.overlapBox(self.box_collider)):
                pygame.draw.circle(canvas, (255,255,0), (self.x, self.y), 5)
            if(l.line5.overlapBox(self.box_collider)):
                pygame.draw.circle(canvas, (255,255,0), (self.x, self.y), 5)
        pass
    def update(self):
        GameObject.update(self)
        for b in bs:
            overlap = BoxCollider.overlap(b.boxa, self.box_collider) or BoxCollider.overlap(b.boxb, self.box_collider) or BoxCollider.overlap(b.boxmid, self.box_collider)
            if overlap:
                b.player.run = False
                break
        
                

        

def load_map(json_file_url):
    # 1 load js >> text
    text = open(json_file_url, "r").read()
    # 2 convert text into dictionary
    map_dict = json.loads(text)
    map = Dict(map_dict)
    data = map.layers[0].data
    width = map.width
    height = map.height
    # 3 convert dic to object
    return data, width, height
def generate_map(json_file_url):
    data, width, height = load_map(json_file_url)
    for index, title in enumerate(data):
        title_x = (index % width)*2 + 1
        title_y = (index // width)*2 + 1
        if title == 0:
            pass
        elif title == 1:
            add(Tree(title_x,title_y,"assets/images/tree.png"))
if __name__ == "__main__":
    generate_map("../assets/maps/map2.json")
