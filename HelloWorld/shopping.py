shopping_list = ["milk", "bread", "pasta", "cheese", "tomato"]

# for item in shopping_list:
#     if item != "milk":
#         print("Buy " + item)

for item in shopping_list:
    if item == "milk":
        continue
    print("Buy " + item)

item_to_find = "tomato"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index

print(found_at)