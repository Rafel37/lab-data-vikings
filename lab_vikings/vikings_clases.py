# Project lab-data-vikings
import random as rm


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
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name


    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battle_cry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"

# War
class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self, viking):
        self.viking_army.append(viking)
        
    def add_saxon(self, saxon):
        self.saxon_army.append(saxon)

    def viking_attack(self):
        saxon = rm.choice( self.saxon_army)
        viking = rm.choice( self.viking_army)
        result_viking_attack = saxon.receive_damage(viking.strength)
        [self.saxon_army.remove(saxon) 
        for saxon in self.saxon_army  
        if saxon.health <= 0]
        return result_viking_attack

    def saxon_attack(self):
        saxon = rm.choice( self.saxon_army)
        viking = rm.choice( self.viking_army)
        result_saxon_attack = viking.receive_damage(saxon.strength)
        [self.viking_army.remove(viking) 
        for viking in self.viking_army  
        if viking.health <= 0]
        return result_saxon_attack

    def show_status(self):
        if len(self.saxon_army) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.viking_army) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxon_army) >= 1 & len(self.viking_army) >= 1:
            return "Vikings and Saxons are still in the thick of battle."


    
