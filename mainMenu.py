import pygame
import joinGame

buttons = ['res/squareBlock.png']
title = 'title.png'

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
        self.rect.y = 200
        self.rect.x = 400
    
def main():
    pygame.init()
    screen = pygame.display.set_mode([900, 450])

    pygame.display.set_caption('Menu')

    allSprites = pygame.sprite.Group()

    background = Background()
    allSprites.add(background)

    clock = pygame.time.Clock()

    done = False

    startGameButton = MenuButton(0)

    while not done:

        event = pygame.event.poll()

        if event.type == pygame.MOUSEBUTTON:
            if pygame.mouse.get_pressed()[0]:
                if startGameButton.rect.collidepoint(pygame.mouse.get_pos()):
                    print 'join game'
            
        screen.fill(WHITE)
 
        allSprites.draw(screen)
        allTiles.draw(screen)
        menuGroup.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)

if __name__ == "__main__":
    main()
    
