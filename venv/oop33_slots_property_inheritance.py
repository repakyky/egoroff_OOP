# Slots свойства и наследование
# У дочерних классов есть __dict__, slots уже как бы нету, но как бы есть
# Короч чтобы работало как надо, необходимо расширить slots в дочернем классе
# Если вдруг расширять род. класс не нужно, то __slots__ = tuple() - пустой кортеж

class Rectangle:
    __slots__ = ('__height', 'wight')

    def __init__(self, a, b):
        self.height = a  # Здесь вызывается @height.setter
        self.wight = b

    @property
    def perimeter(self):
        return (self.wight + self.height) * 2

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        print('height.setter called')
        self.__height = value


class Square(Rectangle):
    __slots__ = 'colour'

    def __init__(self, a, colour):
        super().__init__(a, b=a)  # Инициализируем a через родительский класс

        self.colour = colour
