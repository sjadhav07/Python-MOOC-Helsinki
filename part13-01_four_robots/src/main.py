
# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

width = 640
height = 480

window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

r_width = robot.get_width()
r_height = robot.get_height()

window.fill((0, 0, 0))

window.blit(robot, (0, 0))
window.blit(robot, (0, height-r_height))
window.blit(robot, (width-r_width, 0))
window.blit(robot, (width-r_width, height-r_height))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()