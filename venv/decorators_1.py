def decorator(func):

    def inner(*args, **kwargs):
        print('start decorator...')
        func(*args, **kwargs)
        print('...finish decorator')

    return inner

def say(name):
    print('hello ', name)

def bye():
    print('bye world')

say = decorator(say)
bye = decorator(bye)

say('was')
bye()