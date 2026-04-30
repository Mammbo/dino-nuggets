# make the player class 
import pygame
LANES = [150, 360, 570]  # y pixel positions for each lane                                                 
PLAYER_X = 150 

class Player: 
    def __init__ (self):
        self.lane = 1 # 0 = left, 1 = mid, 2 = right
        self.jumping = False
        self.ducking = False
        self.jump_offset = 0
        self.jump_vel = 0

    # switch to left lane
    def move_left(self):
        if self.lane > 0:
            self.lane -= 1
    # switch to right lane
    def move_right(self):
        if self.lane < 2:
            self.lane += 1
    # jump over obstacle
    def jump(self):  # ---> set jumping to True
        if not self.jumping:
            self.jumping = True
            self.jump_vel = -15
    # duck under obstalce --> set ducking to True
    def duck(self):
        if not self.ducking:
            self.ducking = True
    # handel jump arc (gravity)
    def update(self):
        if self.jumping: 
            self.jump_vel += 0.8
            self.jump_offset += self.jump_vel
            if self.jump_offset >= 0: #landed
                self.jump_offset = 0
                self.jump_vel = 0
                self.jumping = False
    # return pygame.Rect for collision
    def get_rect(self):
        y = LANES[self.lane] + self.jump_offset
        if self.ducking: 
            return pygame.Rect(PLAYER_X, y + 40, 60, 40) # half height when ducking
        return pygame.Rect(PLAYER_X, y, 60, 80)
    