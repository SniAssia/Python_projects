
"""
def solve_quartic(a, b, c, d, e):
    p = (-3 * b **2) / (8 * a ** 2) + (c / a)
    q = (b * 3) / (8 * a3) - (b * c) / (2 * a * 2) + (d / a)
    r = (-3 * b * 4) / (256 * a4) + (c * b2) / (16 * a3) - (b * d) / (4 * a * 2) + (e / a)

    discriminant = q * 2 - 4 * p * 3
    if discriminant > 0:
        A = (-q + discriminant ** 0.5) / 2
        B = (-q - discriminant ** 0.5) / 2

        y1 = (A * (1 / 3) + B * (1 / 3)) - b / (4 * a)
        y2 = complex(-(A * (1 / 3) + B(1 / 3)) / 2 - (A - B)(1 / 3) * (3) * 0.5 / 2j) - b / (4 * a)
        y3 = complex(-(A * (1 / 3) + B(1 / 3)) / 2 + (A - B)(1 / 3) * (3) * 0.5 / 2j) - b / (4 * a)

        return y1, y2, y3
    elif discriminant == 0:
        K = q / 2
        L = p ** (1 / 3)

        y1 = -2 * L - b / (4 * a)
        y2 = L - b / (4 * a)

        return y1, y2
    else:
        t = (-27 * r + 9 * p * q - 2 * p * 3) / (54 * discriminant) * 0.5
        theta = 3 * (4 * p * 3 - 9 * p * q + 27 * r) / (2 * discriminant) * 0.5

        y1 = (-2 * t - theta ** (1 / 3)) - b / (4 * a)
        y2 = (-2 * t + (theta * (1 / 3)) * (-1 + 1j * 3 * 0.5)) - b / (4 * a)
        y3 = (-2 * t + (theta * (1 / 3)) * (-1 - 1j * 3 * 0.5)) - b / (4 * a)

        return y1, y2, y3


# Coefficients de l'équation du 4e degré : ax^4 + bx^3 + cx^2 + dx + e = 0
a = 1
b = 2
c = 3
d = 4
e = 5
solutions = solve_quartic(a, b, c, d, e)
print("Les solutions de l'équation sont : ", solutions)

for i in l4:
    i.remove(i[0])
print(l4)
for i in l4:
    i.sort()
l5=[]
for i in l4:
    l0=[]
    for j in i:
            m = i.count(j)
"""


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def comb(l):
    count = {}
    for num in l:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return count

def final(dict):
    return [fact(j) for j in dict[i][0]]

handle = open("input","r")
l0=[]
for i in handle :
    l=i.split()
    l0.append(l)
l1=l0[1:]
for i in l1:
    i.remove(i[0])
l3=[]
for i in l1:
    l2=[]
    for j in i:
        s=int(j)
        l2.append(s)
        l2.sort()
    l3.append(l2)

print(l3)

l=[]
r=1
for i in l3:
    for k in comb(i):
        comb(i)[k]=j
        a=int(j)
        s=fact(a)
        r*=s
    l.append(r)

final_res = []
for i in range(len(l3)):
    final_res.append(final(comb(l3[i]))[0])

print(final_res)