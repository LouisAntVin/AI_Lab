import random

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_win(board, player):
    for row in board:
        if all(mark == player for mark in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def select_spot(board, player):
    while True:
        row = int(input(f'Player {player}, enter row (1, 2, or 3): '))
        col = int(input(f'Player {player}, enter column (1, 2, or 3): '))
        row-=1
        col-=1
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            return row, col
        print('Invalid move! Try again.')

def play_game():
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)

    while True:
        print_board(board)
        row, col = select_spot(board, current_player)
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f'Player {current_player} wins!')
            break
        if check_draw(board):
            print_board(board)
            print('It\'s a draw!')
            break
        current_player = players[(players.index(current_player) + 1) % 2]

play_game()

