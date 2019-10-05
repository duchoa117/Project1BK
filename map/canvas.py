from gameObject import GameObject
from renderers.image_renderer import ImageRenderer

class Background(GameObject):
    def __init__(self):
        GameObject.__init__(self, 400, 320)
        self.renderer = ImageRenderer("/Users/apple/Desktop/ai:mlPr/carDrive/mapImages/map.png")
    