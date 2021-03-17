
# Пользовательские исключения
# Лучше наследоваться от Exception, а не от BaseException,
#   чтобы не залетали специфичные исключения


class MyException(Exception):
    """
    my Exception
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'MyException ({self.message})'
        else:
            return 'MyException is empty'


raise MyException(1, 2, 3)
