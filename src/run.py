from os import system
from random import randint, choice

from main import BoardState, BoardMaker, PLAYER_SYMBOLS
from Player import Player, CPUOpponent


BoardMaker = BoardMaker()
game_state = BoardState()

player = Player(PLAYER_SYMBOLS.pop(randint(0,1)))
cpu_player = CPUOpponent(PLAYER_SYMBOLS.pop(0))
current_player = player
other_player = cpu_player
draw = False

while not game_state.game_is_over():
    print(f'{game_state.get_columns()=}')
    print(f'{game_state.POSITION_HASH.values()=}')
    print(f'{other_player.symbol=}')
    if current_player.is_cpu == False:
        BoardMaker.make_board(game_state)
        print(f"{current_player.symbol}, it's your turn. Go!")
        move = input("Enter the coordinates for your move: ")
        if not game_state.move_is_valid(move):
            print("Sorry, that move is not valid.")
            continue
# TODO: put this checking logic in BoardState then pass it to the CPUOpponent
    elif any([row.count(other_player.symbol) == 2
              and row.count(" ") == 1 for row in game_state.POSITION_HASH.values()]):
        print('here')
        move = current_player.block_win(game_state)
    else:
        move = choice(game_state.open_positions)
    print(f'{move=}')
    game_state.update_board_state(position=move, player=current_player.symbol)
    game_state.open_positions.remove(move.upper())
    # system("clear")
    if not game_state.game_is_over():
        current_player, other_player = other_player, current_player
    if len(game_state.open_positions) < 1:
        draw = True


BoardMaker.make_board(game_state)
if draw:
    print("It's a draw!")
else:
    print(f"Game over! {current_player.symbol.upper()} won!")

