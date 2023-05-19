from ..conf.Conf import cf
import pygame

class Background:

    def __init__(self, screen: pygame.Surface, **BG_CF):

        self.screen = screen

        self.grid = [[0]*BG_CF["column_nb"] for _ in range(BG_CF["column_nb"])]

        side_len = min(self.screen.get_width(), self.screen.get_height())

        self.square_side = side_len // BG_CF["column_nb"]

        self.grid_surface = self.get_grid_surface()



    def get_square_rect(self, coordinates: tuple[int]) -> pygame.Rect :
        
        return pygame.Rect(coordinates[0]*self.square_side, coordinates[1]*self.square_side, self.square_side, self.square_side)
    

    def get_grid_surface(self):

        surface = self.screen.copy()

        sprite = pygame.image.load(cf["App"]["assets_dir"] / "grass1.png").convert()
        sprite = pygame.transform.scale(sprite, (self.square_side, self.square_side))

        y, x = 0, 0

        for y in range(len(self.grid)):

            for x in range(len(self.grid)):

                square = self.get_square_rect((y, x))

                surface.blit(sprite, square)

        return surface

                

                



                

        
