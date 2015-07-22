import pygame
import random

gameSpeed = 20

#Colors
white = (255, 255, 255)
red   = (255,   0,   0)
blue  = (  0,   0, 255)
green = (  0, 255,   0)

class Game(object):
    """Class Level Variables"""

    #Clock
    clock = pygame.time.Clock()

    #Screen Setup
    screen_width = 600
    screen_height = 400

    #Green Dot
    green_dot = pygame.image.load("img/green_dot.png")
    gd_x = (screen_width / 2) - 25
    gd_y = (screen_height / 2) - 25

    #Grid Setup
    noTilesX = 8
    noTilesY = 8
    tile_width = screen_width / noTilesX
    tile_height = screen_height / noTilesY

    #Initialization
    def __init__(self):
        """Place initialization methods here"""
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height], 0, 32)
        self.screen.fill(blue)

    #Load Content
    def loadContent(self):
        "Place content loading here"
        #print "content loaded"

    #Update Calls
    def update(self):
        "Update calls here"
        #print "updating..."
        self.clock.tick(gameSpeed)

        #Green dot random movement
        gd_xmove = random.randint(-1,1)
        self.gd_x += gd_xmove
        gd_ymove = random.randint(-1,1)
        self.gd_y += gd_ymove


    #Draw Calls
    def draw(self):
        "Draw calls here"
        #print "drawing"
        self.screen.fill(blue)
        self.screen.blit(self.green_dot,(self.gd_x,self.gd_y))
