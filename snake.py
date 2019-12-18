from food import Food
from game_functions import Game
import pygame
import sys
import random
import time


# X0 and Y0 --- starting position of left upper corner of snake's head
X0 = 100
Y0 = 150
# STEP --- distance of moving snake per one cycle
STEP = 10
# BOARDWIDTH --- the width of the obstacles, which are set on the boards
BOARDWIDTH = 20
# the upper point of the playing  area
Y_STARTING_POINT = 50

class Snake():
    def __init__(self, snake_color):
        global X0, Y0, STEP
        self.snake_head_pos = [X0, Y0]
        # at first snake has 3 segments: head, body and tail, it grows when eating food
        self.snake_body = [[X0, Y0], [X0-STEP, Y0], [X0-2*STEP, Y0]]
        self.snake_color = snake_color
        # starting direction of moving sets here
        self.direction = "RIGHT"
        self.change_to = self.direction

    def validate_direction_and_change(self):
        # it's impossible to change direction to the opposite
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def change_head_position(self):
        global STEP
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += STEP
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= STEP
        elif self.direction == "UP":
            self.snake_head_pos[1] -= STEP
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += STEP

    def snake_body_mechanism(self, score, barriers, food_pos, screen_width, screen_height):
        global STEP, BOARDWIDTH
        # moving snake's body
        self.snake_body.insert(0, list(self.snake_head_pos))
        # if the snake eats the food
        if self.snake_head_pos[0] == food_pos[0] and self.snake_head_pos[1] == food_pos[1]:
            # placing new food
            truth = 0
            while not truth:
                truth = 1
                food_pos = [random.randrange(1 + BOARDWIDTH / STEP, (screen_width - BOARDWIDTH) / STEP) * STEP,
                            random.randrange(1 + (Y_STARTING_POINT + BOARDWIDTH) / STEP, (screen_height - BOARDWIDTH) / STEP) * STEP]
                for block in barriers:
                    for brick in block:
                        truth *= (brick.x != food_pos[0] and brick.y != food_pos[1])
            score += 1
            checking_eating_food = True
        else:
            # at first we replaced every part of the snake and added one block for new snake's head position
            # now we need to delete the last segment, if the shake hasn't eaten food
            self.snake_body.pop()
            checking_eating_food = False

        return score, food_pos, checking_eating_food

    def draw_snake(self, play_surface):
        global STEP
        # we draw segments of the snake's body here
        for pos in self.snake_body:
            pygame.draw.rect(play_surface, self.snake_color, pygame.Rect(pos[0], pos[1], STEP, STEP))

    def check_for_boundaries(self, game_over, barriers, screen_width, screen_height):
        # checking collisions with walls
        global STEP, BOARDWIDTH, Y_STARTING_POINT
        if any((
                self.snake_head_pos[0] > screen_width - BOARDWIDTH - 2*STEP,
                self.snake_head_pos[0] < BOARDWIDTH + STEP,
                self.snake_head_pos[1] > screen_height - BOARDWIDTH - STEP,
                self.snake_head_pos[1] < BOARDWIDTH + STEP + Y_STARTING_POINT
                )):
            game_over()

        # checking collisions with barriers
        for block in barriers:
            for brick in block:
                if self.snake_head_pos[0] == brick.x and self.snake_head_pos[1] == brick.y:
                    game_over()

        # checking eating tail
        for block in self.snake_body[1:]:
            if block[0] == self.snake_head_pos[0] and block[1] == self.snake_head_pos[1]:
                game_over()


