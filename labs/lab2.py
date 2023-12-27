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
