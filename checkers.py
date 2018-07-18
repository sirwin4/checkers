board = [["0", "o", "0", "o", "0", "o", "0", "o"],
["o", "0", "o", "0", "o", "0", "o", "0"],
["0", "0", "0", "0", "0", "0", "0", "0"],
["0", "0", "0", "0", "0", "0", "0", "0"],
["0", "0", "0", "0", "0", "0", "0", "0"],
["0", "0", "0", "0", "0", "0", "0", "0"],
["0", "x", "0", "x", "0", "x", "0", "x"],
["x", "0", "x", "0", "x", "0", "x", "0"]]

# with open("thing", "r") as var:

turn = -1

def print_board(): 
    print(["  0", "1", "2", "3", "4", "5", "6", "7"])
    line_number = 0
    for line in board:
        print(line_number, line)
        line_number += 1


print_board()

 
player = "x"

def alternate_user(number):
    global player
    if turn > 0:
        if number == "x": 
            player = "o"
            return player

        else:
            player = "x"

    return player


def mover(from_x, from_y, where_to_x, where_to_y, user):
    if (user is "x"):
        if(from_y - 1 == where_to_y):
            print("cool")
            if(from_x == where_to_x or from_x + 1 == where_to_x or from_x -1 == where_to_x):
                print("cooler")
                if(not (from_x == where_to_x and from_y - 1 == where_to_y)):
                    print("coolest")
                    if(board[where_to_y][where_to_x] == "0" or board[where_to_y][where_to_x] == "o"):
                        return True

        return False
         
    else:
        if(from_y + 1 == where_to_y):
            if(from_x == where_to_x or from_x + 1 == where_to_x or from_x -1 == where_to_x):
                if(not (from_x == where_to_x and from_y + 1 == where_to_y)):
                    if(board[where_to_y][where_to_x] == "0" or board[where_to_y][where_to_x] == "x"):
                        return True

        return False

