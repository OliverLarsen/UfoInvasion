from random import randint
import pygame
class Ufo():
    """Creating ufo class, to create a single ufo"""
    def __init__(self, x, y, speed):
        # self.x and self.y is being used in create_fleet in Ufos class
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30
        self.speed = speed
        # Scaling ufo image to its giving width and height
        self.image = pygame.transform.scale(pygame.image.load("resources/ufo.png"),(self.width, self.height))
        self.image_rect  = pygame.Rect(self.x, self.y, self.width, self.width)
        
    def move_ufo(self,settings):
        """Moving the ufos down the screen"""
        # When ufos getting below the screen set its x and y cordinates to a random number at above the top of the screen.    
        if self.image_rect.bottom > 640:
            self.image_rect.x, self.image_rect.y = randint(settings.delta, settings.width - settings.delta), randint(-500,-40)
        self.image_rect.y += self.speed 

    def draw_ufo(self, screen):
        """Draw the ufo to the screen"""
        screen.blit(self.image,(self.image_rect.x,self.image_rect.y))
    
        
        

