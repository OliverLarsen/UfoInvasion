import pygame
class Settings():

    def __init__(self):
        # Screen width, height and delta
        self.width = 800
        self.height = 600
        self.delta = self.width/10
        
        # Spaceship
        self.ship_speed_factor = 6
        
        # bullet
        self.max_bullets = 5
        self.bullet_speed_factor = 6
        
        # Colors
        self.white = (250,250,250)
        self.black = (0,0,0)

        # astro image
        self.astro_image = pygame.transform.scale(pygame.image.load("resources/astro.png"), (55,40))
        