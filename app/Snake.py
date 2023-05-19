from .conf.Conf import cf
import pygame


Direction = list[int]


class Snake:

    def __init__(self, **SNAKE_CF):

        self.speed = SNAKE_CF["speed"] # pixel per frame
        self.length = SNAKE_CF["initial_length"] # pixels
        self.__direction_vect = [0, 0]

        
        self.img = pygame.image.load(cf["App"]["root_dir"] / "app/assets/snake.jpg").convert()
        self.rect = pygame.Rect(0, 0, self.img.get_width(), self.img.get_height())



    def change_direction(self, direction : Direction) -> None:
        self.__direction_vect = direction



    def move(self, screen):
        """Moove the snake on the screen accordingly with his speed and direction."""

        s = self

        s.rect.move_ip(s.speed*s.__direction_vect[0], s.speed*s.__direction_vect[1])
        
        screen.blit(s.img, s.rect)