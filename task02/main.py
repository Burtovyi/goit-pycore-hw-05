import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор, що знаходить усі дійсні числа у тексті.

    :param text: Вхідний текст
    :return: Генератор чисел
    """

    pattern = r'(?<=\s)-?\d+\.\d+|(?<=\s)-?\d+(?=\s)'
    for match in re.finditer(pattern, f' {text} '):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальну суму чисел у тексті, використовуючи задану функцію генератора.

    :param text: Вхідний текст
    :param func: Функція-генератор чисел
    :return: Сума чисел
    """
    return sum(func(text))


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
