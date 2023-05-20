import abc
from pygame import Surface, Rect
from ..Snake import Snake



class Element_ABC(abc.ABC):

    type = None

    def __init_subclass__(cls) -> None:
        # Make static attribute 'type' abstract.
        if Element_ABC.type is cls.type:
            raise NotImplementedError(f"Static attribute 'type' has not been overriden in class '{cls.__name__}'")

    @abc.abstractmethod
    def __init__(self, surface_side):
        self.surface_side = surface_side

    @abc.abstractmethod
    def get_surface(self) -> Surface:
        pass

    @abc.abstractmethod
    def draw(self,rect: Rect, screen: Surface):
        pass

    @abc.abstractmethod
    def collision_callback(self, snake: Snake):
        """This callback will be called if the snake collide with the element."""
        pass


