# Battleship, the classic game
# Author: Matthew Walker, Oct 20, 2015

from random import randint

# Creating a playing board, 5x5
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

# Start the game
print "Let's play Battleship!"
print_board(board)


# Pick a random location for the target
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row   /for debugging
#print ship_col


# Iterate the turns for game play
for turn in range(4):
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col: # Victory condition
      print "Congratulations! You sunk my battleship!"
      break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"
            board[ship_row][ship_col] = "B"

    print_board(board)

