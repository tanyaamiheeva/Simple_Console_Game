from armies import Army, Squad, HumanSquad, SpecialHumanSquad, CentaursSquad, CyclopsSquad
from armies import MercenaryTraining, DragonSquad, Mercenary
from service import Side
from battle import Battle
import unittest


class TestArmy(unittest.TestCase):
    def setUp(self) -> None:
        self.first_army = Army(Side.Demigods)
        self.second_army = Army(Side.Monsters)
        self.first_army.add(HumanSquad(self.first_army.side, 5))
        self.first_army.add(CentaursSquad(self.first_army.side, 7))

    def test_TotalHealth(self):
        self.assertEqual(self.first_army.total_health, 950)

    def test_TotalAttack(self):
        self.assertEqual(self.first_army.total_attack, 95)

    def test_MembersCount(self):
        self.assertEqual(len(self.first_army.participants), 12)
        self.assertEqual(len(self.second_army.participants), 0)

    def test_CoinsCount(self):
        self.assertEqual(self.first_army.coins, 105)
        self.assertEqual(self.second_army.coins, 200)

    def test_CoinsAreLimited(self):
        self.second_army.add(DragonSquad(self.second_army.side, 6))
        self.assertEqual(self.second_army.total_attack, 200)
        self.assertEqual(self.second_army.total_health, 800)
        self.assertEqual(len(self.second_army.participants), 4)

    def test_Mercenary(self):
        self.first_army.add(MercenaryTraining(self.first_army.side, Mercenary()))
        self.assertEqual(len(self.first_army.participants), 13)
        self.assertEqual(self.first_army.coins, 85)

    def test_MercenaryClass(self):
        unit = MercenaryTraining(self.first_army.side, Mercenary())
        self.assertTrue(isinstance(unit, Squad))


class TestBattle(unittest.TestCase):
    def setUp(self) -> None:
        self.first_army = Army(Side.Monsters)
        self.first_army.add(DragonSquad(self.first_army.side, 4))
        self.battle = Battle(self.first_army)

    def test_Winner(self):
        self.assertEqual(self.battle.battle(), 0)


if __name__ == '__main__':
    unittest.main()
