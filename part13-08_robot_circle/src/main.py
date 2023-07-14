# WRITE YOUR SOLUTION HERE:
# TRY AGAIN
import pygame
import math
pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
clock = pygame.time.Clock()
angle = 0
number = 10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    for i in range(number):
        x = 320 + math.cos(angle+2*math.pi*i/number)*150-width/2
        y = 240 + math.sin(angle+2*math.pi*i/number)*150-height/2
        
        window.blit(robot, (x, y))
    pygame.display.flip()
    angle += 0.01
    clock.tick(60)