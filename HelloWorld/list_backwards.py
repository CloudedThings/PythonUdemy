data = [104, 456, 123, 845, 124, 885, 649, 574, 12, 96, 111, 23, 999,
        45, 89, 112, 745, 58, 29]

min_valid = 100
max_valid = 200

for index in range(len(data) - 1, - 1, - 1):
    if data[index] < min_valid or data[index] > max_valid:
        del data[index]

print(data)