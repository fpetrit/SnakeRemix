from conf.Conf import cf
import pygame

snake_cf = cf["Snake"]


class Snake:

    def __init__(self, speed = snake_cf["initial_speed"], intitial_length = snake_cf["initial_length"]):

        self.speed = speed # pixel per frame
        self.length = intitial_length # pixels
        self.direction_vect = [0, 0]

        
        self.img = pygame.image.load(cf["App"]["root_dir"] / "assets/snake.jpg").convert()
        self.rect = pygame.Rect(0, 0, self.img.get_width(), self.img.get_height())
        

