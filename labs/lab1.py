import math
def task1():
  x = float(input("x: "))
  y = float(input("y: "))
  z = float(input("z: "))
  
  a = (math.sqrt(abs(x**0.5)))-(math.sinh(y))/(1 + math.log(x) - math.cosh(y))
  b = 2*math.sin(x) + (math.sqrt(1 + math.log(z)))
  
  print(a,b)


task1()

def task2():
  b = -1
  c = 2
  
  x = float(input("x: "))
  
  f = ((c*(x**3)+x)/(b*(x**2)))+((x**2)**(1/3))
  
  print(f)


task2()

def task3():
    x = float(input("x: "))
  
    f = ((abs(math.log((math.cosh(x**2)), 3)))/(math.sinh((x**2)+(x**1/2))))
  
    print(f)


task3()

def task4():
    m = float(input("Длина образующей: "))
    R = float(input("Длина радиуса: "))
    r = float(input("радиус: "))
  
    h = (m**2-(R-r))**1/2
  
    print("Длина высоты: ",h)
  

task4()

def task5():
    m1 = float(input("Масса 1 тележки: "))
    u1 = float(input("Скорость 1 тележки:"))
    m2 = float(input("Масса 2 тележки:"))
    u2 = float(input("Скорость 2 тележки:"))
  
    f = m1*u1+m2*u2
  
    print(f)


task5()

def task7():
    a = float(input("-10 =< A =< 10 and A != 0: "))
    b = float(input("-10 =< B =< 10: "))
    c = float(input("-10 =< C =< 10: "))

    d = b ** 2 - 4 * a * c
    x1 = (-b + d / 2) / (2 * a)
    x2 = (-b - d / 2) / (2 * a)

    f = a * x1 ** 2 + b * x1 + c == 0
    f = a * x2 ** 2 + b * x2 + c == 0

    print("x1 = ", (max(x1, x2)))
    print("x2 = ", (min(x1, x2)))


task7()

