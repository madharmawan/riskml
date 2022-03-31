from Territory import Territory
import unittest
from Player import Player
import risk

class PlayerTest(unittest.TestCase):
    def test_constructor(self):
        p = Player("Player 1")
        self.assertEquals(p.name, "Player 1", "p's name is Player 1")
        self.assertEquals(p.num_owned, 0, "p owns 0 territories")
        e = Player("Player 2")
        self.assertEquals(e.name, "Player 2", "e's name is Player 2")
        self.assertEquals(p.num_owned, 0, "e owns 0 territories")
        
    
    
if __name__ == '__main__':
    unittest.main()