
# Методы:
# __add__ - сложение,     __radd__ - сложение наоборот
# __mul__ - умножение,    __rmul__
# __sub__ - вычитание,    __rsub__
# __truediv__ - деление,  __rtruediv__

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Клиент {self.name} с балансом {self.balance}'

    def __add__(self, other):

        if isinstance(other, BankAccount):
            self.balance += other.balance

        elif isinstance(other, (int, float)):
            self.balance += other

        else:
            raise NotImplemented

        return self.balance

    def __radd__(self, other):
        self += other
        return self


    def __mul__(self, other):
        self.balance *= other
        return self.balance

    def __sub__(self, other):
        self.balance -= other
        return self.balance

    def __truediv__(self, other):
        self.balance /= other
        return self.balance

