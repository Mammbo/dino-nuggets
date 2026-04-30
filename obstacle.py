import pygame
import random 

LANES = [150, 360, 570]


class Obstacle: 
    def __init__(self):
        self.lane = random.randint(0, 2)
        self.x = 1280
        self.type = random.choice(["high", "low"]) # wehter players needs to jump over or under

    def update(self, speed):
        self.x -= speed

    def is_off_screen(self):
        return self.x < -100
    
    def get_rect(self):
        y = LANES[self.lane]
        if self.type == "high":
            return pygame.Rect(self.x, y, 50, 80)
        else: 
            return pygame.Rect(self.x, y + 40, 80, 40)
        