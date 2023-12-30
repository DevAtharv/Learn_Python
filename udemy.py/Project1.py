def display_board(board):
    print("\033[H\033[J")
    print('   |  | ')
    print(' ' + board[7] + ' |' + board[8] + ' |' + board[9])
    print('-----------')
    print(' ' + board[4] + ' |' + board[5] + ' |' + board[6])
    print('-----------')
    print(' ' + board[1] + ' |' + board[2] + ' |' + board[3])
    print('   |  | ')

def player_input():
    marker = ""
    while marker != "X" and marker != 'O':
        marker = input("Player 1: Choose X or O:").upper()
    if marker == "X":
        return "X", "O"
    else:
        return "O", "X"

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        display_board(theBoard)
        if turn == 'Player 1':
            # Player1's turn.
            position = int(input('Player 1, choose your next position (1-9): '))
            if space_check(theBoard, position):
                place_marker(theBoard, player1_marker, position)
                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Congratulations! Player 1 has won the game!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'
            else:
                print('This position is already occupied. Choose another position.')
        else:
            # Player2's turn.
            position = int(input('Player 2, choose your next position (1-9): '))
            if space_check(theBoard, position):
                place_marker(theBoard, player2_marker, position)
                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Congratulations! Player 2 has won the game!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'
            else:
                print('This position is already occupied. Choose another position.')

    if not replay():
        break
