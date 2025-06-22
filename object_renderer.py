import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/textures/ceiling2.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.digit_size = 90
        #self.win_image = self.get_texture('resources/textures/win.png', RES)

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        # floor
        # pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))
        #se ficar pesado é por isso aqui
        for y in range(HALF_HEIGHT, HEIGHT):
            brightness = int(100 + (y - HALF_HEIGHT) * 155 / (HEIGHT - HALF_HEIGHT))
            color = (brightness, brightness, brightness)  # tons de cinza
            pg.draw.line(self.screen, color, (0, y), (WIDTH, y))
        

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/wall.png'),
            2: self.get_texture('resources/textures/atendente.png'),
            3: self.get_texture('resources/textures/direita.png'),
            4: self.get_texture('resources/textures/esquerda.png'),
            5: self.get_texture('resources/textures/quadro.png'),
            6: self.get_texture('resources/textures/hedy.png'),
            9: self.get_texture('resources/textures/marie.png')
        }