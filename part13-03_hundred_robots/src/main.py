# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0,0,0))

for i in range(10):
    for j in range(10):
        window.blit(robot, (50+i*40+j*10, 100+j*20))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    