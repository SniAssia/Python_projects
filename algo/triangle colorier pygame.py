import pygame
import math
xa = 100
ya= 400

xb = 200
yb = 100

xc = 300
yc = 300
# calcul de l'aire du triangle
def surface(xa,ya,xb,yb,xc,yc):
    a = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
    b = math.sqrt((xc - xb) ** 2 + (yc - yb) ** 2)
    c = math.sqrt((xc - xa) ** 2 + (yc - ya) ** 2)
    s = (a + b + c) / 2
    if s > a and s > b and s > c:
        return  math.sqrt(s * (s - a) * (s - b) * (s - c))
    return 0
tab={}


def is_point_inside_triangle(xa, ya, xb, yb, xc, yc, px, py, tol=1e-6):
    """
    Vérifie si un point (px, py) est à l'intérieur d'un triangle en utilisant des aires,
    avec une tolérance pour éviter les erreurs de calcul en virgule flottante.
    """
    total_area = surface(xa, ya, xb, yb, xc, yc)
    area1 = surface(px, py, xb, yb, xc, yc)
    area2 = surface(xa, ya, px, py, xc, yc)
    area3 = surface(xa, ya, xb, yb, px, py)

    return abs((area1 + area2 + area3) - total_area) < tol


for i in range(500):
    for j in range(500):
        tab[i,j]=0
for i in range(500):
    for j in range(500):
        tab[i,j]=is_point_inside_triangle(xa, ya, xb, yb, xc, yc,i,j, tol=1e-6)


def colorier(x,y):
    r=0
    g=0
    b=0
    if tab[x,y]==1:
        r=255
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