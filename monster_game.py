import random

print("Hello wanderer, welcome to the dungeon.")
class Creature:
        def __init__(self, name, health):
            self.name = name
            self.health = health

answer = "y"

while answer.casefold() == 'y':
    
    user_name = input("What is your name?\n")
    
    print("Hello " + user_name + "! A monster approaches!")
    
    monster = Creature("Gorgon", 100)
    player = Creature(user_name, 100)
    
    print("The " + monster.name + " has spotted you, " + player.name + "!")
    
    while monster.health > 0 and player.health > 0:
        player_choice = input("What would you like to do?\n1. Attack\n2. Heal\n")
    
        if (player_choice == "1" or player_choice == "2"):
            player_choice = int(player_choice)
        else:
            print("You can't do that!")
            continue
        
        if player_choice == 1:
            atk_dmg = random.randint(1, 20)
            print(player.name + " dealt " + str(atk_dmg) + " damage to " + monster.name + "!")
            monster.health -= atk_dmg
            if monster.health <= 0:
                break
            print(monster.name + "'s health: " + str(monster.health))
        else:
            restore = random.randint(1, 15)
            if (player.health + restore) > 100:
                restore = 100 - player.health
            print(player.name + " healed themself for " + str(restore) + ".")
            print(player.name + "'s health: " + str(player.health))
            player.health += restore
            
        print("Now it's " + monster.name + "'s turn!")
    
        monster_choice = random.randint(1, 2)
    
        if monster_choice == 1:
            atk_dmg = random.randint(1, 20)
            print(monster.name + " dealt " + str(atk_dmg) + " damage to " + player.name + "!")
            player.health -= atk_dmg
            if player.health <= 0:
                break
            print(player.name + "'s health: " + str(player.health))
        else:
            restore = random.randint(1, 15)
            if (monster.health + restore) > 100:
                restore = 100 - monster.health
            print(monster.name + " healed themself for " + str(restore))
            print(monster.name + "'s health: " + str(monster.health))
            monster.health += restore

    if player.health <= 0:
        print(player.name + " has died!")
    else:
        print(monster.name + " has died!")
        print(player.name + " is victorious!")
        
    answer = input("Would you like to play again? y or n:\n")
    while answer[0].lower() not in  ("y", "n"):
        answer = input("That is an invalid input, please re-enter.\n")
