#Serrin Doscher
#CSCI 39538
#Pokemon Assignment

#THIS IS A TEST
import pprint
import random
from random import randint
import time
import sys

def slow_print(s):
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.014)

def slower_print(s):
    for char in s:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)

#========== Player Class =========#
class Player:
    def __init__(self, name, gender, nature, money, pokemon_list =[], bag =[], fainted = []):
        self.name = name
        self.gender = gender
        self.nature = nature
        self.pokemon_list = pokemon_list
        self.bag = bag
        self.money = money
        self.fainted = fainted

    def __repr__(self):
        return f"The player's name is {self.name}. \n" \
               f"The player's gender is {self.gender}.\n" \
               f"The player's nature is {self.nature}.\n" \
               f"The player has {self.money} coins.\n" \
               f"The player has {self.pokemon_list}.\n" \
               f"The player has {self.bag}.\n"

    def choose_name(self):
        player_name = str(input("Enter your players name: "))
        return player_name
    def choose_gender(self):
        player_gender = str(input("Enter your players gender: "))
        return player_gender
    def choose_nature(self):
        player_nature = str(input("Enter your players personality: "))
        return player_nature
    def choose_starter(self):
        poke_choice = int(input("\nChoose Your Starter Pokemon: \n"
              "1. Bulbasaur\n"
              "2. Charmander\n"
              "3. Squirtle\n"
              "ENTER: "))

        if poke_choice == 3:
            return Squirtle
        if poke_choice == 2:
            return Charmander
        if poke_choice == 1:
            return Bulbasaur
#========= Inventory Class =========#
class Bag:
    def __init__(self, name, description):
        self.name = name
        self.description = description

#========== Trainer Class =========#
class Trainer:
    def __init__(self, name, health, money_awarded, gift_awarded, pokemon_list = [], fainted = []):
        self.name = name
        self.health = health
        self.money_award = money_awarded
        self.gift_award = gift_awarded
        self.pokemon_list = pokemon_list
        self.fainted = fainted

#========== Pokemon Class =========#
class Pokemon:
    def __init__(self, name, health, gender, nature, moves = []):
        self.name = name
        self.health = health
        self.gender = gender
        self.nature = nature
        self.moves = moves

#========== Move List Classs =========#
class MoveList:
    def __init__(self, name, power):
        self.name = name
        self.power = power


#========== BATTLE SEQUENCE =========#
def battle_sequence(player, enemy):
    BATTLE = True
    slow_print(f'{enemy.name} challenges you to a battle!\n')
    while BATTLE:
        # time.sleep(1)
        choice = str(input("What do you want to do? \n"
                           "1. Run\n"
                           "2. Fight\n"
                           "ENTER: "))
        if choice == "1":
            BATTLE = False
            slow_print("You ran away successfully!\n")
        if choice == "2":
            print("\n========= BATTLE START! ==========\n"
                  "\nChoose a Pokemon: ")
            for i in range(len(player.pokemon_list)):
                print(f'{i+1}. {player.pokemon_list[i].name}')
            player_choice = int(input('ENTER: '))
            battle_poke = player.pokemon_list[player_choice - 1]
            slow_print(f'\nGO {battle_poke.name}!\n')

            enemy_poke = random.choice(enemy.pokemon_list)
            slow_print(f'{enemy.name} sent out {enemy_poke.name}!\n')
            while len(enemy.pokemon_list) > 0:
                #===== Player attack =====#
                print("\n==== Choose an option: ====")
                for i in range(len(battle_poke.moves)):
                    print(f'{i+1}. {battle_poke.moves[i].name}')
                print(f'{i+2}. Run')
                attack_choice = int(input("ENTER: "))
                if attack_choice == (i+2):
                    break
                poke_attack = battle_poke.moves[attack_choice - 1]
                slow_print(f'\n{battle_poke.name} used {poke_attack.name}!')

                enemy_poke.health = enemy_poke.health - poke_attack.power

                slow_print(f'\n{poke_attack.name} did {poke_attack.power} damage!\n'
                      f'\nEnemy {enemy_poke.name} health == {enemy_poke.health}\n')
                if enemy_poke.health <= 0:
                    enemy_poke.health = 1
                    slow_print(f'Enemy {enemy_poke.name} fainted\n'
                          f'You won the battle!\n'
                          f'You received {enemy_poke.name} and {enemy.money_award} coins from {enemy.name}\n\n')
                    time.sleep(1)
                    enemy.fainted.append(enemy_poke)
                    enemy.pokemon_list.remove(enemy_poke)
                    player.money = player.money + enemy.money_award
                    player.fainted.append(enemy_poke)
                    BATTLE = False
                    break
                else:
                    #===== Enemy Attack =====#
                    enemy_attack = random.choice(enemy_poke.moves)
                    slow_print(f'\nEnemy {enemy_poke.name} used {enemy_attack.name}!\n'
                               f'It hit {battle_poke.name} for {enemy_attack.power} damage\n')
                    battle_poke.health = battle_poke.health - enemy_attack.power
                    slow_print(f'\n{battle_poke.name} health == {battle_poke.health}\n')
                    if battle_poke.health <= 0:
                        battle_poke.health = 0
                        slow_print(f'{battle_poke.name} has fainted!\n')
                        player.fainted.append(battle_poke)
                        player.pokemon_list.remove(battle_poke)
                        if len(player.pokemon_list) == 0:
                            BATTLE = False
                            break
                        else:
                            break

