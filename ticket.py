from sprite_object import *


class Ticket(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/ticket/ticket.png', scale=0.5):
        super().__init__(game=game, path=path, scale=scale)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.ticket_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())

    def draw(self):
        if self.player.holding_ticket:
            self.game.screen.blit(self.images[0], self.ticket_pos)
        else:
            return
