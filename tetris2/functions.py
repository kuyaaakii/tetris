from constants import *
def draw_matrix_border():
    #this function makes the border for the matrix

    blok = 0
    x = WIDTH//3 - BLOCK_SIZE
    xdiff = WIDTH//3 + BLOCK_SIZE * 10

    for i in range(20):
        rect = pygame.Rect(x, blok, BLOCK_SIZE, BLOCK_SIZE)
        rectdiff = pygame.Rect(xdiff, blok, BLOCK_SIZE, BLOCK_SIZE)

        pygame.draw.rect(win, (0, 0, 255), rect)
        pygame.draw.rect(win, (0, 0, 255), rectdiff)
        pygame.draw.rect(win, (0, 0, 0), rect,1)
        pygame.draw.rect(win, (0, 0, 0), rectdiff,1)

        blok = blok + BLOCK_SIZE

def test():
    draw_block(0, 0, COLORS[0])

def get_block_coordinates(x, y):
    blockx = WIDTH//3 + x * BLOCK_SIZE 
    blocky = y * BLOCK_SIZE 
    return [blockx, blocky]

def draw_block(x,y,color):
    block = pygame.Rect(get_block_coordinates(x,y)[0], get_block_coordinates(x,y)[1], BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(win,color,block)  