#========= Inventory Access =========#
def access_inv():
    while True:
        print(f'\nINVENTORY:\n'
              f'1. Pokemon\n'
              f'2. Bag\n'
              f'3. Exit')
        inv_choice = int(input("ENTER: "))
        if inv_choice == 1:
            print("\nPokemon List:")
            for i in range(len(MAIN_CHARACTER.pokemon_list)):
                print(f'{i + 1}. {MAIN_CHARACTER.pokemon_list[i].name}, {MAIN_CHARACTER.pokemon_list[i].health}')
            print("Fainted List:")
            for i in range(len(MAIN_CHARACTER.fainted)):
                print(f'{i + 1}. {MAIN_CHARACTER.fainted[i].name}')
            time.sleep(1)
        if inv_choice == 2:
            print(f'\nYou have {MAIN_CHARACTER.money} coins')
            for i in range(len(MAIN_CHARACTER.bag)):
                print(f'{i + 1}. {MAIN_CHARACTER.bag[i]}')
            time.sleep(1)
        if inv_choice == 3:
            print("\n")
            break

#========== Hospital/Heal Pokemon =========#
def heal_pokemon(player):
    slow_print("Welcome to the Hospital!\n"
          "It will be 50 coins to heal all your Pokemon!")
    heal = int(input("Do you want to heal your Pokemon?\n"
                     "1. Yes\n"
                     "2. No\n"
                     "ENTER: "))

    if heal == 1 and player.money >= 50:
        for i in range(len(player.pokemon_list)):
            if len(player.fainted) > 0:
                for j in range(len(player.fainted)):
                    if player.fainted[j].health < 270:
                        health_difference = 270 - player.fainted[j].health
                        player.fainted[j].health = player.fainted[j].health + health_difference
                player.pokemon_list.append(player.fainted[j])
                player.fainted.remove(player.fainted[j])

            if player.pokemon_list[i].health < 500:
                health_difference = 270 - player.pokemon_list[i].health
                player.pokemon_list[i].health = player.pokemon_list[i].health + health_difference
        player.money = player.money - 50
        slow_print("Your Pokemon are fully healed! Come again soon!\n\n")

    elif heal == 1 and player.money < 50:
        slow_print("I'm sorry you don't have enough coins!\n")
    else:
        slow_print("Have a good day! \n")


#========== MEWSTERY =========#
def find_mew(player, mystery):
    check = 0
    print(f'A truck sits next to a river,\n'
          f'Do you want to investigate?\n'
          f'1. No\n'
          f'2. Yes')
    check_truck = int(input("ENTER: "))
    if check_truck == 1:
        slow_print("Move Along\n")

    if check_truck == 2:
        while check < 5:
            print("It's just a truck, nothing mysterious here\n"
                  "Check again?\n"
                  "1. No\n"
                  "2. Yes")
            check += 1
            check_again = int(input("ENTER: "))
            if check_again == 1:
                break
            if check_again == 2:
                continue
            if check == 4:
                slow_print("NOTHING MEWSTERIOUS HERE!")

        if check >= 5:
            slow_print("YOU FOUND MEW UNDER THE TRUCK!\n")
            player.pokemon_list.append(mystery)

