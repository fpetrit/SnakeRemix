from ..conf.Conf import cf
import pygame
from .elements.Obstacle import Obstacle
from .Element_ABC import Element_ABC

class Grid:

    def __init__(self, screen: pygame.Surface, **BG_CF):

        self.screen = screen

        self.column_nb = BG_CF["column_nb"]

        side_len = min(self.screen.get_width(), self.screen.get_height())
        self.square_side = side_len // self.column_nb

        self.element_grid = [[0]*self.column_nb for _ in range(self.column_nb)]

        # TEST #
        self.element_grid[3][5] = Obstacle(self.square_side)
        self.element_grid[3][5].draw(self.get_square_rect((5, 3)), self.screen)
        # # # # #

        self.rect_list = self.get_rect_list()

        self.grid_surface = self.get_background_surface()

        self.grid_element_surface = self.get_element_surface()



    def coord_to_index(self, coord: tuple[int]):
        x, y = coord[0], coord[1]
        return self.column_nb * y + x


    def index_to_coord(self, index: int) -> tuple[int]:
        x, y = index % self.column_nb, index // self.column_nb
        return (x, y)



    def get_square_rect(self, coordinates: tuple[int]) -> pygame.Rect :
        return pygame.Rect(coordinates[0]*self.square_side, coordinates[1]*self.square_side, self.square_side, self.square_side)



    def get_rect_list(self) -> list[pygame.Rect]:

        l = list()

        for y in range(self.column_nb):
            for x in range(self.column_nb):
                
                l.append(self.get_square_rect((x, y)))

        return l
    


    def get_elements_rect(self) -> dict[tuple, pygame.Rect]:

        d = dict()

        for y in range(self.column_nb):
            for x in range(self.column_nb):
                if self.element_grid[y][x] != 0:
                    d[(x, y)] = self.get_square_rect((x, y))

        return d



    def get_background_surface(self):

        surface = self.screen.copy()

        sprite = pygame.image.load(cf["App"]["assets_dir"] / "grass1.png").convert()
        sprite = pygame.transform.scale(sprite, (self.square_side, self.square_side))

        for square in self.rect_list:

                surface.blit(sprite, square)

        return surface
    


    def get_element_surface(self) -> pygame.Surface:

        surface = self.grid_surface.copy()

        for y in range(self.column_nb):
            for x in range(self.column_nb):
                if self.element_grid[y][x] != 0:
                    self.element_grid[y][x].draw(self.get_square_rect((x, y)), surface)
        
        return surface
    