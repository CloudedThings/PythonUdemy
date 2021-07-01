# creating sets two different ways

farm_animals = {"sheep", "cow", "chicken"}

wild_animals = set(["lion", "tiger", "panther", "elephant"])

farm_animals.add("horse")
# print(farm_animals)

even = set(range(0,40, 2))
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

# combinging two sets excluding dubblets
print(even.union(squares))
print(len(even.union(squares)))

# finding common elements between two sets, two ways to do it
print("-" * 40)
print(even.intersection(squares))
print(even & squares)

# substracting
print("-" * 40)
print("even minus squares")
print(sorted(even))
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))

# updating set with values from another set
print("-" * 40)
even.difference_update(squares)
print(sorted(even))

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))