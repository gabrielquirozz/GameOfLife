#Gabriel Quiroz 19255
#Game of Life

import pygame
import random

blanco = (255, 255, 255)
negro = (0, 0, 0)
rows = 20

class Life(object):
    def __init__(self, screen):
        _, _, self.width, self.height = screen.get_rect()
        self.screen = screen


    def clear(self):
        self.screen.fill(negro)

    def pixel(self, x, y, color):
        self.screen.set_at((x, y), color)

    def copy(self):
        self.prev_turn = self.screen.copy()
    
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                vecinos = 0
                try:
                    if (self.prev_turn.get_at((i+1,j))[0] == 255):
                        vecinos += 1
                except:
                    pass
                
                try:
                    if (self.prev_turn.get_at((i-1,j))[0] == 255):
                        vecinos += 1
                except:
                    pass
                
                try:
                    if (self.prev_turn.get_at((i,j-1))[0] == 255):
                        vecinos += 1
                except:
                    pass
                
                try:
                    if (self.prev_turn.get_at((i,j+1))[0] == 255):
                        vecinos += 1
                except:
                    pass
                
                try:
                    if (self.prev_turn.get_at((i+1,j+1))[0] == 255):
                        vecinos += 1
                except:
                    pass
                
                try:
                    if (self.prev_turn.get_at((i-1,j-1))[0] == 255):
                        vecinos += 1
                except:
                    pass
                
                try:
                    if (self.prev_turn.get_at((i-1,j+1))[0] == 255):
                        vecinos += 1
                except:
                    pass
                
                try:
                    if (self.prev_turn.get_at((i+1,j-1))[0] == 255):
                        vecinos += 1
                except:
                    pass
                
                if (self.prev_turn.get_at((i,j))[0] == 255):
                    if vecinos < 2:
                        self.pixel(i, j, negro)
                    if vecinos == 2 or vecinos == 3:
                        self.pixel(i, j, blanco)
                    if vecinos > 3:
                        self.pixel(i, j, negro)
                if (self.prev_turn.get_at((i,j))[0] == 0):
                    if vecinos == 3:
                        self.pixel(i, j, blanco)
  



pygame.init()
screen = pygame.display.set_mode((200, 200))
r = Life(screen)


for i in range(r.width * rows ):
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    r.pixel(x,y, blanco)
    

while True:
  pygame.time.delay(100)
  r.copy()
  r.clear()
  r.render()
  pygame.display.flip()