def jump_handler(from_x, from_y, zum_x, zum_y, user):
    if(user == "x"):
        opposite_user = "o"
    else:
        opposite_user = "x"
    global board

    if(zum_x < from_x):
        if(zum_x - 1 >= 0):
            if(user == "x"):
                if(zum_y - 1 >= 0):
                    if(board[(zum_y - 1)][(zum_x - 1)] == "0"):
                        board[from_y][from_x] = "0"
                        board[zum_y][zum_x] = "0"
                        board[zum_y - 1][zum_x - 1] = user
                        if zum_y - 3 >= 0:
                            if board[zum_y - 2][zum_x - 2] == opposite_user and board[zum_y - 2][zum_x] == opposite_user:
                                if board[zum_y - 3][zum_x - 3] == "0" and board[zum_y - 3][zum_x + 1] =="0":
                                    print_board()
                                    correct_input = False
                                    while (correct_input == False):
                                        choice = input(f"{user}, you have a double jump choice, would you like to go to {zum_x - 3} or {zum_x + 1}?")
                                        choice = int(choice)
                                        if choice == (zum_x + 1):
                                            board[zum_y - 1][zum_x - 1] = "0"
                                            board[zum_y - 2][zum_x] = "0"
                                            board[zum_y - 3][zum_x + 1] = user
                                            correct_input = True
                                        
                                        if choice == (zum_x - 3):
                                            board[zum_y - 1][zum_x - 1] = "0"
                                            board[zum_y - 2][zum_x - 2] = "0"
                                            board[zum_y - 3][zum_x - 3] = user
                                            correct_input = True
                                    return board

                            if board[zum_y - 2][zum_x - 2] == opposite_user or board[zum_y - 2][zum_x] == opposite_user:
                                if board[zum_y - 2][zum_x - 2] == opposite_user and board[zum_y-3][zum_x-3] == "0":
                                    board[zum_y - 1][zum_x - 1] = "0"
                                    board[zum_y - 2][zum_x - 2] = "0"
                                    board[zum_y - 3][zum_x - 3] = user
                                    
                                if board[zum_y - 2][zum_x] == opposite_user and board[zum_y - 3][zum_x + 1] == "0":
                                    board[zum_y - 1][zum_x - 1] = "0"
                                    board[zum_y - 2][zum_x] = "0"
                                    board[zum_y - 3][zum_x + 1] = user


    if(zum_x > from_x):
        if(zum_x + 1 >= 0):
            if(user == "x"):
                if(zum_y - 1 >= 0):
                    if(board[(zum_y - 1)][(zum_x + 1)] == "0"):
                        board[from_y][from_x] = "0"
                        board[zum_y][zum_x] = "0"
                        board[zum_y - 1][zum_x + 1] = user
                        if zum_y - 3 >= 0:
                            if board[zum_y - 2][zum_x + 2] == opposite_user and board[zum_y - 2][zum_x] == opposite_user:
                                if board[zum_y - 3][zum_x - 1] == "0" and board[zum_y - 3][zum_x + 3] =="0":
                                    print_board()
                                    correct_input = False
                                    while (correct_input == False):
                                        choice = input(f"{user}, you have a double jump choice, would you like to go to {zum_x + 3} or {zum_x - 1}?")
                                        choice = int(choice)
                                        if choice == (zum_x - 1):
                                            board[zum_y - 1][zum_x + 1] = "0"
                                            board[zum_y - 2][zum_x] = "0"
                                            board[zum_y - 3][zum_x - 1] = user
                                            correct_input = True
                                        
                                        if choice == (zum_x + 3):
                                            board[zum_y - 1][zum_x + 1] = "0"
                                            board[zum_y - 2][zum_x + 2] = "0"
                                            board[zum_y - 3][zum_x + 3] = user
                                            correct_input = True
                                    return board

                            if board[zum_y - 2][zum_x + 2] == opposite_user or board[zum_y - 2][zum_x] == opposite_user:
                                if board[zum_y - 2][zum_x + 2] == opposite_user and board[zum_y - 3][zum_x + 3] == "0":
                                    board[zum_y - 1][zum_x + 1] = "0"
                                    board[zum_y - 2][zum_x + 2] = "0"
                                    board[zum_y - 3][zum_x + 3] = user
                                    
                                if board[zum_y - 2][zum_x] == opposite_user and board[zum_y - 3][zum_x + 1] == "0":
                                    board[zum_y - 1][zum_x + 1] = "0"
                                    board[zum_y - 2][zum_x] = "0"
                                    board[zum_y - 3][zum_x + 1] = user
                                                
    if(zum_x < from_x):
        if(zum_x - 1 >= 0):
            if(user == "x"):
                if(zum_y - 1 >= 0):
                    if(board[(zum_y - 1)][(zum_x - 1)] == "0"):
                        board[from_y][from_x] = "0"
                        board[zum_y][zum_x] = "0"
                        board[zum_y - 1][zum_x - 1] = user
                        if zum_y - 3 >= 0:
                            if board[zum_y - 2][zum_x - 2] == opposite_user and board[zum_y - 2][zum_x] == opposite_user:
                                if board[zum_y - 3][zum_x - 3] == "0" and board[zum_y - 3][zum_x + 1] =="0":
                                    print_board()
                                    correct_input = False
                                    while (correct_input == False):
                                        choice = input(f"{user}, you have a double jump choice, would you like to go to {zum_x - 3} or {zum_x + 1}?")
                                        choice = int(choice)
                                        if choice == (zum_x + 1):
                                            board[zum_y - 1][zum_x - 1] = "0"
                                            board[zum_y - 2][zum_x] = "0"
                                            board[zum_y - 3][zum_x + 1] = user
                                            correct_input = True
                                        
                                        if choice == (zum_x - 3):
                                            board[zum_y - 1][zum_x - 1] = "0"
                                            board[zum_y - 2][zum_x - 2] = "0"
                                            board[zum_y - 3][zum_x - 3] = user
                                            correct_input = True
                                    return board

                            if board[zum_y - 2][zum_x - 2] == opposite_user or board[zum_y - 2][zum_x] == opposite_user:
                                if board[zum_y - 2][zum_x - 2] == opposite_user and board[zum_y-3][zum_x-3] == "0":
                                    board[zum_y - 1][zum_x - 1] = "0"
                                    board[zum_y - 2][zum_x - 2] = "0"
                                    board[zum_y - 3][zum_x - 3] = user
                                    
                                if board[zum_y - 2][zum_x] == opposite_user and board[zum_y - 3][zum_x + 1] == "0":
                                    board[zum_y - 1][zum_x - 1] = "0"
                                    board[zum_y - 2][zum_x] = "0"
                                    board[zum_y - 3][zum_x + 1] = user

            if(user == "o"):
                if(zum_y + 1 >= 0):
                    if(board[(zum_y + 1)][(zum_x - 1)] == "0"):
                        board[from_y][from_x] = "0"
                        board[zum_y][zum_x] = "0"
                        board[zum_y + 1][zum_x - 1] = user
                        if zum_y + 3 >= 0:
                            if board[zum_y + 2][zum_x - 2] == opposite_user and board[zum_y + 2][zum_x] == opposite_user:
                                if board[zum_y + 3][zum_x + 1] == "0" and board[zum_y + 3][zum_x - 3] =="0":
                                    print_board()
                                    correct_input = False
                                    while (correct_input == False):
                                        choice = input(f"{user}, you have a double jump choice, would you like to go to {zum_x - 3} or {zum_x + 1}?")
                                        choice = int(choice)
                                        if choice == (zum_x + 1):
                                            board[zum_y - 1][zum_x - 1] = "0"
                                            board[zum_y + 2][zum_x] = "0"
                                            board[zum_y + 3][zum_x + 1] = user
                                            correct_input = True
                                        
                                        if choice == (zum_x - 3):
                                            board[zum_y + 1][zum_x - 1] = "0"
                                            board[zum_y + 2][zum_x - 2] = "0"
                                            board[zum_y + 3][zum_x - 3] = user
                                            correct_input = True
                                    return board

                            if board[zum_y + 2][zum_x - 2] == opposite_user or board[zum_y + 2][zum_x] == opposite_user:
                                if board[zum_y + 2][zum_x - 2] == opposite_user and board[zum_y + 3][zum_x - 3] == "0":
                                    board[zum_y + 1][zum_x - 1] = "0"
                                    board[zum_y + 2][zum_x - 2] = "0"
                                    board[zum_y + 3][zum_x - 3] = user
                                    
                                if board[zum_y + 2][zum_x] == opposite_user and board[zum_y + 3][zum_x - 1] == "0":
                                    board[zum_y + 1][zum_x - 1] = "0"
                                    board[zum_y + 2][zum_x] = "0"
                                    board[zum_y + 3][zum_x - 1] = user                                                

    return board
                        # if board[zum_x - 1][zum_y - 2] == opposite_user or board[zum_x + 1][zum_y - 2] == opposite_user:
                            

            
    # else:
    #     if(zum_x 1 + 1 <= 8):


def my_go(current_user):
    correct_input = False
    jump = False
    while (correct_input == False):
        go_x = input(f"{current_user}, input your desired piece's x coordinate to move")
        go_y = input(f"{current_user}, input your desired piece's y coordinate to move")
        to_x  = input("choose an adjacent coordinate, and input the x coordinate")
        to_y  = input("choose an adjacent coordinate, and input the y coordinate")
        go_x = int(go_x)
        go_y = int(go_y)
        to_x = int(to_x)
        to_y = int(to_y)

        if (board[go_y][go_x] is current_user and mover(go_x, go_y, to_x, to_y, current_user) is True):
            if (current_user == "o"):
                if(board[to_y][to_x] == "x"):
                    jump = True
                    

            if (current_user == "x"):
                if(board[to_y][to_x] == "o"):
                    jump = True
            correct_input = True

        else:
            print("Not a valid piece or move")

    if(correct_input is True and jump is False):
        board[go_y][go_x] = "0"
        board[to_y][to_x] = current_user
        print_board()
    
    if (correct_input is True and jump is True):
        jump_handler(go_x, go_y, to_x, to_y, current_user)
        print_board()



while (turn < 20):
    turn += 1 
    alternate_user(player)
    my_go(player)
    

    
    

