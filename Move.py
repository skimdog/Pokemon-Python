class Move:
  def __init__(self, name, type, cat, pow, acc, pp):
    self.name = name
    self.type = type
    self.cat = cat
    self.pow = pow
    self.acc = acc
    self.pp = pp
    self.maxPp = self.pp

  def __str__(self):
    s = ""
    s += "[" + self.name + "] \n pp: "
    s += str(self.pp) + " / " + str(self.maxPp)
    return s

  def losePP(self, amt):
    self.pp -= amt
    if(self.pp < 0):
      self.pp = 0

# all the moves
THUNDER_SHOCK = Move("Thunder Shock", "Electric","Special", 40, 100, 30)

TAIL_WHIP = Move("Tail Whip", "Normal", "Status", 0 , 100, 30)

WATER_GUN = Move("Water Gun", "Water", "Special", 40, 100,25)

BODY_SLAM = Move("Body Slam", "Normal", "Physical", 85, 100, 15)

LEAF_STORM = Move("Leaf Storm", "Grass", "Special", 130, 90, 5)

SLASH = Move("Slash", "Normal", "Physical", 70, 100, 20)

FLAMETHROWER = Move("Flamethrower", "Fire", "Special", 90, 100, 15)

DOUBLE_EDGE = Move("Double Edge", "Normal", "Physical", 120, 100, 15)

PSYBEAM = Move("Psybeam", "Psychic", "Special", 65, 100, 20)

FURY_SWIPES = Move("Fury Swipes", "Normal", "Physical", 18, 80, 50)

THUNDER = Move("Thunder", "Electric", "Special", 110, 70, 10)

HEX = Move("Hex", "Ghost", "Special", 65, 100, 10)

SUCKER_PUNCH = Move("Sucker Punch", "Dark", "Physical", 70, 100, 5)