#===== Board Creation =====#
class Board(list):
    def __str__(self):
        return "\n".join(" ".join(row) for row in self)

#===== Game Creation =====#
class Game(object):

    Player = "[X]"
    Grass = "[g]"
    Path = "[ ]"
    Trainer1 = "[S]"
    Trainer2 = "[B]"
    Trainer3 = "[G]"
    Item = "[0]"
    Money = "[$]"
    Mewstery = "[?]"
    Hospital = "[H]"

    Controls = [
        "A",
        None,
        "D",
        "W",
        None,
        "S",
    ]
    Start = [0, 0]
    Inventory = "i"
    Map = [["[ ]"] * 8 for i in range(8)]

    def __init__(self):
        self.flag = True
        self.map = Board(Game.Map)
        self.current_pos = Game.Start[:]
        self.prev_pos = Game.Start[:]
        self.movement()

    def __del__(self):
        pass

    def movement(self):
        playerX_change, playerY_change = self.prev_pos
        playerX, playerY = self.current_pos
        if (-1 < playerX < 8) and (-1 < playerY < 8):
            self.map[playerY_change][playerX_change] = Game.Path
            self.map[playerY][playerX] = Game.Player

        else:
            print("ENTER A VALID DIRECTION")
            self.current_pos = self.prev_pos[:]
            self.movement()

        self.map[2][1] = Game.Trainer1
        self.map[4][5] = Game.Trainer2
        self.map[0][7] = Game.Trainer3
        self.map[5][3] = Game.Item
        self.map[0][4] = Game.Money
        self.map[6][6] = Game.Mewstery
        self.map[7][0] = Game.Hospital

        #=========== BATTLE SEQUENCE CALLED =========#
        if self.map[playerY][playerX] == Game.Trainer1:
            if len(Trainer_One.fainted) > 0:
                slow_print("You already battled this Trainer\n")
            else:
                battle_sequence(MAIN_CHARACTER, Trainer_One)

        if self.map[playerY][playerX] == Game.Trainer2:
            if len(Trainer_Two.fainted) > 0:
                slow_print("You already battled this Trainer\n")
            else:
                battle_sequence(MAIN_CHARACTER, Trainer_Two)

        if self.map[playerY][playerX] == Game.Trainer3:
            if len(Trainer_Three.fainted) > 0:
                slow_print("You already battled this Trainer\n")
            else:
                battle_sequence(MAIN_CHARACTER, Trainer_Three)


        #========= ITEM PICK UP =========#
        if self.map[playerY][playerX] == Game.Item:
            if (Pidgey in MAIN_CHARACTER.pokemon_list):
                slow_print("You already picked this item up!\n")
            else:
                slow_print("PICKED UP POKEBALL!\n"
                           "It contained a Pidgey!\n\n")
                MAIN_CHARACTER.pokemon_list.append(Pidgey)
                time.sleep(1)



        #========= HOSPITAL =========#
        if self.map[playerY][playerX] == Game.Hospital:
            heal_pokemon(MAIN_CHARACTER)


        if self.map[playerY][playerX] == Game.Mewstery:
            find_mew(MAIN_CHARACTER, Mew)


    def play_game(self):
        while self.flag == True:
            print(str(self.map))
            Moves = input("Move left(A), right(D), up(W), down(S),\n"
                          "or (I) for Inventory: ").upper()
            print("\n")
            if Moves == "I":
                access_inv()

            if Moves in Game.Controls:
                direction = Game.Controls.index(Moves)
                self.prev_pos = self.current_pos[:]
                self.current_pos[direction > 2] += direction - (1 if direction < 3 else 4)
                self.movement()
            else:
                print("ENTER A VALID DIRECTION")



            #If Fainted list is greater then 0 and Players pokemon are exhausted then GAME OVER!
            if len(MAIN_CHARACTER.fainted) > 0 and len(MAIN_CHARACTER.pokemon_list) == 0:
                time.sleep(1)
                slow_print("All your pokemon have fainted!\n")
                slower_print("==== GAME OVER ====")
                break

            if len(MAIN_CHARACTER.pokemon_list) >= 5:
                slower_print("==== YOU WIN! ====\n")
                print("You collected:")
                for i in range(len(MAIN_CHARACTER.pokemon_list)):
                    slow_print(f'{i+1}. {MAIN_CHARACTER.pokemon_list[i].name}\n')
                break





