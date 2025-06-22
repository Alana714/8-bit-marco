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
            brightness = int(20 + (y - HALF_HEIGHT) * 105 / (HEIGHT - HALF_HEIGHT))
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

            5: self.get_texture('resources/textures/criacoes/hedy5.png'),
            6: self.get_texture('resources/textures/criacoes/marie6.png'),
            7: self.get_texture('resources/textures/criacoes/ada7.png'),
            8: self.get_texture('resources/textures/criacoes/grace8.png'),
            9: self.get_texture('resources/textures/criacoes/valerie9.png'),
            10: self.get_texture('resources/textures/criacoes/radia10.png'),
            11: self.get_texture('resources/textures/criacoes/chieko11.png'),

            12: self.get_texture('resources/textures/arte/anita12.png'),
            13: self.get_texture('resources/textures/arte/artemisia13.png'),
            14: self.get_texture('resources/textures/arte/elisabeth14.png'),
            15: self.get_texture('resources/textures/arte/georgina15.png'),
            16: self.get_texture('resources/textures/arte/tamara16.png'),
            17: self.get_texture('resources/textures/arte/mary17.png'),
            18: self.get_texture('resources/textures/arte/cecilia18.png'),
            19: self.get_texture('resources/textures/arte/emily19.png'),

            20: self.get_texture('resources/textures/historia/dia20.png'),
            21: self.get_texture('resources/textures/historia/onu21.png'),
            22: self.get_texture('resources/textures/historia/triangle22.png'),
            23: self.get_texture('resources/textures/historia/ny23.png'),
            24: self.get_texture('resources/textures/historia/1917_24.png'),
            25: self.get_texture('resources/textures/historia/clara25.png'),

            26: self.get_texture('resources/textures/mundo/harriet26.png'),
            27: self.get_texture('resources/textures/mundo/joana27.png'),
            28: self.get_texture('resources/textures/mundo/anne28.png'),
            29: self.get_texture('resources/textures/mundo/rosa29.png'),
            30: self.get_texture('resources/textures/mundo/simone30.png'),
            31: self.get_texture('resources/textures/mundo/sofia31.png'),
            32: self.get_texture('resources/textures/mundo/bertha32.png'),
            33: self.get_texture('resources/textures/mundo/malala33.png'),

            34: self.get_texture('resources/textures/brasil/maria34.png'),
            35: self.get_texture('resources/textures/brasil/bertha35.png'),
            36: self.get_texture('resources/textures/brasil/mariapenha36.png'),
            37: self.get_texture('resources/textures/brasil/clarice37.png'),
            38: self.get_texture('resources/textures/brasil/irma38.png'),
            39: self.get_texture('resources/textures/brasil/carmen39.png'),
            40: self.get_texture('resources/textures/brasil/elis40.png'),
            41: self.get_texture('resources/textures/brasil/fernanda41.png'),

            42: self.get_texture('resources/textures/historia/moldura.png'),
            43: self.get_texture('resources/textures/criacoes/moldura2.png'),
            44: self.get_texture('resources/textures/mundo/moldura3.png'),
            45: self.get_texture('resources/textures/brasil/moldura4.png'),

        }