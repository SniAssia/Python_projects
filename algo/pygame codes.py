# fonction colorier
# a chaque pixel(x,y) on associe une couleur (r,g,b)
# carré bleu
import pygame
def colorier(x,y):
    r=0
    g=0
    b=0
    if x>100 and x<400:
        if y>100 and y<200:
            b=225
    return (r,g,b)

pygame.init()
window =pygame.display.set_mode((500,500))

run =True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size()) // 2] * 2))

    tx = pygame.time.get_ticks() / 1000.
    for x in range(500):
        for y in range(500):
            color = colorier(x, y)
            window.set_at((x, y), color)

    pygame.display.flip()


# exo 2 : dessiner un disque bleu de centre (xc,yc) et de rayon r

import math
def colorier2(x,y):
    xc = 250
    yc = 250
    R = 150
    r= 0
    g=0
    b=0
    # la distance entre le centre et n'importe quel point du disque
    d=math.sqrt((x-xc)**2+(y-yc)**2)
    if d < R :
        b =255
    return (r,g,b)

pygame.init()
window =pygame.display.set_mode((500,500))

run =True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size()) // 2] * 2))

    tx = pygame.time.get_ticks() / 1000.
    for x in range(500):
        for y in range(500):
            color = colorier2(x, y)
            window.set_at((x, y), color)

    pygame.display.flip()

# exo 3 :
# faire un degradé bleu vers rouge
# de gauche a droite de l'écran
def colorier3(x,y):
    f=x/500

    g=0
    r=255*f
    b=255*(1-f)

    return (r,g,b)


pygame.init()
window =pygame.display.set_mode((500,500))

run =True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size()) // 2] * 2))

    tx = pygame.time.get_ticks() / 1000.
    for x in range(500):
        for y in range(500):
            color = colorier3(x, y)
            window.set_at((x, y), color)

    pygame.display.flip()
# realiser un damier

n=10
l12=50
tab={}
for i in range(500):
    for j in range(500):
        tab[i,j]=0

def square(xs,ys,ls):
    for i in range(ls):
        for j in range(ls):
            tab[xs+i,ys+j]=1

def even(k):
    if 2 * int(k / 2) == k:
        return 1
    else:
        return 0


for i in range(n):
    for j in range(n):
        z=even(i)+even(j)
        if even(z):
            square(i*l12,j*l12,l12)

def colorierr(x,y):
    r=0
    g=0
    b=0

    if tab[x,y]==1:
        r=255
        g=255
        b=255

    return (r,g,b)



pygame.init()
window =pygame.display.set_mode((500,500))

run =True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    window.fill(0)
    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size()) // 2] * 2))

    tx = pygame.time.get_ticks() / 1000.
    for x in range(500):
        for y in range(500):
            color = colorierr(x, y)
            window.set_at((x, y), color)

    pygame.display.flip()




























pygame.quit()
exit()
