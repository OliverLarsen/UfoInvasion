import pygame

class Bullet():
    
    def __init__(self, settings, screen, spaceship):
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load("resources/light_bullet.png"),(15,15))
        self.rect = self.image.get_rect()
        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top
        self.speed_factor = settings.bullet_speed_factor
        # empty list to place bullets in
        self.list = []
        
    def move_bullet(self):
        """Move the bullet up the screen"""
        self.rect.y -= self.speed_factor
    
    def draw_bullet(self):
        """Draw the bullet at the top center of the spaceship"""
        self.screen.blit(self.image, (self.rect.centerx, self.rect.top))