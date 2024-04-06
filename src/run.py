from random import randint, choice
from main import BoardState, BoardMaker, Player, CPUOpponent


BoardMaker = BoardMaker()
game_state = BoardState()

symbols = ["x", "o"]

player = Player(symbols.pop(randint(0,1)))
cpu_player = CPUOpponent(symbols.pop(0))
current_player = player
other_player = cpu_player

while not game_state.game_is_over():
    if current_player.is_cpu == False:
        BoardMaker.make_board(game_state)
        print(f"{current_player.symbol}, it's your turn. Go!")
        move = input("Enter the coordinates for your move: ")
        if not game_state.move_is_valid(move):
            print("Sorry, that move is not valid.")
            continue
        cpu_player.open_positions.remove(move.upper())
    else:
        move = choice(cpu_player.open_positions)
    game_state.update_board_state(position=move, player=current_player.symbol)
    if not game_state.game_is_over():
        current_player, other_player = other_player, current_player
    if len(cpu_player.open_positions) < 1:
        game_state.game_is_over("true")
        print("It's a draw!")

BoardMaker.make_board(game_state)
print(f"Game over! {current_player.symbol.upper()} won!")

