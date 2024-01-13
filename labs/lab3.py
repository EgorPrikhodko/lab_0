def print_char_list(array):
    for char in array:
        print(char, end=' ')

def proverka1(array, symbol):
    if symbol in array:
        print(f'Символ "{symbol}" входит в последовательность "{"".join(array)}".')

def proverka2(array, first_symbol, second_symbol):
    pairs_count = sum(1 for i in range(len(array)-1) if array[i] == first_symbol and array[i+1] == second_symbol)
    print(f'Количество пар соседних символов "{first_symbol}{second_symbol}" в: {pairs_count}.')

def proverka3(array):
    identical_pairs_count = sum(1 for i in range(len(array)-1) if array[i] == array[i+1])
    print(f'Число соседних одинаковых пар символов равно: {identical_pairs_count}.')

def proverka4(array):
    for i in range(1, len(array)-1):
        if array[i-1] == array[i+1]:
            print(f'В позициях есть соседние символы {i-1} и {i+1} в последовательности.')
            return
    print('Не найдено соседних символов с одинаковыми соседями..')

def proverka5(array):
    spaces_count = array.count(' ')
    print(f'Количество пробелов в последовательности равно: {spaces_count}.')

def task1():
    n = int(input('Введите длину последовательности: '))
    char_array = []
    for _ in range(n):
        char = input('Введите символ: ')
        char_array.append(char)

    print_char_list(char_array)
    print()  # To add a newline

    symbol = input('Введите символ для proverka1: ')
    proverka1(char_array, symbol)

    first_symbol = input('Введите первый символ для proverka2: ')
    second_symbol = input('Введите второй символ для proverka2: ')
    proverka2(char_array, first_symbol, second_symbol)

    proverka3(char_array)
    proverka4(char_array)
    proverka5(char_array)

task1()

def task3():
    with open("output.txt", "w") as file:
        for _ in range(5):
            user_input = input("Введите текст: ")
            file.write(user_input + '\n')
    print("Задача выполнена. Проверьте 'output.txt' на наличие письменного текста.")

task3()

import random

def print_string_list(array):
    for element in array:
        print(element)

def random_choice(array):
    return random.choice(array)

def task4():
    words_array = [
        "Python", "JavaScript", "GitHub", "Machine Learning",
        "Social Media", "Artificial Intelligence", "Web Development",
        "Data Science", "Open Source", "Programming"
    ]

    print_string_list(words_array)

    input("Чтобы получить случайный элемент массива, нажмите Enter:")

    random_element = random_choice(words_array)
    print(f"Случайный элемент: {random_element}")

    input("Нажмите Enter для выхода из программы.")

task4()

def task5():
    user_input = input("Введите текст: ")

    with open("task1.out", "w") as file:
        file.write(user_input)

    print(f"Текст, записанный в 'task1.out': {user_input}")

task5()
