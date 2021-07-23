def factorial(i: int) -> int:
    """
    Calculate factorial of provided number
    :param i: proviaded integer
    :return: factorial of argument
    """
    if i == 0:
        return 1
    else:
        return i * (factorial(i - 1))


# for i in range(0, 900):
#     print(factorial(i))

try:
    print(factorial(908))
except RecursionError:
    print("THIS PROGRAM CANNOT CALCULATE FACTORIAL THAT LARGE")

print("Program terminating...")
