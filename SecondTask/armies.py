from factory import Demigods, Monsters
from units import Warrior, Demigod, Zombie, ArmedZombie, Centaur, Cyclops, Dragon
import service
import random
from collections import defaultdict


class Squad:
    def __init__(self, side: service.Side):
        self.participants = []
        if side == service.Side.Demigods:
            self.base = Demigods()
        else:
            self.base = Monsters()

    def attendees(self):
        return self.participants


class CentaursSquad(Squad):
    def __init__(self, side: service.Side, key: int):
        super().__init__(side)
        self.centaur = self.base.recruit_centaur()
        for i in range(key):
            self.participants.append(self.centaur)


class DragonSquad(Squad):
    def __init__(self, side: service.Side, key: int):
        super().__init__(side)
        self.dragon = self.base.recruit_dragon()
        for i in range(key):
            self.participants.append(self.dragon)


class CyclopsSquad(Squad):
    def __init__(self, side: service.Side, key: int):
        super().__init__(side)
        self.cyclops = self.base.recruit_cyclops()
        for i in range(key):
            self.participants.append(self.cyclops)


class SpecialHumanSquad(Squad):
    def __init__(self, side: service.Side, key: int):
        super().__init__(side)
        self.special_human = self.base.recruit_special_human()
        for i in range(key):
            self.participants.append(self.special_human)

            
class HumanSquad(Squad):
    def __init__(self, side: service.Side, key: int):
        super().__init__(side)
        self.human = self.base.recruit_human()
        for i in range(key):
            self.participants.append(self.human)


class Mercenary:
    def __init__(self):
        self.potential = int(random.uniform(5, 60))
        print('I can deal {} points of damage!'.format(self.potential))


class MercenaryTraining(Squad):
    def __init__(self, side: service.Side, person: Mercenary):
        super().__init__(side)
        if person.potential in range(5, 10):
            self.unit = self.base.recruit_human()
        elif person.potential in range(10, 15):
            self.unit = self.base.recruit_centaur()
        elif person.potential in range(15, 20):
            self.unit = self.base.recruit_special_human()
        elif person.potential in range(20, 50):
            self.unit = self.base.recruit_cyclops()
        else:
            self.unit = self.base.recruit_dragon()
        self.unit.cost = 20
        self.participants.append(self.unit)


class Army(Squad):
    def __init__(self, s: service.Side):
        super().__init__(s)
        self.side = s
        self.total_health = 0
        self.total_attack = 0
        self.coins = 200

    def add(self, unit: Squad):
        for soldier in unit.attendees():
            self.coins -= soldier.cost
            if self.coins < 0:
                self.coins += soldier.cost
                print('Not enough coins')
                print('You have {} coins left'.format(self.coins))
                return
            else:
                self.total_health += soldier.health
                self.total_attack += soldier.attack
                self.participants.append(soldier)

    def get_str_participants(self):
        dict_of_units = defaultdict(int)
        for unit in self.participants:
            if self.side == service.Side.Demigods:
                if isinstance(unit, Warrior):
                    dict_of_units['warrior'] += 1
                if isinstance(unit, Demigod):
                    dict_of_units['demigod'] += 1
            else:
                if isinstance(unit, Zombie):
                    dict_of_units['zombie'] += 1
                if isinstance(unit, ArmedZombie):
                    dict_of_units['armed zombie'] += 1
            if isinstance(unit, Centaur):
                dict_of_units['centaur'] += 1
            if isinstance(unit, Cyclops):
                dict_of_units['cyclops'] += 1
            if isinstance(unit, Dragon):
                dict_of_units['dragon'] += 1
        list_of_units = ''
        for key in dict_of_units:
            list_of_units += '{} - {} '.format(key, dict_of_units[key])
        return list_of_units

    def __repr__(self):
        return self.get_str_participants()

    def current_state(self):
        print('Current status of army:')
        print('COINS: {}'.format(self.coins))
        print('HEALTH: {}'.format(self.total_health))
        print('ATTACK: {}'.format(self.total_attack))
