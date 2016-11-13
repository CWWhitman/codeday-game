import level
lev = map(list, level.l)
import pygame, sys
from player import *
from pygame.locals import *
from copy import deepcopy

class Block(pygame.sprite.Sprite):
    def __init__(self, color, pos):
        super(Block, self).__init__()
        self.rect = Rect(pos)

class gameplay:
    """The Main PyMan Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width=900,height=450):
        self.state = {"x": 12}
        pygame.init()
        pygame.display.set_caption('videogames')
        self.basicfont = pygame.font.SysFont(None, 48)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background_screen = pygame.Surface((self.width, self.height))
        self.players = pygame.sprite.Group()
        self.world = pygame.sprite.Group()
        self.setupgame()

    def setupgame(self):
        self.text = self.basicfont.render("testing memes", True, (0,0,0), (0,0,255))
        for x, _ in enumerate(lev):
            for y, char in enumerate(lev[x]):
                pos = (y * 30, x * 30, 30,30)
                if int(char):
                    color = (255,0,100)
                    self.world.add(Block(color, pos))
                else:
                    color = (0,0,255)
                pygame.draw.rect(self.background_screen, color, pos)
        tommy = Player(0,200)
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
                brec = deepcopy(a.rect)
                a.rect.h = 15
                a.rect.top = brec.top + 17
                #pygame.draw.rect(self.screen, (255,255,0), a.rect)
                if not pygame.sprite.spritecollideany(a, self.world):
                    a.on_ground = False
                    a.above_land = False
                else:
                    a.above_land = True
                a.rect = brec
            intd = pygame.sprite.groupcollide(self.players, self.world, False, False)
            for a in intd:
                player, block = a,intd[a]
                print player,block
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
                    player.rect.x = player.rect.x - player.vel_x
                    player.rect.y = player.rect.y - player.vel_y
                    player.vel_y = player.vel_y - player.accl_y
                    player.vel_x = player.vel_x - player.accl_x
                if blockf.w > blockf.h:
                    #top/bottom int
                    player.vel_y = 0
                    player.rect.y = player.rect.y - (blockf.h if player.above_land else -1 * blockf.h)
                    player.on_ground = True
                else:
                    #left/r intesection
                    player.vel_x = 0
                    player.rect.x = player.rect.x - blockf.w

            for a in self.players:
                pygame.draw.rect(self.screen, (0,255,255), a.rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
    main = gameplay()
    main.mainloop()
