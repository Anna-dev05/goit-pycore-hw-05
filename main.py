def caching_fibonacci():
    cache: dict[int, int] = {0: 0, 1: 1}

    def fibonacci(n: int) -> int:
        if not isinstance(n, int):
            raise TypeError("n має бути цілим числом")
        if n < 0:
            raise ValueError("n має бути невід'ємним")
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))  # 55
    print(fib(15))  # 610


#Task2
import re
from decimal import Decimal, InvalidOperation, getcontext
from typing import Callable, Iterator

getcontext().prec = 28

def generator_numbers(text: str) -> Iterator[Decimal]:

    pattern = r'(?<=\s)(\d+(?:\.\d+)?)(?=\s)'
    for m in re.finditer(pattern, f" {text} "):  
        try:
            yield Decimal(m.group(1))
        except InvalidOperation:
            continue  # на випадок неочікуваних форматів

def sum_profit(text: str, func: Callable[[str], Iterator[Decimal]]) -> Decimal:

    return sum(func(text), Decimal("0"))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")  # Очікувано: 1351.46
