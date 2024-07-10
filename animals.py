from abc import ABC, abstractmethod


class Animals(ABC):
    @abstractmethod
    def voice(self): pass


class Cat(Animals):
    __SOUND = 'meow'

    def __init__(self, name):
        self.__name = name

    @classmethod
    def voice(cls):
        print(cls.__SOUND)


if __name__ == "__main__":
    Cat.voice()
