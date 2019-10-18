


boardvalues = [' ']*10
wins=[(1,2,3), (4,5,6), (7,8,9), (1,5,9), (3,5,7), (1,4,7), (2,5,8), (3,6,9)]


def board(boardvalues):
    ''' Prints our board '''
    print(boardvalues[1]+'|'+boardvalues[2]+'|'+boardvalues[3])
    print('-'+ '|' + '-' + '|' + '-')
    print(boardvalues[4]+'|'+boardvalues[5]+'|'+boardvalues[6])
    print('-' + '|' + '-' + '|' + '-')
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

    global player1
    global player2

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
        global winner
        players='XO'

        if boardvalues[a]==boardvalues[b]==boardvalues[c] and a in players:
            #wszystko działą, ALE boardvalues wszsytkie sa 0 wiec zawsze powyzszy warunek spelniony, dopiero dziala jak na koncu jest X a X wygrywa
            #mozna zrobic ewentualknie liste graczy i X i O i czy boardvalues a in this: tu problem: a przed zmiana jest intigerem

            # I am not sure yet how to determine who won the game player 1 or 2: go back to it: i chyba bedzie z if
            if boardvalues[a]=='O':
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
    check_if_win()

    if player:
        ind=int(input('Player1: '))
        boardvalues[ind]=player1
        player=not player

        board(boardvalues)

        check_if_win()
# if check_if_win nie ma po tych if-ach to się zawiesza z jakiegoś powodu
    else:
        ind = int(input('Player2: '))
        boardvalues[ind] = player2
        player = not player

        board(boardvalues)
        check_if_win()


# Działa! Ale nie działa sprawdzanie czy jest wygrana
# można nadpisywać numerki: trzeba to ukrócić