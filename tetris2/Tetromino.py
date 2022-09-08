from constants import *
from functions import *

class Tetromino():
    def __init__(self, shape , color, matrix) -> None:
        self.shape = shape
        self.color = color
        self.matrix = matrix
        self.rotation = 0
        self.moving = 1
        self.point_x = 4
        self.point_y = -4

    def check_collisions(self):
        for y,arrays in enumerate(self.shape[self.rotation]):

            for x, blocks in enumerate(arrays):
                if blocks == 1:
                    for tetrominos in self.matrix.tetrominos:

                        for t_y, t_arrays in enumerate(tetrominos.shape[tetrominos.rotation]):

                            for t_x, t_blocks in enumerate(t_arrays):
                                if t_blocks == 1:

                                    if self.point_x + x == tetrominos.point_x + t_x and self.point_y + y == tetrominos.point_y + t_y:
                                        return True

                    if self.point_x + x not in range(0, 10):
                        return True

                    elif self.point_y + y > 19:
                        return True
    
    def move_x(self, val):
        self.point_x += val
        if self.check_collisions():
            self.point_x -= val
    
        
    def update_y(self):
        self.point_y += self.moving  
        if self.check_collisions():
            self.point_y -= self.moving
            self.moving = 0 

    def rotate(self):
        self.rotation += 1 
        if self.rotation > len(self.shape) - 1:
            self.rotation = 0
            print('bruhr')
            
        if self.check_collisions():
            self.rotation -= 1
               

    def draw(self):
        for y, arrays in enumerate(self.shape[self.rotation]):

            for x, blocks in enumerate(arrays):
                if blocks == 1:

                    draw_block(self.point_x + x, self.point_y + y, self.color)            