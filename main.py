"""
Author: Neel Edara, Gia Santos, Raine Gibson, Malcolm Dickens
Date: 10-1-2022 to 10-2-2022
Project Description: Water Emblem is an unique rpg game which the user goes through a dungeon.
"""
from random import randint
from time import sleep

# Menu Screen
def menu():
  sleep(0.2)
  print("".center(105,"-"))
  sleep(0.2)
  print("___       __        _____                   __________            ______  ______                  ")
  sleep(0.2)
  print("__ |     / /______ ___  /______ ________    ___  ____/_______ ___ ___  /_ ___  /_____ _______ ___ ")
  sleep(0.2)
  print("__ | /| / / _  __ `/_  __/_  _ \__  ___/    __  __/   __  __ `__ \__  __ \__  / _  _ \__  __ `__ \\")
  sleep(0.2)
  print("__ |/ |/ /  / /_/ / / /_  /  __/_  /        _  /___   _  / / / / /_  /_/ /_  /  /  __/_  / / / / /")
  sleep(0.2)
  print("____/|__/   \__,_/  \__/  \___/ /_/         /_____/   /_/ /_/ /_/ /_.___/ /_/   \___/ /_/ /_/ /_/ ")
  sleep(0.2)
  print("                                                                                                  ")
  sleep(0.2)
  print("".center(105,"-"))

# Print out the win screen
def win_screen():
  sleep(0.2)
  print("".center(60,"-"))
  sleep(0.2)
  print("__  _________ _____  __   ___       _______________   __  ")
  sleep(0.2)
  print("_ \/ /__  __ \__  / / /   __ |     / /____  _/___  | / /  ")
  sleep(0.2)
  print("__  / _  / / /_  / / /    __ | /| / /  __  /  __   |/ /   ")
  sleep(0.2)
  print("_  /  / /_/ / / /_/ /     __ |/ |/ /  __/ /   _  /|  /___ ")
  sleep(0.2)
  print("/_/   \____/  \____/      ____/|__/   /___/   /_/ |_/ _(_)")
  sleep(0.2)
  print("".center(60,"-"))

# Print out the lose screen
def loose_screen():
  sleep(0.2)
  print("".center(70,"-"))
  sleep(0.2)
  print("__  _________ _____  __   ______                                 ")
  sleep(0.2)
  print("_ \/ /__  __ \__  / / /   ___  / ______ ______ _____________     ")
  sleep(0.2)
  print("__  / _  / / /_  / / /    __  /  _  __ \_  __ \__  ___/_  _ \    ")
  sleep(0.2)
  print("_  /  / /_/ / / /_/ /     _  /___/ /_/ // /_/ /_(__  ) /  __/___ ")
  sleep(0.2)
  print("/_/   \____/  \____/      /_____/\____/ \____/ /____/  \___/ _(_)")
  sleep(0.2)
  print("-----------------------------------------------------------------")
  sleep(0.2)
  print("______        ________ _______ _______________________           ")
  sleep(0.2)
  print("___  / ______ ___  __ \___    |___  __/____  _/__  __ \          ")
  sleep(0.2)
  print("__  /  ___/ /___  /_/ /__  /| |__  /    __  /  _  / / /          ")
  sleep(0.2)
  print("_  /___/_  __/_  _, _/ _  ___ |_  /    __/ /   / /_/ /           ")
  sleep(0.2)
  print("/_____/ /_/   /_/ |_|  /_/  |_|/_/     /___/   \____/            ")
  sleep(0.2)
  print("".center(70,"-"))

usrn = []
pswd = []

def title():
    new_log = str(input("Log in or Sign up: "))

    def login():
        Username = str(input("Username/E-Mail: "))
        flag = True
        while (flag == True):
            if Username in usrn:
                Password = str(input("Password: "))
                if Password in pswd:
                    entr = str(input("Please type enter to continue. "))
                    flag = False
                else:
                    flag = True
            else:
                flag = True
    def signup():
        Username = str(input("Username/E-Mail: "))
        Password = str(input("Password: "))
        entr = str(input("Please type enter to continue. "))
        usrn.append(Username.lower())
        pswd.append(Password.lower())
        login()

    if new_log.lower() == "log in":
        login()
    elif new_log.lower() == "sign up":
        signup()

    print("")

class Player():
    def __init__(self, name, health, shield, attack, level, exp):
        self.exp = exp
        self.level = level

        self.name = name
        self.health = health
        self.shield = shield
        self.attack = attack

class Archer(Player):
    def __init__(self, name, health, shield, attack, lvl, exp):
        super().__init__(name, health, shield, attack, lvl, exp)
        self.health = health / 1.25
        self.attack = attack * randint(1, 5)

class Warrior(Player):
    def __init__(self, name, health, shield, attack, lvl, exp):
        super().__init__(name, health, shield, attack, lvl, exp)
        self.health = health * 2

class Enemy():
    def __init__(self, name, health, shield, attack):
        self.name = name
        self.health = health
        self.shield = shield
        self.attack = attack

class Boss(Enemy):
    def __init__(self, name, health, shield, attack):
        super().__init__(name, health, shield, attack)
        self.health **= 3
        self.shield *= 5
        self.attack *= 5

