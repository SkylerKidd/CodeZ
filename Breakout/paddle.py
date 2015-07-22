import pygame

#I PUT THIS IN CAUSE EVERYONE ELSE DID (knowledge of screen and start point?)
class Paddle(object):
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        #Actual Size of Object
        self.width, self.height = 30, 5

        #Not Entirely Sure...something about velocity
        self.x = (screen_width / 2) - (self.width / 2)
        self.y = screen_height - 25
        self.x_vel = 0

        #ITS A RECTANGLE
        self.rect = (self.x, self.y, self.width, self.height)

        #Color
        self.color = (232,73,225)

        #Update Function
        def update(self):
            self.x += self.x_vel

        #Drawing Things
        def draw(self, screen):
    		pygame.draw.rect(screen, self.color, self.rect, 0)
