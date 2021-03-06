
# Наследование от базового класса object
# Всё - объект: 34, 'asdasd', int, Person. Можно проверить через isinstance(something, object)
# По-умолчанию любой класс наследуется от object

class Person:   # == Person(object):
    pass


class Mylist(list):    # Можно наследоваться от любого встроенного класса
    pass



# >>> dir(object) -- аттрибуты класса object
#
# __class__   ............. определяет класс или тип, экзмепляром которого является объект
# __delattr__   ........... поведение экземпляра при воздействии на него инструкцией del.
# __dir__   ............... что вернёт экземпляр класса когда его вызвали через dir()
# __doc__   ............... документ-строка, отсюда же берётся help()
# __eq__   ................ equal - поведение при сравнении (a == b)
# __format__   ............ Позволяет определить представление объекта при запросе его отформатированного представления,
#                           хз что это значит
# __ge__   ................ greater equal - поведение при нестрогом сравнении (больше или равно) (a >= b)
# __getattribute__   ...... https://tirinox.ru/getattribute/ - вот тут нормально написано, вроде это геттер но не совсем
# __gt__   ................ greater than - поведение при строгом сравнении (a > b)
# __hash__   .............. каким образом вычисляется hash
# __init__   .............. специальный метод, который автоматически вызывается, когда создается объект
# __init_subclass__   ..... автоматически вызывается, когда происходит наследование от класса, в котором
#                           данный метод определён. По умолчанию не делает ничего. Однако поднимает TypeError,
#                           если ей переданы аргументы.
# __le__   ................ less equal - меньше или равно (a <= b)
# __lt__   ................ less than - строго меньше (a < b)
# __ne__   ................ not equal - не равно (a != b)
# __new__   ............... http://python-3.ru/page/gibkoe-sozdanie-obektov-v-python-s-pomoshhju-metoda-__new__
#                           выделяет память под «пустой» объект и вызывает __init__, чтобы его инициализировать
# __reduce__   ............ Обеспечивает сериализацию объекта для pickle, не знаю что это
# __reduce_ex__   ......... Обеспечивает сериализацию с указанием версии протокола (((
# __repr__   .............. как увидят объект другие разрабы (как он отбражается в консоли в списке объектов)
# __setattr__   ........... сеттер, поведение при присвоении значения атрибуту (a.my_attr = 1)
# __sizeof__   ............ является частью Python C API. Возвращает размер объекта в байтах,
#                           переопределение в пользовательских классах не имеет смысла
# __str__   ............... как увидят объект пользователи, если применить к нему str() или print()
# __subclasshook__   ...... http://www.rupython.com/python-subclasscheck-subclasshook-40491.html