def xp(value):
    value = value * 10
    return value

def lev(experience):
    level_up = 1 + (experience // 50)

    return level_up

def boss_fight(player, boss):
    cont = ''
    shield_up = False
    print(f'{player.name} has been quite noisey, and the boss awakens')

    while boss.health > 0 and player.health > 0:

        sleep(1.5)
        battle_movement = input('\nWill you attack or shield? ')
        sleep(1.5)
        if (battle_movement.lower() != 'attack' and battle_movement.lower() != 'shield'):
            while (battle_movement.lower() != 'attack' and battle_movement.lower() != 'shield'):
                print('invalid input')
                battle_movement = input('\nWill you attack or shield? ')
                sleep(1.5)

        if (battle_movement.lower() == 'attack'):
            print('\nYou attack!')
            hit_or_miss = randint(1, 20)
            if (hit_or_miss <= 5):
                print('\n...But your attack missed')
                sleep(1.5)
            else:
                if shield_up == True:
                    print(f'\nYou did {player.attack / 2} damage!')
                    sleep(1.5)
                    boss.health -= player.attack / 2
                    shield_up = False
                else:
                    print(f'\nYou did {player.attack} damage!')
                    sleep(1.5)
                    boss.health -= player.attack

        elif (battle_movement.lower() == 'shield'):
            print('\nYou decided to shield')
            sleep(1.5)
            shield_up = True
        shield_up = False
        if (boss.health > 0 and player.health > 0):
            print('\nThe Boss decides to attack')
            sleep(1.5)
            x = randint(1, 10)
            if (x >= 6):
                if (shield_up == False):
                    player.health -= boss.attack
                    if player.health >= 0:
                        print(f'\nYou took damage, and only have {player.health} HP left')
                        sleep(1.5)
                    else:
                        print(f'\nYou took damage, and only have 0 HP left')
                        sleep(1.5)
                else:
                    player.health -= boss.attack / 2
                    if player.health >= 0:
                        print(f'\nYou took damage, and only have {player.health} HP left')
                        sleep(1.5)
                        shield_up = False
                    else:
                        print(f'\nYou took damage, and only have 0 HP left')
                        sleep(1.5)
                        shield_up = False

            else:
                shield_up == True
                print('The Boss has decided to shield.')
        elif (player.health <= 0):
            pass
    if (player.health > 0):
        print(f'\nCongratulations {player.name}, you win')
        sleep(1.5)
        print(f'\nYou gained {xp(boss.attack)} XP')
        sleep(1.5)
        player.exp += xp(boss.attack)
        player.level = lev(player.exp)
        print(f'\nYou\'re current level is {player.level}')
        sleep(1.50)
        win_screen()
    else:
        loose_screen()

if __name__ == '__main__':
    title()
    menu()
    play_name = input('What is the name of your warrior? ')
    print(f'\n{play_name} can be one of two classes: Warrior or Archer')
    sleep(1.5)
    print('\nWarriors have high health and consisten damage')
    sleep(1.5)
    print('\nArchers have lower health but potential for higher damage')
    sleep(1.5)
    player_class = input('\nAnd what would you like your class to be (Warrior or Archer) ')
    if (player_class.lower() != 'warrior' and player_class.lower() != 'archer'):
        while (player_class.lower() != 'warrior' and player_class.lower() != 'archer'):
            print('invalid input')
            player_class = input('\nAnd what would you like your class to be (Warrior or Archer) ')
    if (player_class.lower() == 'warrior'):
        player = Warrior(play_name, 35, 1 / 2, 10, 1, 0)
        player_health = player.health
        player_shield = player.shield
        player_attack = player.attack
    elif (player_class.lower() == 'archer'):
        player = Archer(play_name, 35, 1 / 2, 10, 1, 0)
        player_health = player.health
        player_shield = player.shield
        player_attack = player.shield

    enemy1 = Enemy('Gia', randint(1, 5), randint(1, 2), randint(1, 3))

    print('\nYour first enemy approaches, how will you react?')
    while enemy1.health > 0 and player.health > 0:
        shield_up = False
        battle_movement = input('\nWill you attack or shield? ')
        sleep(1.5)
        if (battle_movement.lower() != 'attack' and battle_movement.lower() != 'shield'):
            while (battle_movement.lower() != 'attack' and battle_movement.lower() != 'shield'):
                print('\ninvalid input')
                battle_movement = input('\nWill you attack or shield? ')
                sleep(1.5)

        if (battle_movement.lower() == 'attack'):
            print('\nYou attack!')
            sleep(1.5)
            hit_or_miss = randint(1, 20)
            if (hit_or_miss <= 5):
                print('\n...But your attack missed')
                sleep(1.5)
            else:
                print(f'\nYou did {player.attack} damage!')
                sleep(1.5)
                enemy1.health -= player.attack + lev(player.exp)
        elif (battle_movement.lower() == 'shield'):
            print('\nYou decided to shield')
            sleep(1.5)
            shield_up = True

        if (enemy1.health > 0 and player.health > 0):
            print('\nThe enemy decides to attack')
            sleep(1.5)

            if (shield_up == False):
                player.health -= enemy1.attack
                if player.health >= 0:
                    print(f'\nYou took damage, and only have {player.health} HP left')
                    sleep(1.5)
                    shield_up = False
                else:
                    print(f'\nYou took damage, and only have 0 HP left')
                    sleep(1.5)
                    shield_up = False
            else:
                player.health -= enemy1.attack / 2
                if player.health >= 0:
                    print(f'\nYou took damage, and only have {player.health} HP left')
                    sleep(1.5)
                    shield_up = False
                else:
                    print(f'\nYou took damage, and only have 0 HP left')
                    sleep(1.5)
                    shield_up = False
                sleep(1.5)
        elif (player.health <= 0 and enemy1.health > 0):
            pass

    if (player.health > 0):
        print(f'\nCongratulations {player.name}, you win')
        sleep(1.5)
        print(f'\nYou gained {xp(enemy1.attack)} XP')
        sleep(1.5)
        player.exp += xp(enemy1.attack)
        print('\nYou will use the XP to lvl up. The harder the enemy, the more XP you will get')
        sleep(3.5)
        player.level = lev(player.exp)
        print(f'\nYou\'re current level is {player.level}')
        sleep(1.5)
        if (player_health > player.health):
            player.health += (player_health + lev(player.exp) - player.health) * 1.5
        print(f'\nYour health has been partially restored and you now have {player.health} HP left')
        sleep(1.5)

        cont = ''

        while (cont != 'no'):
            print('\nAnother enemy approaches, what wll you do?')
            if (enemy1.health <= 0):
                enemy1 = Enemy('Gia', randint(1 * (2 * player.level - 1), 5 * (2 * player.level - 1)), \
                               randint(1 * (2 * player.level - 1), 2 * (2 * player.level - 1)), \
                               randint(1 * (2 * player.level - 1), 3 * (2 * player.level - 1)))
            while enemy1.health > 0 and player.health > 0:
                shield_up = False

                battle_movement = input('\nWill you attack or shield? ')
                sleep(1.5)
                if (battle_movement.lower() != 'attack' and battle_movement.lower() != 'shield'):
                    while (battle_movement.lower() != 'attack' and battle_movement.lower() != 'shield'):
                        print('invalid input')
                        battle_movement = input('\nWill you attack or shield? ')
                        sleep(1.5)

                if (battle_movement.lower() == 'attack'):
                    print('\nYou attack!')
                    hit_or_miss = randint(1, 20)
                    if (hit_or_miss <= 5):
                        print('\n...But your attack missed')
                        sleep(1.5)
                    else:
                        print(f'\nYou did {player.attack} damage!')
                        sleep(1.5)
                        enemy1.health -= player.attack + lev(player.exp)
                elif (battle_movement.lower() == 'shield'):
                    print('\nYou decided to shield')
                    sleep(1.5)
                    shield_up = True

                if (enemy1.health > 0 and player.health > 0):
                    print('\nThe enemy decides to attack')
                    sleep(1.5)

                    if (shield_up == False):
                        player.health -= enemy1.attack
                        if player.health >= 0:
                            print(f'\nYou took damage, and only have {player.health} HP left')
                            sleep(1.5)
                            shield_up = False
                        else:
                            print(f'\nYou took damage, and only have 0 HP left')
                            sleep(1.5)
                            shield_up = False
                            sleep(1.5)
                    else:
                        player.health -= enemy1.attack / 2
                        if player.health >= 0:
                            print(f'\nYou took damage, and only have {player.health} HP left')
                            sleep(1.5)
                            shield_up = False
                        else:
                            print(f'\nYou took damage, and only have 0 HP left')
                            sleep(1.5)
                            shield_up = False
                            sleep(1.5)
                elif (player.health <= 0 and enemy1.health > 0):
                    pass
            if (player.health > 0):
                print(f'\nCongratulations {player.name}, you win')
                sleep(1.5)
                print(f'\nYou gained {xp(enemy1.attack)} XP')
                sleep(1.5)
                player.exp += xp(enemy1.attack)
                player.level = lev(player.exp)
                print(f'\nYou\'re current level is {player.level}')
                sleep(1.50)
                if (player_health > player.health):
                    player.health += (player_health + lev(player.exp) - player.health) * 1.5
                print(f'\nYour health has been partially restored and you now have {player.health} HP left')
                sleep(1.5)
                cont = input('\nWould you like to continue? ')
                sleep(1.5)
                if (cont.lower() != 'yes' and cont.lower() != 'no'):
                    while (cont.lower() != 'yes' and cont.lower() != 'no'):
                        print('\ninvalid input')
                        cont = input('\nWould you like to continue ')
                        sleep(1.5)
                if (cont.lower() == 'yes'):
                    pass
                elif cont.lower() == 'no':
                    cont = 'no'

        print(f'{player.name} has decided to move on.....')
        sleep(2.0)
        boss = Boss("Gia", 10, 5, 5)
        boss_fight(player, boss)

    elif (player.health <= 0):
        loose_screen()


