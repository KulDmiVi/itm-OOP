class SingletonMeta(type):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


class SingletonBaseMeta(metaclass=SingletonMeta):
    pass


class A(SingletonBaseMeta):
    pass


class B(SingletonBaseMeta):
    pass


class Order:
    def __init__(self, price, num):
        self.price = price
        self.num = num

    # def __getattribute__(self, attrname):
    #     try:
    #         return object.__getattribute__(self, attrname)
    #     except AttributeError:
    #         print("НЕТ такого")

    def __getattr__(self, attrname):
        if attrname == "total":
            return self.price * self.num
        else:
            raise AttributeError


def counter():
    i = 3
    while i <= 10:
        yield i
        if i < 5:
            i += 1.5
        else:
            i += 0.5


for z in counter():
    print(z)

order = Order(10, 15)
print(order.num)
print(order.total)

print(A())
print(A())
print(B())
