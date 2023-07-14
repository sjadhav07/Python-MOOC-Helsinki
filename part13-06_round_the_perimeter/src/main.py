# # WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

clock = pygame.time.Clock()

x_velocity = 1
y_velocity = 0
x = 0
y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += x_velocity
    y += y_velocity
    if x + width >= 640 and x_velocity > 0:
        x_velocity = 0
        y_velocity = 1
    if y + height >= 480 and y_velocity > 0:
        y_velocity = 0
        x_velocity = -1
    if x<=0 and x_velocity < 0:
        x_velocity = 0
        y_velocity = -1
    if y <= 0 and y_velocity <0:
        y_velocity = 0
        x_velocity = 1
    
    clock.tick(120)

#OFFICIAL SOLUTION:
# import pygame
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# robot = pygame.image.load("robot.png")
 
# x = 0
# y = 0
# direction = 1 # 1 = to right, 2 = to down, 3 = to left, 4 = to up
# clock = pygame.time.Clock()
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
 
#     screen.fill((0, 0, 0))
#     screen.blit(robot, (x, y))
#     pygame.display.flip()
 
#     if direction == 1:
#         x += 1
#         if x+robot.get_width() == width:
#             direction = 2
#     elif direction == 2:
#         y += 1
#         if y+robot.get_height() == height:
#             direction = 3
#     elif direction == 3:
#         x -= 1
#         if x == 0:
#             direction = 4
#     elif direction == 4:
#         y -= 1
#         if y == 0:
#             direction = 1
 
#     clock.tick(60)