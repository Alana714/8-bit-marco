from sprite_object import *
class Dialogs(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/atendente/dialogo.png', scale=0.5, pos=(6, 13)):
        super().__init__(game=game, path=path, scale=scale, pos=pos)
        self.pos = pos
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (8, 16) or self.game.player.map_pos == (9, 16)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return