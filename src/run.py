from os import system
from random import randint, choice

from main import BoardState, BoardMaker, PLAYER_SYMBOLS
from Player import Player, CPUOpponent


BoardMaker = BoardMaker()
game_state = BoardState()
symbols = PLAYER_SYMBOLS.copy()
player = Player(symbols.pop(randint(0,1)))
cpu_player = CPUOpponent(symbols.pop(0))
current_player = player
other_player = cpu_player
DRAW = False
first_cpu_move = True

while not game_state.game_is_won() and not game_state.game_is_draw():
    move = ""
    rows = game_state.get_rows()
    columns = game_state.get_columns()
    diagonals = game_state.get_diagonals()
    if not current_player.is_cpu:
        BoardMaker.make_board(game_state)
        print(f"{current_player.symbol}, it's your turn. Go!")
        move = input("Enter the coordinates for your move: ")
        if not game_state.move_is_valid(move):
            print("Sorry, that move is not valid.")
            continue

    if isinstance(current_player, CPUOpponent):
# TODO: put this checking logic in BoardState then pass it to the CPUOpponent
        row_almost_won = any(row.count(other_player.symbol) == 2 and\
                row.count(" ") == 1 for row in rows)
        column_almost_won = any(col.count(other_player.symbol) == 2 and\
                col.count(" ") == 1 for col in columns)
        diag_almost_won = any(diag.count(other_player.symbol) == 2 and\
            diag.count(" ") == 1 for diag in diagonals)

        booleans = [row_almost_won, column_almost_won, diag_almost_won, first_cpu_move]
        for bool in booleans:
            print(f"{bool=}")

        if first_cpu_move:
            move = current_player.first_move(game_state)
            first_cpu_move = False
        elif diag_almost_won:
            move = current_player.block_diagonal_win(game_state)
        elif row_almost_won:
            breakpoint()
            move = current_player.block_row_win(game_state)
        elif column_almost_won:
            move = current_player.block_column_win(game_state)
        else:
            move = choice(game_state.open_positions)

    assert(move is not None)
    game_state.update_board_state(position=move, player=current_player)
# TODO: manage open positions in the BoardState class
    game_state.open_positions.remove(move.upper())
    DRAW = game_state.game_is_draw()
    if not game_state.game_is_won() and not DRAW:
        current_player, other_player = other_player, current_player

BoardMaker.make_board(game_state)
if DRAW:
    print("It's a draw!")
else:
    print(f"Game over! {current_player.symbol.upper()} won!")
