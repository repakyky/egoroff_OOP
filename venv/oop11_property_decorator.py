class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property   # Это получился геттер
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, balance=0):
        if not isinstance(balance, (int, float)):
            raise ValueError('incorrect value')
        self.__balance = balance
        return balance

    @my_balance.deleter
    def my_balance(self):
        del self.__balance
