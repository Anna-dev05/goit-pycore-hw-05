
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
            continue  

def sum_profit(text: str, func: Callable[[str], Iterator[Decimal]]) -> Decimal:

    return sum(func(text), Decimal("0"))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")  