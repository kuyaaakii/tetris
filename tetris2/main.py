from constants import *
from functions import *
from Tetromino import Tetromino
from matrix import Matrix

pygame.init()



def main():
  tetromino_number = 0
  next_tetrominos = [0,1,2,3,4,5,6]
  random.shuffle(next_tetrominos)
  M = Matrix()
  T = Tetromino(SHAPES[next_tetrominos[tetromino_number]], COLORS[next_tetrominos[tetromino_number]], M)

  run = True
  while run:
    pygame.time.delay(200)
    clock.tick(30)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_DOWN:          
                  pass
                
               elif event.key == pygame.K_r:
                  T.rotate()

               elif event.key == pygame.K_UP:
                  pass 

               elif event.key == pygame.K_RIGHT:
                  T.move_x(1)

               elif event.key == pygame.K_LEFT:
                  T.move_x(-1)
    T.draw()
    draw_matrix_border()
    T.update_y()

    if not T.moving:
      M.tetrominos.append(T)
      tetromino_number += 1
      M.update_matrix()
      M.check_lines()
      M.clear_lines()

      if tetromino_number > 6:

        next_tetrominos.clear()
        next_tetrominos = [0,1,2,3,4,5,6]
        random.shuffle(next_tetrominos)
        tetromino_number = 0

      T = Tetromino(SHAPES[next_tetrominos[tetromino_number]], COLORS[next_tetrominos[tetromino_number]], M)
    
    M.draw_fallen_tetrominos()
    pygame.display.update()
    win.fill((0, 0, 0))                
  pygame.quit()    

if __name__ == "__main__":
  main()