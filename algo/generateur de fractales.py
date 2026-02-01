import math
import pygame
x = 4
z = (2 + 3j)*(5 + x*1j)
print(z)

def colorier(x,y):
    r=0
    g=0
    b=0
    k=10
    x0=2*(x-250)/250
    y0=2*(y-250)/250
    z=0
    n=0
    while n<k and abs(z)<2:
        z=z**2+x0 +y0*1j
        n+=1
    if abs(z)<1.5:
        g=200
    return (r,g,b)
#A présent : comment représenter toutes les couches simultanément ?

def colorier1(x, y):
    r = 0
    g = 0
    b = 0
    # Changement de répères :
    x2 = 2 * (x - 250) / 250.
    y2 = 2 * (y - 250) / 250.

    # Calcule z(k) :
    z = 0
    n = 0
    while n < 30 and abs(z) < 2:
        z = z ** 2 + x2 + y2 * 1j
        n += 1

    if n <= 29:
        k = n % 4
        if k == 0:
            g = 100
        if k == 1:
            g = 150
        if k == 2:
            g = 200
        if k == 3:
            g = 150

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
            color = colorier1(x, y)
            window.set_at((x, y), color)
    pygame.display.flip()
pygame.quit()
exit()

