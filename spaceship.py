import pygame
class Spaceship:
    
    
    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.xpos = settings.width//2
        self.ypos = settings.height - 50
        self.width = 55
        self.height = 40
        self.image = pygame.image.load("resources/spaceship_red.png")
        #scaling and rotating spaceship
        self.ship = pygame.transform.rotate(pygame.transform.scale(self.image,(self.width,self.height)),180)
        # Creating rectangle around spaceship image
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)

    def draw_spaceship(self):
        # Drawing spaceship with the rectangle x and y coordinates
        self.screen.blit(self.ship, (self.rect.x, self.rect.y))

    def move_spaceship(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x-= self.settings.ship_speed_factor
        if keys_pressed[pygame.K_RIGHT] and self.rect.x < self.settings.width - 70:
            self.rect.x += self.settings.ship_speed_factor