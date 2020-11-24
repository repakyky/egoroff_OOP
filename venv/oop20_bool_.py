
# Метод __bool__

# bool(object) >>> True / False
# Любое непустое значение преобразуется в True:
# >>> bool(0)
# False
# >>> bool('')
# False
# >>> bool(7)
# True
# >>> bool('azaz')
# True
#
# Если метод __bool__ не объявлен, то функция bool(object) будет смотреть на метод __len__
# Если методы __bool__ и __len__ не объявлены, то любой экземпляр класса будет True

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        return self.x != 0 or self.y != 0

    # def __bool__ должен обязательно возвращать True или False