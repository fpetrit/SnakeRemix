import pygame
from ..Element_ABC import Element_ABC
from ..element_types import OBSTACLE_TYPE
from ...conf.Conf import cf
from ...Snake import Snake


class Obstacle(Element_ABC):

    type = OBSTACLE_TYPE

    def __init__(self, surface_side):
        super().__init__(surface_side)
        
        self.surface = self.get_surface()


    def get_surface(self) -> pygame.Surface:
        super().get_surface()

        img = pygame.image.load(cf["App"]["assets_dir"] / "obstacle.jpg").convert()
        img = pygame.transform.scale(img, (self.surface_side, self.surface_side))
    
        return img
    

    def draw(self, rect: pygame.Rect, surface: pygame.Surface):
        super().draw(rect, surface)

        surface.blit(self.get_surface(), rect)
        


    def collision_callback(self, snake: Snake):
        super().collision_callback(snake)
        snake.die()


        
