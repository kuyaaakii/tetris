import pygame
pygame.init()
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
blocksize = HEIGHT//20
win = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
pygame.display.set_caption("tetris")

def drawplayareaborder():

    diff = (WIDTH//3 - HEIGHT//2)//2
    print(diff)
    blok = 0
    x = WIDTH//3+diff
    xdiff = WIDTH//3*2-diff

    for i in range(20):
        rect = pygame.Rect(x, blok, blocksize, blocksize)
        rectdiff = pygame.Rect(xdiff, blok, blocksize, blocksize)

        pygame.draw.rect(win, (0, 0, 255), rect)
        pygame.draw.rect(win, (0, 0, 255), rectdiff)
        pygame.draw.rect(win, (0, 0, 0), rect,1)
        pygame.draw.rect(win, (0, 0, 0), rectdiff,1)

        blok = blok + blocksize
    


def main():
    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawplayareaborder()
        pygame.display.update()
    pygame.quit()        

main()