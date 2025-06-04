import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.theme = pg.mixer.music.load(self.path + 'Glow.mp3')
        pg.mixer.music.set_volume(0.3)