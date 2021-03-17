
# Инструкция raise
# Вызывает исключение

try:
    [1, 2, 3][0]
except (KeyError, IndexError) as error:
    print(f'Logging error: {repr(error)}')
    raise TypeError from None

try:
    raise ValueError
except ValueError as first:
    try:
        raise IndexError
    except IndexError as second:
        raise Exception from first