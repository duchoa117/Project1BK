import pygame
from frameCounter import FrameCounter
f1 = FrameCounter(10)
f2 = FrameCounter(10)
f1.expired = True
f2.expired = True

class InputManager:
    def __init__(self):
        self.right_pressed = False
        self.left_pressed = False


    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:           
                self.right_pressed = True         
            elif event.key == pygame.K_LEFT:           
                self.left_pressed = True                   
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right_pressed = False     
            elif event.key == pygame.K_LEFT:
                self.left_pressed = False
                
                