

class Entity:
    def __init__(self, name, health):
        self.max_health = health
        self.health = health
        self.name = name
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        if not self.is_alive():
            return False
        if amount > self.get_health():
            self.health = 0
        else:
            self.health -= amount
        return True

    def take_healing(self, amount):
        if not self.is_alive():
            return False

        if amount > self.max_health - self.health:
            self.health = self.max_health

        else:
            self.health += amount

        return True

    def has_weapon(self):
        return self.weapon

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            if self.weapon.critical_hit():
                return self.weapon.damage * 2
            return self.weapon.damage

        return 0
