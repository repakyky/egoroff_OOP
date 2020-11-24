class BankAccount:
    def __init__(self, name, balance, passport):
        self.name = name            # publick
        self._balance = balance     # protected
        self.__passport = passport  # private

    def print_data(self):
        print(self.name, self._balance, self.__passport)

    def __private_method(self):
        pass

account_1 = BankAccount('Bob', 100000, 4608117605)

account_1.print_data()
print(account_1.name)           # publick
print(account_1._balance)       # protected
print(account_1.__passport)     # private