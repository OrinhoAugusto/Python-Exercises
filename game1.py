from random import randrange

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

endgame = False

# --- FUNÇÕES --- #

def lines(board):
    global vic_lines
    vic_lines = [[board[0], board[1], board[2]], 
                 [board[3], board[4], board[5]],
                 [board[6], board[7], board[8]],
                 [board[0], board[3], board[6]],
                 [board[1], board[4], board[7]],
                 [board[2], board[5], board[8]],
                 [board[0], board[4], board[8]],
                 [board[6], board[4], board[2]]]

def print_board(board):
    print("+-----+-----+-----+")
    print("|  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  |")
    print("+-----+-----+-----+")
    print("|  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  |")
    print("+-----+-----+-----+")
    print("|  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  |")
    print("+-----+-----+-----+")

def free_fields_list(board):
    global free_fields
    free_fields = []
    counter = 0
    for i in board:
        if i == "-":
            free_fields.append(counter)
        counter += 1

def draw_move(board):
    free_fields_list(board)
    move_random = randrange(len(free_fields))
    move = free_fields[move_random]
    board[move] = "X"
    print_board(board)

def enter_move(board):
    free_fields_list(board)
    global decision
    decision = int(input('Enter a move from 0 to 8: '))
    if decision not in range(0, 9):
        while decision not in range(0, 9):
            decision = int(input('Invalid output. Enter a move from 0 to 8: '))
    else: 
        while decision not in free_fields:
            decision = int(input('This spot is already taken. Enter a move from 0 to 8: '))
    board[decision] = "O"

def checkEndgame(board):
    global endgame
    free_fields_list(board)
    if free_fields == []:
        endgame = True
        print('The game tied!')

    lines(board)
    for i in range(len(vic_lines)):
        if vic_lines[i][0] == "X":
            if vic_lines[i][0] == vic_lines[i][1] == vic_lines[i][2]:
                endgame = True
                print('You lost!')
                print_board(board)
        if vic_lines[i][0] == "O":
            if vic_lines[i][0] == vic_lines[i][1] == vic_lines[i][2]:
                endgame = True
                print('You won!')
                print_board(board)

while endgame == False:
    draw_move(board)
    checkEndgame(board)
    enter_move(board)
    checkEndgame(board)