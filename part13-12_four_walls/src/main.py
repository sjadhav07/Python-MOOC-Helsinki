# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()

width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

x, y = 360-robot.get_height()/2, 240-robot.get_height()/2
to_left = False
to_right = False
to_up = False
to_down = False
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            
    if to_up:
        y -= 2
    if to_down:
        y += 2
    if to_left:
        x -= 2
    if to_right:
        x += 2
    x = max(x, 0)
    x = min(x, width- robot.get_width())
    y = max(y, 0)
    y = min(y, height - robot.get_height())
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)