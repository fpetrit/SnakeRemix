from Window import Window

class Game:

    def __init__(self):

        self.win = Window((1080, 720), 40)


    def launch(self):
        self.win.main_loop()

