from math import pi
#a, b, c = [int(a) for a in input().split()]
#a, b, c = input()
s = float
pole = float
inputs = []
for i in range(3):
    inputs.append(input())
a = inputs[0]
b = inputs[1]
c = inputs[2]
if b == 0 and c == 0:
    def policz_kolo(a):
        return pi * a * a
    pole = '%0.2f' %policz_kolo(a)
    print(pole)
elif c == 0:
    def policz_prostokata(a,b):
        return a * b
    pole = '%0.2f' %policz_prostokata(a,b)
    print(pole)
elif a != 0 and b != 0 and c != 0:
    s = (a + b + c) / 2
    def policz_trojkata(a,b,c):
        #if a > b and a > c:
         #   return (1/2)*b*c
        #elif b > a and b > c:
         #   return (1/2)*a*c
        #elif c > a and c > b:
          #  return (1/2)*a*b 
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5 
    pole = '%0.2f' %policz_trojkata(a,b,c)
    print(pole)
else:
    print("Błąd: można podać maksymalnie 3 liczby")
#print(pole)