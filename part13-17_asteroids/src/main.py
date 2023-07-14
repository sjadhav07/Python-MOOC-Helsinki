# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

to_left = False
to_right = False

rocks = []
number = 5
clock = pygame.time.Clock()
for i in range(number):
    rocks.append([-1000, height])
x, y = 0, 480-robot.get_height()

point = 0
font = pygame.font.SysFont("Arial", 24)
while True:
   
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render(f"Points: {point}", True, (255, 0, 0))
    window.blit(text, (550, 20))
    

    if to_left:
        x -= 2
    if to_right:
        x += 2
    for i in range(number):
        # CODE THE CONDITION FOR WHICH A NEW ROCK IS CREATED IF THE CONDITION IS FOLLOWED
        if not( rocks[i][0] + rock.get_width() < x  or  rocks[i][0] > x+robot.get_width()) and rocks[i][1] >= 480-robot.get_height():
            rocks[i][0] = randint(0, width-rock.get_width())
            rocks[i][1] = -randint(100, 1000)
            point += 1
        
        if rocks[i][1] > height and (rocks[i][0] + rock.get_width() < x  or  rocks[i][0] > x+robot.get_width()):
            exit()
        if rocks[i][1]  < height:
            rocks[i][1] += 2
        
        else:
            if rocks[i][0] < -rock.get_width() or rocks[i][0] > width or rocks[i][1]>=height:
                rocks[i][0] = randint(0, width-rock.get_width())
                rocks[i][1] = -randint(100, 1000)
    for i in range(number):
        window.blit(rock, (rocks[i][0], rocks[i][1]))
        

    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)