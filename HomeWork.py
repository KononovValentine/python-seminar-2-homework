import random
import math


# Домашняя работа к семинару 2, для выбора необходимой программы запустите код и введите номер программы для проверки.


# Задача 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def PorgramOne():
    some_str = input('Введите вещественное число = ')
    sum = 0
    for i in some_str:
        sum = sum + int(i)
    print('Сумма цифр =', sum)
    MainProgram()


# Задача 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def ProgramTwo():
    num = int(input('Введите число = '))
    list = [0] * num
    for i in range(num):
        if i == 0:
            list[i] = 1
        else:
            list[i] = list[i - 1] * (i + 1)
    print(list)
    MainProgram()


# Задача 3 Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

def ProgramThree():
    num = int(input('Введите число = '))
    list = [''] * num
    for i in range(len(list)):
        list[i] = (f'{i + 1} : {round((1 + 1 / (i + 1)) ** (i + 1), 2)}')
    print(list)
    MainProgram()


# Задача 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def ProgramFour():
    num = int(input('Введите число = '))
    listNumbers = [0] * num
    for i in range(num):
        listNumbers[i] = random.randint(-num, num)

    count = int(input('Введите количество элементов которые нужно подсчитать (не меньше 1, '
                      'но не больше общего количества) = '))
    listSelectedNumbers = [None] * count

    while count < 1 or count > num:
        count = int(input('Введите количество элементов которые нужно подсчитать (не меньше 1, '
                          'но не больше общего количества) = '))

    if count <= num:
        doRandomOrInOrder = int(input('Введите 1, чтобы подсчитать произведения элементов по порядку или 2,'
                                      ' чтобы подсчитать и вывести произведение случайных элементов = '))

        while doRandomOrInOrder < 1 or doRandomOrInOrder > 2:
            print(doRandomOrInOrder)
            doRandomOrInOrder = int(input('Введите 1, чтобы подсчитать произведения элементов по порядку или 2,'
                                          ' чтобы подсчитать и вывести произведение случайных элементов = '))

        ## Записывает в файл прямую последовательность индексов от 0 до указанного количества
        if doRandomOrInOrder == 1:
            file = open('file.txt', 'w')
            for i in range(count):
                file.write(f'{i}\n')
                listSelectedNumbers[i] = i
            file.close()

        ## Записывает в файл случайную последовательность индексов от 0 до указанного размера изначального списка
        elif doRandomOrInOrder == 2:
            file = open('file.txt', 'w')
            randomList = list(range(0, num))
            random.shuffle(randomList)
            for i in range(count):
                file.write(f'{randomList[i]}\n')
                listSelectedNumbers[i] = randomList[i]
            file.close()

        ## Открывает файл и подсчитывает произведение элементов из основного списка по списку заданных в файле индексов
        result = 1
        file = open('file.txt', 'r')
        for i in file:
            if i == '':
                break
            result *= listNumbers[int(i)]
        file.close()

    print(f'Изначальный список = {listNumbers}')
    print(f'Список индексов элементов для подсчета = {listSelectedNumbers}')
    print(f'Результат подсчета =  {result}')
    MainProgram()

# Задача 5 Реализуйте алгоритм перемешивания списка.

def ProgramFive():
    list = [1, 2, 3, 4, 5]
    option = int(input('Выберите способ решения (1 через Shuffle, 2 через цикл) = '))
    if option == 1:
        print('Изначальный массив =', list)
        random.shuffle(list)
        print('Итоговый массив =', list)
    elif option == 2:
        resultList = [None] * len(list)
        counter = 0
        while None in resultList:
            randomNumber = int(random.uniform(0, len(list)))
            if resultList[randomNumber] == None:
                resultList[randomNumber] = list[counter]
                counter = counter + 1
        print('Изначальный массив =', list)
        print('Итоговый массив =', resultList)
    MainProgram()


def MainProgram():
    print('Введите номер программы (1-5), либо введите "Q" для выхода.')
    program = input('Программа № = ')
    if program.lower() == 'q':
        print('До свидания!')
    elif program.isdigit():
        if int(program) == 1:
            PorgramOne()
        elif int(program) == 2:
            ProgramTwo()
        elif int(program) == 3:
            ProgramThree()
        elif int(program) == 4:
            ProgramFour()
        elif int(program) == 5:
            ProgramFive()
        else:
            print('Введен некорректный номер, попробуйте еще раз.')
            MainProgram()
    else:
        print('Ввод некорректен, пожалуйста, попробуйте еще раз.')
        MainProgram()


print('Здравствуйте!')
MainProgram()
