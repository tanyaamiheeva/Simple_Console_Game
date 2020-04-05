from factory import DemigodsArmy, MonstersArmy
from service import Army
import unittest


class TestWarrior(unittest.TestCase):

    def setUp(self):
        self.fighter = DemigodsArmy().recruit_human()

    def test_Weapon(self):
        self.assertEqual(self.fighter.weapon, 'sword')

    def test_Health(self):
        self.assertEqual(self.fighter.health, 50)

    def test_IsAlive(self):
        self.assertEqual(self.fighter.alive, True)

    def test_Attack(self):
        self.assertEqual(self.fighter.attack, 5)

    def test_Army(self):
        self.assertEqual(self.fighter.army, Army.Demigods.value)


class TestEnemyCentaur(unittest.TestCase):

    def setUp(self):
        self.fighter = MonstersArmy().recruit_centaur()

    def test_Weapon(self):
        self.assertEqual(self.fighter.weapon, 'crossbow')

    def test_Health(self):
        self.assertEqual(self.fighter.health, 100)

    def test_IsAlive(self):
        self.assertEqual(self.fighter.alive, True)

    def test_Attack(self):
        self.assertEqual(self.fighter.attack, 10)

    def test_Army(self):
        self.assertEqual(self.fighter.army, Army.Monsters.value)


class TestDemigod(unittest.TestCase):

    def setUp(self):
        self.fighter = DemigodsArmy().recruit_special_human()

    def test_Weapon(self):
        self.assertEqual(self.fighter.weapon, 'special power')

    def test_Health(self):
        self.assertEqual(self.fighter.health, 50)

    def test_IsAlive(self):
        self.assertEqual(self.fighter.alive, True)

    def test_Attack(self):
        self.assertEqual(self.fighter.attack, 20)

    def test_Army(self):
        self.assertEqual(self.fighter.army, Army.Demigods.value)
    

if __name__ == '__main__':
    unittest.main()
