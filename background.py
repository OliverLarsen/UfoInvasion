import pygame
class Background():
      def __init__(self, screen):
            self.screen = screen
            self.bg_image = pygame.image.load("resources/starry-night-sky.jpg")
            self.bg_image_rect = self.bg_image.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
            
            self.bgY2 = self.bg_image_rect.height
            self.bgX2 = 0
 
            self.moving_speed = 2
         
      def update(self):
          #Every time it is called, it increments self.bgY1 and self.bgY2, then changing the coordinates to which the background is drawn.
          # When Y1 and Y2 hit the height at the bottom of the screen it will then change to a minus coordinate, so it will be at -600.
        self.bgY1 += self.moving_speed
        self.bgY2 += self.moving_speed
        if self.bgY1 >= self.bg_image_rect.height:
            self.bgY1 = -self.bg_image_rect.height
        if self.bgY2 >= self.bg_image_rect.height:
            self.bgY2 = -self.bg_image_rect.height
             
      def draw_bg(self):
        #The first blit starts at the origin point, the top left corner and the second initializes at the top of the screen, just out of sight (above) the screen). imaging having the same picture printet above
         self.screen.blit(self.bg_image, (self.bgX1, self.bgY1))
         self.screen.blit(self.bg_image, (self.bgX2, self.bgY2))