from Move import *
import random

#constructor
class Pokemon:
  def __init__(self, name, types, hp, atk, deff, spatk, spdeff, spd, lvl=1):
    self.name = name
    self.types = types
    self.lvl = lvl
    self.maxLvl = 100
    self.baseHp = hp
    self.maxHp = hp
    self.hp = hp
    self.baseAtk = atk
    self.maxAtk = self.calcStat(atk)
    self.atk = self.maxAtk
    self.baseDeff = deff
    self.maxDeff = self.calcStat(deff)
    self.deff = self.maxDeff
    self.baseSpatk = spatk
    self.maxSpatk = self.calcStat(spatk)
    self.spatk = self.maxSpatk
    self.baseSpdeff = spdeff
    self.maxSpdeff = self.calcStat(spdeff)
    self.spdeff = self.maxSpdeff
    self.baseSpd = spd
    self.maxSpd = self.calcStat(spd)
    self.spd = self.maxSpd
    self.setMaxXp()
    self.Xp = self.maxXp
    self.moves = []
    self.fainted = False
    self.statuses = []

  #string rep
  def __str__(self):
    print(self.Xp)
    s = ""
    s += self.name 
    s += " [HP: " + str(self.hp) + " / " + str(self.maxHp) + " ]"
    return s
  
  def loseHP(self,amt):
    self.hp -= amt
    if self.hp < 0:
      self.hp = 0
    print(self.name + " took " + str(amt) + " damage!")

  def gainHP(self, amt):
    self.hp += amt
    if self.hp > self.maxHp:
      self.hp = self.maxHp
    print(self.name + " gained " + str(amt) + " HP!")

  def gainXP(self, amt):
    self.Xp += amt
    if self.Xp >= self.maxXp:
      self.levelUp()

  
  def isAlive(self):
    if self.hp > 0:
      return True
    return False

  def setHp(self):
    self.maxHp = round(self.baseHp * 2 * self.lvl / 100 + 10 + self.lvl)
    self.hp = self.maxHp

  def calcStat(self, stat):
    return round(stat * 3 * self.lvl/ 10 + 5)

  def setMaxXp(self):
    self.maxXp = round(0.8 * pow(self.lvl,3))

  def levelUp(self):
    self.lvl += 1
    print(self.name + " leveled up to " + str(self.lvl) + "!")
    self.setHp()
    self.maxAtk = self.calcStat(self.baseAtk)
    self.maxDeff = self.calcStat(self.baseDeff)
    self.maxSpatk = self.calcStat(self.baseSpatk)
    self.maxSpdeff = self.calcStat(self.baseSpdeff)
    self.maxSpd = self.calcStat(self.baseSpd)
    self.setMaxXp()

  def calcXpYield(self):
    y =  round((30 * self.lvl) / (7))
    return y


  #adds a given move to moves
  def addMove(self, move):
    self.moves.append(move)

  def getMove(self, i):
    return self.moves[i]

  def printMoves(self):
    for i in range (len(self.moves)):
      print(str(i) +": " + str(self.moves[i]))

  def getRandomMoveNum(self):
    choice = random.randint(0, len(self.moves)-1)
    return choice

pikachu = Pokemon("Pikachu", ["Electric"], 35, 55, 30, 50, 40,90)
pikachu.addMove(THUNDER_SHOCK)
pikachu.addMove(TAIL_WHIP)
pikachu.addMove(THUNDER)

bulbasaur = Pokemon("Bulbasaur", ["Grass", "Poison"],45, 49, 49, 65, 65, 45)
bulbasaur.addMove(BODY_SLAM)
bulbasaur.addMove(LEAF_STORM)

squirtle = Pokemon("Squirtle", ["Water"], 44, 48, 65, 50, 64, 43)
squirtle.addMove(WATER_GUN)
squirtle.addMove(TAIL_WHIP)

charmander = Pokemon("Charmander", ["Fire"], 39, 52, 43, 60, 50, 65)
charmander.addMove(SLASH)
charmander.addMove(FLAMETHROWER)

rattata = Pokemon("Rattata",["Normal"], 30, 56, 35, 25, 35, 72)
rattata.addMove(TAIL_WHIP)
rattata.addMove(DOUBLE_EDGE)

psyduck = Pokemon("Psyduck", ["Psychic", "Water"], 50, 52, 48, 65, 50, 55)
psyduck.addMove(PSYBEAM)
psyduck.addMove(FURY_SWIPES) 

electabuzz = Pokemon("Electabuzz", ["Electric"], 65, 83, 57, 93, 85, 105)
electabuzz.addMove(THUNDER_SHOCK)
electabuzz.addMove(THUNDER)

gengar = Pokemon("Gengar",["Ghost","Poison"], 60, 65, 60, 130, 75, 110)
gengar.addMove(HEX)
gengar.addMove(SUCKER_PUNCH)