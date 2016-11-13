import level
lev = map(list, level.l)
import pygame, sys
from player import *
from pygame.locals import *
from copy import deepcopy
import networking
import time

class Block(pygame.sprite.Sprite):
    def __init__(self, name, pos):
        super(Block, self).__init__()
        self.image = pygame.image.load(name)
        self.name = name

        self.rect = self.image.get_rect()
        self.rect.y = pos[1]
        self.rect.x = pos[0]

class gameplay:
    """The Main PyMan Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self):
        self.worldf = networking.getLevels()
        self.currentWorld = 0
        self.startTime = time.time()
        self.state = {"x": 12}
        pygame.init()
        pygame.display.set_caption('CPG')
        self.basicfont = pygame.font.SysFont(None, 48)
        #self.width = width
        #self.height = height
        self.screen = pygame.display.set_mode((900, 450))
        self.background_screen = pygame.image.load('res/scaledbg.png')
        self.players = pygame.sprite.Group()
        self.world = pygame.sprite.Group()
        self.setupgame()

        #images
        self.idle = pygame.image.load("res/idle.png")
        self.idler = pygame.transform.flip(self.idle, True, False)

    def setupgame(self):
        self.background_screen = pygame.image.load('res/scaledbg.png')
        self.text = self.basicfont.render("testing memes", True, (0,0,0), (0,0,255))
        self.players.empty()
        self.world.empty()
        worldNew = self.worldf[self.currentWorld]
        for x, _ in enumerate(worldNew):
            for y, char in enumerate(worldNew[x]):
                pos = (x * 30, y * 30)

                if char not in ['res/blankBlock1.png', 'res/startBlock.png']:
                    self.world.add(Block(char, pos))
                if char == 'res/finishBlock.png':
                    finishPos = pos
                if char == 'res/startBlock.png':
                    self.startPos = pos
                
                self.background_screen.blit(pygame.image.load(char), pos)
        a,b = self.startPos
        tommy = Player(a,b)
        tommy.on_ground = True
        self.players.add(tommy)
        pygame.display.update()
    #todo, make underbelly collision
    #todo, fix 3 way collision
    def mainloop(self):
        clock = pygame.time.Clock()
        while True:
            self.screen.blit(self.background_screen, (0,0))
            for a in self.players:
                a.update()
                if a.rect.x > 900 or a.rect.x < 0 or a.rect.y >= 450 or a.rect.y <= 0:
                    a.rect.x = self.startPos[0]
                    a.rect.y = self.startPos[1]
                a.player_on_wall = False
                brec = deepcopy(a.rect)
                a.rect.h = 4
                a.rect.w = 8
                a.rect.left = a.rect.left + 11
                a.rect.top = brec.top + 28
                if not pygame.sprite.spritecollideany(a, self.world):
                    a.on_ground = False
                    a.above_land = False
                else:
                    a.above_land = True
                a.rect.h = 8
                a.rect.w = 4
                a.rect.left = brec.left - 4
                a.rect.top = brec.top + 11
                #pygame.draw.rect(self.screen, (255,255,0), a.rect)
                if not pygame.sprite.spritecollideany(a, self.world):
                    a.world_is_left = False
                else:
                    a.world_is_left = True
                a.rect = brec
            intd = pygame.sprite.groupcollide(self.players, self.world, False, False)
            for a in intd:
                player, block = a,intd[a]
                a = [x.name for x in block]
                if 'res/Spiky Wheel.png' in a:
                    player.rect.x = self.startPos[0]
                    player.rect.y = self.startPos[1]
                if 'res/finishBlock.png' in a:
                    if self.currentWorld < len(self.worldf) - 1:
                        self.currentWorld += 1
                        self.setupgame()
                    else:
                        print networking.roundFinished(time.time() - self.startTime)
                yes = False
                if len(block) == 2:
                    if (block[0].rect.top == block[1].rect.top) or (block[1].rect.left == block[0].rect.left):
                        r = block[0].rect.clip(player.rect)
                        r1 = block[1].rect.clip(player.rect)
                        blockf = r.union(r1)
                if len(block) in [3,4]:
                    yes = True
                    r1 = block[0].rect.clip(player.rect)
                    r2 = block[1].rect.clip(player.rect)
                    r3 = block[2].rect.clip(player.rect)
                    # get all the recs
                    # iterate through them sperately, correct any two of them not unioned
                if len(block) == 1:
                    blockf = block[0].rect.clip(player.rect)
                # blocks are
                # deal with only one of the collided world blocks
                # ltaer, deal with one, then check the other one and deal if needed
                #pygame.draw.rect(self.screen, (255,255,0), blockf)
                if yes:
                    # 3way
                    player.rect.x = player.rect.x - player.vel_x - 0.001
                    player.rect.y = player.rect.y - player.vel_y - 0.001
                    player.vel_y = player.vel_y - player.accl_y - 0.001
                    player.vel_x = player.vel_x - player.accl_x - 0.001
                else:
                    if blockf.w > blockf.h:
                        #top/bottom int
                        player.vel_y = 0
                        player.rect.y = player.rect.y - (blockf.h if player.above_land else -1 * blockf.h)
                        player.on_ground = True
                    else:
                        player.player_on_wall = True
                        #left/r intesection
                        player.vel_x = 0
                        player.rect.x = player.rect.x - (blockf.w if not player.world_is_left else -1 * blockf.w)

            for a in self.players:
                #pygame.draw.rect(self.screen, (0,255,255), a.rect)
                if a.orientation_r:
                    self.screen.blit(self.idle, a.rect)
                else:
                    self.screen.blit(self.idler, a.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
    main = gameplay(lev)
    main.mainloop()
