from sprite_object import *


class Dialogs(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/atendente/dialogo.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo_atendente = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (5, 4) or self.game.player.map_pos == (4.5, 4)):
            self.game.screen.blit(self.images[0], self.dialogo_atendente)
        else:
            return