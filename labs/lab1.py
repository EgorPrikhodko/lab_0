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
