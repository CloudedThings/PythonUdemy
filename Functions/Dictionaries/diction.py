fruit = {"orange": "a sweet, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow",
         "grape": "a small, sweet, good for wines",
         "lime": " a sour, green fruit"}

# print(fruit)
# print(fruit["lime"])
# fruit["pear"] = "an odd shapped apple"
# print(fruit)

veg = {"cabbage": "child favorite",
       "carrot": "good for skin",
       "spinach": "very good"}

# veg.update(fruit)
# print(veg)

everything = fruit.copy()
everything.update(veg)
print(everything)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print(f'{dict_key} is not in the dictionary')