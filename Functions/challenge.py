LOW = 1
HIGH = 100


def fizz_buzz(i: int) -> str:
    """
    Return `string` with proper answer depending on modulo

    :param i: provided number
    :return: `string` answer
    """
    if i % 3 == 0 and i % 5 == 0:
        return 'fizz buzz'
    elif i % 3 == 0:
        return 'fizz'
    elif i % 5 == 0:
        return 'buzz'
    else:
        return str(i)


input("Play fizz buzz. Press enter to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Your go: ")
    if player_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, your reached {}".format(correct_answer))
