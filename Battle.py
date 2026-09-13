from Trainer import *
from Pokemon import *
from Move import *
import random


class Battle:
  def __init__(self, player, enemy):
    self.player = player # both these are Trainer objects
    self.enemy = enemy

  def printBattle(self):
    print (":( " + self.enemy.name)
    print(self.enemy.getFirstPokemon())
    print()
    print(":) " + self.player.name)
    print(self.player.getFirstPokemon())
    self.player.printItems()

  def loop(self):
    print("Trainer " + self.enemy.name + " wants to battle!" )
    print("Trainer " + self.enemy.name + " sent out " + self.enemy.getFirstPokemon().name + "!")
    print("Trainer " + self.player.name + " sent out " + self.player.getFirstPokemon().name + "!")
    while True:
      #player's turn
      print()
      self.printBattle()
      print()
      print("a: attack")
      print("p: pokemon")
      print("i: items")
      print("r: run")
      print()
      choice = input("Enter a command: ")
      
      if choice == "a":
        print("")
        moveNum = self.playerAttack()
        if self.player.getFirstPokemon().getMove(moveNum).pp == 0:
          print("You can not use that move anymore. \n ")
          continue
        print(self.player.getFirstPokemon().name + " uses " + self.player.getFirstPokemon().getMove(moveNum).name + "!")
        self.player.getFirstPokemon().getMove(moveNum).losePP(1)
        dmg = self.calcDamage(self.player.getFirstPokemon(), self.enemy.getFirstPokemon(), self.player.getFirstPokemon().getMove(moveNum))
        self.enemy.getFirstPokemon().loseHP(dmg)
      if choice == "p":
        pass
      if choice == "i":
        pass
      if choice == "r":
        print("")
        print("Trainer " + self.player.name + " has chosen to run away!")
        break
      if self.enemy.getFirstPokemon().isAlive() == False:
        y = self.enemy.getFirstPokemon().calcXpYield()
        print("Your oponent's ", self.enemy.getFirstPokemon(), " has feinted")
        print(self.player.getFirstPokemon(), " gained ", y, "XP")
        self.player.getFirstPokemon().gainXP(y);
      if self.enemy.isDead() == False:
        self.enemy.switchAlive()
        print("The enemy has sent out ", self.enemy.getFirstPokemon())

      
      #enemy's turn
      moveNum = self.enemy.getFirstPokemon().getRandomMoveNum()
      print(self.enemy.getFirstPokemon().name + " uses " + self.enemy.getFirstPokemon().getMove(moveNum).name + "!")
      self.enemy.getFirstPokemon().getMove(moveNum).losePP(1)
      dmg = self.calcDamage(self.enemy.getFirstPokemon(), self.player.getFirstPokemon(), self.enemy.getFirstPokemon().getMove(moveNum))
      self.player.getFirstPokemon().loseHP(dmg)
      if self.player.getFirstPokemon().isAlive() == False:
        x = self.player.getFirstPokemon().calcXpYield()
        print("Your ", self.player.getFirstPokemon(), " has feinted")
        print(self.enempy.geFirstPokemon(), " gained ", x, "XP")
        self.enemy.getFirstPokemon().gainXP(x)
      

  def playerAttack(self):
    self.player.getFirstPokemon().printMoves()
    print()
    choice = int(input("Enter move #: "))
    print()
    return choice


  def calcDamage(self, attacker, receiver, move):
    dmg = 0
    atk = 0
    deff = 1
    if move.type == "Physical":
      atk = attacker.atk
      deff = receiver.deff
    elif move.type == "Special":
      atk = attacker.spatk
      deff = receiver.spdeff
    atkBonus = 1
    stabBonus = 0
    for rt in receiver.types:
      if stabBonus < stab[move.type][rt]:
        stabBonus = stab[move.type][rt]
    if move.type in attacker.types:
      atkBonus = 1.5
    dmg = ((((((((2 * attacker.lvl / 5 + 2) * atk * move.pow)/deff) / 50) + 2) * atkBonus) * stabBonus) * random.randint(217, 255)) / 255
    if stabBonus == 0:
      print("The attack had no effect")
    if stabBonus == 0.5:
      print("The attack was not effective")
    if stabBonus == 1:
      print("The attack was effective")
    if stabBonus == 2:
      print("The attack was super-effective!")
    return round(dmg)



    


# STAB chart
stab = {}
stab["Normal"] = {"Normal":1,"Fire":1,"Water":1,"Electric":1,"Grass":1,"Ice":1,"Fighting":1,"Poison":1,"Ground":1,"Flying":1,"Psychic":1,"Bug":1,"Rock":0.5,"Ghost":0,"Dragon":1,"Dark":1,"Steel":0.5,"Fairy":1}

stab["Fire"] = {"Normal":1,"Fire":0.5,"Water":0.5,"Electric":1,"Grass":2,"Ice":2,"Fighting":1,"Poison":1,"Ground":1,"Flying":1,"Psychic":1,"Bug":2,"Rock":0.5,"Ghost":0,"Dragon":0.5,"Dark":1,"Steel":2,"Fairy":1}

stab["Water"] = {"Normal":1,"Fire":2,"Water":0.5,"Electric":1,"Grass":0.5,"Ice":1,"Fighting":1,"Poison":1,"Ground":2,"Flying":1,"Psychic":1,"Bug":1,"Rock":2,"Ghost":1,"Dragon":0.5,"Dark":1,"Steel":1,"Fairy":1}

