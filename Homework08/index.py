"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.

def mc_trial(board, player):
    """The function play a game starting with the given player by making
        random moves, alternating between players."""
    while board.check_win() is None:
        empty_list = board.get_empty_squares()
        rand_empty_item = random.choice(empty_list)
        board.move(rand_empty_item[0], rand_empty_item[1], player)
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """The function score the completed board and update the scores grid."""
    dim = int(board.get_dim())
    winner = board.check_win()
    other_player = provided.switch_player(player)
    for row in range(dim):
        for col in range(dim):
            if winner == player and board.square(row, col) == player:
                scores[row][col] += SCORE_CURRENT
            elif winner == player and board.square(row, col) == other_player:
                scores[row][col] += (-1) * SCORE_OTHER
            elif winner == other_player and board.square(row, col) == player:
                scores[row][col] += (-1) * SCORE_CURRENT
            elif winner == other_player and board.square(row, col) == other_player:
                scores[row][col] += SCORE_OTHER


def get_best_move(board, scores):
    """The function find all of the empty squares with the maximum score
        and randomly return one of them as a (row,column) tuple."""
    dim = int(board.get_dim())
    max_score = -100
    tuple_list = []
    for row in range(dim):
        for col in range(dim):
            if scores[row][col] >= max_score and board.square(row, col) == provided.EMPTY:
                max_score = scores[row][col]
    for row in range(dim):
        for col in range(dim):
            if scores[row][col] == max_score and board.square(row, col) == provided.EMPTY:
                tuple_list.append((row, col))
    return random.choice(tuple_list)


def mc_move(board, player, trials):
    """The function use the Monte Carlo simulation described above to return
        a move for the machine player in the form of a (row,column) tuple."""
    dim = int(board.get_dim())
    scores = [[0 for col in range(dim)]
              for row in range(dim)]
    for _ in range(trials):
        cloned_board = board.clone()
        mc_trial(cloned_board, player)
        mc_update_scores(scores, cloned_board, player)
    best_move = get_best_move(board, scores)
    return best_move


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

