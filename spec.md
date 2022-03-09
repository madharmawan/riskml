# Project Title: Destroying the Game of RISK With Machine Learning
Project members: Matthew Dharmawan, Joseph Selfani, Oscar Tapia

# Goals
The goal of this project is threefold: to learn how to recreate a game and generalize it, 
learn about how to make it an online type of game, creating some GUI and interactive parts to it, and 
and finally, to apply principles of machine learning on top of it and learn how one might implement that.
Either way, we will gain experience as programers in the development of RISK, and learn a bit about
machine learning and how it can be used to find the best strategy for this complex game.

The game will be created in Python because of its ability to handle OOP, a for its community for GUI and ML packages


# Overview of the Project

## High-Level Overview of RISK
In the game of RISK, players own troops that control territory. Each TERRITORY belongs to a
CONTINENT, and each CONTINENT belongs to a MAP. Each TERRITORY contains information on which player
owns the territory, what continent it belongs to, which territories border it, and how many troops are 
located in the territory. 

## Start of the Game
To being playing, we are given a MAP, with CONTINENT contained in MAP, and each CONTINENT contains one or
more TERRITORYs. 
Players take turns in a cyclic pattern, and during a PLAYER's turn, there are five phases that make up 
the turn
1. Placing reinforcements
2. Turning in Risk cards
3. Attacking
4. Fortifying
5. Receiving Risk cards

## Setup 
Depending on the amount of players that will be playing will determine how many troops they will receive at the start of the game.
- If 2 are playing, see special instructions at the end of this markdown.
- If 3 are playing, each player counts out 35 Troops.
- If 4 are playing, each player counts out 30 Troops.
- If 5 are playing, each player counts out 25 Troops.
- If 6 are playing, each player counts out 20 Troops.

PLAYERs will be able to choose the TERRITORYs they want to claim. However, the order that will be chosen is based on one die roll,
with the PLAYER with the highest die roll going first, and the player after them in sequence following, and so on. PLAYERs must place
one troop down on any unmarked TERRITORY until all TERRITORYs are claimed. Then with the excess, each PLAYER will then place the remaining
troops in any TERRITORY they want, split in any way they want. There is no limit to the number of troops in a TERRITORY.

The PLAYER who started first will start the game.

## End of Game
The game will end when all territories are owned by one PLAYER. That PLAYER wins the game. When a PLAYER loses all their TERRITORYs, they are out
of the game, meaning their turn will not exist and skipped. In addition, the PLAYER who delivers the final blow to the other player will receive all the
CARDS that the defeated PLAYER owns. 

## 5 Phases

### 1. Placing Reinforcements
At the beginning of every turn, PLAYER will receive a certain amount of troops, based on territories owned, 
and if they control an entire CONTINENT. The continent values are dependent on many factors, but size, and number
of TERRITORYs. However, this will be a free choice to us in our data structure. Once this number is calculated, 
the PLAYER is free to place them anywhere they want in territories that they own. For example if TERRA, TERRB, TERRC 
all belong to CONT1, and PLAYER1 owns all of them, they get (number TERRITORIES) + (CONTINENT bonus) troops. Let's say
the calculation returns 6 troops. PLAYER1 can place them all in TERRA or split it among TERRB and TERRC.

### 2. Turning in Risk Cards
CARDs add an extra layer to the game since they can be turned in for more troops. There are two types of CARDs: standard and wildcard
The STANDARD CARD is a CARD that contains one of three object types: Infantry, Cavalry, or Artillery. A WILDCARD is a CARD that contains 
all three. In addition, each STANDARD CARD contains a territory. If the player turns in a set that contains a TERRITORY they own, they will
receive 2 extra troops, but these troops must be placed on the particular territory.


The way the card system works is that if at least one territory is captured by a PLAYER1 from another PLAYER2, then PLAYER1 will
receive a CARD, which could either be STANDARD or WILDCARD. Only one card is given at the end of their turn (See 5. Receiving Risk Cards) if 
the requirement is met. PLAYERs can turn in cards or not turn in cards. In addition, once a PLAYER has 6 or more CARDS, they must trade it in 
at the start of their next turn.

During this phase, a PLAYER can turn in their CARDS to gain more troops if they desire. they either have to turn in:
- 3 of the same CARD type
- 1 of each CARD type
For example, if PLAYER1 has an Infantry, Cannon, and Wildcard, they are eligible to turn them in for more troops. However, PLAYER 2 has
two Infantry card and a Wildcard; they are not eligible to turn them in.

The amount of troops determined depends on how many sets have turned in for the GAME so far. This means if PLAYER1 turns in a set, gets
their troops, and then finishes up their turn, and then PLAYER2 turns in a set. PLAYER2 earns the amount of troops associated with the 
second set being turned in. Then PLAYER4 turns in a set during their turn, then PLAYER4 receives the amount associated with the third set
being turned in. 

Here is the scaling of the sets:
- First set: 4 troops
- Second set: 6 troops
- Third set: 8 troops
- Fourth set: 10 troops
- Fifth set 12 troops
- Sixth set: 15 troops
- Every additional set is work 5 more armies than the last. So the seventh is 20 troops, eigth is 25 troops, etc.

After the troops are given, the PLAYER can place them anywhere they want with any amount for each, except for the ones 
designated by the TERRITORY if they own it.

### 3. Attacking
After phase 2, the PLAYER can choose to attack any territory they do not own, that borders a territory that they do own.
A battle is fought by a roll of the dice. The only requirement for a battle to occur is that the PLAYER's TERRITORY needs
at least two troops located in it to be able to attack a territory that borders it. 

A PLAYER can attack as much as they want, until the TERRITORY has two troops in it. They can choose any time to stop the 
attacking phase.

To attack, the PLAYER must announce the territory they are attacking with and the TERRITORY that borders it that it will battle.
A dice roll will result the outcome of a battle. Here are the rules of a battle:

Battle Setup and Dice Number
- Both the player and opponent must announce the number of dice to roll, and they must be rolled at the same time. The attacker can
- choose any number between 1 to 3. The number of dice rolled is determined by the PLAYER. However, there must be one more army in 
  the territory than the number of dice that is rolled
- The defender can roll either 1 or 2 dice. To roll 2 dice, they must have at least 2 armies on their territory. 

Outcome of the Battle
- Roll the dice for both sides. Sort it from greatest to least. Start with the greatest value the die from both sides and compare them.
    - If attacker's is higher, then the defender loses one troop from the territory under attack
    - If the defender's is higher or equal to, the attacker loses one troop from the territory they attacked from
    - Then do the same for the two next-highest dice and so on until one or both sides do not have anymore dice

This is an example of one battle, but the attacker can have as many battles as they want, as long as they have 2 or more troops in the TERRITORY
they attack from.

Note that a PLAYER can also choose not to attack at all and move on to the next phase.

### 4. Fortifying
After the attacking phase is done, the PLAYER ends their turn by fortifying their current assets. The PLAYER can move as many troops from one and
only one of their TERRITORYs into one and only of the adjacent TERRITORYs that they own. The PLAYER can also choose not to do anything, and move 
on to the final phase.

### 5. Receiving RISK Cards
If the PLAYER has successfully gained a territory, they will receive one RISK Card, which will be completely random. Then it is the next player's 
turn and the cycle will continue
