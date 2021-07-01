import shelve

fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour yellow citrus"
fruit['grape'] = "great for making wines"
fruit['lime'] = "a sour green citrus fruit"

print(fruit["lemon"]),
fruit.close()
