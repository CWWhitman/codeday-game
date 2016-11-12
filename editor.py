import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

class Background(pygame.sprite.Sprite):

    def __init__(self):
        """ Constructor function """
 
        pygame.sprite.Sprite.__init__()
        self.image = pygame.image.load("background.png")

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0

class Tile(pygame.sprite.Sprite):

    def __init__(self, x, y, name):

        pygame.sprite.Sprite.__init__()
        self.image = pygame.image.load(name)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changeImage(self, name):

        self.image = pygame.image.load(name)
