import pygame
import sys
import random
import time
class Game():
    def __init__(self):
        # screen parameters
        self.screen_width = 800
        self.screen_height = 600

        # colors for use
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)

        # Frame per second controller
        self.fps_controller = pygame.time.Clock()

        # scores in game
        self.score = 0

    def init_and_check_for_errors(self):
        # checks errors
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')

    def set_surface_and_title(self):
        # main surface of the game and title
        self.play_surface = pygame.display.set_mode((
            self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake Game')

    def event_loop(self, new_direction):
        # check events from the keyboard

        # ищем нужные нам события из списка (нажатия стрелочек)
        for event in pygame.event.get():
            # проверка того, что нажали именно какую-то клавишу
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    new_direction = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    new_direction = "LEFT"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    new_direction = "DOWN"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    new_direction = "UP"
                    # нажали escape
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return new_direction

    def refresh_screen(self):
        # screen update
        pygame.display.flip()
        # FIXME: хз как это работает, 23 надо сделать глобальной константой
        self.fps_controller.tick(23)

    def show_score(self, choice=1):
        # show resiult
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render('Score: {0}'.format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        # result is placed in the upper left corner if other parameters aren't given
        if choice == 1:
            s_rect.midtop = (80, 10)
        # result is placed in the center in the end of the game
        else:
            s_rect.midtop = (360, 120)
        # the label with score is placed ON the main surface
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self):
        # show results when ending the game
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

