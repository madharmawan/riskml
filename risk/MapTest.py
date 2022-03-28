from Map import Map
import unittest

class TestMap(unittest.TestCase):
    def test_constructor(self):
        m = Map()
        self.assertEquals(m.num_continents, 0, "There should be 0 continents")
    
    def test_add_continent(self):
        m = Map()
        m.add_continent("Europe")

    def test_remove_continent():
        return

if __name__ == "__main__":
    unittest.main()