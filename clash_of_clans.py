#Design a dummy game like clash of clans

from abc import ABC, abstractmethod
class soldier(ABC):
    def gather(self):
        print("Gather")

    @abstractmethod
    def attack(self):
        pass
    
class refillable(ABC):
    @abstractmethod
    def refil(self):
        pass

class timebasedrefil(refillable):
    def refil(self):
        print("Time Based Refil")

class weaponbasedrefil(refillable):
    def refil(self):
        print("Weapon Based Refil")

class healing(ABC):
    @abstractmethod
    def heal(self):
        pass

class selfheal(healing):
    def heal(self):
        print("Self Heal")

class externalheal(healing):
    def heal(self):
        print("External Heal")        
           
class archer(soldier):
    def attack(self):
        print("Archer attack")

    def refil(self):
        return timebasedrefil().refil()

    def heal(self):
        return selfheal().heal()

class spearman(soldier):
    def attack(self):
        print("Spearman attack")

    def heal(self):
        return selfheal().heal()

class ironman(soldier):
    def attack(self):
        print("Iron Man Attack")

    def refil(self):
        return weaponbasedrefil().refil()

    def heal(self):
        return externalheal().heal()

class hulk(soldier):
    def attack(self):
        print("Hulk Attack")

    def heal(self):
        return selfheal().heal()

class gunman(soldier):
    def attack(self):
        print("Gunman Attack")

    def refil(self):
        return weaponbasedrefil().refil()

    def heal(self):
        return selfheal().heal()

class swordman(soldier):
    def attack(self):
        print("Swordman Attack")

    def refil(self):
        return weaponbasedrefil().refil()

    def heal(self):
        return selfheal().heal()

a=archer()
a.attack()
a.gather()
a.refil()
a.heal()

print("\n")
b=spearman()
b.attack()
b.gather()
b.heal()

print("\n")
c=ironman()
c.attack()
c.gather()
c.refil()
c.heal()

print("\n")
d=hulk()
d.attack()
d.gather()
d.heal()

print("\n")
e=gunman()
e.attack()
e.gather()
e.refil()
e.heal()

print("\n")
f=swordman()
f.attack()
f.gather()
f.refil()
f.heal()
