import pygame, sys
from bullet import Bullet

class Gamecontroller():
    """Check events"""
    def __init__(self, settings, screen, play_button, play_again_button, spaceship, gamestats):
        self.settings = settings
        self.screen = screen
        self.play_button = play_button
        self.play_again_button = play_again_button
        self.spaceship = spaceship
        self.gamestats = gamestats
        self.gameover = False
        self.gameactive = False
        
    def check_events(self, bullets, ufos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Add to bullet to bullet list if its under the maximum limit
                    if len(bullets) < self.settings.max_bullets:
                        new_bullet = Bullet(self.settings, self.screen, self.spaceship)
                        bullets.append(new_bullet)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_clicked = self.play_button.rect.collidepoint(mouse_x, mouse_y)
                button_clicked1 = self.play_again_button.rect.collidepoint(mouse_x,mouse_y)
                if button_clicked and self.gameover == False:
                    self.gameactive = True
                    print("clicked play to start game")
                if button_clicked1 and self.gameover == True:
                    self.gamestats.game_reset_stats(ufos)
                    self.gameactive = True
                    self.gameover = False
                    print("You clicked to play again")