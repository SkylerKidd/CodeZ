import pygame

#I PUT THIS IN CAUSE EVERYONE ELSE DID (knowledge of screen and start point?)
class Paddle(object):
    def __init__(self, screen_width, screen_height, color, bkg_color):
        self.screen_width = screen_width
        self.screen_height = screen_height

        #Actual Size of Object
        self.width, self.height = 80, 15

        #Not Entirely Sure...something about velocity
        self.x = (screen_width / 2) - (self.width / 2)
        self.y = screen_height - 25
        self.x_vel = 0

        #ITS A RECTANGLE
        self.rect = (self.x, self.y, self.width, self.height)
        self.shadow_rect = (self.x+3, self.y+3, self.width, self.height)

        #Color
        self.color = color
        self.shadow_color = bkg_color

    #Update Function
    def update(self):

        #Paddle reaches left side
        if self.x <= 0 and not self.x_vel > 0:
            self.x_vel = 0

        #Paddle reaches right side
        if self.x >= (self.screen_width-self.width) and not self.x_vel < 0:
            self.x_vel = 0

        self.x += self.x_vel
        self.rect = (self.x, self.y, self.width, self.height)
        self.shadow_rect = (self.x+3, self.y+3, self.width, self.height)


    #Drawing Things
    def draw(self, screen):
        pygame.draw.rect(screen, self.shadow_color, self.shadow_rect, 0)
        pygame.draw.rect(screen, self.color, self.rect, 0)

    def set_x_vel(self, x_vel):
        self.x_vel = x_vel
