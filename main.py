import pygame
blocksize = 54
pygame.init()
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
win = pygame.display.set_mode((1920,1080)) 
pygame.display.set_caption("tetris")

def drawplayarea():
    blok = 0
    x = WIDTH//3+50
    xdiff = WIDTH//3*2-50
    for i in range(20):
        print (xdiff)
        print(x)
        rect = pygame.Rect(x, blok, blocksize, blocksize)
        rectdiff = pygame.Rect(xdiff, blok, blocksize, blocksize)
        pygame.draw.rect(win, (0, 0, 255), rect)
        pygame.draw.rect(win, (0, 0, 255), rectdiff)
        pygame.draw.rect(win, (0, 0, 0), rect,1)
        pygame.draw.rect(win, (0, 0, 0), rectdiff,1)
        blok = blok + 54
    


def main():
    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawplayarea()
        pygame.display.update()
    pygame.quit()        

main()