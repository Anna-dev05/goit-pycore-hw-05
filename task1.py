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
    print(fib(10))  
    print(fib(15)) 


