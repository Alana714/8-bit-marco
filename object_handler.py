from sprite_object import *
class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite

        # sprite map
        # add_sprite(SpriteObject(game, path=self.static_sprite_path + 'wecan.png', scale=1.0, pos=(3.5, 2.5), shift=0.3))

        add_sprite(BlockObject(game, pos=(8.7, 15)))
        add_sprite(BlockObject(game, pos=(8.2, 15)))
        # add_sprite(SpriteObject(game, path=self.static_sprite_path + 'atendente.png', pos=(5.95, 4.5), shift=0.08))

        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'mulheres/1.png', pos=(11.95, 1.5), shift=0.05))

    # def check_win(self):
    #     if not len(self.npc_positions):
    #         self.game.object_renderer.win()
    #         pg.display.flip()
    #         pg.time.delay(1500)
    #         self.game.new_game()

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        # self.check_win()

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
