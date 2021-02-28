# slots
# Можно ограничить создание атрибутов и методов
# В таком случае экземпляры будут хранить только заданные аттрибуты и методы
# Так же при использовании slots экземпляры занимают меньше памяти,
# так как у них теперь нет __dict__.
# Так же при использованиии slots операции над объектами выполняются быстрее
#
from timeit import timeit

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_cls_point():
    a = Point(1, 1)
    a.x = 100
    del a.x


def make_cls_pointslots():
    a = PointSlots(1, 1)
    a.x = 100
    del a.x

a = Point(1, 1)
b = PointSlots(1, 1)
print(a.__sizeof__() + a.__dict__.__sizeof__())
print(b.__sizeof__())

print(timeit(make_cls_point))
print(timeit(make_cls_pointslots))