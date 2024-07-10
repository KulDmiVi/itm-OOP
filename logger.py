

class MyClass:
    def __init__(self, attr1, attr2, attr3):
        self.__attr1 = attr1
        self.__attr2 = attr2
        self.__attr3 = attr3

    @property
    def attr1(self):
        return self.__attr1

    @attr1.setter
    def attr1(self, new_value):
        print(f"change attribute {self.__attr1} -> {new_value}")
        self.__attr1 = new_value

    @property
    def attr2(self):
        return self.__attr2

    @attr2.setter
    def attr2(self, new_value):
        print(f"change attribute {self.__attr2} -> {new_value}")
        self.__attr2 = new_value

    @property
    def attr3(self):
        return self.__attr3

    @attr3.setter
    def attr3(self, new_value):
        print(f"change attribute {self.__attr3} -> {new_value}")
        self.__attr3 = new_value

if __name__ == "__main__":
    test = MyClass(1, 2, 3)
    test.attr1 = 4