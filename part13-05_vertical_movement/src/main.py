# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
height = robot.get_height()
x = 0
y = 0

velocity = 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    y+=velocity
    if y + height >= 480:
        velocity = -velocity
    if y <= 0:
        velocity = -velocity

    clock.tick(120)