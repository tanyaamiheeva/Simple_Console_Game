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


class Demigods(UnitFactory):
    def recruit_human(self):
        return Warrior()

    def recruit_special_human(self):
        return Demigod()

    def recruit_centaur(self):
        return FriendlyCentaur()

    def recruit_cyclops(self):
        return FriendlyCyclops()

    def recruit_dragon(self):
        return FriendlyDragon()


class Monsters(UnitFactory):
    def recruit_human(self):
        return Zombie()

    def recruit_special_human(self):
        return ArmedZombie()

    def recruit_centaur(self):
        return EnemyCentaur()

    def recruit_cyclops(self):
        return EnemyCyclops()

    def recruit_dragon(self):
        return EnemyDragon()
