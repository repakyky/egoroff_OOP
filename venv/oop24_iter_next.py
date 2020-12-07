
# Методы __iter__ и __next__
# Делают экземпляры класса итерируемыми, можно будет проходить в цикле for

class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter

igor = Student('Igor', 'Petrov', [5, 5, 3, 4, 5])

for i in igor:
    print(i)