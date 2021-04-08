from functools import lru_cache


@lru_cache
def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


print(fib(100))
