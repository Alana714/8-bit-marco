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
        
class DialogHedy(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/hedy/hedy.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (7, 3)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return
        
class DialogMarie(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/marie/marie.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (7, 2)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return

class DialogAda(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/ada/ada.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (8, 1)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return
        
class DialogGrace(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/grace/grace.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (7, 1)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return
        
class DialogValerie(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/valerie/valerie.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (9, 1)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return

class DialogRadia(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/radia/radia.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (9, 2)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return
    
class DialogChieko(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/chieko/chieko.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (9, 3)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return
        
class DialogMaria(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/maria/maria.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (13, 8)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return

class DialogBertha(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/bertha/bertha.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (14, 8)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return

class DialogMariaPenha(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/mariapenha/mariapenha.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (15, 8)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return

class DialogClarice(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/clarice/clarice.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (15, 7)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return

class DialogAna(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/ana/ana.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (15, 6)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return
        
class DialogCarmen(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/carmen/carmen.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (15, 5)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return
        
class DialogElis(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/elis/elis.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (14, 5)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return
        
class DialogFernanda(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/dialogs/criacoes/fernanda/fernanda.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.dialogo = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT * 1.2 - self.images[0].get_height())

    def draw(self):
        if not self.player.holding_ticket and (self.game.player.map_pos == (13, 5)):
            self.game.screen.blit(self.images[0], self.dialogo)
        else:
            return