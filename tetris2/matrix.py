from pygame import time
import pygame
import constants as c
#from functions import *
class Matrix:
    def __init__(self):
        self.tetrominos = []
        self.full_lines = []
        self.matrix = [
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0],
                      ]
    def check_lines(self):
        for y, arrays in enumerate(self.matrix):
            if arrays.count(1) == 10:
                self.full_lines.append(y)
                print(self.full_lines)                
            
    def clear_lines(self):
        if len(self.full_lines) > 0:
            moving_tetrominos = []
            for tetromino in self.tetrominos:
                for y,arrays in enumerate(tetromino.shape[tetromino.rotation]):
                    if tetromino.point_y + y in self.full_lines:
                        for x in range(len(arrays)):
                            tetromino.shape[tetromino.rotation][y][x] = 0
            print(self.matrix[19])                
            for tetromino in self.tetrominos:
                tetromino.moving = 1
                moving_tetrominos.append(tetromino)
            self.tetrominos.clear()

            for tetromino in moving_tetrominos:
                    #print("jabol")   
                    #tetromino.update_y()
                self.tetrominos.append(tetromino)

    def update_matrix(self):
        #this resets all the elements of the matrix to 0
        for y, arrays in enumerate(self.matrix):
            for x, arrays in enumerate(arrays):
                self.matrix[y][x] = 0
        #this loops trough all the tetrominos and determines their position in the matrix
        for tetromino in self.tetrominos:
            for y, arrays in enumerate(tetromino.shape[tetromino.rotation]):
                for x, blocks in enumerate(arrays):
                    if blocks == 1:
                        self.matrix[tetromino.point_y + y][tetromino.point_x + x] = 1             
        
    def draw_fallen_tetrominos(self):
        for tetromino in self.tetrominos:
            tetromino.draw()             
                    