import abc
from units import Warrior, Demigod, FriendlyCentaur, FriendlyCyclops, FriendlyDragon
from units import Zombie, ArmedZombie, EnemyCentaur, EnemyCyclops, EnemyDragon


class UnitFactory:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def recruit_human(self):
        pass

    @abc.abstractmethod
    def recruit_special_human(self):
        pass

    @abc.abstractmethod
    def recruit_centaur(self):
        pass

    @abc.abstractmethod
    def recruit_dragon(self):
        pass

    @abc.abstractmethod
    def recruit_cyclops(self):
        pass


class DemigodsArmy(UnitFactory):
    def recruit_human(self):
        print("Warrior joins Demigods' army!")
        return Warrior()

    def recruit_special_human(self):
        print("Demigod joins Demigods' army!")
        return Demigod()

    def recruit_centaur(self):
        print("Centaur joins Demigods' army!")
        return FriendlyCentaur()

    def recruit_cyclops(self):
        print("Cyclops joins Demigods' army!")
        return FriendlyCyclops()

    def recruit_dragon(self):
        print("Dragon joins Demigods' army!")
        return FriendlyDragon


class MonstersArmy(UnitFactory):
    def recruit_human(self):
        print("Zombie joins Monsters' army!")
        return Zombie()

    def recruit_special_human(self):
        print("Armed Zombie joins Monsters' army!")
        return ArmedZombie()

    def recruit_centaur(self):
        print("Centaur joins Monsters' army!")
        return EnemyCentaur()

    def recruit_cyclops(self):
        print("Cyclops joins Monsters' army!")
        return EnemyCyclops()

    def recruit_dragon(self):
        print("Dragon joins Monsters' army!")
        return EnemyDragon()
