from Game import Game
from conf.Conf import cf

def_win_size = tuple(cf["Window"]["default_size"])
def_fps = cf["Window"]["default_fps"]

class App:

    def __init__(self, size = def_win_size, fps = def_fps):

        self.win = Game(size, fps)


    def launch(self):
        self.win.main_loop()

