theBoard = {'top-Left': ' ', 'top-Mid': ' ', 'top-Right': ' ',
            'mid-Left': ' ', 'mid-Mid': ' ', 'mid-Right': ' ',
            'low-Left': ' ', 'low-Mid': ' ', 'low-Right': ' '}

def printBoard(board):
    print(board['top-Left'] + '|' + board['top-Mid'] + '|' + board['top-Right'])
    print('-+-+-')
    print(board['mid-Left'] + '|' + board['mid-Mid'] + '|' + board['mid-Right'])
    print('-+-+-')
    print(board['low-Left'] + '|' + board['low-Mid'] + '|' + board['low-Right'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for '+ turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)