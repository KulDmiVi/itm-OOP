class Dog:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Dog, cls).__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


if __name__ == "__main__":
    my_dog = Dog("spotty")
    my_dog.get_name()
    my_dog2 = Dog("tim")
    my_dog.get_name()
    my_dog2.get_name()
