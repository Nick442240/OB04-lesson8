from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "удар мечом"

class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"

class Fighter:
        def __init__(self, name):
            self.name = name
            self.weapon = None

        def changeWeapon(self, weapon):
            self.weapon = weapon

        def attack(self):
            if self.weapon:
                print(f"{self.name} наносит {self.weapon.attack()}.")
            else:
                print(f"{self.name} не вооружен.")


class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} побежден!")
        else:
            print(f"{self.name} имеет {self.health} здоровья.")

# Демонстрация боя
def battle(fighter, monster, weapon):
    fighter.changeWeapon(weapon)
    print(f"{fighter.name} выбирает {weapon.__class__.__name__.lower()}.")
    fighter.attack()
    monster.take_damage(50)

# Создание бойца и монстра
fighter = Fighter("Боец")
monster = Monster("Монстр")

# Проведение боя с различным оружием
battle(fighter, monster, Sword())
battle(fighter, monster, Bow())




