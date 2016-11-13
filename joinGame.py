import pygame, sys, eztext, settings, networking, editor

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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

    pygame.display.set_caption('Join Game')

    allSprites = pygame.sprite.Group()

    background = Background()
    allSprites.add(background)

    ip = eztext.Input(maxlength=45, color=BLACK, prompt='enter ip: ')
    ip.set_pos(0,0)
    port = eztext.Input(maxlength=45, color=BLACK, prompt='enter port:(default 28015) ')
    port.set_pos(0,50)
    name = eztext.Input(maxlength=45, color=BLACK, prompt='enter name: ')
    name.set_pos(0,100)

    clock = pygame.time.Clock()

    done = False

    i = 0

    while not done:

        clock.tick(30)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    i +=1
                elif event.key == pygame.K_ESCAPE:
                    i -=1
                

        allSprites.draw(screen)
        if i == 0:
            ip.update(events)
            ip.draw(screen)

        if i == 1:
            port.update(events)
            port.draw(screen)

        if i == 2:
            name.update(events)
            name.draw(screen)

        if i == 3:
            #print ip.value, port.value, name.value
            font = pygame.font.SysFont('Calibri', 30, True, False)
            screen.blit(font.render(("IP = " + ip.value), True, BLACK), [0,0])
            screen.blit(font.render(("port = " + port.value), True, BLACK), [0,50])
            screen.blit(font.render(("name = " + name.value), True, BLACK), [0,100])
            screen.blit(font.render("Press Enter to continue, Escape to go back", True, BLACK), [0,150])

        if i == 4:
            settings.connectionSettings['ip'] = ip.value
            settings.connectionSettings['port'] = port.value
            settings.connectionSettings['user'] = name.value
            networking.startGame()
            editor.main()
            pygame.quit()
            
 
        pygame.display.flip()

 

    pygame.quit()

if __name__ == "__main__":
    main()
    
