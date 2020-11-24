# abs - модуль

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)


class Segment:
    def __init__(self, point_1, point_2):
        self.x_1 = point_1
        self.x_2 = point_2

    def __abs__(self):
        return abs(self.x_2 - self.x_1)

    def __len__(self):
        return abs(self)
