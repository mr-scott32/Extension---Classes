class Player():
    def __init__(self, name, race, cls, atk, health):
        self.name = name
        self.race = race
        self.cls = cls
        self.atk = atk
        self.health = health

class Weapon():
    def __init__(self, name, wpn, dmg):
        self.name = name
        self.wpn = wpn
        self.dmg = dmg

class Enemy():
    def __init__(self, name, type, dmg, health):
        self.name = name
        self.type = type
        self.dmg = dmg
        self.health = health

