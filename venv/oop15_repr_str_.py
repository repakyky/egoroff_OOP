# методы
# __str__ - как увидят объект пользователи, если применить к нему str или print
# и __repr__ - как увидят объект другие разрабы (как он отбражается в консоли в списке объектов)

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"The object Lion - {self.name}"

    def __str__(self):
        return f"Lion - {self.name}"