
# Множественное наследование
# Можно наследоваться от нескольких классов.
# Дочерний сначала ищет методы в первом родительском, потом во втором и т.д.
# Порядок поиска методов можно посмотреть при помощи метода __mro__

class Doctor:

    def __init__(self, degree):
        self.degree = degree


class Builder:

    def __init__(self, rank):
        self.rank = rank


class Person(Doctor, Builder):
    def __init__(self, degree, rank):
        # super(Person, self).__init__(degree)
        super().__init__(degree)
        Builder.__init__(self, rank)

    def __str__(self):
        return f'Person {self.degree} {self.rank}'


print(Person.__mro__)
p = Person('spec', 5)
print(p)
