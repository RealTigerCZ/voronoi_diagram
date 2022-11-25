import pygame
import src.config
import numpy
import random
from typing import Optional
from enum import IntEnum, auto



class Algorithm(IntEnum):
    DEFAULT_SLOW:int = auto()
    D_BUFFER:int = auto() #distance buffer 

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

def generate_surface(algorithm: int, last: Optional[pygame.Surface] = None):
    surface = pygame.Surface(cfg_data.SCREEN_DIMS)
    if len(points) == 0:
        surface.fill(cfg_data.BGCOLOR)
        return surface
    
    if len(points) == 1:
        surface.fill(points[0].c)
        return surface

    if algorithm == Algorithm.DEFAULT_SLOW:
        return generate_surface_slow()
    
    if algorithm == Algorithm.D_BUFFER:
        return generate_surface_buffering(last)
    
    print("[ERROR] Unknown algoritm in generate_surface")
    exit(1)    
    

def generate_surface_slow() -> pygame.Surface:
    surface = pygame.Surface(cfg_data.SCREEN_DIMS)
    
    def get_color(row: int, col: int):
        arr = []
        for point in points:
            arr.append(point.distance(row, col))

        idx = numpy.argmin(arr)
        return points[idx].c
    
    for row in range(cfg_data.SCREEN_WIDTH):
        for col in range(cfg_data.SCREEN_HEIGHT):
            surface.set_at((row, col), get_color(row, col))
    
    return surface

points_distance_buffer: numpy.array = numpy.zeros(shape=cfg_data.SCREEN_DIMS, dtype = int) 

def generate_surface_buffering(last: pygame.Surface) -> pygame.Surface:
    assert len(points) >= 2, "TODO:"
    assert last, "TODO:"
    
    if len(points) == 2:
        with numpy.nditer(points_distance_buffer, flags=['multi_index'], op_flags=['writeonly']) as it:
            for x in it:
                x[...] = points[0].distance(it.multi_index[0], it.multi_index[1])
    
    point = points[-1]
    with numpy.nditer(points_distance_buffer, flags=['multi_index'], op_flags=['writeonly']) as it:
        for x in it:
            distance: int = point.distance(it.multi_index[0], it.multi_index[1])
            if x > distance:
                x[...] = distance
                last.set_at(it.multi_index, point.c)

    return last
                
      
            
        
        

def add_point(x:int, y:int):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    points.append(Point(x, y, pygame.Color(r, g, b)))
        
    
