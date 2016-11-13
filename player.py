import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.health = 2
        self.alive = True
        self.above_land = None
        self.world_is_left = None
        self.player_on_wall = None

        self.rect = pygame.Rect(x, y, 30, 30)
        self.vel_x, self.vel_y = 0.0, 0.0
        self.accl_x, self.accl_y = 0.0, 0.0

        self.on_ground = True
        self.jump_frame = 1

        self.frames_jumped = 0

        self.frames_walked = 0
        self.last_dir = 0

        self.orientation_r = True
        self.state = "idle"

        self.anim_timer = 0

        #images
        self.idle = pygame.image.load("res/idle.png")
        self.idler = pygame.transform.flip(self.idle, True, False)
        self.jumpup = pygame.image.load("res/jumpUp.png")
        self.jumpupr = pygame.transform.flip(self.jumpup, True, False)
        self.jumpdown = pygame.image.load("res/jumpDown.png")
        self.jumpdownr = pygame.transform.flip(self.jumpdown, True, False)
        self.run1 = pygame.image.load("res/run1.png")
        self.run1r = pygame.transform.flip(self.run1, True, False)
        self.run2 = pygame.image.load("res/run2.png")
        self.run2r = pygame.transform.flip(self.run2, True, False)
        


    def spawn(self, x, y):
        self.alive = True
        self.pos_x, self.pos_y = x, y

    def jump(self):
        self.frames_jumped += 1
        self.vel_y += -5/self.frames_jumped
        self.on_ground = False
        if self.frames_jumped > 15:
            self.frames_jumped = 0

    def apply_accel(self):
        self.vel_x += self.accl_x
        self.vel_y += self.accl_y
        if self.on_ground:
            self.vel_y, self.accl_y = 0.0, 0.0

    def apply_vel(self):
        self.rect.move_ip(self.vel_x, self.vel_y)

    def gravity(self):
        if not self.on_ground:
            self.accl_y = 1

    def move_to_floor(self, correction):
        self.rect.move_ip(0, -correction)
        self.accl_y, self.vel_y, self.on_ground = 0, 0, True

    def walk(self, dir):
        if not self.last_dir:
            pass
        elif self.last_dir != dir:
            self.frames_walked = 0

        self.frames_walked += 1
        if self.frames_walked < 10:
            speed = (self.frames_walked//1.25)*dir
        else:
            speed = 8*dir
        self.vel_x = speed
        self.state = "run" + str(self.anim_timer//30+1)

    def get_image(self):
        if not self.orientation_r:
            state = self.state + 'r'
        else:
            state = self.state

        name_to_image = {
                            "idle":self.idle,
                            "idler":self.idler,
                            "jumpup":self.jumpup,
                            "jumpupr":self.jumpupr,
                            "jumpdown":self.jumpdown,
                            "jumpdownr":self.jumpdownr,
                            "run1":self.run1,
                            "run1r":self.run1r,
                            "run2":self.run2,
                            "run2r":self.run2r,
            }

        return name_to_image[state]
                            
                            

    def update(self):
        pygame.event.pump()
        k = pygame.key.get_pressed()
        if k[pygame.K_w] and (self.frames_jumped or self.on_ground):
            self.jump()
        elif k[pygame.K_w] and self.player_on_wall and not self.on_ground:
            self.frames_jumped = 0
            self.jump()
        else:
            self.frames_jumped = 0

        if k[pygame.K_a]:
            self.walk(-1)
            self.orientation_r = False
        elif k[pygame.K_d]:
            self.walk(1)
            self.orientation_r = True 
            
        else:
            self.frames_walked = 0
            self.last_dir = 0
            if self.on_ground:
                self.vel_x = 0
        
        if self.on_ground:
            if not self.vel_x:
                self.state = "idle"
        else:
            if self.vel_y < 0:
                self.state = "jumpup"
            else:
                self.state = "jumpdown"

        self.anim_timer += 1
        self.anim_timer %= 60

        self.apply_accel()
        self.apply_vel()
        self.gravity()

#tommy = Player()
#def show():
#    print tommy.vel_x, tommy.vel_y
#    print tommy.accl_x, tommy.accl_y
