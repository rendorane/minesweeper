import random
import time

width = 10
height = 10
mines = 8
checked = []


def minesweeper():

    hidden_board = create_hidden_board()
    players_board = [[" " for _ in range(width)] for _ in range(height)]
    game_on = True
    start_time = time.time()
    while game_on:
        print_board(players_board)
        try:
            y = int(input("Enter y: "))
            x = int(input("Enter x: "))
            if hidden_board[y][x] == 9:
                players_board[y][x] = hidden_board[y][x]
                print("BANG!")
                players_board = reveal_mines(hidden_board)
                print_board(players_board)
                game_on = False
            else:
                players_board[y][x] = hidden_board[y][x]
            players_board = check_neighbours(y, x, hidden_board, players_board)
            if check_won(players_board):
                game_on = False
                reveal_mines(hidden_board)
                end_time = time.time()
                print_board(players_board)
                print("You win! Time: {:.2f} second(s)".format(end_time-start_time))
        except ValueError:
            print("Enter an integer value from 0 to {}".format(width - 1))
        except IndexError:
            print("Index Error. Enter an integer value from 0 to {}".format(width - 1))


def create_hidden_board():
    hidden_board = [[" " for _ in range(width)] for _ in range(height)]
    i = mines
    while i > 0:
        mine_y = random.randint(0, height - 1)
        mine_x = random.randint(0, width - 1)
        if hidden_board[mine_y][mine_x] != 9:
            hidden_board[mine_y][mine_x] = 9
            i -= 1
    for y in range(height):
        for x in range(width):
            if hidden_board[y][x] == 9:
                continue
            else:
                hidden_board[y][x] = mines_around(y, x, hidden_board)
    return hidden_board


def print_board(board):
    print('  ', end=' ')
    for j in range(width):
        print(j, end=' ')
    print()
    print('  ', end=' ')
    for i in range(width):
        print('-', end=' ')
    print()
    i = 0
    for row in board:
        print(str(i) + '|', *row)
        i += 1


def mines_around(y, x, hidden_board):
    mines_counter = 0

    if y + 1 <= height - 1 and hidden_board[y + 1][x] == 9:
        mines_counter += 1
    if y + 1 <= height - 1 and x - 1 >= 0 and hidden_board[y + 1][x - 1] == 9:
        mines_counter += 1
    if y + 1 <= height - 1 and x + 1 <= width - 1 and hidden_board[y + 1][x + 1] == 9:
        mines_counter += 1
    if x + 1 <= width - 1 and hidden_board[y][x + 1] == 9:
        mines_counter += 1
    if y - 1 >= 0 and hidden_board[y - 1][x] == 9:
        mines_counter += 1
    if y - 1 >= 0 and x - 1 >= 0 and hidden_board[y - 1][x - 1] == 9:
        mines_counter += 1
    if x - 1 >= 0 and hidden_board[y][x - 1] == 9:
        mines_counter += 1
    if y - 1 >= 0 and x + 1 <= width - 1 and hidden_board[y - 1][x + 1] == 9:
        mines_counter += 1

    return mines_counter


def check_neighbours(y, x, hidden_board, players_board):
    global checked

    if [y, x] not in checked:

        checked.append([y, x])

        if hidden_board[y][x] == 0:

            players_board[y][x] = hidden_board[y][x]

            if y + 1 <= height - 1:
                check_neighbours(y + 1, x, hidden_board, players_board)
            if y + 1 <= height - 1 and x - 1 >= 0:
                check_neighbours(y + 1, x - 1, hidden_board, players_board)
            if y + 1 <= height - 1 and x + 1 <= width - 1:
                check_neighbours(y + 1, x + 1, hidden_board, players_board)
            if x + 1 <= width - 1:
                check_neighbours(y, x + 1, hidden_board, players_board)
            if y - 1 >= 0:
                check_neighbours(y - 1, x, hidden_board, players_board)
            if y - 1 >= 0 and x - 1 >= 0:
                check_neighbours(y - 1, x - 1, hidden_board, players_board)
            if x - 1 >= 0:
                check_neighbours(y, x - 1, hidden_board, players_board)
            if y - 1 >= 0 and x + 1 <= width - 1:
                check_neighbours(y - 1, x + 1, hidden_board, players_board)

        if hidden_board[y][x] != 0:
            players_board[y][x] = hidden_board[y][x]

    return players_board


def check_won(board):
    i = 0
    for row in board:
        for cell in row:
            if cell == " ":
                i += 1
    if i == mines:
        return True
    else:
        return False


def reveal_mines(board):
    for y in range(height):
        for x in range(width):
            if board[y][x] == 9:
                board[y][x] = 'X'
    return board


minesweeper()
