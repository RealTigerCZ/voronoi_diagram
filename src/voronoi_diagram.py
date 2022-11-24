import pygame
import src.config
import numpy
import random

cfg_data: src.config.Config_data = src.config.init_cfg()


class Point():
    def __init__(self, x: int, y: int, color: pygame.Color) -> None:
        self.x = x
        self.y = y
        self.c = color
        self.ci = pygame.Color(255 - color.r, 255 - color.g, 255 - color.b)

    def render(self, screen: pygame.Surface) -> None:
        x = int(cfg_data.SCREEN_SCALE * self.x)
        y = int(cfg_data.SCREEN_SCALE * self.y)
        pygame.draw.circle(screen, self.ci, (x, y), cfg_data.POINT_SIZE)
        
    def distance(self, x:int, y:int):
        return (self.x - x)**2 + (self.y - y)**2 #no need to sqrt 


points: list[Point] = []


def get_color(row:int, col:int):
    arr = []
    for point in points:
        arr.append(point.distance(row, col))
        
    idx = numpy.argmin(arr)
    return points[idx].c


    
def generate_surface() ->  pygame.Surface:
    surface = pygame.Surface(cfg_data.SCREEN_DIMS)
    if len(points) == 0:
        surface.fill(cfg_data.BGCOLOR)
        return surface
    
    if len(points) == 1:
        surface.fill(points[0].c)
        return surface
    
    for row in range(cfg_data.SCREEN_WIDTH):
        for col in range(cfg_data.SCREEN_HEIGHT):
            surface.set_at((row, col), get_color(row, col))
    
    return surface


def add_point(x:int, y:int):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    points.append(Point(x, y, pygame.Color(r, g, b)))
        
    
