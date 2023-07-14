# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

for i in range(10):
    window.blit(robot, (50+i*50, 100))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            exit()