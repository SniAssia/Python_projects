
import pygame
import math
def colorier(x, y):
    r = 0
    g = 0
    b = 0

    if x > 100 and x < 400:
        if y > 100 and y < 200:
            b = 255

    return (r, g, b)


pygame.init()
window = pygame.display.set_mode((500, 500))

run = True
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

#pygame.quit()
#exit()
#dessiner un disque bleu de centre (xc,yc) et de rayon R
def colorier1(x,y):
    r=0
    g=0
    b=0
    xc = 250
    yc = 250
    R = 150
    d = math.sqrt((x-xc)**2+(y-yc)**2)
    if d < R :
        b=255
    return (r,g,b)


pygame.init()
window = pygame.display.set_mode((500, 500))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size()) // 2] * 2))

    tx = pygame.time.get_ticks() / 1000.
    for x in range(500):
        for y in range(500):
            color = colorier1(x, y)
            window.set_at((x, y), color)

    pygame.display.flip()


#Faire un dégradé "bleu vers rouge"
# (de gauche à droite de l'écran)
def colorier2(x,y):
    f=x/500
    g=0
    r=255*f
    b=255*(1-f)
    return (r,g,b)


pygame.init()
window = pygame.display.set_mode((500, 500))

run = True
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

tab={}
for i in range(500):
    for j in range(500):
        tab[i,j]=0
# realiser un damier
def square(xs,ys,L):
    for i in range(L):
        for j in range(L):
            tab[xs+i,ys+j]=1
n=10
l=50
for i in range(n):
    for j in range(n):
        if (i+j)%2==0 :
            square(i*l,j*l,l)

def colorier4(x,y):
    r=0
    g=0
    b=0
    if tab[x,y]==1: # white color
        r = 255
        g = 255
        b = 255
    return (r, g, b)


pygame.init()
window = pygame.display.set_mode((500, 500))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size()) // 2] * 2))

    tx = pygame.time.get_ticks() / 1000.
    for x in range(500):
        for y in range(500):
            color = colorier4(x, y)
            window.set_at((x, y), color)

    pygame.display.flip()

pygame.quit()
exit()



