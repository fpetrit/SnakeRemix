import pygame
from .Snake import Snake
from .conf.Conf import SNAKE_CF, cf, LEFT, RIGHT, UP, DOWN


from .background.Background import Background

class Game:

    def __init__(self, size, fps):
        pygame.init()
        self.running = False
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.snake = Snake(**SNAKE_CF)

        self.bg = Background(self.screen, **cf["Background"])



    def handle_events(self):

        s = self.snake

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                match event.unicode:
                    case 'z': self.snake.change_direction(UP)
                    case 's': self.snake.change_direction(DOWN)
                    case 'q': self.snake.change_direction(LEFT)
                    case 'd': self.snake.change_direction(RIGHT)
                



    def game_actions(self):
        
        self.screen.blit(self.bg.grid_surface, (0, 0))

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

