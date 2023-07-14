# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

x = 0
z = 0
velocity = 1
vel = 1

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(robot, (x, 50))
    window.blit(robot, (z, 200))
    x += velocity
    z += vel*2

    if x + width >= 640 or x <= 0:
        velocity = -velocity
    
    if z + width >= 640 or z <= 0:
        vel = -vel

    pygame.display.flip()

    clock.tick(60)