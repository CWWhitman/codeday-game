import pygame
import joinGame
import networking
import editor

BLACK =(0,0,0)
WHITE =(255,255,255)

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



def main(winner):
    
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
    screen.blit(font.render(("Winner! : " + winner), True, WHITE), [400,10])    

    startGameButton = MenuButton(0)
    activeSprites.add(startGameButton)

    backgroundSprites.draw(screen)
    activeSprites.draw(screen)
 

    while not done:

        font = pygame.font.SysFont('Calibri', 30, True, False)
        screen.blit(font.render(("Winner! : " + winner), True, WHITE), [350,100])

        event = pygame.event.poll()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if startGameButton.rect.collidepoint(pygame.mouse.get_pos()):
                    networking.restartGame()
                    editor.main()
                    pygame.quit()

        elif event.type == pygame.QUIT:
            done = True
        
        pygame.display.flip()
 
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
    
