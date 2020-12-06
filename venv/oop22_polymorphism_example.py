from oop22_polymorphism import Rectangle, Square, Circle

rectangle_1 = Rectangle(3, 4)
rectangle_2 = Rectangle(12, 5)

sqre_1 = Square(5)
sqre_2 = Square(7)

circle_1 = Circle(5)
circle_2 = Circle(2)

figures = [rectangle_1, rectangle_2, sqre_1, sqre_2, circle_1, circle_2]

for figure in figures:
    print(figure, 'area =', figure.get_area())