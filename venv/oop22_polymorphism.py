
# Полиморфизм
# Короче это такой принцип написания кода.
# Для трёх разных классов мы написали методы подсчёта площади, которые при этом работают по-разному
# (Для прямоугольника, квадрата и круга)
# При этом названия методов одинаковые - вместо:
# - get_rectangle_area;
# - get_square_area;
# - get_circle_area;
# Везде используется get_area,
# что позволяет в соседнем файле oop22_polymorphism_example.py использовать цикл for без дополнительных условий
#
# Аналогично если мы умножаем число на число, получаем произведение:
# 5 * 3 >>> 15
# А если число на строку:
# 5 * 'a' >>> 'aaaaa'
# Хотя в обоих случаях используется один и тот же оператор '*', функционал различается
# в зависимости от того, к объектам какого класса он применяется

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle {self.a} x {self.b}'

    def get_area(self):
        return self.a * self.b

class Square:

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Square {self.a} x {self.a}'

    def get_area(self):
        return self.a ** 2

class Circle:

    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Circle rad = {self.r}'

    def get_area(self):
        return 3.14 * self.r ** 2