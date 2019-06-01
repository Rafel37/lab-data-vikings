# Project lab-data-vikings
# import random


# Soldier (constructor, ataque y daño)
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        self.health = self.health - damage
# Viking
class Viking(Soldier):
    pass

# Saxon
class Saxon(Soldier):
    pass

# War
class War:
    pass
