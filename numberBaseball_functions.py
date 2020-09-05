from random import *


def computer_gen(_len):
    # this generates an array of 4 random integers
    rand_num = []
    while len(rand_num) < _len:
        rand_num.append(randint(0, 9))
    return rand_num


def check_same(lst):
    # this checks if there are same numbers in the array
    for i in lst:
        if lst.count(i) > 1:
            return True
    return False


def user_input():
    # this receives an input from the user
    _input = input("Please enter a 4 digit integer: ")
    return _input


def check_integer(_input):
    # this checks if the input is an integer
    try:
        int(_input)
        return True
    except ValueError:
        return False


def check_len(_int):
    # this checks the length of the integer
    if len(str(_int)) == 4:
        return True
    return False


def convert_lst(_int):
    # this converts an integer into a list
    lst = []
    for i in list(str(_int)):
        lst.append(int(i))
    return lst


def wrong_value():
    # this prints a ValueError message
    print("Invalid input. Please enter an integer.")


def wrong_len():
    # this prints a digit number error message
    print("Invalid input. Please enter a four digit integer.")


def wrong_same():
    # this prints a same number error message
    print("Invalid input. Please make sure every digit is a different number.")


def check_end(_int, lst):
    # this checks if the check has arrived the end of a list
    if _int == lst[-1]:
        return True
    else:
        return False


def check_coin(_int, lst):
    # this checks if an integer is in the list
    if lst.count(_int) > 0:
        return True
    else:
        return False


def check_index_coin(_int, lst_user, lst_com):
    # this checks if the integer has the same index in the two lists
    if lst_user.index(_int) == lst_com.index(_int):
        return True
    else:
        return False


def check_strikes(lim, stk):
    # this checks if strike limit has reached
    if stk == lim:
        return True
    else:
        return False


def check_attempt(lim, attempt):
    # this checks if attempt limit has reached
    if attempt < lim:
        return True
    else:
        return False


def end_win():
    print("You win!")


def end_lose():
    print("Game Over!")


def end_obs(out, ball, stk):
    print("Out: " + str(out) + ", "
          + "Ball: " + str(ball) + ", "
          + "Strike: " + str(stk)
          + "; Try again!")


def re_com_input():
    lst = computer_gen(4)
    if check_same(lst):
        return re_com_input()
    else:
        return lst


def re_user_input():
    lst = user_input()
    if check_integer(lst):
        if check_len(lst):
            if not check_same(lst):
                return lst
            else:
                wrong_same()
                return re_user_input()
        else:
            wrong_len()
            return re_user_input()
    else:
        wrong_value()
        return re_user_input()


def re_game(_int, lst_com, lst_user):
    out = 0
    ball = 0
    strike = 0
    if check_coin(_int, lst_com):
        if check_index_coin(_int, lst_user, lst_com):
            strike += 1
        else:
            ball += 1
    else:
        out += 1

    return [out, ball, strike]


def obs_result(lst_com, lst_user):
    out = 0
    ball = 0
    strike = 0

    for i in lst_user:
        obs = re_game(i, lst_com, lst_user)
        out += obs[0]
        ball += obs[1]
        strike += obs[-1]
    return [out, ball, strike]

def main(lst_com, attempt):
    if check_attempt(3, attempt):
        lst_user = convert_lst(re_user_input())
        obs = obs_result(lst_com, lst_user)
        end_obs(obs[0],obs[1],obs[-1])
        attempt += 1
        main(lst_com, attempt)
    else:
        end_lose()
