
def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner

def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner

@header # say = header(say)
@table  # say = header(table(say))
def say(name, surname):
    print("hello,", name, surname)


say('Vasya', 'Pupkin')