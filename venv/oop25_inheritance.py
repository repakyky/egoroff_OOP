# Наследование!

# Классам Doctor и Architect доступны все методы родительского класса Person: can_walk, can_breathe
# При этом Doctor наследует и расширяет функционал родительского класса методом can_heal
# А класс Ortoped в свою очередь наследует и расширяет классы Doctor и Person

# Parent:
class Person:

    def can_walk(self):
        print(f'{self.__class__} \t Я могу ходить')

    def can_breathe(self):
        print(f'{self.__class__} \t Я могу дышать')


# Subclass:
class Doctor(Person):

    def can_heal(self):
        print(f'{self.__class__} \t Я могу лечить')


class Ortoped(Doctor):
    def can_heal_fractures(self):
        print(f'{self.__class__} \t Я могу лечить переломы')


# Subclass:
class Architect(Person):

    def can_build(self):
        print(f'{self.__class__} \t Я могу строить')


d = Doctor()
a = Architect()
o = Ortoped()

d.can_heal()
a.can_build()
d.can_walk()
d.can_breathe()
a.can_walk()
a.can_breathe()
o.can_heal_fractures()

print(issubclass(Doctor, Person))
print(isinstance(a, Person))
