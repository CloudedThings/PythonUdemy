vowels = set(["A", "E", "I", "O", "U", "Y"])
text = input("Type in a text: ").upper()
text_set = set()
for letter in text:
    text_set.add(letter)

text_set.difference_update(vowels)
print(sorted(text_set))