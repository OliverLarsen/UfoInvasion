import pygame
from background import Background
from spaceship import Spaceship
from settings import Settings
from button import Button
from gamestats import GameStats
from gamecontroller import Gamecontroller
from ufos import Ufos
from bullet import Bullet
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
url = resource_path('resources/astro.png')
astro_url = pygame.image.load(url)
url1 = resource_path('resources/light_bullet.png')
bullet_url = pygame.image.load(url1)
url2 = resource_path('resources/starry-night-sky.jpg')
bg_url = pygame.image.load(url2)
url3 = resource_path('resources/ufo.png')
ufo_url = pygame.image.load(url3)
url4 = resource_path('resources/spaceship_red.png')
spaceship_url = pygame.image.load(url4)

# pygame initialise
pygame.init()

def draw_window(screen, settings, ufos, spaceship, bullets, gamestats):
    """draw things on screen"""
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
    gamestats.draw_score(48, 10, 5)
    gamestats.draw_level(48, 680, 10)
    
    # Draw astronaut as HP (health)
    gamestats.draw_astro(settings)

def update_bullets(bullets):
    """When the bullet disappear from the top of the screen, remove bullet from the list"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
def bullet_ufo_collision(ufos, bullets, gamestats):
    """Remove ufo from list when it gets hit by a bullet and add +1 to score"""
    for ufo in ufos.ufo_list:
        for bullet in bullets:
            if bullet.rect.colliderect(ufo.image_rect):
                print("UFO HIT")
                ufos.ufo_list.remove(ufo)
                bullets.remove(bullet)  
                gamestats.score += 1

def ufo_spaceship_collision(ufos, spaceship, gamestats):
    """Remove ufo from list and decrease HP by 1"""
    for ufo in ufos.ufo_list:
        if spaceship.rect.colliderect(ufo.image_rect):
            # when ufo hit spaceship remove ufo
            ufos.ufo_list.remove(ufo)
            # remove one astro from list
            if gamestats.hp >= 1:
                gamestats.hp -= 1
                print("spaceship got hit!")

def run_game():

    # creating object of settings Class
    settings = Settings()
    # Frames per second
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
    gamecontroller = Gamecontroller(settings, screen, play_button, play_again_button, spaceship, gamestats)
    bg = Background(screen)
    ufos = Ufos(settings)
    bullets = Bullet(settings, screen, spaceship)
                                        
    # motor
    while True:
        clock.tick(framerate)
        # check events
        gamecontroller.check_events(bullets.list, ufos)
        
        if gamecontroller.gameactive:
            # Game active screen
            bg.draw_bg()
            bg.update()
            # When ufo_list is empty gain stats and create a new fleet of ufos
            if len(ufos.ufo_list) == 0:
                gamestats.ufo_speed += 1
                gamestats.level += 1
                gamestats.ufo_wave_length += 1
                ufos.create_fleet(gamestats)          
            spaceship.move_spaceship()  
            update_bullets(bullets.list)
            bullet_ufo_collision(ufos, bullets.list, gamestats)
            ufo_spaceship_collision(ufos, spaceship, gamestats)
            draw_window(screen, settings, ufos, spaceship, bullets.list, gamestats)
            # When hp equals 0, make active false and gameover true, to switch screen.
            if gamestats.hp == 0:
                gamecontroller.gameactive = False
                gamecontroller.gameover = True

        elif gamecontroller.gameover:
            # Game over screen
            screen.fill(settings.black)
            gamestats.draw_gameover(72, settings.width/2 - 150, settings.height/2 -200)
            gamestats.draw_score(48,settings.width/2 - 100, settings.height/2 + 25)
            gamestats.draw_level(48,settings.width/2 - 100, settings.height/2 + 75)
            gamestats.draw_highscore(48,settings.width/2 -100, settings.height/2 + 125)
            play_again_button.draw_button()
        
        else:
            # Start screen
            screen.fill((250,250,250))
            play_button.draw_button()
               
        pygame.display.update()
        
run_game()

