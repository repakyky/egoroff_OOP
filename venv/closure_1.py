# Замыкания

def main_func(name):
    def inner_func():
        print('hello', name)
    return inner_func

a = main_func('Misha')
b = main_func('Vasya')
    # У каждой переменной теперь своя область видимости
a()
b()

# def second_func(name):
#     print('Hello, ', name)
#
# c = second_func('Kolya')
# d = second_func('Petya')
#
# c()
# d()

def counter():
    count = 0
    def inner_func():
        nonlocal count
        count += 1
        return count

    return inner_func

q_1 = counter()
q_2 = counter()
q_3 = counter()
q_4 = counter()

q_1()
q_2()
q_3()
q_4()