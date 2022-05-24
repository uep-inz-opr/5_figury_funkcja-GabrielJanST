from math import pi
lst = []
wynik = 0
liczba_figur = int(input())
for i in range(liczba_figur):
    lst = list(map(float, input().split()))
#s = float
#pole = float
if len(lst) == 1:
    a = float(lst[0])
    def policz_kolo(a):
        return pi * a * a
    pole = '%0.2f' %policz_kolo(a)
    if wynik == 0:
        wynik = pole
    else:
        #wynik = wynik + pole
        wynik = sum(wynik,pole)
    #wynik.append(pole)
#elif c == 0:
elif len(lst) == 2:
    a = float(lst[0])
    b = float(lst[1])
    def policz_prostokata(a,b):
        return a * b
    pole = '%0.2f' %policz_prostokata(a,b)
    if wynik == 0:
        wynik = pole
    else:
        wynik = sum(wynik,pole)
    #wynik.append((pole).strip())
    #print(pole)
elif len(lst) == 3:
    a = float(lst[0])
    b = float(lst[1])
    c = float(lst[2])
    s = ((a + b + c)/2)
    def policz_trojkata(a,b,c):
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5 
    pole = '%0.2f' %policz_trojkata(a,b,c)
    if wynik == 0:
        wynik = pole
    else:
        wynik = sum(wynik,pole)
    #wynik.append((pole).strip())
    #print(pole)
else:
    print("Błąd: można podać maksymalnie 3 liczby")
print ((wynik))