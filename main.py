import pygame
import sys
import random
import time
from game_functions import Game
from snake import Snake
from food import Food
from obstacles import ObstacleRectangles


# the upper point of the playing  area
Y_STARTING_POINT = 50
# BOARDWIDTH --- the width of the obstacles, which are set on the boards
BOARDWIDTH = 20
# frequency of screen updating
FPS = 12
# changing FPS for this value when eating one food
DELTAFPS = 1
# X0 and Y0 --- starting position of left upper corner of snake's head
X0 = 100
Y0 = 150
# STEP --- distance of moving snake per one cycle
STEP = 10


# all objects are being drawn here
def draw_all_objects_on_the_surface(surface_color):
    global list_obstacles_boards
    game.play_surface.fill(surface_color)
    snake.draw_snake(game.play_surface)
    food.draw_food(game.play_surface)
    for obs in list_obstacles_boards:
        obs.draw_obstacle(game.play_surface)


# set everything for game
game = Game()
snake = Snake(game.green)
food = Food(game.brown, game.screen_width, game.screen_height)
# making obstacles
list_obstacles_boards = []
obstacle_left = ObstacleRectangles(game.black,
                                   BOARDWIDTH, game.screen_height - Y_STARTING_POINT,
                                   0, Y_STARTING_POINT)
list_obstacles_boards += [obstacle_left]
obstacle_right = ObstacleRectangles(game.black,
                                    BOARDWIDTH, game.screen_height - Y_STARTING_POINT,
                                    game.screen_width - BOARDWIDTH, Y_STARTING_POINT)
list_obstacles_boards += [obstacle_right]
obstacle_up = ObstacleRectangles(game.black,
                                 game.screen_width, BOARDWIDTH,
                                 0, Y_STARTING_POINT)
list_obstacles_boards += [obstacle_up]
obstacle_down = ObstacleRectangles(game.black,
                                   game.screen_width, BOARDWIDTH,
                                   0, game.screen_height - BOARDWIDTH)
list_obstacles_boards += [obstacle_down]


game.init_and_check_for_errors()
game.set_surface_and_title()


# main cycle of the game
while True:
    snake.change_to = game.event_loop(snake.change_to)

    snake.validate_direction_and_change()
    snake.change_head_position()
    game.score, food.food_pos, checking_eating_food = snake.snake_body_mechanism(
        game.score, food.food_pos, game.screen_width, game.screen_height)

    draw_all_objects_on_the_surface(game.white)

    snake.check_for_boundaries(
        game.game_over, game.screen_width, game.screen_height)

    if checking_eating_food:
        game.changing_fps()

    game.show_score()
    game.refresh_screen()

