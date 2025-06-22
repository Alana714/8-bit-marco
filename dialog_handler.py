from dialogs import *
class DialogHandler:
    def __init__(self, game):
        self.game = game
        self.dialog_path = 'resources\sprites\dialogs'
        draw_dialog = self.draw_dialog

        draw_dialog(Dialogs(game, pos=(5,1)))
        draw_dialog(Dialogs(game, pos=(5,2)))

    def draw_dialog(self, dialog):
        Dialogs(dialog)