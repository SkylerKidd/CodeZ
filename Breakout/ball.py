import pygame

class Ball(object):
    def __init__(self, screen_width, screen_height, x, y):
        self.screen_width = screen_width
        self.screen_height = screen_height

        #DECIDE WHAT RADIUS SHOULD BE
        self.r = 15

        self.x, self.y = x, y
        self.x_vel, self.y_vel = 0, 0

        self.circ = (self.x, self.y, self.r)

        self.linked = True

        #(color is green)
        self.color = (73,232,74)

    def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.r, 0)
