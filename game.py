def print_board(board):
    print("  " + " | ".join(board[0]))
    print("-------------")
    print("  " + " | ".join(board[1]))
    print("-------------")
    print("  " + " | ".join(board[2]))

# Function to check if someone has won
def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        row = int(input("Enter the row (1-3): ")) - 1
        col = int(input("Enter the column (1-3): ")) - 1
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print("Player", current_player, "wins!")
                break
            elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

# Start the game
play_game()