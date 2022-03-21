from ufo import Ufo
from random import randint
class Ufos():
    # data structur = objects of ufo class in list
    def __init__(self, settings):
        self.settings = settings
        self.ufo_list =  []


    def create_fleet(self, wave_length, gamestats):
        for num in range(wave_length):
            xpos = randint(self.settings.delta, self.settings.width - self.settings.delta)
            ypos = randint(-1000, -100)
            ufo = Ufo(xpos, ypos, gamestats.ufo_speed)
            self.ufo_list.append(ufo)