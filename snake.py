from food import Food
from game_functions import Game
import pygame
import sys
import random
import time


# X0 and Y0 --- starting position of left upper corner of snake's head
X0 = 100
Y0 = 50
# STEP --- distance of moving snake per one cycle
STEP = 10


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

    def snake_body_mechanism(self, score, food_pos, screen_width, screen_height):
        global STEP
        # moving snake's body
        self.snake_body.insert(0, list(self.snake_head_pos))
        # if the snake eats the food
        if self.snake_head_pos[0] == food_pos[0] and self.snake_head_pos[1] == food_pos[1]:
            # placing new food
            food_pos = [random.randrange(1, screen_width / STEP) * STEP,
                        random.randrange(1, screen_height / STEP) * STEP]
            score += 1
        else:
            # если еды тут не оказалось, то удаляем последний элемент, который создавали в начале этой функции
            self.snake_body.pop()

        return score, food_pos

    def draw_snake(self, play_surface, surface_color):
        global STEP
        # we draw segments of the snake's body here
        # FIXME я так понимаю, что сначала мы фон заливаем основным цветом, так что прорисовка препедствий тут где то тоже будет
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(play_surface, self.snake_color, pygame.Rect(pos[0], pos[1], STEP, STEP))

    def check_for_boundaries(self, game_over, screen_width, screen_height):
        # checking collisions with walls
        global STEP
        if any((
                self.snake_head_pos[0] > screen_width - STEP
                or self.snake_head_pos[0] < 0,
                self.snake_head_pos[1] > screen_height - STEP
                or self.snake_head_pos[1] < 0
                    )):
            game_over()
        # checking eating tail
        for block in self.snake_body[1:]:
            if (block[0] == self.snake_head_pos[0] and
                    block[1] == self.snake_head_pos[1]):
                game_over()


