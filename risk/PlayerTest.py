from Territory import Territory
import unittest
from Player import Player
import risk

class PlayerTest(unittest.TestCase):
    def test_constructor(self):
        p = Player("Player 1")
        self.assertEquals(p.name, "Player 1", "p's name is Player 1")
        self.assertEquals(p.owned_territories, 0, "p owns 0 territories")
        
    
    
if __name__ == '__main__':
    unittest.main()