import abc
from service import Side, ExistingWeapons


class Fighter:
    __metaclass__ = abc.ABCMeta
    __slots__ = ('health',
                 'attack',
                 'weapon',
                 'cost',
                 'alive',
                 'army')

    def __init__(self):
        pass

    def killed(self):
        if self.alive:
            self.alive = False

    def change_weapon(self, new_weapon: str):
        if new_weapon not in ExistingWeapons.weapons:
            print("This weapon doesn't exist!")
        else:
            self.weapon = new_weapon


class Human(Fighter):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 5
        self.cost = 5
        self.alive = True


class Warrior(Human):
    def __init__(self):
        super().__init__()
        self.weapon = "sword"
        self.army = Side.Demigods.value


class Demigod(Human):
    def __init__(self):
        super().__init__()
        self.attack = 15
        self.weapon = "special power"
        self.cost = 10
        self.army = Side.Demigods.value


class Zombie(Human):
    def __init__(self):
        super().__init__()
        self.weapon = "fangs"
        self.army = Side.Monsters.value


class ArmedZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.attack = 15
        self.weapon = "sword"
        self.cost = 10
        self.army = Side.Monsters.value


class Centaur(Fighter):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.attack = 10
        self.weapon = "crossbow"
        self.cost = 10
        self.alive = True


class FriendlyCentaur(Centaur):
    def __init__(self):
        super().__init__()
        self.army = Side.Demigods.value


class EnemyCentaur(Centaur):
    def __init__(self):
        super().__init__()
        self.army = Side.Monsters.value


class Cyclops(Fighter):
    def __init__(self):
        super().__init__()
        self.health = 200
        self.attack = 20
        self.weapon = "cudgel"
        self.cost = 20
        self.alive = True


class FriendlyCyclops(Cyclops):
    def __init__(self):
        super().__init__()
        self.army = Side.Demigods.value


class EnemyCyclops(Cyclops):
    def __init__(self):
        super().__init__()
        self.army = Side.Monsters.value


class Dragon(Fighter):
    def __init__(self):
        super().__init__()
        self.health = 200
        self.attack = 50
        self.weapon = "fire"
        self.cost = 50
        self.alive = True


class FriendlyDragon(Dragon):
    def __init__(self):
        super().__init__()
        self.army = Side.Demigods.value


class EnemyDragon(Dragon):
    def __init__(self):
        super().__init__()
        self.army = Side.Monsters.value
