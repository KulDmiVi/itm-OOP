class MeansOfTransport:
    def __init__(self, color: str, brand: str):
        self.__color = color
        self.__brand = brand
        self.car_drive = 4

    def show_color(self):
        return self.__color

    def show_brand(self):
        return self.__brand

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if isinstance(color, str):
            self.__color = color
        else:
            print("Цвет не установлен, введите строку")

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self.__brand = brand
        else:
            print("Марка не установлена, введите строку")


class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, color: str, brand: str, wheel_count=4):
        self.__color = color
        self.__brand = brand
        self.__wheel_count = wheel_count
        self.show_car_drive()

    @classmethod
    def show_car_drive(cls):
        print(cls.car_drive)


class Moped(MeansOfTransport):
    def __init__(self, color: str, brand: str, wheel_count=2):
        self.__color = color
        self.__brand = brand
        self.__wheel_count = wheel_count
        self.public_var = "public"
        self._protected_var = "protected"
        self.__private_var = "private"

    @staticmethod
    def min_arrival_time(speed: float, length: float):
        return round(length / speed, 1)


if __name__ == "__main__":
    first_car = MeansOfTransport('blue', 'volvo')
    print(first_car.show_color(), first_car.show_brand())
    first_car.color = 5
    first_car.color = 'black'

    first_car.brand = 1.3
    first_car.brand = 'lada'
    print(first_car.color, first_car.brand)

    second_car = Car('ornage', 'kamaz', 6)
    first_moped = Moped('green', 'karpatii')
    print(first_moped.public_var)
    print(first_moped._protected_var)

    try:
        print(first_moped.__private_var)
    except AttributeError as e:
        print(f"Ошбка доступа к пртиватным атрибутам\n {e}")
