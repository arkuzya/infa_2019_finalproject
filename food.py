import pygame
import sys
import random
import time


# STEP --- distance of moving snake per one cycle
STEP = 10
# BOARDWIDTH --- the width of the obstacles, which are set on the boards
BOARDWIDTH = 20

class Food():
    def __init__(self, food_color, screen_width, screen_height):
        global STEP, BOARDWIDTH
        self.food_color = food_color
        self.food_size_x = STEP
        self.food_size_y = STEP
        self.food_pos = [random.randrange(1 + BOARDWIDTH / STEP, (screen_width - BOARDWIDTH) / STEP) * STEP,
                         random.randrange(1 + BOARDWIDTH / STEP, (screen_height - BOARDWIDTH) / STEP) * STEP]

    def draw_food(self, play_surface):
        # setting food on the screen
        pygame.draw.rect(
            play_surface, self.food_color, pygame.Rect(
                self.food_pos[0], self.food_pos[1],
                self.food_size_x, self.food_size_y))