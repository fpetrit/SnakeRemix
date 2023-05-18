import pygame
from Snake import Snake

class Game:

    def __init__(self, size, fps):
        pygame.init()
        self.running = False
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = fps



    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False


    def game_actions(self):
        pass



    def refresh(self):

        pygame.display.flip()
        self.clock.tick(self.fps)


    

    def main_loop(self):
        self.running = True

        while self.running:

            self.handle_events()

            self.game_actions()

            self.refresh()

        pygame.quit()

