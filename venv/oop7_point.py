from math import sqrt
class Point:

    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.movie_to(coord_x, coord_y)
        Point.list_points.append(self)

    def movie_to(self, new_x=0, new_y=0):
        if not (isinstance(new_x, (int, float)) and isinstance(new_y, (int, float))):
            raise ValueError('coords is not a int or float')
        self.x = new_x
        self.y = new_y
        self.print_point()

    def go_home(self):
        self.movie_to()

    def print_point(self):
        print(f'coords: {self.x}, {self.y}')

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError(f'\'{another_point}\' is not point!')
        distance = sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)
        print(distance)

def check_point():
    try:
        a = Point()
        print("1 OK")
    except:
        print("1 FALSE")
    try:
        b = Point(15, 32)
        print("2 OK")
    except:
        print("2 FALSE")
    try:
        c = Point(28.359, 21.154)
        print("3 OK")
    except:
        print("3 FALSE")
    try:
        d = Point(15, 'ddd')
        print('4 FALSE')
    except:
        print("4 OK")
    try:
        e = Point('2', 'sss')
        print('5 FALSE')
    except:
        print('5 OK')
    try:
        a.calc_distance(b)
        print("6 OK")
    except:
        print("6 FALSE")
    try:
        a.calc_distance(14)
        print("7 FALSE")
    except:
        print("7 OK")
    try:
        a.calc_distance(d)
        print("8 FALSE")
    except:
        print("8 OK")
    print("end test")

check_point()