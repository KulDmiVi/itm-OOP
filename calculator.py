class Calculator:
    @staticmethod
    def calculate_sum(a: float, b: float)->float:
        if isinstance(a, (float, int)) and isinstance(b, (float, int)):
            return a+b
        else:
            raise TypeError


class StrCalculator(Calculator):
    @staticmethod
    def calculate_sum(a: str, b: str) -> str:
        if isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            raise TypeError


if __name__ == "__main__":

    try:
        print(Calculator.calculate_sum('qwe', 'qwe'))
    except TypeError:
        print("Не являются числом")

    try:
        print(StrCalculator.calculate_sum('qwe', 'qwe'))
    except TypeError:
        print("Не являются строками")
