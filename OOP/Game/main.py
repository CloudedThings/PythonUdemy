from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing


# ugly_troll = Troll("Pug")
# print("ugly_troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))
#
# brother = Troll("Urg")
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()

# nosferatu = Vampyre("Nosferatu")
# print(nosferatu)
#
# valkyrie = Vampyre("Valkyrie")
# print(valkyrie)
#
# nosferatu.take_damage(20)
# valkyrie.take_damage(300)
# print(nosferatu)
# print(valkyrie)
#
# while nosferatu._alive:
#     nosferatu.take_damage(1)
#     # print(nosferatu)

dracula = VampyreKing("Dracula")
print(dracula)

while dracula._alive:
    dracula.take_damage(10)
