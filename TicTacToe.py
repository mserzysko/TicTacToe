boardvalues = [' ']*10
wins=[(1,2,3), (4,5,6), (7,8,9), (1,5,9), (3,5,7), (1,4,7), (2,5,8), (3,6,9)]
pla1_win=0
pla2_win=0

#poprawić ten ties


print('Welcome to Tic Tac Toe!')
print('Our board looks like this:')

print('1'+'|'+'2'+'|'+'3')
print('-'+ '|' + '-' + '|' + '-')
print('4'+'|'+'5'+'|'+'6')
print('-'+ '|' + '-' + '|' + '-')
print('7'+'|'+'8'+'|'+'9')

print('Insert number representing a cell in order to choose that cell')
print("Ready? Let's play!")

def board(boardvalues):
    ''' Prints our board '''
    print(boardvalues[1]+'|'+boardvalues[2]+'|'+boardvalues[3])
    print('-'+ '|' + '-' + '|' + '-')
    print(boardvalues[4]+'|'+boardvalues[5]+'|'+boardvalues[6])
    print('-' + '|' + '-' + '|' + '-')
    print(boardvalues[7]+'|'+boardvalues[8]+'|'+boardvalues[9])

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
    global winner
    global pla1_win
    global pla2_win
    if len(pla1)==5:
        print('Ties!')
        winner='Player1 and Player2'
    if len(pla1)>2:
        for a, b, c in wins:
            if a in pla1 and b in pla1 and c in pla1:
                winner=player1
                print('Player1 won!')
                pla1_win+=1
                if_play_again()
                break
            elif a in pla2 and b in pla2 and c in pla2:
                winner=player2
                print('Player2 won!')
                pla2_win+=1
                if_play_again()
                break
            else:
                continue

def if_play_again():
    '''cleans out the board and starts the game again'''
    play_again=input('Do you want to play again? Yes/No: ')
    if play_again.lower()=='yes':
        global boardvalues
        global pla1
        global pla2
        global winner
        global player
        boardvalues = [' '] * 10
        pla1 = []
        pla2 = []
        winner = ''
        player = True
    else:
        pass

pla1=[]
pla2=[]
winner=''
player=True
while not winner:

    if player:
        ind=int(input('Player1: '))

        if ind in pla1 or ind in pla2:
            print('Place occupied! Try again!')
        else:
            boardvalues[ind] = player1
            pla1.append(ind)
            player = not player
            board(boardvalues)
            check_if_win()

    else:
        ind=int(input('Player2: '))

        if ind in pla1 or ind in pla2:
            print('Place occupied! Try again!')
        else:
            boardvalues[ind] = player2
            pla2.append(ind)
            player = not player
            board(boardvalues)
            check_if_win()



print(f'Player1 won {pla1_win} games and Player2 won {pla2_win} games')