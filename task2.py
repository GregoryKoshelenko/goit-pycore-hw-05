import re
from typing import Callable


def generator_numbers(text: str):
    # Дійсні числа в тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків
    pattern = r'\s+(\d+\.\d+)\s+' 
    for match in re.finditer(pattern, text):
        yield float(match.group(1))


def sum_profit(text: str, func: Callable):
    return sum(func(text))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, "
        "доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
