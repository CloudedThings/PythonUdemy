
def division(x: int, y: int):
    try:
        print(x / y)
    except TypeError:
        print("You need to provide two integers")


def userInput():
    while True:
        try:
            x = int(input("Type the number: "))
            return x
        except ValueError:
            print("You need to provide an integer")


if __name__ == '__main__':
    x = userInput()
    y = userInput()
    division(x, y)
