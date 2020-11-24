
# метод __call__

# Вызываемые объекты:
#   1. Встроенные функции: len(), int(), print() и т.д.
#   2. Встроенные методы объектов: a.sort()
#   3. Самописные функции, объявленные через def или lambda
#   4. Классы
#   5. Экземпляр класса, если в нём есть метод __call__
#   6. Методы класса (которые через точку)
#   7. Функции-генераторы

from time import perf_counter

class Counter:

    def __init__(self):
        self.counter = 0
        self.summ = 0
        self.lenght = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summ += sum(args)
        self.lenght += len(args)
        print(f'Экземпляр вызывался {self.counter} раз')

    def average(self):
        return self.summ / self.lenght

class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'called function {self.fn.__name__}')
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'lead time {finish - start}')
        return result

@Timer
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

@Timer
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)