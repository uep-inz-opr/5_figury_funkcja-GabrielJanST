from math import pi
lst = []
figura = []
#wynik = []
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
    #def policz_kolo(a):
    #    return pi * a * a
        #pole += '%0.2f' %policz_kolo(a)
        pole += policz_kolo(a)
    #if wynik == 0:
    #   wynik = pole
    #else:
        #wynik = wynik + pole
    #wynik.append((pole).strip())
    #wynik.append(pole)
    #wynik.insert(i, pole)
#elif c == 0:
    elif len(figura) == 2:
        a = float(figura[0])
        b = float(figura[1])
    #def policz_prostokata(a,b):
    #    return a * b
        #pole += '%0.2f' %policz_prostokata(a,b)
        pole += policz_prostokata(a,b)
    #wynik = wynik + pole
    #wynik.append((pole).strip())
    #wynik.append(pole)
    #wynik.insert(i, pole)
    #print(pole)
    elif len(figura) == 3:
        a = float(figura[0])
        b = float(figura[1])
        c = float(figura[2])
        s = ((a + b + c)/2)
    #def policz_trojkata(a,b,c):
     #   return (s*(s-a)*(s-b)*(s-c)) ** 0.5 
    #pole += '%0.2f' %policz_trojkata(a,b,c)
        pole += policz_trojkata(a,b,c)
    #wynik.append((pole).strip())
    #wynik.insert(i, pole)
    #ynik.append(pole)
    else:
        print("Błąd: można podać maksymalnie 3 liczby")
        break
#def zsumuj_liste(wynik):
#    result = 0
#    for x in wynik:
#        result += x
#    return result
#print(zsumuj_liste(wynik))
print(round(pole,2))