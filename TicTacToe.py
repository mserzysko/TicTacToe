
# wins=  1,2,3   4,5,6    7,8,9   1,5,9   3,5,7    1,4,7   2,5,8    3,6,9


boardvalues = ['']*10
wins=[(1,2,3), (4,5,6), (7,8,9), (1,5,9), (3,5,7), (1,4,7), (2,5,8), (3,6,9)]


def board(boardvalues):
    ''' Prints our board '''
    print(boardvalues[1]+'|'+boardvalues[2]+'|'+boardvalues[3])
    print('_'+ '|' + '_' + '|' + '_')
    print(boardvalues[4]+'|'+boardvalues[5]+'|'+boardvalues[6])
    print('_' + '|' + '_' + '|' + '_')
    print(boardvalues[7]+'|'+boardvalues[8]+'|'+boardvalues[9])


print('Welcome to Tic Tac Toe!')
print('Our board looks like this:')

print('1'+'|'+'2'+'|'+'3')
print('-'+ '|' + '-' + '|' + '-')
print('4'+'|'+'5'+'|'+'6')
print('-'+ '|' + '-' + '|' + '-')
print('7'+'|'+'8'+'|'+'9')

print('Insert number representing a cell in order to choose that cell')
print("Ready? Let's play!")


def player_marker():
    '''Should choose markers for the players'''

    player1 = ''
    player2 = ''

    while player1 != 'X' and player1 != 'O':
        player1 = input('Player1, choose "X" or "O": ')

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print(f'Player1 is {player1}, player2 is {player2}')


player_marker()
print('Player1: start!')


def check_if_win():
    for a, b, c in wins:
        if a=b=c:
            # I am not sure yet how to determine who won the game player 1 or 2: go back to it: i chyba bedzie z if
            if a='O':
                winner = 'O won!'
                break
            else:
                winner = 'X won!'
                break
        else:
            continue

winner=''
player=True
while not winner:
    board(boardvalues)

    if player1:
        #nie jestem pewna, czy nie trzeba bedize zrobic z tego intigera jeszcze
        ind=input('Player1: ')
        boardvalues[ind]=player1
        player=not player

        board(boardvalues)

        check_if_win()

    else:
        ind = input('Player2: ')
        boardvalues[ind] = player2
        player = not player

        board(boardvalues)

        check_if_win()




    # player1: insert, apply to the boardvalues, check if win, change player, player 2: insert....




    # jak zrobić wkładanie do boardvalues

    # mogę zrobi ć naprzemiennie: zmieniać kto gra in tak wpisywać czy wygrana, czy nie!



    #potem pytamy sie o wprowadzenie liczmy i wprowadzamy ją na miejsce




    break