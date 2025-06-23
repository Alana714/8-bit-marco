from sprite_object import *
class Dialogs(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/atendente/dialogo.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (8, 16) or self.game.player.map_pos == (9, 16)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return

class DialogsHistoria(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/historia/1917.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if self.game.player.map_pos == (9,12):
            self.game.screen.blit(self.images[0], self.dialogo)
        if self.game.player.map_pos == (9,13):
            self.game.screen.blit(self.images[1], self.dialogo)
        if self.game.player.map_pos == (7,13):
           self.game.screen.blit(self.images[2], self.dialogo)
        if self.game.player.map_pos == (9,11):
            self.game.screen.blit(self.images[3], self.dialogo)
        if self.game.player.map_pos == (7,12):
            self.game.screen.blit(self.images[4], self.dialogo)
        if self.game.player.map_pos == (7,11):
           self.game.screen.blit(self.images[5], self.dialogo)
        else:
            return