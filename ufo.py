from random import randint
import pygame
class Ufo():

    def __init__(self, x, y, speed):
        # self.x and self.y is being used in create_fleet in Ufos class
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load("resources/ufo.png"),(50,30))
        self.image_rect  = pygame.Rect(self.x, self.y, self.width, self.width)
        
    def move_ufo(self,settings):
        # When ufo's is getting below the screen sets it x and y cordinates to random number at the top of the screen.    
        if self.image_rect.bottom > 640:
            self.image_rect.x, self.image_rect.y = randint(settings.delta, settings.width - settings.delta), randint(-500,-40)
        self.image_rect.y += self.speed 

    def draw_ufo(self, screen):
        screen.blit(self.image,(self.image_rect.x,self.image_rect.y))
    
        
        

