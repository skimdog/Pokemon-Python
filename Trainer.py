from Pokemon import *

class Trainer:
  def __init__(self, name, pokemons = [], items=[]):
    self.pokemons = pokemons
    self.items = items
    self.name = name
    self.money = 1000

  def printPokemons(self):
    for p in self.pokemons:
      print(p)

  def printItems(self):
    for i in self.items:
      print(i)

  def getFirstPokemon(self):
    return self.pokemons[0]

  def isDead(self):
    for p in self.pokemons:
      if p.isAlive() == True:
        return False
    return True
    
  def switchAlive(self):
    for i in range(1,len(self.pokemons)):
      if self.pokemons[i].isAlive():
        temp = self.pokemons[0]
        self.pokemons[0] = self.pokemons[i]
        self.pokemons[i] = temp


