'''
Kyle Nida
Z 23410025
Due: 9/12/2018
Homework 1
'''

'''Consider the following sequence of strings S0,S1,S2,...: S0 = "x", S1= "y", and 
Sn= Sn-1||Sn-2 for n>1, where || denotes concatenation. For instance S2="yx", S3="yxy".
Write a function fib_string(n), which for a given natural number n returns the string Sn.'''

def fib_string(n):
    '''n = length of returned string'''

    str_list = ['x', 'y']

    # n = 0 return 'x' base case
    if n == 0: 
        return str_list[0]

    # n = 1 return 'y' base case
    elif n == 1: 
        return str_list[1]

    # n > 1 case
    else:  
        
        '''loop to iterate through loop and concat
        strings in the list accordingly'''
        for i in range(0,n-1): 
            new_string = str_list[-1] + str_list[-2]
            str_list.append(new_string)
        
        # returns desired concatenation for given 'n'
        return str_list[-1]
    

'''Write a Python function gcd_list(ls) which, given a list of integers ls, returns 
the greatest common divisor of the numbers in ls. For instance, gcd_list([12,20,-10]) 
should return 2. Hint: You can use the abs() function to compute the absolute value of 
a number.'''

def gcd_list(ls):

    # new list with all positive list values
    abs_list = []

    # list for all divisors
    divisors = []

    # list for found greatest common divisor
    final_gcd = []

    # loop retrieving positive values
    for i in range(0, len(ls)):
        temp = abs(ls[i])
        abs_list.append(temp)

        # nested for loop to get all divisors in given list
        for j in range(1, temp+1):
            if temp % j == 0:
                divisors.append(j)
    
    # loop to check for greatest common divisors
    # the insert found values into final_gcd
    for value in range(0, len(divisors)+1):
        if divisors.count(value) == 3 and value != 1:
            final_gcd.append(value)

    return final_gcd

'''
Write a function game(), which enables a user to play the following game against the 
computer—the computer must always win if it has the first move:  The game starts with 
a pile of 39 coins being on the table. Now the first player may remove 1, 2 or 3 coins. 
Then the second player may remove 1, 2 or 3 coins, then the first Player may remove 1, 2 
or 3 coins etc. The player taking the last coin wins'''

import random # library for RNG
def game():
    coins = 39

    ''' initializing player to a random choice between
    the user and the computer to see who goes first'''
    player = random.choice(['User', 'Computer']) 
    round = 1

    '''if statement to initialize first and second player to game'''
    if player == 'User':
        player_one = player #player=User
        player_two = 'Computer'
    else:
        player_one = player #player=Computer
        player_two = 'User'
    
    print('First round: ', player, '\n')

    # Game start
    while coins > 0:
        if round % 2 != 0:
            player = player_one
        else:
            player = player_two

        if player == 'User': #Users round to remove coins
            choice = int(input('How many coins will you take?(1,2, or 3): '))
        if player == 'Computer': #Computers round to remove coins
            choice = random.randint(1,3)

            '''If statement checking for first player and setting 
            up to let the computer win if it goes first'''
            if player_one == 'Computer':
                #temp values for coins to allow checks later for cpu win
                temp_coins = coins
                temp_coins = temp_coins - choice

                #if 3 coins are left, cpu will pick 3 and win
                if coins <= 3:
                    choice = coins

                #setup so user will always have to pick from a remaining coin
                #value of 4, if cpu goes first so the computer always wins if it goes first.
                else:
                    while temp_coins % 4 != 0: 
                        temp_coins = coins
                        choice = random.randint(1,3)
                        temp_coins = temp_coins - choice
        
                        #failsafe so the remaining coin values cannot be negative
        if choice > coins:
            choice = coins

        #output formatting for rounds, player display, and coins remaining
        print('Round',round,':', player, 'has removed', choice, 'coins')
        winner = player #winner of the game
        coins = coins - choice 
        print("Remaining coins: ", coins)
        round = round + 1 #increasing round value to make another round

    print("Winner is: ", winner)

# main function
if __name__ == '__main__':

    # test for fib_string
    print(fib_string(4))

    # test for gcd_list
    ls = [12,20,-10]
    print(gcd_list(ls))

    # test for game
    game()