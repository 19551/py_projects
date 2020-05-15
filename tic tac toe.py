    #games tasks
#create game board
#print game board
#play game
#check for winner
    #check rows
    #check colomns
    #check diag
#check tie
#change turn

#create game board
game_board=["_", "_", "_",
            "_", "_", "_",
            "_", "_", "_"]

turn=1
winner = None
game_char="X"
game_is_not_finished=True

#print game board
def print_board():
    print(game_board[0]+" | "+ game_board[1]+" | "+ game_board[2])
    print(game_board[3]+" | "+ game_board[4]+" | "+ game_board[5])
    print(game_board[6]+" | "+ game_board[7]+" | "+ game_board[8])

#main function - playing game
def play_game():
    while game_is_not_finished:
        handle_turn()

        check_if_game_over()

        flip_player()

    if winner=="X" or winner=="O":
        print(winner+" won! ")
    elif winner=="None":
        print("Tie!")

#change turn
def handle_turn():
    global turn
    #this variable handles acceptable values of position
    list=["1", "2", "3", "4", "5", "6", "7", "8","9"]
    #if user enters something which is not in the list, program shows message
    position = input("enter your position from 1 to 10")
    if position not in list:
        while position not in list:
            print("This value is invalid, enter again")
            position = input("enter your position from 1 to 10")


    position = int(position) - 1
    #new char can be putted only inside empty cell
    if game_board[position]=="_":
        game_board[position] = game_char
        print_board()
        turn = turn + 1

    else:
        print("This cell is not empty, try again! You lose your turn ")
        turn = turn + 1
        flip_player()
        handle_turn()

#check if someone win or it is tie
def check_if_game_over():
    check_for_win()
    check_for_tie()

#checking for winner
def check_for_win():
    global winner
    #conditions for winner if rows or columns or diagonales contain same char "X" or "O"
    row_winner=check_rows()
    col_winner=check_col()
    diag_winner=check_diag()
    #this part returns winner's name is it "X" or "O" or none if it's tie
    if row_winner:
        winner=row_winner
    elif col_winner:
        winner=col_winner
    elif diag_winner:
        winner=diag_winner
    else:
        winner=None
    return

#check if all cells are busy but there is no winner
def check_for_tie():
    global  game_is_not_finished
    if "_" not in game_board:
        game_is_not_finished=False
    return

#check rows
def check_rows():
    global game_is_not_finished
    row_1=game_board[0]==game_board[1]==game_board[2]!="_"
    row_2 = game_board[3] == game_board[4] == game_board[5] != "_"
    row_3 = game_board[6] == game_board[7] == game_board[8] != "_"
    if row_1 or row_2 or row_3:
        game_is_not_finished=False
    if row_1:
        return game_board[0]
    if row_2:
        return game_board[3]
    if row_3:
        return game_board[6]
    return

#check columns
def check_col():
    global game_is_not_finished
    col_1 = game_board[0] == game_board[3] == game_board[6] != "_"
    col_2 = game_board[1] == game_board[4] == game_board[7] != "_"
    col_3 = game_board[2] == game_board[5] == game_board[8] != "_"
    if col_1 or col_2 or col_3:
        game_is_not_finished = False
    if col_1:
        return game_board[0]
    if col_2:
        return game_board[1]
    if col_3:
        return game_board[2]
    return

#check diagonales
def check_diag():
    global game_is_not_finished
    diag_1 = game_board[0] == game_board[4] == game_board[8] != "_"
    diag_2 = game_board[2] == game_board[4] == game_board[6] != "_"
    if diag_1 or diag_2:
        game_is_not_finished = False
    if diag_1:
        return game_board[0]
    if diag_2:
        return game_board[6]
    return

#change char, if turn is odd number - then "X" moves otherwise it's "O"
def flip_player():
    global game_char
    if turn % 2 == 1:
        game_char = "X"
    else:
        game_char = "O"
    return

#execute main function
play_game()