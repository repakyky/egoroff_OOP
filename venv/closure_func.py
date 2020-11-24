def add(a, b):
    return a+b

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывалась {count} раз')
        return func(*args, **kwargs)
    return inner

# >>> a = counter(add)
# >>> a(10, 20)
#  функция add вызывалась 1 раз
#  30
# >>> a(1, 2)
#  функция add вызывалась 2 раз
#  3