message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    from math import sqrt
    return sqrt(number)


def calc(your_number):
    """Главная функция."""
    if your_number <= 0:
        return
    number = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {number}')


print(message)
calc(25.5)
