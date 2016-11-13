import pygame

WHITE = (255, 255, 255)

class Background(pygame.sprite.Sprite):

    def __init__(self):
        """ Constructor function """
 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('res/scaledbg.png')

        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode([900, 450])

    pygame.display.set_caption('Menu')

    allSprites = pygame.sprite.Group()

    background = Background()
    allSprites.add(background)

    clock = pygame.time.Clock()

    done = False

    while not done:

        screen.fill(WHITE)
 
        allSprites.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)

if __name__ == "__main__":
    main()
    
