import pygame

class Player:
    def __init__(self):
        self.health = 2
        self.alive = True

        self.hit_x, self.hit_y = 30
        self.draw_x, self.draw_y = 30
        self.pos_x, self.pos_y = 0
        self.vel_x, self.vel_y = 0
        self.accl_x, self.accl_y = 0

        self.on_ground = True
        self.jump_frame = 0
        self.holding_jump = False


    def spawn(self, x, y)
        self.alive = True
        self.pos_x, self.pos_y = x, y
        
