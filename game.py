import level
lev = map(list, level.l)
import pygame, sys
from player import *
from pygame.locals import *

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
        self.bscreen = pygame.Surface((self.width, self.height))
        self.players = pygame.sprite.Group()
        self.world = pygame.sprite.Group()
        self.setupgame()



    def setupgame(self):
        self.text = self.basicfont.render("testing memes", True, (0,0,0), (0,0,255))
        for x, _ in enumerate(lev):
            for y, char in enumerate(lev[x]):
                if int(char):
                    color = (255,0,100)
                else:
                    color = (0,0,255)
                pos = (y * 30, x * 30, 30,30)
                pygame.draw.rect(self.bscreen, color, pos)

        tommy = Player(0,200)
        tommy.on_ground = True
        self.players.add(tommy)
        pygame.display.update()

    def mainloop(self):
        clock = pygame.time.Clock()
        pygame.time.delay(1000)
        while True:
            self.screen.blit(self.bscreen, (0,0))
            for a in self.players:
                a.update()
                pygame.draw.rect(self.screen, (0,255,255), a.rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            clock.tick(60)

if __name__ == '__main__':
    main = gameplay()
    main.mainloop()
