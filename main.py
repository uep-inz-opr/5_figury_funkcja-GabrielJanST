from math import pi
lst = []
figura = []
liczba_figur = int(float(input().strip()))
for i in range(liczba_figur):
    lst.append(input().split())

def policz_kolo(a):
        return pi * a * a
def policz_prostokata(a,b):
        return a * b
def policz_trojkata(a,b,c):
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

pole = 0

for figura in lst:
    if len(figura) == 1:
        a = float(figura[0])
        pole += policz_kolo(a)
    elif len(figura) == 2:
        a = float(figura[0])
        b = float(figura[1])
        pole += policz_prostokata(a,b)
    elif len(figura) == 3:
        a = float(figura[0])
        b = float(figura[1])
        c = float(figura[2])
        s = ((a + b + c)/2)
        pole += policz_trojkata(a,b,c)
    else:
        print("Błąd: można podać maksymalnie 3 liczby")
        break
print(round(pole,2))