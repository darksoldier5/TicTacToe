board = [1,2,3,4,5,6,7,8,9]
def print_board():
        print(board[0],board[1],board[2])
        print(board[3],board[4],board[5])
        print(board[6],board[7],board[8])
        pass
def choose_marker():
        x1 = input('Which marker do you want?')
        print('Player 1 marker is ', x1)
        if x1 == 'X':
            print('Player 2 marker is Y')
        else:
            print('Player 2 marker is X')
def take_input1():
    x = int(input('which cell do you want to place your marker in?'))
    board[x-1] = 'X'
def take_input2():
    y  = int(input('Which cell do you want to place your marker in?')
    board[y-1] = 'Y'
def check_win():
    if(board[0] == board[1] == board[2] == 'X'):
        print('X IS winner')
    elif(board[3] == board[4] == board[5] == 'X'):
        print('X IS winner')
    elif(board[6] == board[7] == board[8] == 'X'):
        print('X IS winner')
    elif(board[0] == board[3] == board[6] == 'X'):
        print('X have a winner')
    elif(board[1] == board[4] == board[7] == 'X'):
        print('X have a winner')
    elif(board[2] == board[5] == board[8] == 'X'):
        print('X have a winner')
    elif(board[0] == board[4] == board [8] == 'X'):
        print('X have a winner')
    elif(board[2] == board[4] == board[6] == 'X'):
        print('X have a winner')
    elif(board[0] == board[1] == board[2] == 'Y'):
        print('Y have a winner')
    elif(board[3] == board[4] == board[5] == 'Y'):
        print('Y have a winner')
    elif(board[6] == board[7] == board[8] == 'Y'):
        print('Y have a winner')
    elif(board[0] == board[3] == board[6] == 'Y'):
        print('Y have a winner')
    elif(board[1] == board[4] == board[7] == 'Y'):
        print('Y have a winner')
    elif(board[2] == board[5] == board[8] == 'Y'):
        print('Y have a winner')
    elif(board[0] == board[4] == board [8] == 'Y'):
        print('Y have a winner')
    elif(board[2] == board[4] == board[6] == 'Y'):
        print('Y have a winner')
    else:
        print("There's a tie")
def play_again():
    h = input('Do you want to play again?')
    return h == 'YES'
print('Welcome to tic tac toe')
def game_starts():
    print_board()
    choose_marker()
    t=0
    p=0
    while t<5:
        take_input1()
        print_board()
        t+=1
    while p<4:
        take_input2()
        p+=1
        print_board()
    check_win()
    if play_again():
        game_starts()
game_starts()













