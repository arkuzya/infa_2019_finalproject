from food import Food
from game_functions import Game
import pygame
import sys
import random
import time

# BOARDWIDTH --- the width of the obstacles, which are set on the boards
BOARDWIDTH = 20
STEP = 10
screen_width = 800
screen_height = 600
Y_STARTING_POINT = 50

X0 = 100
Y0 = 150

MAX_DIST = 5
MAX_DIST_X = MAX_DIST
MAX_DIST_Y = MAX_DIST


class Barrier():
    # Add game. class, add *10 pixels, MAX_DIST - define
    def __init__(self):
        self.x0 = X0
        self.y0 = Y0
        while abs(self.y0 - Y0) <= 3 and abs(self.x0 - X0) <= 1:
            self.x0 = random.randint(BOARDWIDTH / 10 + MAX_DIST_X, screen_width / 10 - BOARDWIDTH / 10 - MAX_DIST_X)
            self.y0 = random.randint(Y_STARTING_POINT / 10 + BOARDWIDTH / 10 + MAX_DIST_Y,
                                     screen_height / 10 - BOARDWIDTH / 10 - MAX_DIST_Y)
        self.length = random.randint(1, round((MAX_DIST_X * 2 + 1) * (MAX_DIST_Y * 2 + 1) / 3))
        self.pixel = [None] * self.length
        self.coor = [0, 0] * self.length

    # create barrier's blocks
    def coordinates(self):
        restart = 1
        while restart:
            restart = 0
            for i in range(self.length):
                if i == 0:
                    self.coor[i] = [0, 0]
                    continue
                truth = False
                counter = 0
                while not truth:
                    truth = 1
                    coordinate = [x + y for x, y in zip(self.coor[i - 1], [random.randint(-1, 1), random.randint(-1, 1)])]
                    for j in range(i - 1):
                        truth *= coordinate != self.coor[i - j - 1]
                    truth *= abs(coordinate[1]) < MAX_DIST_Y
                    truth *= abs(coordinate[0]) < MAX_DIST_X
                    truth *= abs(coordinate[0] - X0) > 3
                    truth *= abs(coordinate[1] - Y0) > 1
                    counter += 1
                    if counter > 10:
                        restart = 1
                        break
                if restart == 1:
                    break
                self.coor[i] = coordinate


    # transform coordinates to original one
    def pixelization(self, step=STEP):
        self.pixel = [None] * self.length
        for i in range(self.length):
            self.pixel[i] = [1, 1, self.coor[i][0], self.coor[i][1]]

    # def scaling(self): #
        for i in range(self.length):
            self.pixel[i][2] += self.x0
            self.pixel[i][3] += self.y0
            for j in range(4):
                self.pixel[i][j] *= step


# To draw the barrier
class BarrierPixels:
    def __init__(self, barrier, barrier_color):
        self.barrier_color = barrier_color
        self.size_x = barrier[0]
        self.size_y = barrier[1]
        self.x = barrier[2]
        self.y = barrier[3]

    def draw_barrier(self, play_surface):
        pygame.draw.rect(
            play_surface, self.barrier_color, pygame.Rect(
                self.x, self.y,
                self.size_x, self.size_y))
