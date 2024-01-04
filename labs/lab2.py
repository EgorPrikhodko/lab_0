def task1():
    def f1(x):
        '''Проверяет четность последней цифры'''
        return (x % 10) % 2 == 0

    def f2(x):
        """Проверка деления на 5"""
        return (x % 5) == 0

    while True:
        while True:
            try:
                x = int(input("x: "))
                break
            except ValueError:
                print("Введите чиcло")

        if f1(x):
            print("Последняя цифра четная")
        else:
            print("Последняя цифра нечетная")

        if f2(x):
            print("Нацело делится на 5")
        else:
            print("Нацело не делится на 5")

task1()

import numpy as np
import matplotlib.pyplot as pl
def task2():
    def f1(x):
        return np.sin(x)*np.cos(x)
    def f2(x):
        return 2*x**2+x
    a = (int(input("a: ")))
    b = (int(input("b: ")))
    x = np.linspace(a, b, 200)
    y = []
    for elem in x:
        if elem >= 0:
            y.append(f1(elem))
        else:
            y.append(f2(elem))
    pl.plot(x,y)
    pl.grid()
    pl.show()

task2()

def task4():
    try:
        a = int(input("Введите первое число: "))
    except ValueError:
        a = int(input("Введите первое ЧИСЛО: "))
    try:
        b = int(input("Введите второе число: "))
    except ValueError:
        b = int(input("Введите второе ЧИСЛО: "))
    try:
        c = int(input("Введите третье число: "))
    except ValueError:
        c = int(input("Введите третье ЧИСЛО: "))

    a1 = abs(a) % 10
    b1 = abs(b) % 10
    c1 = abs(c) % 10

    sum = a1+b1+c1

    if sum % 2 == 0:
        sum1 = abs(sum)%10
        if sum1 % 2 == 0:
            print("Число четное")
        else:
            print("Число нечетное")
    else:
        print("Сумма нечетная")

task4()
