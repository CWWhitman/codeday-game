import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

SIZE_X = 50
SIZE_Y = 25

blocks = ['spikes.png']
blocksSelected = ['spikesSelected.png']

class Background(pygame.sprite.Sprite):

    def __init__(self):
        """ Constructor function """
 
        pygame.sprite.Sprite.__init__()
        self.image = pygame.image.load('bg.png')

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

    def getName(self):

        return self.name

class Menu(pygame.sprite.Sprite):

    menuTileList = []
    x = 0
    selected = 0

    def __init__(self, x, selected):

        self.x = x
        self.selected = selected
        pygame.sprite.Sprite.__init__()
        
        self.changeX(x, selected)

    def changeX(self, x):

        self.x = x
        
        self.image = pygame.Surface([30, SIZE_Y])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = x

        menuTiles = pygame.sprite.Group()
        for i in range(len(blocks)):
            if (i-1) == self.selected:
                tile = Tile(x, (i-1) * SIZE_Y, blocksSelected[i-1])
                self.menuTileList.append(tile)
                menuTiles.add(tile)
            else:
                tile = Tile(x, (i-1) * SIZE_Y, blocks[i-1])
                self.menuTileList.append(tile)
                menuTiles.add(tile)

        menuTiles.draw(self.image)

    def changeSelection(self, selected):

        self.selected = selected
        
        self.image = pygame.Surface([30, SIZE_Y])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = self.x

        menuTiles = pygame.sprite.Group()
        for i in range(len(blocks)):
            if (i-1) == selected:
                tile = Tile(self.x, (i-1) * SIZE_Y, blocksSelected[i-1])
                self.menuTileList.append(tile)
                menuTiles.add(tile)
            else:
                tile = Tile(self.x, (i-1) * SIZE_Y, blocks[i-1])
                self.menuTileList.append(tile)
                menuTiles.add(tile)

        menuTiles.draw(self.image)

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

    menu = Menu(0, 0)

    clock = pygame.time.Clock()

    pygame.mouse.set_visible(True)
 
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

        event = pygame.event.poll()

        if event.type == pygame.QUIT:
                done = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                mousePressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pressed()[0]:
                    mousePressed = False

        elif event.type == pygame.KEYDOWN:
            if event[1] == pygame.K_w:
                menu.changeSelection(menu.selection-1)

            if event[1] == pygame.K_s:
                menu.changeSelection(menu.selection+1)

        if pygame.mouse.pos()[0] >= (SIZE_X / 2):
            menu.changeX(0)
        else:
            menu.changeX(SIZE_X - 30)

        if mousePresse
