from Territory import Territory
import unittest
from Player import Player

class TestTerritory(unittest.TestCase):
    def test_constructor(self):
        c = Territory("California", 42)
        self.assertEqual(c.name, "California", "Should be California")
        self.assertEqual(c.value, 42, "the value should be 42")
        d = Territory("test", 21)
        self.assertEqual(d.name, "test", "Territory name should be test")
        self.assertEqual(d.value, 21, "there should be 21 value")

    def test_change_troops(self):
        c = Territory("C", 42)
        self.assertEqual(c.troops, 0, "Troops should be 0")

        c.change_troops(4)
        self.assertEquals(c.troops, 4, "Troops should be 4")
    
    def test_set_border(self):
        c = Territory("C", 21)
        d = Territory("D", 34)
        e = Territory("E", 25)
        
    def test_set_owner(self):
        c = Territory("C1", 1)
        d = Territory("D1", 2)
        P = Player()
        c.set_owner()



if __name__ == '__main__':
    unittest.main()