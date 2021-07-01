name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
elif age == 90:
    print("Your to old")
else:
    print("You're too young to vote")

