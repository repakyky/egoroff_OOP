from functools import wraps

def table(func):

    @wraps(func)
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner

@table
def sqr(x):
    """
    :param x:
    :return x**2:
    """
    print(x**2)

