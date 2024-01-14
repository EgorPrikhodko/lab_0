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

def task2():
    import numpy as np
    import matplotlib.pyplot as pl
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

def task3():
    def toBASEint(num, base):
        alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = abs(num)
        b = alpha[n % base]
        while n >= base:
            n = n // base
            b += alpha[n % base]
        return ('' if num >= 0 else '-') + b[::-1]

    def toBaseFrac(frac, base, n=16):
        alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b = ''
        while n:
            frac *= base
            frac = round(frac, n)
            b += str(alpha[int(frac)])
            frac -= int(frac)
            n -= 1
        return b

    Number = input("Число: ")
    Basein = 10
    Baseout = int(input("Введите СС: "))
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if '.' in Number:
        num, frac = map(str, Number.split('.'))
        num = int(num, Basein)
        a = toBASEint(num, Baseout)
        b = 0
        k = Basein
        for i in frac:
            b += alpha.index(i) / k
            k *= Basein
        b = str(toBaseFrac(b, Baseout)).rstrip('0')
        print("Итог: ",a + '.' + b)
    else:
        print("Итог: ",toBASEint(int(Number, Basein), Baseout))

task3()

def task4():
    import matplotlib.pyplot as plt
    import numpy as np

    def is_point_inside_figure(x, y, point_x, point_y):
        n = len(x)
        inside = False

        for i in range(n):
            j = (i + 1) % n
            if ((y[i] > point_y) != (y[j] > point_y)) and \
                    (point_x < (x[j] - x[i]) * (point_y - y[i]) / (y[j] - y[i]) + x[i]):
                inside = not inside

        if inside:
            return "Точка находится внутри фигуры"
        else:
            return "Точка не находится внутри фигуры"

    x_coordinates_shape1 = [-7, 1, 0, -4, -2, -6, 5]
    y_coordinates_shape1 = [7, 4, -1, 0, -6, -4, 2]

    x_coordinates_shape2 = [1, -1, 1, 3, 5, 7, 6, 3]
    y_coordinates_shape2 = [-7, -4, -2, -1, 2, 4, -1, -4]

    test_point_x = float(input("Введите координату X контрольной точки: "))
    test_point_y = float(input("Введите координату Y контрольной точки: "))

    # Построение обеих фигур и заданной пользователем контрольной точки
    plt.plot(x_coordinates_shape1 + [x_coordinates_shape1[0]], y_coordinates_shape1 + [y_coordinates_shape1[0]],
             marker='o', linestyle='-', label='Фигура 1')
    plt.plot(x_coordinates_shape2 + [x_coordinates_shape2[0]], y_coordinates_shape2 + [y_coordinates_shape2[0]],
             marker='o', linestyle='-', label='Фигура 2')
    plt.scatter(test_point_x, test_point_y, color='red', label='Заданная точка')

    # Выделяет выпуклую оболочку каждой фигуры.
    plt.fill(x_coordinates_shape1 + [x_coordinates_shape1[0]], y_coordinates_shape1 + [y_coordinates_shape1[0]],
             alpha=0.2)
    plt.fill(x_coordinates_shape2 + [x_coordinates_shape2[0]], y_coordinates_shape2 + [y_coordinates_shape2[0]],
             alpha=0.2)

    plt.xlabel('X-ось')
    plt.ylabel('Y-ось')
    plt.title('Фигуры с заданной пользователем точкой')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Проверяет, находится ли заданная пользователем контрольная точка внутри какой-либо из фигур.
    result_shape1 = is_point_inside_figure(x_coordinates_shape1, y_coordinates_shape1, test_point_x, test_point_y)
    result_shape2 = is_point_inside_figure(x_coordinates_shape2, y_coordinates_shape2, test_point_x, test_point_y)

    print(result_shape1)
    print(result_shape2)

task4()

def task5():
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

task5()

def task6():
    try:
        a = int(input("Введите количество бактерий:"))
    except ValueError:
        a = int(input("Введите число:"))
    try:
        b = int(input("Введите время деления: "))
    except ValueError:
        b = int(input("Введите число: "))

    a1 = a

    for i in range(1,b):
        a2 = a1*2
        print("Количество бактерий: ",a2)
        a1 = a2

task6()

def task8():
    from math import factorial

    try:
        n = int(input("Введите длину последовательности: "))
    except ValueError:
        n = int(input("Введите число: "))
    try:
        x = int(input("Введите x: "))
    except ValueError:
        x = int(input("Введите число: "))
        
    subcount = 0
    s = 0

    for count in range(1, n + 1):
        s += (factorial(count-1)/factorial(subcount+count))*(x**subcount+count)
        subcount += 1
    print(f"Cумма последовательности при x = {x} и длине {n} равна {s}")

task8()

