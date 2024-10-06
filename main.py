
# initializes a list called board with 9 spaces, representing the 9 spaces on the Tic Tac Toe board
board = [" " for x in range(9)]

# Function print_board() will print the Tic Tac Toe board.
# It creates 3 strings, row1, row2, and row3, to represent each row of the board.
# The spaces in the board are filled with the values from the board list.
# Function then prints each row with separators to create the appearance of a 3×3 grid.
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Function player_move() allows a player to make a move by marking a space on the board with their icon (X or O).
# It takes the player’s icon as an argument and asks the player to enter their move (1-9) in the terminal.
# If the space the player chooses is blank, the function will place the player’s icon in that space.
# Otherwise, it will inform the player that the space is full.
def player_move(icon):
  if icon == "X":
     number = 1
  elif icon == "O":
     number = 2
  print("Your turn player {}".format(number))
  choice = int(input("Enter your move (1-9): ").strip())
  if board[choice - 1] == " ":
     board[choice - 1] = icon
  else:
    print()
    print("That space is already taken!")


# Function is_victory() checks if a player has won the game.
# It takes the player’s icon as an argument and checks if there are three of that icon in a row on the board.
# It returns True if a player has won, otherwise it returns False.

def is_victory(icon):
    if  (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

# Function is_draw() checks if the game is a draw by checking if all spaces on the board are filled.
# When all spaces are filled and no player has won, it returns True, otherwise it returns False.
def is_draw():
  if " " not in board:
    return True
  else:
    return False

# The while loop continues the game until a player has won or the game is a draw.
# Within the loop, the board is printed.
# Then, the player_move() function calls and allows the first player to make a move.
# The board prints again to show the updated state.
# Then, calling the is_victory() function will check if the first player has won.
# When they win, the game ends and a victory message shows.
# If not, the is_draw() function is called to check if the game is a draw.
# If the game is a draw, a message is displayed and the game ends.
# If neither the first player nor the game has won or ended in a draw,
# the second player makes a move and the process repeats.
while True:
  print_board()
  player_move("X")
  print_board()
  if is_victory("X"):
    print("X wins! Congratulations!")
    break
  elif is_draw():
    print("It's a draw!")
    break
  player_move("O")
  if is_victory("O"):
     print_board()
     print("O wins! Congratulations!")
     break
  elif is_draw():
    print("It's a draw!")
    break