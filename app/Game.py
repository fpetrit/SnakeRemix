import pygame
from .Snake import Snake
from .conf.Conf import SNAKE_CF, cf, LEFT, RIGHT, UP, DOWN
from .grid.Grid import Grid



class Game:

    def __init__(self, size, fps):
        pygame.init()
        self.running = False
        self.size = size
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.snake = Snake(**SNAKE_CF)
        self.grid = Grid(self.screen, **cf["Background"])
        self.map = pygame.Rect((0, 0), self.size)



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
        
        # Draw the background
        self.screen.blit(self.grid.grid_surface, (0, 0))
        
        # Move the snake
        self.snake.move(self.screen)

        # Check if the snake is in the map, if not throw an event
        if not self.snake.is_in_rect(self.map):
            print("Out of the map")

        # Check if the snake collided, throw the appropriate event



        
        



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

