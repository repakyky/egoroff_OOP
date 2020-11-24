
class Example:

    @staticmethod
    def static_hello():
        print('static hello')

# >>> Example.static_hello()
# static hello
# >>> a = Example()
# >>> a.static_hello()
# static hello

    @classmethod
    def class_hello(cls):
        print(f'class hello {cls}')

# >>> Example.class_hello()
# class hello <class '__main__.Example'>
# >>> a = Example()
# >>> a.class_hello()
# class hello <class '__main__.Example'>