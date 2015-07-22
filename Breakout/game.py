import pygame
from pygame.locals import *
import random, sys
from block import Block
from ball import Ball
from paddle import Paddle

# Color Pallet
blue = (73,145,232)
purple = (232,73,225)
orange = (232,160,73)
green = (73,232,74)

# Game Speed
game_speed = 2

class Game(object):
    """Main program"""

    def __init__(self):
        #Initialize pygame and window
        pygame.init()
        self.screen_width, self.screen_height = 400, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        self.screen.fill(blue)
        pygame.display.update()

        #Clock
        self.clock = pygame.time.Clock()

        #Bricks
        self.blocks = list()
        for w in range(1,self.screen_width,50):
			for h in range(23, 198, 22):
				self.blocks.append(Block(self.screen_width, self.screen_height, w, h))

        #Paddle
        self.paddle = Ball(self.screen_width, self.screen_height)

        #Ball
        self.ball = Ball(self.screen_width, self.screen_height, green, blue)

    def update(self):
        self.clock.tick(game_speed)

    def draw(self):
        #Redraw Background
        self.screen.fill(blue)

        for block in self.blocks:
            block.draw(self.screen)

        self.ball.draw(self.screen)
        self.paddle.draw(self.screen)

    def new_game(self):
        self.game_over = False
        self.round = 0

        self.play()

    def new_round(self):
        pass

    def play(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()
            self.draw()
            pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.new_game()
