import pygame

class GameStats():
    """ Draw score, level, game over, highscore, and astronaunt as hp"""
    def __init__(self, screen, settings):
        self.score = 0
        self.level = 0
        self.highscore = 0
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ufo_last_increase_speed = 0
        self.ufo_speed = 1
        self.ufo_wave_length = 3
        self.hp = 3
        
    def draw_score(self, font_size, x, y):
        """Draw score on gameactive and gameover screen"""
        self.myfont = pygame.font.SysFont(None, font_size)
        text = self.myfont.render(f"score: {self.score}", True, self.settings.white)
        self.screen.blit(text, (x, y))

    def draw_level(self, font_size, x, y):
        """Draw level stats on gameactive and gameover screen"""
        self.myfont = pygame.font.SysFont(None, font_size)
        text = self.myfont.render(f"level: {self.level}", True, self.settings.white)
        self.screen.blit(text, (x,y))
    
    def draw_gameover(self, font_size, x, y):
        """Draw game over into gameover screen"""
        self.myfont = pygame.font.SysFont(None, font_size)
        text = self.myfont.render("GAME OVER!", True, self.settings.white)
        self.screen.blit(text, (x,y))

    def draw_highscore(self, font_size,x,y):
        """Draw highscore and set highscore equal to score if it become greater"""
        self.myfont = pygame.font.SysFont(None, font_size)
        text = self.myfont.render(f"High Score: {self.highscore}", True, self.settings.white)
        self.screen.blit(text, (x,y))
        if self.score >= self.highscore:
            self.highscore = self.score

    def draw_astro(self, settings):
        """Draw astro at the buttom right corner and draw astro next to it at the left side"""
        # When spaceship gets hit by a ufo self.hp is decreased and will only show 2 or 1 astro image
        if self.hp  >= 1:
            self.screen.blit(settings.astro_image, (745, 560))
        if self.hp >= 2:
            self.screen.blit(settings.astro_image, (690,560))
        if self.hp >= 3:
            self.screen.blit(settings.astro_image, (635,560))
    
    def game_reset_stats(self, ufos):
        """On game active screen, resetting gamestats and removing displayed ufos on screen"""
        self.score = 0
        self.level = 0
        self.ufo_wave_length = 3
        self.ufo_speed = 1
        self.hp = 3
        ufos.ufo_list.clear()
        
        