# jabber = open("sample.txt", 'r')
#
# for line in jabber:
#     print(line)
#
# jabber.close()

# with open("sample.txt") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()