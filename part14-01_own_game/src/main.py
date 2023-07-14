import pygame
from random import randrange

class Robotman:
    def __init__(self):
        pygame.init()

        # Colors
        self.LIGHTGREY = (192, 192, 192)
        self.DARKGREY = (128, 128, 128)
        self.YELLOW = (255, 255, 0)
        self.RED = (255, 0, 0)

        self.load_images()
        self.screen_height = 900
        self.screen_width = 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Robotman")

        # Robot position
        self.robot_x = 250 - self.images[0].get_width()/4
        self.robot_y = 450 - self.images[0].get_height()/2

        # Coin position
        self.coin_x = randrange(50, self.screen_width-50)
        self.coin_y = randrange(-3 * self.screen_height, -800)

        # Movement
        self.move_right = False
        self.move_left = False

        # Counter
        self.counter = 0

        # Monster position
        self.monster_y = 880

        # Monster pseudo boundary
        self.boundary = 700

        # Game states
        self.game_running = False
        self.main_menu = True

        # Font
        self.font = pygame.font.SysFont("8-Bit-Madness", 38)

        # Points
        self.points = 0

        # Stars
        self.create_star_speeds()

        # Robot obstacles
        self.laser_middle_y = -3000
        self.laser_left_y = -2000
        self.laser_right_y = -1000

        # FPS
        self.clock = pygame.time.Clock()
        self.main_loop()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_left = True
                if event.key == pygame.K_RIGHT:
                    self.move_right = True
                if event.key == pygame.K_ESCAPE:
                    exit()

                if not self.game_running:
                    if event.key == pygame.K_RETURN:
                        self.game_running = True
                    if event.key == pygame.K_F1:
                        self.main_menu = False
                    if event.key == pygame.K_F2:
                        self.main_menu = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.move_left = False
                if event.key == pygame.K_RIGHT:
                    self.move_right = False

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_screen()
            self.clock.tick(60)

    def load_images(self):
        self.images = []
        for name in ["robot", "monster", "coin"]:
            self.images.append(pygame.image.load(name + ".png"))

    def create_star_speeds(self):
        self.fast_stars = []
        self.medium_stars = []
        self.slow_stars = []

        # Creating speeds for fast stars
        for _ in range(50):
            speed_x = randrange(0, self.screen_width)
            speed_y = randrange(0, self.screen_height)
            self.slow_stars.append([speed_x, speed_y])

        # Creating speeds for medium stars
        for _ in range(35):
            speed_x = randrange(0, self.screen_width)
            speed_y = randrange(0, self.screen_height)
            self.medium_stars.append([speed_x, speed_y])

        # Creating speeds for slow stars
        for _ in range(15):
            speed_x = randrange(0, self.screen_width)
            speed_y = randrange(0, self.screen_height)
            self.fast_stars.append([speed_x, speed_y])

    def draw_stars(self):
        for speed in self.slow_stars:
            speed[1] += 1
            if speed[1] > self.screen_height:
                speed[0] = randrange(0, self.screen_width)
                speed[1] = randrange(-20, -5)
            pygame.draw.circle(self.screen, self.DARKGREY, speed, 3)

        for speed in self.medium_stars:
            speed[1] += 4
            if speed[1] > self.screen_height:
                speed[0] = randrange(0, self.screen_width)
                speed[1] = randrange(-20, -5)
            pygame.draw.circle(self.screen, self.LIGHTGREY, speed, 2)

        for speed in self.fast_stars:
            speed[1] += 8
            if speed[1] > self.screen_height:
                speed[0] = randrange(0, self.screen_width)
                speed[1] = randrange(-20, -5)
            pygame.draw.circle(self.screen, self.YELLOW, speed, 1)

    def draw_screen(self):
        if self.game_running:
            # Game background
            self.screen.fill((4, 4, 4))
            self.draw_stars()

            # Show points
            text = self.font.render(f"Points: {self.counter}", True, (0, 255, 0))
            self.screen.blit(text, (370, 50))

            # Load images
            robot = self.images[0].convert_alpha()
            monster = self.images[1].convert_alpha()
            coin = self.images[2].convert_alpha()

            # Draw coin
            self.screen.blit(coin, (self.coin_x, self.coin_y))
            self.coin_y += 10

            # Robot rectangle
            self.robot_rect = robot.get_rect(topleft=(self.robot_x, self.robot_y))
            self.coin_rect = coin.get_rect(topleft=(self.coin_x, self.coin_y))

            # Check if robot collides with coin
            if self.robot_rect.colliderect(self.coin_rect):
                self.counter += 1
                self.coin_x = randrange(50, self.screen_width-50)
                self.coin_y = randrange(-3 * self.screen_height, -800)

            # If coin reaches the boundary, monsters approach
            if self.coin_y > self.boundary:
                self.monster_y -= 100
                self.boundary -= 100
                self.coin_x = randrange(50, self.screen_width-50)
                self.coin_y = randrange(-3 * self.screen_height, -800)

            # Move the robot to the right
            if self.move_right:
                if self.robot_x + robot.get_width() < self.screen_width:
                    self.robot_x += 10

            # Move the robot to the left
            if self.move_left:
                if self.robot_x - robot.get_width() > -robot.get_width():
                    self.robot_x -= 10

            # Draw monsters
            monster_y = self.monster_y
            for _ in range(3):
                monster_x = 5
                monster_y -= 50

                for _ in range(12):
                    self.screen.blit(monster, (monster_x, monster_y))
                    monster_x += 40
            self.screen.blit(robot, self.robot_rect)

            # If monsters collide with the robot, end the game
            if self.monster_y == 580:
                self.game_running = False
                self.monster_y = 880
                self.boundary = 700
                self.points = self.counter
                self.counter = 0
                self.laser_middle_y = -3000
                self.laser_left_y = -2000
                self.laser_right_y = -1000

            # Draw obstacles
            self.draw_obstacles()

        else:
            self.draw_menu()
            self.draw_stars()

        pygame.display.flip()

    def draw_menu(self):
        self.screen.fill((0, 0, 0))

        # Font
        font = pygame.font.SysFont("8-Bit-Madness", 64)

        # Final score
        if self.points > 0:
            score_text = self.font.render(f"Final score: {self.points}", True, (0, 255, 0))
            score_text_rect = score_text.get_rect(midtop=(self.screen_width/2, self.screen_height/2 - 200))

        # Start button
        start_button = self.font.render("Press 'Enter' to start", True, (255, 0, 0))
        start_button_rect = start_button.get_rect(center=(self.screen_width/2, self.screen_height/2))

        # Instructions button
        instructions_button = self.font.render("F1 for instructions", True, (255, 255, 255))
        instructions_button_rect = instructions_button.get_rect(topleft=(5, self.screen_height-30))

        if self.main_menu:
            # Display text on screen
            self.screen.blit(instructions_button, instructions_button_rect)
            self.screen.blit(start_button, start_button_rect)
            if self.points > 0:
                self.screen.blit(score_text, score_text_rect)
        else:
            # Instructions text
            instructions_list = [
                "Robot is trying to escape from monsters",
                "Coins are falling from the sky",
                "If Robot catches a coin:",
                "Robot gets a point",
                "If monsters catch a coin:",
                "They will approach closer to the robot",
                "Robot should avoid obstacles",
                "Robot should collect coins",
                "If Robot encounters obstacles:",
                "Robot will die and the game will end",
                "If monsters catch the Robot:",
                "Robot will die and the game will end",
                "Good luck and have fun!"
            ]

            x = self.screen_width
            y = 150
            for instruction in instructions_list:
                instructions_font = pygame.font.SysFont("8-Bit-Madness", 28)
                instructions_text = instructions_font.render(instruction, True, (255, 0, 0))
                instructions_text_rect = instructions_text.get_rect(center=(x/2, y))

                self.screen.blit(instructions_text, instructions_text_rect)
                y += 50

            # Back button
            back_button = self.font.render("F2 to return", True, (255, 255, 255))
            back_button_rect = back_button.get_rect(topleft=(5, self.screen_height-30))
            self.screen.blit(back_button, back_button_rect)

    def draw_obstacles(self):
        # Middle laser
        laser_middle = pygame.Rect(125, self.laser_middle_y, 250, 5)
        pygame.draw.rect(self.screen, self.RED, laser_middle)
        self.laser_middle_y += 10

        # Left laser
        laser_left = pygame.Rect(0, self.laser_left_y, 130, 5)
        pygame.draw.rect(self.screen, self.RED, laser_left)
        self.laser_left_y += 10

        # Right laser
        laser_right = pygame.Rect(370, self.laser_right_y, 500, 5)
        pygame.draw.rect(self.screen, self.RED, laser_right)
        self.laser_right_y += 10

        if self.laser_middle_y > 900:
            self.laser_middle_y = -3000

        elif self.laser_left_y > 900:
            self.laser_left_y = -2000

        elif self.laser_right_y > 900:
            self.laser_right_y = -1000

        # If two lasers collide, reset the middle laser
        if laser_middle.colliderect(laser_left) or laser_middle.colliderect(laser_right):
            self.laser_middle_y = -3000

        # If coin collides with a laser
        if self.coin_rect.colliderect(laser_middle) or self.coin_rect.colliderect(laser_left) or self.coin_rect.colliderect(laser_right):
            self.coin_y = randrange(-2 * self.screen_height, -800)

        # If robot collides with a laser
        if self.robot_rect.colliderect(laser_middle) or self.robot_rect.colliderect(laser_left) or self.robot_rect.colliderect(laser_right):
            self.game_running = False
            self.monster_y = 880
            self.boundary = 700
            self.points = self.counter
            self.counter = 0
            self.coin_y = randrange(-3 * self.screen_height, -800)
            self.laser_middle_y = -3000
            self.laser_left_y = -2000
            self.laser_right_y = -1000


if __name__ == '__main__':
    Robotman()
