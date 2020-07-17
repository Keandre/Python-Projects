def position(x,y):
    pos = 0
    if y == 2:
        pos += 3
    elif y == 1:
        pos += 6
    pos += x - 1
    return pos
def print_board(board):
    print("---------\n| ", end="")
    for i in range(9):
        if (i + 1 == 6 or i + 1 == 3):
            print("%s |\n| " % board[i], end="")
        elif (i + 1 == 9):
            print("%s | " % board[i])
        else:
            print("%s " % board[i], end="")
    print("---------")
def separate_list(obj):
    new_list = []
    for element in obj:
        new_list.append(element)
    return new_list
def is_valid(string):
    symbols = set('~!@#$%^&*()_+[]{}\|;\':\",./<>?\"abcdefghijklmnopqrstuvwxyz')
    return not any((s in string) for s in symbols)
def check_win(cells):
    # check win conditions
    # checking downwards
    for i in range(3):
        if cells[i] == cells[i + 3] and cells[i] == cells[i + 6] and cells[i] != "_":
            print(cells[i],"wins")
            return True
    # checking diagonally
    if ((cells[0] == cells[4] and cells[0] == cells[8]) or (cells[2] == cells[4] and cells[2] == cells[6])) and cells[4] != "_":
        print(cells[i], "wins")
        return True
    # checking horizontally
    for i in range(0, 9, 3):
        if cells[i] == cells[i + 1] and cells[i] == cells[i + 2] and cells[i] != "_":
            print(cells[i], "wins")
            return True
    if not "_" in cells:
        print("Draw")
        return True
    return False
def apply_move(board,x,y,char):
    if x<0 or y < 0 or x >3 or y > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    if board[position(x,y)] == "_":
        board[position(x,y)] = char
        return True
    else:
        print("This cell is occupied! Choose another one!")
        return False
    return
move = ""
board = "_________"
print_board(board)
x = 0
y = 0
player_turn = 1
while True:
    if player_turn == 1:
        move = input("Enter the coordinates: ")
        if is_valid(move):
            board = separate_list(board)
            x = int(move[0])
            y = int(move[2])
            while True:
                if apply_move(board,x,y,'X'):
                    break
                else:
                    move = input("Enter the coordinates: ")
                    while not is_valid(move):
                        print("You should enter numbers!")
                        move = input("Enter the coordinates: ")
                    x = int(move[0])
                    y = int(move[2])
            "".join(board)
            print_board(board)
            player_turn = 2
            if check_win(board):
                break
        else:
            print("You should enter numbers!")
    if player_turn == 2:
        move = input("Enter the coordinates: ")
        if is_valid(move):
            board = separate_list(board)
            x = int(move[0])
            y = int(move[2])
            while True:
                if apply_move(board,x,y,'O'):
                    break
                else:
                    move = input("Enter the coordinates: ")
                    while not is_valid(move):
                        print("You should enter numbers!")
                        move = input("Enter the coordinates: ")
                    x = int(move[0])
                    y = int(move[2])
            "".join(board)
            print_board(board)
            player_turn = 1
            if check_win(board):
                break
        else:
            print("You should enter numbers!")
