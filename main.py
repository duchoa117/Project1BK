
import pygame 
from inputManager import InputManager
from gameObject import game_objects, GameObject, add
from map.canvas import Background
from map.matrixMap import generate_map
from point import Point
from boxes import Boxes
from createPlayer import createplayer,playerL
from createBoxes import createBoxes, bs
from createLines import createLines, lines


# 0. setup game
inputManager = InputManager()
# bg = Background()
# add(bg)
# player = Player(inputManager)
createplayer(inputManager)
point = Point()
add(point)
# add(player)
createBoxes()
createLines()
generate_map("assets/maps/map2.json")

# 1. Init pygame
pygame.init()
# 2. Set screen
SIZE = (32*25, 20*32)
canvas = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Hello baibe')
# 3. Clock
clock = pygame.time.Clock()

loop = True







while loop:
    # 1. Event processing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            inputManager.update(event)
    canvas.fill((0, 0, 0))
    for player in playerL:
        player.update()
        player.render(canvas)
    for obj in game_objects:
        obj.render(canvas)
        obj.update()
    for b in bs:
        b.update()
        b.render(canvas)
    for l in lines:
        l.update()
        l.render(canvas)
    
    # 3. Flip
    pygame.display.flip()
    clock.tick(60)