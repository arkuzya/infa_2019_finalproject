from food import Food
from game_functions import Game
import pygame
import sys
import random
import time

# BOARDWIDTH --- the width of the obstacles, which are set on the boards
BOARDWIDTH = 20

class Obstacles():
    def __init__(self, obstacle_color):
        self.obstacle_color = obstacle_color

class ObstacleRectangles(Obstacles):
    def __init__(self, obstacle_color, size_x, size_y, x, y):
        self.obstacle_color = obstacle_color
        self.size_x = size_x
        self.size_y = size_y
        self.x = x
        self.y = y

    def draw_obstacle(self, play_surface):
        pygame.draw.rect(
            play_surface, self.obstacle_color, pygame.Rect(
                self.x, self.y,
                self.size_x, self.size_y))

