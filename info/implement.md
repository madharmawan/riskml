This markdown serves as a detailed discussion on how things will be implemented. Add questions, comments and concerns at the top and make a pull request for it if needed.

# Map, Continent, Territory Classes

Here are my ideas on these classes

## Map
Map class holds all the continent objects. Probably a list might be the best to hold them in.

Let's make one map object only (or can we make multiple Map instances?)

### Class Variables

### Methods

__init__(self, name, continents):
  self.name = name
  self.continents = continents

check_owned(self, map):
  for contin in map.continents:
    if contin.owned_by != self:
      return False
  endGame();
 
## Continent
Continent class holds Territories, but it also has more to it. It has a designated point value when initialized and contains a list of territories
### Class Variables

### Methods
__init__(self, name, troops, territories):
  assert isinstance(territories, list)
  self.name = name
  self.territories = territories
  self.troops = troops
  self.owned_by = null; #changes if a player owns all territories in a continent

check_owned(self, continent):
  for terr in continent.territories:
    if terr.owner != self:
        return False
  return True


## Territory
Territory class holds information about troops, what is borders it, and which continent it is located in.
Do we need to know what continent a territory is in? Or do we just need to know the territories in a continent? (They are two different entities).
### Class Variables

### Methods
__init__(self, name, troops=0):
  self.name = name
  self.troops = troops
  self.owned_by = null
  self.borders = []

create_border(terr1, terr2):
  terr1.borders.append(terr2)
  terr2.borders.append(terr1)
  

# Cards, Standard, Wildcard

# Player

# Game
