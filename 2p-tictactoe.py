'''
Two player TIC -TAC -TOE

HOW TO PLAY: 
Use numeric keypad to enter position of marker. 
---------------                                                                                                                       
TIC - TAC - TOE                                                                                                                       
---------------                                                                                                                       
  7 | 8 | 9                                                                                                                           
  4 | 5 | 6                                                                                                                           
  1 | 2 | 3

'''

# Print board
def printBoard(board):
    print("---------------")
    print("  "+board[7]+'|'+board[8]+'|'+board[9])
    print("  "+board[4]+'|'+board[5]+'|'+board[6])
    print("  "+board[1]+'|'+board[2]+'|'+board[3])
    print("---------------")
    
# Player 1 input for marker to start the game.
def playerInput():
    marker=''
    while not (marker == 'X' or marker =='O'):
        marker=input('Player 1: Do you want to be X or O? ').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
 
# Mark board with player's marker at given position
def place_marker(board,marker,position):
    board[position]=' '+marker+' '

# Check if the position is empty
def space_check(board, position):
    return board[position] == '   '
    
# Take player's input for marker's position and check if it is available.
def player_choice(board):
    while True:
        pos=int(input('Enter position(1-9): '))
        if pos in [1,2,3,4,5,6,7,8,9] and space_check(board,pos):
            break;
    return pos
    
# Win Condition
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# Check if board is full
def board_full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#-----------------------------------------------------------------
print("---------------")
print("TIC - TAC - TOE")
print("---------------")

board=['   ']*10
player1,player2=playerInput()
win=False
turn='P1'

#Continue playing while no one wins or game is draw.
while win==False:
    if turn =='P1':
        printBoard(board)
        position=player_choice(board)
        place_marker(board,player1,position)
        count=+count
        turn='P2'
        if win_check(board,' '+player1+' '):
            printBoard(board) 
            print('Player1 won!')
            win=True
        else:
            if board_full_check(board):
                printBoard(board) 
                print('Game is draw!')
                win=True
    else:
        printBoard(board)
        position=player_choice(board)
        place_marker(board,player2,position)
        count=+count
        turn='P1'
        if win_check(board,' '+player2+' '):
            printBoard(board) 
            print('Player2 won!')
            win=True
        else:
            if board_full_check(board):
                printBoard(board) 
                print('Game is draw!')
                win=True
