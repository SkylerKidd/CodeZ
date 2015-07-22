import pygame

class Block(object):
    def __init__(self, screen_width, screen_height, x, y, color, bkg_color):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width, self.height = 48, 20

        self.x = x
        self.y = y

        self.rect = (self.x, self.y, self.width, self.height)
        self.shadow_rect = (self.x+3, self.y+3, self.width, self.height)

        self.color = color
        self.shadow_color = bkg_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.shadow_color, self.shadow_rect, 0)
        pygame.draw.rect(screen, self.color, self.rect, 0)
