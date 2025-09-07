import random

def print_board(board):
    print("\nBoard:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def player_move(board):
    while True:
        try:
            move = input("Enter your move (row and column, e.g. 1 2): ")
            row, col = map(int, move.split())
            if row not in [1,2,3] or col not in [1,2,3]:
                print("Please enter numbers between 1 and 3.")
                continue
            row -= 1
            col -= 1
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell already taken.")
        except:
            print("Invalid input. Enter two numbers separated by space.")

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    row, col = random.choice(empty_cells)
    print(f"Computer chose: {row+1} {col+1}")
    board[row][col] = "O"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print("You are X, Computer is O.")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("😞 Computer wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
