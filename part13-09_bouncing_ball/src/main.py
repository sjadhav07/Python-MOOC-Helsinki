# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

width = ball.get_width()
height = ball.get_height()

clock = pygame.time.Clock()

x = 0
y = 0
vel_x = 1
vel_y = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill((0, 0, 0))
    screen.blit(ball, (x, y))
    pygame.display.flip()

    x += vel_x
    y += vel_y
    if x + width >= 640 or x <= 0:
        vel_x = -vel_x
    if y + height >= 480 or y <= 0:
        vel_y = -vel_y
    clock.tick(120)