if __name__ == "__main__":
    #========= MOVE LIST =========#
    ThunderShock = MoveList("Thunder Shock", 60)
    QuickAttack = MoveList("Quick Attack", 40)
    Headbutt = MoveList("HeadButt", 50)
    WaterGun = MoveList("Water Gun", randint(20,40))
    Bite = MoveList("Bite", randint(30,60))
    Surf = MoveList("Surf", 95)
    Flamethrower = MoveList("Flamethrower", 90)
    Scratch = MoveList("Scratch", 40)
    Ember = MoveList("Ember", 40)
    VineWhip = MoveList("Vine Whip", 45)
    RazorLeaf = MoveList("Razor Leaf", 55)
    Tackle = MoveList("Tackle", 40)
    Spark = MoveList("Spark", 65)
    HyperBeam = MoveList("Hyper Beam", 150)
    Rollout = MoveList("Roll Out", randint(20, 30))
    Gust = MoveList("Gust", 40)

    Nothing = MoveList("Nothing", 0)
    #========= POKEMON LIST =========#
    Pika = Pokemon("Pikachu", 250, "Female", "Cute/Aggressive", [ThunderShock, Headbutt, QuickAttack])
    Squirtle = Pokemon("Squirtle", 270, "Male", "Lazy", [WaterGun, Surf, Bite])
    Charmander = Pokemon("Charamander", 270, "Female", "Tempermental", [Flamethrower, Scratch, Ember])
    Bulbasaur = Pokemon("Bulbasaur", 210, "Male", "Sleepy", [VineWhip, RazorLeaf])
    Eevee = Pokemon("Eevee", 200, "Female", "Cute", [Tackle, QuickAttack])
    Voltorb = Pokemon("Voltorb", 225, "Unknown", "Energetic", [ThunderShock, Spark])
    Geodude = Pokemon("Geodude", 210, "Male", "Solid", [Rollout])
    Rattata = Pokemon("Rattata", 200, "Female", "Weird", [QuickAttack, Bite])
    Pidgey = Pokemon("Pidgey", 230, "Male", "Stoic", [Gust, QuickAttack])

    Mew = Pokemon("Mew", 500, "Unknown", "Unknown", [HyperBeam])

    #========== TRAINER LIST ===========#
    Trainer_One = Trainer("Stinky Pete", 100, 50, "Bedazzled Stick", [Eevee], [])
    Trainer_Two = Trainer("Billy Boy", 100, 150, "Fresh Apple", [Geodude, Voltorb], [])
    Trainer_Three = Trainer("Gary", 100, 200, "Friendship Bracelet", [Pika, Charmander], [])

    #========== CHARACTER CREATION =========#
    my_name = Player.choose_name(self='')
    my_gender = Player.choose_gender(self='')
    my_nature = Player.choose_nature(self='')
    my_starter = Player.choose_starter(self='')

    MAIN_CHARACTER = Player(my_name, my_gender, my_nature, 20, [my_starter], [], [])
    slow_print(f"\n{my_name} is a {my_gender} player and their personality is {my_nature}. \n"
          f"They start with 100 coins\n"
          f"Their starter pokemon is {my_starter.name}.\n"
          f"They start with nothing in their inventory\n")

    #========== STARTING INVENTORY =========#

    #===== TESTING DELETE LATER =====#

    # MAIN_CHARACTER = Player("Pyro", "Male", "Shy", 20, [Player.choose_starter(self='')],
    #                         ['Book', 'Letter from Mom'],
    #                         [])
    # print(f'\n{MAIN_CHARACTER}')

    #===== Main Game Loop =====#
    my_game = Game()
    my_game.play_game()

