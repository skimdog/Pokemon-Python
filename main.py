from Pokemon import *
from Battle import *
from Trainer import *

player = Trainer("Red", [gengar])
print(pikachu)
enemy = Trainer("Black", [pikachu])

battle = Battle(player, enemy)

battle.loop()
