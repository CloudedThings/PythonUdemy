
password = "TajneHaslo228"
word = input("check if word is in the password: ")

if word in password.casefold():
    print("yes {} is in password {}".format(word, password))
