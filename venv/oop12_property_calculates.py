from math import sqrt

class Square:
    def __init__(self, side=None, area=None, perimeter=None):
        if side != None:
            self.__side = side
            self.__area = None
            self.__perimeter = None

        elif area != None:
            self.__area = area
            self.__side = sqrt(self.__area)
            self.__perimeter = None

        else:
            self.__perimeter = perimeter
            self.__side = self.__perimeter/4
            self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None
        self.__perimeter = None

    @property
    def area(self):
        if self.__area == None:
            self.__area = self.__side**2
        return self.__area

    @area.setter
    def area(self, value):
        self.__side = sqrt(value)
        self.__area = value

    @property
    def perimeter(self):
        if self.__perimeter == None:
            self.__perimeter = self.__side*4
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__side = value/4
        self.__perimeter = value