import random

highest = 10
answer = random.randint(1, 10)

print("Please guess number between 1 and {}: ".format(highest))
guess = 0
while guess != answer:
        guess = int(input())
        if guess > answer:
            print("Your guess is too high")
        elif guess < answer:
            print("Your guess is too low")
        elif guess == answer:
            print("correct answer!")
            break