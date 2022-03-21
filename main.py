import pygame
from background import Background
from spaceship import Spaceship
from settings import Settings
from button import Button
from gamestats import GameStats
from gamecontroller import Gamecontroller
from ufos import Ufos

# pygame initialise
pygame.init()
# Frames per second

def run_game():

# creating object of settings Class
    settings = Settings()

    framerate = 60
    clock = pygame.time.Clock()
    # screen
    screen = pygame.display.set_mode((settings.width,settings.height))
    # caption
    pygame.display.set_caption("Ufo Invasion")

    # creating objects of Classses
    spaceship = Spaceship(settings,screen)
    play_button = Button(screen, "Play")
    play_again_button = Button(screen, "Play again")
    gamestats = GameStats(screen,settings)
    gamecontroller = Gamecontroller(settings,screen,play_button,play_again_button,spaceship,gamestats)
    bg = Background(screen)
    ufos = Ufos(settings)

    # empty list to place bullets in
    bullets = []

    def draw_window(ufos, spaceship, bullets):
        """drawing things on screen"""
        #draw ufos and make them move 
        for ufo in ufos.ufo_list:
            ufo.draw_ufo(screen)
            ufo.move_ufo(settings)
                
        # draw spaceship into screen
        spaceship.draw_spaceship()
        
        #draw bullet and move it op the screen
        for bullet in bullets:
            bullet.draw_bullet()
            bullet.move_bullet()
            
        # Draw score and level on the screen
        gamestats.draw_score(48,10,5)
        gamestats.draw_level(48,680,10,ufos)
        
        # Draw astronaut as HP (health)
        gamestats.draw_astro(settings)

    def update_bullets(bullets):
        # If the bullet disappear at the top of the screen remove the bullet from the list
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
    
    def bullet_ufo_collision(ufos, bullets):
        """remove ufo from list when it gets hit by a bullet and add +1 to score"""
        for ufo in ufos.ufo_list:
            for bullet in bullets:
                if bullet.rect.colliderect(ufo.image_rect):
                    print("UFO HIT")
                    ufos.ufo_list.remove(ufo)
                    bullets.remove(bullet)  
                    gamestats.score += 1
    
    def ufo_spaceship_collision(ufos):
        for ufo in ufos.ufo_list:
            if spaceship.rect.colliderect(ufo.image_rect):
                # when ufo hit spaceship remove ufo
                ufos.ufo_list.remove(ufo)
                # remove one astro from list - fjerner det sidste index i listen.
                if gamestats.hp >= 1:
                    gamestats.hp -= 1
                    print("spaceship got hit!")
                                           
    # motor
    while True:
        clock.tick(framerate)
        # check events
        gamecontroller.check_events(bullets, ufos)

        if gamecontroller.gameactive:
            
            bg.update()
            bg.blitme()
            if len(ufos.ufo_list) == 0:
                gamestats.ufo_speed += 1
                gamestats.level += 1
                gamestats.ufo_wave_length += 1
                ufos.create_fleet(gamestats.ufo_wave_length, gamestats)          
            spaceship.move_spaceship()  
            update_bullets(bullets)
            bullet_ufo_collision(ufos, bullets)
            ufo_spaceship_collision(ufos)
            draw_window(ufos, spaceship, bullets)
            if gamestats.hp == 0:
                gamecontroller.gameactive = False
                gamecontroller.gameover = True

        elif gamecontroller.gameover:
            screen.fill(settings.black)
            gamestats.draw_gameover(72, settings.width/2 - 150, settings.height/2 -200)
            gamestats.draw_score(48,settings.width/2 - 100, settings.height/2 + 25)
            gamestats.draw_level(48,settings.width/2 - 100, settings.height/2 + 75, ufos)
            gamestats.draw_highscore(48,settings.width/2 -100, settings.height/2 + 125)
            play_again_button.draw_button()
        
        else:
            screen.fill((250,250,250))
            play_button.draw_button()
               
        pygame.display.update()
        
run_game()
    


