import pygame 
import random 
from player import Player
from obstacle import Obstacle 

class Game: 
    def __init__ (self):
        self.player = Player()
        self.obstacles = []
        self.score = 0 
        self.speed = 5
        self.spawn_timer = 0

    def spawn_obstalce(self):
        self.obstacles.append(Obstacle())
    
    def update(self): # called every frame, does 4 things
        self.player.update()
        for obstacle in self.obstacles:
            # check if they are off scrren
            obstacle.update(self.speed)
        self.obstacles = [o for o in self.obstacles if not o.is_off_screen()]
        self.score += 1
    

    def check_collision(self):
        player_rect = self.player.get_rect()
        for obstacle in self.obstacles:
            if player_rect.colliderect(obstacle.get_rect()):
                return True
        return False

