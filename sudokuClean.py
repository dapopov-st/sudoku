# Algorithm idea + initial board inspired by https://www.youtube.com/watch?v=eqUwSA0xI-s&t=10s&ab_channel=TechWithTim
# return None line inspired by https://www.youtube.com/watch?v=G_UYXzGuqvM&ab_channel=Computerphile

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]]


def print_board(brd):
    """ Prints a formatted board"""

    print("       Sudoku board")
    print(" _______________________")
    for i in range(9):
        print("|", end=" ")
        for j in range(9):
            print(brd[i][j], end=" ")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0:
            print(" _______________________")


def is_valid(brd, num, x, y):
    """is_valid takes the board and a number num to try in the position x,y.
    Returns True if the position is valid, False otherwise"""
    for j in range(9):
        if j != y and brd[x][j] == num:
            return False  # can't put in that row since the num is already in one of the row positions

    for i in range(9):
        if x != i and brd[i][y] == num:
            return False
    # Check each square, using the following calculation to start in the top left corner
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if x != x0 + i and j != y0 + j and brd[x0 + i][y0 + j] == num:
                return False

    return True


def no_empty_squares(brd):
    """This function takes the board and returns True if there are no empty squares,
    False otherwise"""
    for i in range(9):
        for j in range(9):
            if brd[i][j] == 0:
                return False
    return True


def solver(brd):
    """This is the main function containing the backtracking algorithm. It takes the board as input
    and checks it is solvable by trying each valid number in each empty square and backtracking to the previous
    square if there is no valid solution starting from that number"""
    if no_empty_squares(brd):
        print_board(brd)
        return True

    for i in range(9):
        for j in range(9):
            if brd[i][j] == 0:  # See the return on line 79.  Will either solve the board or return None and go back to the
                for num in range(1,10):  # previous number and increment it to num+1 (since no solution resulted with num)
                    if is_valid(brd, num, i, j):
                        brd[i][j] = num
                        solver(brd)  # 1 Will return True from the base case only
                        brd[i][j] = 0  # 3 #Will only get to this line if did not return True above
                return None  # 2 Return None if the board at position was 0 (empty), and you tried all valid possibilities
                # Key: Look at lines 74 -75: If you tried all valid numbers at a square, and no solution results,
                # you're done with the inner for loop starting from the prev. valid num.  Go to Line 80 and return None.
                # Detailed explanation:
                # After tried nums 1-9 in the next empty square and none worked, done with inner for loop.
                # Go to line 80, return None
                # Pop the solver() with that specific board off the recursion stack
                # Try the next valid number up in the previous position (Note: the state from for loop is 'remembered')
                # Try again, going forward and backtracking until a solution is found or determine that there is no sol.

    return False


def display_program():
    """This function takes no inputs, displays the original board, then the final board
    if a solution is possible"""
    print("Initial board: \n")
    print_board(board)
    print("Final board: \n")
    solver(board)

display_program()
