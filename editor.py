import pygame
import networking
from game import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

SIZE_X = 30
SIZE_Y = 15

blocks = ['res/blankBlock1.png', 'res/Spiky Wheel.png', 'res/Wall.png', 'res/startBlock.png', 'res/finishBlock.png']
blocksSelected = ['res/blankBlockSelected.png', 'res/SpikyWheelSelect.png', 'res/Wall Select.png',
                  'res/startBlockSelected.png', 'res/finishBlockSelected.png']

class Background(pygame.sprite.Sprite):

    def __init__(self):
        """ Constructor function """
 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('res/scaledbg.png')

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0

class Tile(pygame.sprite.Sprite):

    name = ''

    def __init__(self, x, y, name):

        self.name = name

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(name)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changeImage(self, name):

        self.image = pygame.image.load(name)
        self.name = name

    def getName(self):

        return self.name

class Clear(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([120, 60])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.y = 195
        self.rect.x = 390

        font = pygame.font.SysFont('Calibri', 25, True, False)
        self.image.blit(font.render("Clear all?", True, BLACK), [10, 5])
        self.image.blit(font.render("  Y        N", True, BLACK), [10, 35])

class Menu(pygame.sprite.Sprite):

    x = 0
    selected = 0

    def __init__(self, x, selected):

        self.x = x
        self.selected = selected
        pygame.sprite.Sprite.__init__(self)
        
        self.changeX(x)

    def changeX(self, x):

        self.x = x
        
        self.image = pygame.Surface([30, SIZE_Y * 30])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = x

        menuTiles = pygame.sprite.Group()
        for i in range(len(blocks)):
            if (i) == self.selected:
                tile = Tile(0, (i) * 30, blocksSelected[i])
                menuTiles.add(tile)
            else:
                tile = Tile(0, (i) * 30, blocks[i])
                menuTiles.add(tile)

        font = pygame.font.SysFont('Calibri', 13, True, False)
        self.image.blit(font.render("up-k", True, WHITE), [0, 370])
        self.image.blit(font.render("down", True, WHITE), [0, 400])
        self.image.blit(font.render("-s", True, WHITE), [0, 410])
        self.image.blit(font.render("clr-c", True, WHITE), [0, 440])

        menuTiles.draw(self.image)

    def changeSelection(self, selected):

        if selected < 0:
            selected = 0
        if selected > len(blocks) - 1:
            selected = (len(blocks) - 1)

        self.selected = selected

def main():

    pygame.init()
    screen = pygame.display.set_mode([SIZE_X * 30, SIZE_Y * 30])
    
    pygame.display.set_caption('CPG.e')

    allSprites = pygame.sprite.Group()
    menuGroup = pygame.sprite.Group()

    menu = Menu(0, 0)
    menuGroup.add(menu)
    clear = Clear()

    background = Background()
    allSprites.add(background)

    tiles = []
    allTiles = pygame.sprite.Group()
    
    for i in range(SIZE_X):
        tilesRow = []
        for j in range(SIZE_Y):
            tile = Tile((i)*30, (j)*30, 'res/blankBlock1.png')
            tilesRow.append(tile)
            allTiles.add(tile)
        tiles.append(tilesRow)

    activeTile = tiles[0][0]
    
    clock = pygame.time.Clock()

    clearing = False;

    pygame.mouse.set_visible(True)
    mousePressed = False

    start = False
    end = False
 
    done = False

    while not done:

        event = pygame.event.poll()

        mouseX = int(round(pygame.mouse.get_pos()[0]/30))
        if mouseX > 29:
            mouseX = 29
        mouseY = int(round(pygame.mouse.get_pos()[1]/30))
        if mouseY > 14:
            mouseY = 14
        activeTile = tiles[mouseX][mouseY]

        if event.type == pygame.QUIT:
            done = True

        if pygame.mouse.get_pressed()[0]:
            mousePressed = True
        else:
            mousePressed = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                menu.changeSelection(menu.selected-1)

            if event.key == pygame.K_s:
                menu.changeSelection(menu.selected+1)

            if event.key == pygame.K_SPACE:
                done = True

            if event.key == pygame.K_c:
                menuGroup.add(clear)
                clearing = True

            if event.key == pygame.K_n and clearing:
                menuGroup.remove(clear)
                clearing = False

            if event.key == pygame.K_y and clearing:
                menuGroup.remove(clear)
                tilesNew = []
                allTiles.empty()
                for i in range(SIZE_X):
                    tilesRow = []
                    for j in range(SIZE_Y):
                        tile = Tile((i)*30, (j)*30, 'res/blankBlock1.png')
                        tilesRow.append(tile)
                        allTiles.add(tile)
                    tilesNew.append(tilesRow)
                tiles = tilesNew
                start = False
                end = False
                clearing = False

        if pygame.mouse.get_pos()[0] >= (SIZE_X / 2 * 30):
            menu.changeX(0)
        else:
            menu.changeX((SIZE_X - 1) * 30)

        if mousePressed and menu.selected == 3 and not start:
            activeTile.changeImage(blocks[menu.selected])
            start = True;

        elif mousePressed and menu.selected == 4 and not end:
            activeTile.changeImage(blocks[menu.selected])
            end = True;
            
        elif mousePressed and not menu.selected == 3 and not menu.selected == 4:
            if menu.selected == 0 and activeTile.getName() == 'res/startBlock.png':
                start = False
            if menu.selected == 0 and activeTile.getName() == 'res/finishBlock.png':
                end == False
            activeTile.changeImage(blocks[menu.selected])
 
        allSprites.draw(screen)
        allTiles.draw(screen)
        menuGroup.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)
        
    font = pygame.font.SysFont('Calibri', 50, True, False)
    screen.blit(font.render("Waiting for players...", True, RED), [0, 0])
    pygame.display.flip()
    #networking.levelBuilt(convirtList(tiles))
    game1 = gameplay(convertList(tiles))
    game1.mainloop()

def convertList(inputList):
    returnList = []
    for i in range(SIZE_X):
        returnListRow = []
        for j in range(SIZE_Y):
            tile = inputList[i][j]
            returnListRow.append(tile.getName())
        returnList.append(returnListRow)
    return returnList

if __name__ == "__main__":
    main()
