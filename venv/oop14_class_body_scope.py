# Тут про области видимости

class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV, self.__class__.__name__)

    def info2(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV, DepartmentIT.__name__)

    @property
    def info_prop(self):
        print(self.PYTHON_DEV,self.GO_DEV, self.REACT_DEV)

    @classmethod
    def info_class(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    @staticmethod
    def info_static():
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    def hiring_python_dev(self):
        DepartmentIT.PYTHON_DEV += 1

it1 = DepartmentIT()

it1.info()
it1.info2()
it1.info_prop
it1.info_class()
it1.info_static()
it1.hiring_python_dev()
print(DepartmentIT.PYTHON_DEV)