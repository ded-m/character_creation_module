from math import sqrt

MESSAGE = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number: float) -> None:
    """Проверяет число на корректность, печатает результат"""
    if your_number <= 0:
        return
    square_root = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {square_root}')


print(MESSAGE)
calc(25.5)
