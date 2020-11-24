# Практика по property
from string import digits

class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    # PASSWORD

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('пароль должен быть строкой')
        if len(value) < 4:
            raise ValueError('Слишком короткий пароль')
        if len(value) > 12:
            raise ValueError('Слишком длинный пароль')
        if not self.is_include_number(value):
            raise ValueError('пароль должен содержать хотя бы одну цифру')
        self.__password = value

    # LOGIN

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__login = value

    # TECHNIC FUNC
    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False