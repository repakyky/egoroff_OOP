
# __eq__, __hash__ и как они связаны
# hash считается от айдишника, после определения eq надо переопределять и hash
# hash можно найти только у неизменяемых объектов (строки, числа и т.д.)
# например, если мы хотим использовать объекты как ключи в словаре - нужен хеш

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) \
               and self.x == other.x \
               and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    # Получается, у двух экземпляров с одинаковыми x, y будет одинаковый hash