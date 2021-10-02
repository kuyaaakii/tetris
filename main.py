import pygame
import random
pygame.init()

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
BORDER = WIDTH//3
BLOCK_SIZE = HEIGHT//20

win = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
pygame.display.set_caption("tetris")
clock = pygame.time.Clock()

I = [
     [
      [0,0,0,0],
      [0,0,0,0],
      [1,1,1,1],
      [0,0,0,0]
     ],
     [
      [0,0,1,0],
      [0,0,1,0],
      [0,0,1,0],
      [0,0,1,0]
     ]
    ]
J = [
     [
      [0,0,0],
      [1,1,1],
      [0,0,1]
     ],
     [
      [0,1,0],
      [0,1,0],
      [1,1,0]
     ],
     [
      [1,1,1],
      [1,0,0],
      [0,0,0]
     ],
     [
      [0,1,1],
      [0,1,0],
      [0,1,0]
     ]
    ]      
L = [
     [
      [0,0,0],
      [1,1,1],
      [1,0,0]
     ],   
     [
      [1,1,0],
      [0,1,0],
      [0,1,0]
     ],
     [
      [0,0,1],
      [1,1,1],
      [0,0,0]
     ],
     [
      [0,1,0],
      [0,1,0],
      [0,1,1]
     ]
    ]   
O = [
     [
      [1,1],
      [1,1]
     ]
    ]    
S = [
     [
      [0,0,0],
      [0,1,1],
      [1,1,0]
     ],
     [
      [0,1,0],
      [0,1,1],
      [0,0,1]
     ]
    ]
T = [
     [
      [0,0,0],
      [1,1,1],
      [0,1,0]
     ],
     [
      [0,1,0],
      [1,1,0],
      [0,1,0]
     ],
     [
      [0,1,0],
      [1,1,1],
      [0,0,0]
     ],
     [
      [0,1,0],
      [0,1,1],
      [0,1,0]
     ]
    ]
Z = [
     [
      [0,0,0],
      [1,1,0],
      [0,1,1]
     ],
     [
      [0,0,1],
      [0,1,1],
      [0,1,0]
     ]
    ]
shapes = [I,J,L,O,S,T,Z]
colors = [(0,233,233),(0,0,233),(233,155,0 ),(233,233,0),(0,233,0),(155,0,233),(233,0,0)]

def random_array(array):
    for i in range(0,7):
        array.append(random.randrange(0,6))


def draw_matrix_border():
    #this function makes the border for the matrix

    blok = 0
    x = WIDTH//3-BLOCK_SIZE
    xdiff = x + BLOCK_SIZE * 10

    for i in range(20):
        rect = pygame.Rect(x, blok, BLOCK_SIZE, BLOCK_SIZE)
        rectdiff = pygame.Rect(xdiff, blok, BLOCK_SIZE, BLOCK_SIZE)

        pygame.draw.rect(win, (0, 0, 255), rect)
        pygame.draw.rect(win, (0, 0, 255), rectdiff)
        pygame.draw.rect(win, (0, 0, 0), rect,1)
        pygame.draw.rect(win, (0, 0, 0), rectdiff,1)

        blok = blok + BLOCK_SIZE

def get_block_coordinates(x, y):
    blockx = BORDER + x * BLOCK_SIZE 
    blocky = y * BLOCK_SIZE 
    return [blockx, blocky]

def draw_block(x,y,color):
    block = pygame.Rect(get_block_coordinates(x,y)[0], get_block_coordinates(x,y)[1], BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(win,color,block)

class Tetromino():
    def __init__(self, shape , color ,fallen_blocks_array) -> None:
        self.shape = shape
        self.color = color
        self.rotation = 0
        self.speed = 1
        self.point_x = 4
        self.point_y = -4
        self.fallen_blocks = fallen_blocks_array


    def checkcollitions(self):
        for y,arrays in enumerate(self.shape[self.rotation]):

            for x,blocks in enumerate(arrays):

                if blocks == 1:

                    for tetrominos in self.fallen_blocks:

                        for diff_y,diff_arrays in enumerate(tetrominos.shape[tetrominos.rotation]):

                            for diff_x,diff_blocks in enumerate(diff_arrays):
                                if diff_blocks == 1:
                                    if self.point_x + x == tetrominos.point_x + diff_x and self.point_y + y == tetrominos.point_y + diff_y:
                                        return True
                                        
                                    elif self.point_y + y == 20:
                                        return True
                                    else:
                                        return False
    def move_x(self, addval):
        self.point_x += addval

        if self.checkcollitions():

            self.point_x -= addval
                
        elif self.point_x not in range(0,10,1):
            self.point_x -= addval

    def update_y(self):

        self.point_y += self.speed
        if self.checkcollitions():
            self.point_y -= self.speed
            self.speed = 0


    def draw(self):
     
        for y,arrays in enumerate(self.shape[self.rotation]):
          
            for x,blocks in enumerate(arrays):
                if blocks == 1:
                    draw_block(self.point_x + x,self.point_y + y,self.color)
        



blocks_number = 0
next_blocks = []
random_array(next_blocks)
fallen_blocks = []
t = Tetromino(shapes[next_blocks[blocks_number]], colors[next_blocks[blocks_number]],fallen_blocks)

def main():
    global t, blocks_number,next_blocks
    run = True
    
    while(run):
        pygame.time.delay(200)
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_DOWN:
                  pass

               elif event.key == pygame.K_UP:
                    pass    

               elif event.key == pygame.K_RIGHT:
                    t.move_x(1)

               elif event.key == pygame.K_LEFT:
                    t.move_x(-1)
        t.update_y()

        draw_matrix_border()

        t.draw()

        if t.speed == 0:
            t.fallen_blocks.append(t)
            blocks_number += 1

            if blocks_number > 6:
                next_blocks = []
                random_array(next_blocks)
                blocks_number = 0

            t = Tetromino(shapes[next_blocks[blocks_number]], colors[next_blocks[blocks_number]],fallen_blocks)

        

        for blocks in t.fallen_blocks:
            blocks.draw()  
        
        pygame.display.update()
        win.fill((0,0,0))        
    pygame.quit()
if __name__ == '__main__':
    main()


