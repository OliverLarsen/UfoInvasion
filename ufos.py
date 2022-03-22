from ufo import Ufo
from random import randint
class Ufos():
    """ A Ufos class to create multible ufos"""
    # using list as data structure. Objects of ufo class in list
    def __init__(self, settings):
        self.settings = settings
        self.ufo_list =  []
        
    def create_fleet(self, gamestats):
        """Create a ufo fleet from ufo class"""
        # initializing xpos, ypos, and gamestats.ufo_speed into ufo attributes
        for num in range(gamestats.ufo_wave_length):
            xpos = randint(self.settings.delta, self.settings.width - self.settings.delta)
            ypos = randint(-1000, -100)
            ufo = Ufo(xpos, ypos, gamestats.ufo_speed)
            self.ufo_list.append(ufo)