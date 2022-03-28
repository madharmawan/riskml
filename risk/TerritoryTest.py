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
        c.set_border(d)
        border = c.get_border(d)
        original = border.get_border(c)
        self.assertEquals(border, d, "border should be d")
        self.assertEqual(border.value, d.value, "value of Territory is 34")
        self.assertEquals(original, c, "territory is c")
        self.assertEquals(d.get_border(d), None, "d is not in the borders of d")
        self.assertEquals(c.get_border(d).get_border(c), c, "border of d's borader is c")
        c.set_border(e)
        e.set_border(d)
        self.assertEquals(c.get_border(e).get_border(d).get_border(c), c, "c's border e's border d's border is c")
        self.assertEquals(c.get_border(d.get_border(e)), e, "e is in c's border")
        f = Territory("F", 1)
        self.assertEquals(c.get_border(e.get_border(f)), None, "f is not bordering anything")
        f.set_border(c)
        self.assertEquals(e.get_border(d).get_border(c).get_border(f), f, "e borders d borders c borders f")
        self.assertEquals(e.get_border(d).get_border(f), None, "e borders d, but d does not border f")
        
    def test_set_owner(self):
        c = Territory("C1", 1)
        d = Territory("D1", 2)
        P = Player()
        c.set_owner()



if __name__ == '__main__':
    unittest.main()