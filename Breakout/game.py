import pygame
import random

# Color Palet
blue = (73,145,232)
purple = (232,73,225)
orange = (232,160,73)
green = (73,232,74)

class Game(object):
    """Main program"""

    def __init__(self):
        #Initialize pygame and window
        pygame.init()
        self.screen_width, self.screen_height = 600, 1000

        #Clock
        self.clock = pygame.time.Clock()


    def draw(self):

        #Redraw Background
        self.screen.fill(blue)

    def new_game(self):
        self.game_over = False
        self.round = 0

    def new_round(self):
        pass

    def play(self):
        pass

if __name__ == '__main__':
	game = Game()
	game.new_game()
