
#Create a board and a table of 'moves'
#make players choose X or O
# game itself plus checking if somebody did not won

# wins   1,2,3   4,5,6    7,8,9   1,5,9   3,5,7    1,4,7   2,5,8    3,6,9



boardvalues=['']*10

def board(boardvalues):
    '''prints our board'''
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
