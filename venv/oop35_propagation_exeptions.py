
# Распространение исключений
# Короч это и так было видно
# Исключения вызывают весь стек вызовов
# Можно обрабатывать исключения на любом уровне, хоть весь код в try-except завернуть.

def first():
    print('start first')
    second()
    print('finish first')

def second():
    print('start second')
    try:
        1/0
    except ZeroDivisionError:
        print('handled')
    print('finish second')

print('hello')
first()


# Traceback (most recent call last):
#   line 17, in <module>    first()
#   line 8, in first        second()
#   line 13, in second      1/0
#   ZeroDivisionError: division by zero