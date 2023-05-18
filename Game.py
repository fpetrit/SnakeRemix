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

            
            elif event.type == pygame.KEYUP:
                s.direction_vect = [0, -1]

            elif event.type == pygame.KEYDOWN:
                s.direction_vect = [0, 1]



    def game_actions(self):
        
        s = self.snake

        self.screen.fill("black", s.rect)

        s.rect.move_ip(s.speed*s.direction_vect[0], s.speed*s.direction_vect[1])

        self.screen.blit(s.img, s.rect)
        



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

