from os import system
from random import randint, choice

from main import BoardState, BoardMaker, PLAYER_SYMBOLS
from Player import Player, CPUOpponent


def check_for_blocks() -> str:
    """ Returns a string representing the axis to block """
    axis = ""
    row_almost_won = any(row.count(other_player.symbol) == 2 and\
            row.count(" ") == 1 for row in game_state.get_rows())
    column_almost_won = any(col.count(other_player.symbol) == 2 and\
            col.count(" ") == 1 for col in game_state.get_columns())
    diag_almost_won = any(diag.count(other_player.symbol) == 2 and\
            diag.count(" ") == 1 for diag in game_state.get_diagonals())
    if diag_almost_won:
        axis = "diag"
    elif row_almost_won:
        axis = "row"
    elif column_almost_won:
        axis = "col"
    return axis


def block_player(axis):
    move = choice(game_state.open_positions)
    if axis == "diag":
        move = cpu_player.block_diagonal_win(game_state)
    elif axis == "row":
        move = cpu_player.block_row_win(game_state)
    elif axis == "col":
        move = cpu_player.block_column_win(game_state)
    return move


BoardMaker = BoardMaker()
game_state = BoardState()
symbols = PLAYER_SYMBOLS.copy()
player = Player(symbols.pop(randint(0,1)))
cpu_player = CPUOpponent(symbols.pop(0))
player_turn = True
cpu_turn = False
DRAW = False

while not game_state.game_is_won() and not game_state.game_is_draw():
# TODO: put this checking logic in BoardState then pass it to the CPUOpponent
    current_player = player
    other_player = cpu_player
    if player_turn is True:
        BoardMaker.make_board(game_state)
        print(f"{current_player.symbol}, it's your turn. Go!")
        move = input("Enter the coordinates for your move: ")
        if not game_state.move_is_valid(move):
            print("Sorry, that move is not valid.")
            continue
<<<<<<< HEAD
=======
    elif diag_almost_won:
        move = current_player.block_diagonal_win(game_state)
    elif row_almost_won:
        move = current_player.block_row_win(game_state)
    elif column_almost_won:
        print("column almost won")
        move = current_player.block_column_win(game_state)
>>>>>>> was-working
    else:
        current_player = cpu_player
        other_player = player
        axis_to_block = check_for_blocks()
        print(f"{axis_to_block=}")
        move = block_player(axis_to_block)
    print(f"{move=}")
    game_state.update_board_state(position=move, player=current_player.symbol)
    game_state.open_positions.remove(move.upper())
    DRAW = game_state.game_is_draw()
    if not game_state.game_is_won() and not DRAW:
        player_turn, cpu_turn = cpu_turn, player_turn


BoardMaker.make_board(game_state)
if DRAW:
    print("It's a draw!")
else:
    print(f"Game over! {current_player.symbol.upper()} won!")
