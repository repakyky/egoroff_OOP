
# Обработка исключений
# При появлении исключения дальнейшее выполнение блока try не происходит
# exceptoв можно написать сколько угодно
# При этом питон будет искать соответствующий except сверху вниз
# Можно писать except(ValueError, NameError, ...)
# Тип исключения можно вообще не писать, тогда отлавливается вообще всё
# finally выполняется всегда
# else выполняется когда нет исключений
# Можно использовать try-finally

try:
    int('hello')
    1/0
    a + b

except ValueError:
    print('Value Error handled')
except ZeroDivisionError:
    print('ZeroDivisionError handled')
except NameError:
    print('NameError handled')

# _______________________________________________________________________#

s = 'hello'


try:
    s[6]
except IndexError:
    print('IndexError')
except LookupError:
    print('LookupError')
finally:
    print('end')

# _______________________________________________________________________#

f = open('oop35_propagation_exeptions.py')
def execute(file):
    pass

try:
    execute(f)
finally:
    f.close()