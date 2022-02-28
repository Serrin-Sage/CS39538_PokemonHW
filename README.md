# CS39538_PokemonHW
This repo is used for the Pokemon Hw assignment for CSCI 39538.

Added Mechanics:
I added a fainted list to the Player and Trainer class to keep track of Fainted pokemon.
  When a pokemons health reaches 0 then it faints and is appended to the Fainted list.
  It is also removed from the respective pokemon list. 
  This is part of the Win/Lose condition. If the players pokemonlist is equal to zero and their fainted list is greater than 0 then they lose. If there Pokemon List is greater than 4 than they win!
  
 I added a hospital to heal fainted pokemon. The player can pay 50 gold to heal all pokemon in their pokemon list and fainted   
  list. 
    KNOWN ISSUES: If there are multiple fainted pokemon the program fails to heal all of them to heal them, I believe it has some issue with creating the list object. Best work around is to get your pokemon healed before getting multiple fainted.

I have made some progress on an Item class and inventory system but have not yet implemented it.

Battle Sequence works well, but had some problems with Opponent switching Pokemon, I may be able to fix that.
Tried incorporating random number generation instead of type advantage, didn't work well so each attack has a static value, will work to change that. 

I want to add random Pokemon battles but will only do it if I have time to spare.


KNOWN ISSUES: The bottom and right of my grid don't have boundaries and the program will crash if the player tries moving past those boundaries. 
Giving Trainers the same symbol on the map causing all trainer battles to be called when crossing over one of the symbols. Made it so each trainer had a unique symbol.

