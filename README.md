# CS39538_PokemonHW
This repo is used for the Pokemon Hw assignment for CSCI 39538.

Added Mechanics:
I added a list to the Player and Trainer class to keep track of Fainted pokemon.
  When a pokemons health reaches 0 then it faints and is appended to the Fainted list.
  It is also removed from the respective pokemon list. 
  This is part of the Win/Lose condition. If the players pokemonlist is equal to zero and their fainted list is greater than 0   then they lose.
  
 I added a hospital to heal fainted pokemon. The player can pay 50 gold to heal all pokemon in their pokemon list and fainted   
  list. 
    KNOWN ISSUES: If there are multiple fainted pokemon the program crashes when trying to heal them, I believe it has some issue with creating the list object. Best work around is to get your pokemon healed before getting multiple fainted.
