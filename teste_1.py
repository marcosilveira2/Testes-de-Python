import pygame
import math

def main():

    pygame.init()
    tela = pygame.display.set_mode((480, 300))

    blue = pygame.Rect(255, 285, 30, 15)
    green = pygame.Rect(225, 285, 30, 15)
    red = pygame.Rect(195, 285, 30, 15)
    angulo = 20

    time = pygame.time.Clock()

    x = 1
    y = -1/math.tan((angulo/180)*math.pi)

    bgc = 0
    r = (255, 0, 0)
    g = (0, 255, 0)
    b = (0, 0, 255)


    fim = False
    while fim == False:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fim = True

        blue = blue.move(x,y)
        green = green.move(0,y)
        red = red.move(-x,y)

        if green.top < 0 or green.top > 285:
            y = -y
        if blue.right > 480 or blue.left < 0 or blue.colliderect(green):
            x = -x

        time.tick(30)

        cor_fundo = (bgc, bgc, bgc)
        tela.fill(cor_fundo)

        pygame.draw.rect(tela,b,blue)
        pygame.draw.rect(tela,g,green)
        pygame.draw.rect(tela,r,red)

        pygame.display.flip()

    pygame.quit()

main()
