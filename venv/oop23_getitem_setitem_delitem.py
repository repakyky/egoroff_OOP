
#               >>> v = Vector(1, 2, 3)
#
# __getitem__:  >>> v[0]
#               1
# __setitem__:  >>> v[4] = 5
#               [1, 2, 3, 0, 5]
# __delitem__:  >>> del v[4]
#               [1, 2, 3, 0]

# Короче это методы для работы с классом как с коллекцией


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def check_value(self, key):
        if isinstance(key, int):
            if 0 <= key < len(self.values):
                return 2
            elif 0 < key:
                return 1
            else:
                raise IndexError('Индекс за границами коллекции')
        else:
            raise TypeError('Индекс должен быть числом')

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, key):
        if self.check_value(key) == 2:
            return self.values[key]

    def __setitem__(self, key, value):
        if self.check_value(key) == 2:
            self.values[key] = value
        elif self.check_value(key) == 1:
            diff = key - len(self.values) + 1
            self.values.extend([0]*diff)
            self.values[key] = value

    def __delitem__(self, key):
        if self.check_value(key) == 2:
            del self.values[key]
