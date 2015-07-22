import pygame

class Ball(object):
    def __init__(self, screen_width, screen_height, color, bkg_color, linked = True):
        self.screen_width = screen_width
        self.screen_height = screen_height

        #DECIDE WHAT RADIUS SHOULD BE
        self.r = 12

        self.x = screen_width / 2
        self.y = screen_height - 37

        self.x_vel, self.y_vel = 0, 0

        self.circ = (self.x, self.y, self.r)

        self.linked = linked

        self.color = color
        self.shadow_color = bkg_color


    #update ball position
    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel

    #update ball velocity
    def accelerate(self, x_multipier, y_multiplier):
        self.x_vel *= x_multiplier
        self.y_vel *= y_multiplier

    #set ball velocity when "linked"
    def set_x_vel(self, x_vel):
        self.x_vel = x_vel

    def draw(self, screen):
        pygame.draw.circle(screen, self.shadow_color, (self.x+3, self.y+3), self.r, 0)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r, 0)
