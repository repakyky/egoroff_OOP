class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if not isinstance(new_balance, (int, float)):
            raise ValueError('incorrect data')
        self.__balance = new_balance
        return self.__balance

    balance = property(fget=get_balance, fset=set_balance)