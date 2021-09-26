import unittest
from teste import Charcter

class TestCharacters(unittest.TestCase):
    def setUp(self):
        self.azura = Charcter('azura',100,100,100,100,100,100,100)
        self.gilder_snake = Charcter('gilder_snake',70,70,70,70,70,70,70)
        
    def teste_poder_ataque(self):
        self.assertEqual(self.azura.ataques['atk_1'].power, 100)
        self.assertEqual(self.azura.atk, 310)
        self.azura.level_up()
        self.assertEqual(self.azura.atk, 313)
        self.assertEqual(self.gilder_snake.atk, 178)
        self.assertEqual(self.azura.calc_dmg('atk_1', self.gilder_snake), 149)

if __name__ == "__main__":
    unittest.main()