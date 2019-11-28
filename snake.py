from food import Food
from game_functions import Game
import pygame
import sys
import random
import time
class Snake():
    def __init__(self, snake_color):
        #FIXME лучше бы сделать это глобальными константами или прописать в документации
        self.snake_head_pos = [100, 50]
        # at first snake has 3 segments: head, body and tail, it grows when eating food
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_color = snake_color
        # starting direction of moving
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
        #FIXME шаг движения - 10 пикселей, возможно, тут нужна глобальная константа
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10

    def snake_body_mechanism(self, score, food_pos, screen_width, screen_height):
        # moving snake's body
        self.snake_body.insert(0, list(self.snake_head_pos))
        # if the snake eats the food
        if self.snake_head_pos[0] == food_pos[0] and self.snake_head_pos[1] == food_pos[1]:
            # placing new food
            food_pos = [random.randrange(1, screen_width / 10) * 10,
                        random.randrange(1, screen_height / 10) * 10]
            score += 1
        else:
            # если еды тут не оказалось, то удаляем последний элемент, который создавали в начале этой функции
            self.snake_body.pop()

        return score, food_pos

    def draw_snake(self, play_surface, surface_color):
        # we draw segments of the snake's body here
        # FIXME я так понимаю, что сначала мы фон заливаем основным цветом, так что прорисовка препедствий тут где то тоже будет
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(play_surface, self.snake_color, pygame.Rect(pos[0], pos[1], 10, 10))

    def check_for_boundaries(self, game_over, screen_width, screen_height):
        # checking collisions with walls
        if any((
                self.snake_head_pos[0] > screen_width - 10
                or self.snake_head_pos[0] < 0,
                self.snake_head_pos[1] > screen_height - 10
                or self.snake_head_pos[1] < 0
                    )):
            game_over()
        # checking eating tail
        for block in self.snake_body[1:]:
            if (block[0] == self.snake_head_pos[0] and
                    block[1] == self.snake_head_pos[1]):
                game_over()


