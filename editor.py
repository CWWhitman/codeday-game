import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

SIZE_X = 50
SIZE_Y = 25

class Background(pygame.sprite.Sprite):

    def __init__(self):
        """ Constructor function """
 
        pygame.sprite.Sprite.__init__()
        self.image = pygame.image.load('background.png')

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0

class Tile(pygame.sprite.Sprite):

    name = ''

    def __init__(self, x, y, name):

        self.name = name

        pygame.sprite.Sprite.__init__()
        self.image = pygame.image.load(name)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changeImage(self, name):

        self.image = pygame.image.load(name)

    def getName(self)

        return self.name

class menu(pygame.sprite.Sprite)

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__()
        
        self.image = pygame.Surface([30, SIZE_Y])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

def main():

    pygame.init()
    screen = pygame.display.set_mode([SIZE_X * 30, SIZE_Y * 30])
    
    pygame.display.set_caption('Editor')

    background = Background()
    allSprites = pygame.sprite.Group()
    allSprites.add(background)

    tiles = []
    allTiles = pygame.sprite.Group()
    
    for i in range(SIZE_X):
        tilesRow = []
        for j in range(SIZE_Y):
            tile = Tile((i-1)*SIZE_X, (i-1)*SIZE_Y, 'blank.png')
            tilesRow.append(tile)
            allTiles.add(tile)
        tiles.append(tilesRow)

    clock = pygame.time.Clock()

    pygame.mouse.set_visible(True)

    tilePos = (0,0)
    mousePressed = False
 
    done = False

##    while not done:
##
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                done = True
##
##            if event.type == pygame.MOUSEBUTTONDOWN:
##                if pygame.mouse.get_pressed()[0]:
##                    mousePressed = True
##                    #tilePos = pygame.mouse.pos()
##
##            if event.type == pygame.MOUSEBUTTONUP:
##                if pygame.mouse.get_pressed()[0]:
##                    mousePressed = False

        while not done:

            if pygame.event.poll().type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mousePressed = True

            if pygame.event.poll().type == MOUSEBUTTONUP:
                if pygame.mouse.get_pressed()[0]:
                    mousePressed = False

            if pygame.event.poll().type == MOUSEBUTTONUP:
                
