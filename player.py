from random import random

import pygame

from invasion import AlienInvasion
class AIPlayer:

    def __init__(self, ai_game):

        self.ai_game = ai_game

    def run_game(self):
        self.ai_game.stats.game_active = True
        pygame.mouse.set_visible(False)


        self._modify_speed(5)

        self.fleet_size = len(self.ai_game.aliens)


        while True:
            self.ai_game._check_events()
            self._implement_strategy()

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._update_aliens()

            self.ai_game._update_screen()

    def make_right_left(self):
        ship = self.ai_game.ship
        screen_rect = self.ai_game.screen.get_rect()

        if not ship.moving_right and not ship.moving_left:
            ship.moving_right = True
        elif (ship.moving_right
                    and ship.rect.right > screen_rect.right - 10):
            ship.moving_right = False
            ship.moving_left = True
        elif ship.moving_left and ship.rect.left < 10:
            ship.moving_left = False
            ship.moving_right = True

    def _modify_speed(self, speed_factor):
        self.ai_game.settings.ship_speed *= speed_factor
        self.ai_game.settings.bullet_speed *= speed_factor
        self.ai_game.settings.alien_speed *= speed_factor

if __name__ == '__main__':
    ai_game = AlienInvasion()

    ai_player = AIPlayer(ai_game)
    ai_player.run_game()