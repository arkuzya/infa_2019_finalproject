import pygame
import sys
import random
import time
from game_functions import Game
from snake import Snake
from food import Food

game = Game()
snake = Snake(game.green)
food = Food(game.brown, game.screen_width, game.screen_height)

game.init_and_check_for_errors()
game.set_surface_and_title()

# main cycle of the game

while True:
    snake.change_to = game.event_loop(snake.change_to)

    snake.validate_direction_and_change()
    snake.change_head_position()
    game.score, food.food_pos, checking_eating_food = snake.snake_body_mechanism(
        game.score, food.food_pos, game.screen_width, game.screen_height)
    snake.draw_snake(game.play_surface, game.white)

    food.draw_food(game.play_surface)

    snake.check_for_boundaries(
        game.game_over, game.screen_width, game.screen_height)

    if checking_eating_food:
        game.changing_fps()

    game.show_score()
    game.refresh_screen()

