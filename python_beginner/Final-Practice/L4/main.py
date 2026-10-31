def factorial(num: int) -> int:
    factorial: int = 1
    for i in range(num, 0, -1):
        factorial *= i
    return factorial
