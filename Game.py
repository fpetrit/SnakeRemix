import pygame
from Snake import Snake

class Game:

    def __init__(self, size, fps):
        pygame.init()
        self.running = False
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.snake = Snake()



    def handle_events(self):

        s = self.snake

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                pass
                



    def game_actions(self):
        
        self.snake.move(self.screen)
        



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

