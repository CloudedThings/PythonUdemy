answer = None

while answer != 0:
    print("Please choose your option from the list below: "
          "\n1. Learn Python"
          "\n2. Learn Java"
          "\n3. Go swimming"
          "\n4. Have dinner"
          "\n5. Go to bed"
          "\n0. Exit")
    answer = int(input("Your choice: "))
    if answer == 1:
        print("You've chosen {}".format(answer))
    elif answer == 2:
        print("You've chosen {}".format(answer))
    elif answer == 3:
        print("You've chosen {}".format(answer))
    elif answer == 4:
        print("You've chosen {}".format(answer))
    elif answer == 5:
        print("You've chosen {}".format(answer))
    else:
        print("Please choose number between 0 and 5")

else:
    print("You enter 0. Quitting...")