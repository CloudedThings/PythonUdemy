computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
#print(computer_parts)
#computer_parts[3] = "trackball"
print(computer_parts)
print(computer_parts[3:])
computer_parts[3:] = ["trackball"]
print(computer_parts)

data = [10, 30, 190, 320, 448, 273, 200, 187, 20, 19, 99, 146, 76, 230,
        490, 111, 222, 232, 123]
data.sort()
min_valid = 100
max_valid = 200

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
del data[:stop]
print(data)

start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break
del data[start:]
print(data)