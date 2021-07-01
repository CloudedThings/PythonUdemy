panagram = """The quick brown
 fox jumps\t over the
  lazy dog"""

words = panagram.split()

print(words)

numbers = "9,456, 123, 445, 84546.22.54;45"
separators = ", .;"
print(numbers.split(separators))
values = "".join(char if char not in separators else " " for char in numbers).split()
real_numbers = " ".join(values)
print(real_numbers)

for index in range(len(real_numbers)):
    real_numbers[index] = int(real_numbers[index])

print(real_numbers)