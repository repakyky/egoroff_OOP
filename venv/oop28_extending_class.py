
# extending - добавление новых методов в дочерний класс
# overriding - переопределение существующих методов в дочернем классе

class Person:

    def combo(self):

        if hasattr(self, 'walk') and hasattr(self, 'sleep'):
            self.walk()
            self.sleep()


class Doctor(Person):

    def sleep(self):
        print('Доктор спит')

    def walk(self):
        print('Доктор идёт')


d = Doctor()
d.combo()

p = Person()
p.combo()