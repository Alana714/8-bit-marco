from dialogs import *
class DialogHandler:
    def __init__(self, game):
        self.game = game
        self.dialogs_list = []
        self.dialogs_path = 'resources/sprites/dialogs/'
        add_dialog = self.add_dialog

        # sprite map
        add_dialog(Dialogs(game, pos=(5, 1)))

    def update(self):
        [dialog.update() for dialog in self.dialogs_list]

    def add_dialog(self, dialog):
        self.dialogs_list.append(dialog)
