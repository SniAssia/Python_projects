import pygame
import math
xc = 250
yc = 250
r1 = 150
r2=220

tab={}
for i in range(500):
    for j in range(500):
        tab[i,j]=0

for i in range(500):
    for j in range(500):
        a=math.sqrt((i-xc)**2+(j-yc)**2)
        if a<r1 :
            tab[i,j]=0
        elif a>r1 and a<r2:
            tab[i,j]=1

def colorier(x,y):
    r=0
    g=0
    b=0
    if tab[x,y]==1:
       x0=x-250
       y0=y-250
       angle = 180+180*math.atan2(x0,y0)/math.pi
       if angle >=0 and angle < 120:
           f=255*angle/120
           b=255-f
           r=f
       elif angle>= 120 and angle < 240 :
           f =255*(angle-120)/120
           g=f
           r=255-f
       else :
           f = 255 * (angle-240) / 120
           b =f
           g = 255-f


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
            color = colorier(x, y)
            window.set_at((x, y), color)
    pygame.display.flip()
pygame.quit()
exit()
