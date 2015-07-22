import sys
import pygame
import game
from pygame.locals import *

pygame.init()
game = game.Game()
game.loadContent()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    game.update()
    game.draw()
    pygame.display.update()
