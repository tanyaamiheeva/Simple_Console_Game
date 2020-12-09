from armies import Army, HumanSquad, SpecialHumanSquad, CentaursSquad, CyclopsSquad, DragonSquad
from service import Side
import random


def create_default_army(main_army: Army):
    if main_army.side == Side.Demigods:
        default_army = Army(Side.Monsters)
    else:
        default_army = Army(Side.Demigods)

    default_army.add(DragonSquad(default_army.side, 3))
    default_army.add(CyclopsSquad(default_army.side, 2))
    default_army.add(SpecialHumanSquad(default_army.side, 1))
    return default_army


class Battle:
    def __init__(self, main_army: Army):
        self.first = main_army
        self.second = create_default_army(main_army)

    def battle(self):
        beginner = random.choice([1, 2])
        while self.first.total_health > 0 and self.second.total_health > 0:
            if beginner == 1:
                self.second.total_health -= self.first.total_attack
                if self.second.total_health <= 0:
                    print('You won!')
                    return 1
                self.first.total_health -= self.second.total_attack
                if self.first.total_health <= 0:
                    print('This time you failed to defeat the enemy, try again!')
                    return 0
            else:
                self.first.total_health -= self.second.total_attack
                if self.first.total_health <= 0:
                    print('This time you failed to defeat the enemy, try again!')
                    return 0
                self.second.total_health -= self.first.total_attack
                if self.second.total_health <= 0:
                    print('You won!')
                    return 1
