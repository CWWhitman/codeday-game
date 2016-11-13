import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.health = 2
        self.alive = True

        self.rect = pygame.Rect(x, y, 30, 30)
        self.vel_x, self.vel_y = 0.0, 0.0
        self.accl_x, self.accl_y = 0.0, 0.0

        self.on_ground = True
        self.jump_frame = 1
        self.jkp = False
        self.holding_jump = False

        self.frames_walked = 0


    def spawn(self, x, y):
        self.alive = True
        self.pos_x, self.pos_y = x, y

    def jump(self):
        if self.on_ground:
            self.on_ground = False

        self.vel_y += int(-(25 - self.jump_frame)/8)
        if self.jump_frame > 20:
            self.jump_frame = 1.0
            self.holding_jump = False
        else:
            self.jump_frame += 1.0

    def apply_accel(self):
        self.vel_x += self.accl_x
        self.vel_y += self.accl_y
        if self.on_ground:
            self.vel_y, self.accl_y = 0.0, 0.0

    def apply_vel(self):
        self.rect.move_ip(self.vel_x, self.vel_y)

    def gravity(self):
        if not self.on_ground:
            self.accl_y = 1.0

    def move_to_floor(self, correction):
        self.rect.move_ip(0, -correction)
        self.accl_y, self.vel_y, self.on_ground = 0, 0, True

    def walk(self, dir):
        self.frames_walked += 1
        if self.frames_walked < 60:
            speed = (self.frames_walked//12)*dir
        else:
            speed = 5*dir
        self.rect.move_ip(speed, 0)

    def update(self):
        pygame.event.pump()
        k = pygame.key.get_pressed()
        if k[pygame.K_UP]:
            self.jkp = True
        else:
            self.jkp = False
        if k[pygame.K_LEFT]:
            self.walk(-1)
        elif k[pygame.K_RIGHT]:
            self.walk(1)
        else:
            self.frames_walked = 0

        if self.on_ground and self.jkp:
            self.holding_jump = True

        if not self.jkp and self.holding_jump:
            self.holding_jump = False

        if (self.jkp and self.on_ground) or self.holding_jump:
            self.jump()


        self.apply_accel()
        self.apply_vel()
        self.gravity()

#tommy = Player()
#def show():
#    print tommy.vel_x, tommy.vel_y
#    print tommy.accl_x, tommy.accl_y
