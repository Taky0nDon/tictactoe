from random import choice
from main import BoardState, PLAYER_SYMBOLS

class Player:
    def __init__(self, symbol:str, cpu=False):
        self.symbol = symbol
        self.is_cpu = cpu

    def take_turn(self, position) -> str:
        return position


class CPUOpponent(Player):
    def __init__(self, symbol):
        self.is_cpu = True
        self.symbol = symbol

    def block_column_win(self, board_state: BoardState):
        opponent = PLAYER_SYMBOLS.copy().remove(self.symbol)[0]
        columns = board_state.get_columns()
        print("**")
        print(columns)
        print("**")
        for column_number, col in enumerate(columns):
            if col.count(" ") + col.count(opponent) == 3:
                row = chr(67 - col.index(" "))
                print(f"{column_number=}")
                move = row + str(column_number)
                print(move)
                return move


    def block_row_win(self, board_state: BoardState):
        for label, row in zip('ABC', board_state.get_rows()):
            if row.count(" ") != 1:
                return choice(board_state.open_positions)
            row_counts = { char:row.count(char) for char in row}
            if row_counts[' '] == 1 and 2 in row_counts.values():
                print("row almost win detected")
                return label + str(row.index(" ") + 1)

    def block_diagonal_win(self, board_state: BoardState):
        print(f"{self.symbol=}")
        print(f"{PLAYER_SYMBOLS=}")
        diags = {
                label: diag for label, diag in zip\
                        (("ABC", "CBA"), board_state.get_diagonals()) 
                }
        
        opp_symbol = [symbol for symbol in PLAYER_SYMBOLS if symbol != self.symbol][0]
        for diag in diags:
            current_diag = diags[diag]
            if current_diag.count(" ") != 1:
                return choice(board_state.open_positions)
            if current_diag.count(opp_symbol) == 2:
                open_index = current_diag.index(" ")
                desired_col = str(open_index + 1)
                open_row = diag[open_index]
                blocking_move = open_row + desired_col
                return blocking_move

    def get_diag_win(self, board_state: BoardState):
        if current_diag.count(self.symbol) == 2:
            return 


                
