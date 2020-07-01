import random
import os


def intro():
    print('Welcome!\nFigure out the 4 digits to win, lets see if you are a haxor.\nYou have 3 attempts to get'
          'it right.\nFormat example when you enter your attempt -> X X X X')
    return None


def game(incoming):
    # math
    rannum1 = random.randint(1, 2) + incoming
    rannum2 = random.randint(1, 2) + incoming
    rannum3 = random.randint(1, 2) + incoming
    rannum4 = random.randint(1, 2) + incoming
    comp_added = rannum1 + rannum2 + rannum3 + rannum4
    comp_multi = rannum1 * rannum2 * rannum3 * rannum4
    div_num1 = rannum1 * 2
    div_num4 = rannum4 * 3
    mod_num2 = rannum2 % 2
    mod_num3 = rannum3 % 2
    lives = 3

    print('\nLevel: ' + str(incoming))

    print('\nAll numbers add up to: ' + str(comp_added))
    print('All numbers multiplied: ' + str(comp_multi))
    print('The 1st number is 1/2 of: ' + str(div_num1))

    if mod_num2 == 0:
        print('The 2nd number even')
    else:
        print('The 2nd number odd')
    if mod_num3 == 0:
        print('The 3rd number even')
    else:
        print('The 3rd number odd')

    print('The 4th number is 1/3 of: ' + str(div_num4))

    while True:
        print('\nLives:' + str(lives) + '\n')
        in_list = input().split()
        guess_added = 0
        guess_multi = 1
        lives -= 1
        if len(in_list) != 4:
            print('Format is wrong.')
        else:
            for i in in_list:
                guess_added += int(i)

            for i in in_list:
                guess_multi *= int(i)

            if guess_added == comp_added and guess_multi == comp_multi:
                return True
            elif lives < 1:
                return False, '\nAnswer: ' + str(rannum1) + ' ' + str(rannum2) + ' ' + str(rannum3) + ' ' + str(rannum4)
            else:
                print('Wrong, try again...')



'''main function'''


def main_func():
    level = 1
    maxlevel = 1000000
    gamestatus = True

    while gamestatus == True:
        intro()
        gamestatus = game(level)
        level += 1
        os.system('cls')

    print(gamestatus[1])
    print('Game Over. Your max level was ' + str(level))


if __name__ == '__main__':
    main_func()