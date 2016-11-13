import pygame
import joinGame,

WHITE = (255, 255, 255)

buttons = ['res/startgamee.png']
title = 'res/title.png'

class Background(pygame.sprite.Sprite):

    def __init__(self):
        """ Constructor function """
 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('res/scaledbg.png')

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0

class MenuButton(pygame.sprite.Sprite):

    def __init__(self, button):
        """Constructor"""

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(buttons[button])

        self.rect = self.image.get_rect()
        self.rect.y = 400
        self.rect.x = 400



def main(winners):
    pygame.init()
    screen = pygame.display.set_mode([900, 450])

    pygame.display.set_caption('Menu')

    backgroundSprites = pygame.sprite.Group()
    activeSprites = pygame.sprite.Group()

    background = Background()
    backgroundSprites.add(background)

    clock = pygame.time.Clock()

    done = False

    font = pygame.font.SysFont('Calibri', 30, True, False)
    screen.blit(font.render(("1st: " + winners[0]), True, BLACK), [400,10])
    screen.blit(font.render(("2nd: " + winners[1]), True, BLACK), [400,30])
    screen.blit(font.render(("3rd: " + winners[2]), True, BLACK), [400,50])
    

    startGameButton = MenuButton(0)
    activeSprites.add(startGameButton)

    while not done:

        event = pygame.event.poll()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if startGameButton.rect.collidepoint(pygame.mouse.get_pos()):
                    joinGame.main()
                    pygame.quit()

        elif event.type == pygame.QUIT:
            done = True
            
        screen.fill(WHITE)
 
        backgroundSprites.draw(screen)
        activeSprites.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
    
