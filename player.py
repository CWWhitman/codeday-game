import pygame

jump_key_pressed = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.health = 2
        self.alive = True

        self.rect = pygame.Rect(0, 0, 30, 30)
        self.vel_x, self.vel_y = 0.0, 0.0
        self.accl_x, self.accl_y = 0.0, 0.0

        self.on_ground = True
        self.jump_frame = 1
        self.holding_jump = False


    def spawn(self, x, y):
        self.alive = True
        self.pos_x, self.pos_y = x, y

    def jump(self):
        if self.on_ground:
            self.on_ground = False

        self.vel_y += 2/self.jump_frame
        if self.jump_frame > 15:
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
            self.accl_y = -1.0

    def update(self):

        if not jump_key_pressed and self.holding_jump:
            self.holding_jump = False

        if (jump_key_pressed and self.on_ground) or self.holding_jump:
            jump()
        self.apply_accel()
        self.apply_vel()
        self.gravity()

#tommy = Player()
#def show():
#    print tommy.vel_x, tommy.vel_y
#    print tommy.accl_x, tommy.accl_y
