# WRITE YOUR SOLUTION HERE
import pygame
pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

positions = [[0, 0], [robot.get_width(), robot.get_height()]]
controls = []
# key, robot name, horizontal movement, vertical movement
controls.append((pygame.K_LEFT, 0, -2, 0))
controls.append((pygame.K_RIGHT, 0, 2, 0))
controls.append((pygame.K_UP, 0, -0, -2))
controls.append((pygame.K_DOWN, 0, 0, 2))
controls.append((pygame.K_a, 1, -2, 0))
controls.append((pygame.K_d, 1, 2, 0))
controls.append((pygame.K_w, 1, -0, -2))
controls.append((pygame.K_s, 1, 0, 2))

key_pressed = {}
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_pressed[event.key] = True
        if event.type == pygame.KEYUP:
            del key_pressed[event.key]
        if event.type == pygame.QUIT:
            exit()
        
    for key in controls:
        if key[0] in key_pressed:
            positions[key[1]][0] += key[2]
            positions[key[1]][1] += key[3]
        
    screen.fill((0, 0, 0))
    for i in range(2):
        screen.blit(robot, (positions[i][0], positions[i][1]))
    pygame.display.flip()
    clock.tick(60)