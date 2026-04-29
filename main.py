# game loop file 
import pygame

pygame.init()
# make this take in a cmd argument later
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True 

while running: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # render game 

    pygame.display.flip()

    # limits fps to 60
    clock.tick(60)
pygame.quit()
