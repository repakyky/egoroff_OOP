# Делегирование, функция super()

# super().method вызывает метод под названием "method" у родительского класса

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def breathe(self):
        print('Человек дышит')


class Doctor(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def breathe(self):
        print('Доктор дышит')
        super().breathe()       # Человек дышит
