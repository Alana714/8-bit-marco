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
        
class DialogsArte(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/arte/anita.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if self.game.player.map_pos == (6, 9):
            self.game.screen.blit(self.images[0], self.dialogo)
        elif self.game.player.map_pos == (5, 9):
            self.game.screen.blit(self.images[1], self.dialogo)
        elif self.game.player.map_pos == (11, 9):
            self.game.screen.blit(self.images[2], self.dialogo)
        elif self.game.player.map_pos == (5, 6):
            self.game.screen.blit(self.images[3], self.dialogo)
        elif self.game.player.map_pos == (10, 9):
            self.game.screen.blit(self.images[4], self.dialogo)
        elif self.game.player.map_pos == (6, 6):
            self.game.screen.blit(self.images[5], self.dialogo)
        elif self.game.player.map_pos == (11, 6):
            self.game.screen.blit(self.images[6], self.dialogo)
        elif self.game.player.map_pos == (10, 6):
            self.game.screen.blit(self.images[7], self.dialogo)
        else:
            return
        
class DialogsMundo(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/mundo/anne.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if self.game.player.map_pos == (1, 8):
            self.game.screen.blit(self.images[0], self.dialogo)
        elif self.game.player.map_pos == (2, 5):
            self.game.screen.blit(self.images[1], self.dialogo)
        elif self.game.player.map_pos == (3, 8):
            self.game.screen.blit(self.images[2], self.dialogo)
        elif self.game.player.map_pos == (2, 8):
            self.game.screen.blit(self.images[3], self.dialogo)
        elif self.game.player.map_pos == (3, 5):
            self.game.screen.blit(self.images[4], self.dialogo)
        elif self.game.player.map_pos == (1, 7):
            self.game.screen.blit(self.images[5], self.dialogo)
        elif self.game.player.map_pos == (1, 6):
            self.game.screen.blit(self.images[6], self.dialogo)
        elif self.game.player.map_pos == (1, 5):
            self.game.screen.blit(self.images[7], self.dialogo)
        else:
            return