from abc import ABC, abstractmethod


class IAppend(ABC):
    @abstractmethod
    def append_item(self, item):
        pass


class Person:
    def __init__(self, last_name, first_name, patr_name):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name


class Persons(IAppend):
    def __init__(self, person_list):
        self.__persons = person_list

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.__persons):
            self.index += 1
            return self.__persons[self.index - 1].first_name
        else:
            raise StopIteration

    def append_item(self, item):
        self.__persons.append(item)


if __name__ == "__main__":
    temp = [Person("Иванов", "Иван", "Иванович"), Person("Иванов", "Петр", "Иванович")]
    test_persons = Persons(temp)
    for i in test_persons:
        print(i)
    test_persons.append_item(Person("Иванов", "Сергей", "Иванович"))
    for i in test_persons:
        print(i)