stab["Electric"] = {"Normal":1,"Fire":1,"Water":2,"Electric":0.5,"Grass":0.5,"Ice":1,"Fighting":1,"Poison":1,"Ground":0,"Flying":2,"Psychic":1,"Bug":1,"Rock":1,"Ghost":1,"Dragon":0.5,"Dark":1,"Steel":1,"Fairy":1}

stab["Grass"] = {"Normal":1,"Fire":0.5,"Water":2,"Electric":1,"Grass":0.5,"Ice":1,"Fighting":1,"Poison":0.5,"Ground":2,"Flying":0.5,"Psychic":1,"Bug":0.5,"Rock":2,"Ghost":1,"Dragon":0.5,"Dark":1,"Steel":0.5,"Fairy":1}

stab["Ice"] = {"Normal":1,"Fire":0.5,"Water":0.5,"Electric":1,"Grass":2,"Ice":0.5,"Fighting":1,"Poison":1,"Ground":2,"Flying":2,"Psychic":1,"Bug":1,"Rock":1,"Ghost":1,"Dragon":2,"Dark":1,"Steel":0.5,"Fairy":1}

stab["Fighting"] = {"Normal":2,"Fire":1,"Water":1,"Electric":1,"Grass":1,"Ice":2,"Fighting":1,"Poison":0.5,"Ground":1,"Flying":0.5,"Psychic":0.5,"Bug":0.5,"Rock":2,"Ghost":0,"Dragon":1,"Dark":2,"Steel":2,"Fairy":0.5}

stab["Poison"] = {"Normal":1,"Fire":1,"Water":1,"Electric":1,"Grass":2,"Ice":1,"Fighting":1,"Poison":0.5,"Ground":0.5,"Flying":1,"Psychic":1,"Bug":1,"Rock":0.5,"Ghost":0.5,"Dragon":1,"Dark":1,"Steel":0,"Fairy":2}

stab["Ground"] = {"Normal":1,"Fire":2,"Water":1,"Electric":2,"Grass":0.5,"Ice":1,"Fighting":1,"Poison":2,"Ground":1,"Flying":0,"Psychic":1,"Bug":0.5,"Rock":2,"Ghost":1,"Dragon":1,"Dark":1,"Steel":2,"Fairy":1}

stab["Flying"] = {"Normal":1,"Fire":1,"Water":1,"Electric":0.5,"Grass":2,"Ice":1,"Fighting":2,"Poison":1,"Ground":1,"Flying":1,"Psychic":1,"Bug":2,"Rock":0.5,"Ghost":1,"Dragon":1,"Dark":1,"Steel":0.5,"Fairy":1}

stab["Psychic"] = {"Normal":1,"Fire":1,"Water":1,"Electric":1,"Grass":1,"Ice":1,"Fighting":2,"Poison":2,"Ground":1,"Flying":1,"Psychic":0.5,"Bug":1,"Rock":1,"Ghost":1,"Dragon":1,"Dark":0,"Steel":0.5,"Fairy":1}

stab["Bug"] = {"Normal":1,"Fire":0.5,"Water":1,"Electric":1,"Grass":2,"Ice":1,"Fighting":0.5,"Poison":0.5,"Ground":1,"Flying":0.5,"Psychic":2,"Bug":1,"Rock":1,"Ghost":0.5,"Dragon":1,"Dark":2,"Steel":0.5,"Fairy":0.5}

stab["Rock"] = {"Normal":1,"Fire":2,"Water":1,"Electric":1,"Grass":1,"Ice":2,"Fighting":0.5,"Poison":1,"Ground":0.5,"Flying":2,"Psychic":1,"Bug":2,"Rock":1,"Ghost":1,"Dragon":1,"Dark":1,"Steel":0.5,"Fairy":1}

stab["Ghost"] = {"Normal":0,"Fire":1,"Water":1,"Electric":1,"Grass":1,"Ice":1,"Fighting":1,"Poison":1,"Ground":1,"Flying":1,"Psychic":2,"Bug":1,"Rock":1,"Ghost":2,"Dragon":1,"Dark":0.5,"Steel":1,"Fairy":1}

stab["Dragon"] = {"Normal":1,"Fire":1,"Water":1,"Electric":1,"Grass":1,"Ice":1,"Fighting":1,"Poison":1,"Ground":1,"Flying":1,"Psychic":1,"Bug":1,"Rock":1,"Ghost":1,"Dragon":2,"Dark":1,"Steel":0.5,"Fairy":0}

stab["Dark"] = {"Normal":1,"Fire":1,"Water":1,"Electric":1,"Grass":1,"Ice":1,"Fighting":0.5,"Poison":1,"Ground":1,"Flying":1,"Psychic":2,"Bug":1,"Rock":1,"Ghost":2,"Dragon":1,"Dark":0.5,"Steel":1,"Fairy":0.5}

stab["Steel"] = {"Normal":1,"Fire":0.5,"Water":0.5,"Electric":0.5,"Grass":1,"Ice":2,"Fighting":1,"Poison":1,"Ground":1,"Flying":1,"Psychic":1,"Bug":1,"Rock":2,"Ghost":1,"Dragon":1,"Dark":1,"Steel":0.5,"Fairy":2}

stab["Fairy"] = {"Normal":1,"Fire":0.5,"Water":1,"Electric":1,"Grass":1,"Ice":1,"Fighting":2,"Poison":0.5,"Ground":1,"Flying":1,"Psychic":1,"Bug":1,"Rock":1,"Ghost":1,"Dragon":2,"Dark":2,"Steel":0.5,"Fairy":1}