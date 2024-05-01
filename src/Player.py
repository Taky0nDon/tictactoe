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


    def first_move(self, game_state: BoardState) -> str:
        options = ["A1", "A3", "B2", "C1", "C3"]
        move = choice([opt for opt in options if opt in game_state.open_positions])
        return move


    def block_column_win(self, board_state: BoardState) -> str:
        opponent = [s for s in PLAYER_SYMBOLS if s != self.symbol][0]
        columns = board_state.get_columns()
        for col in columns:
            if col.count(' ') + col.count(opponent) == 3:
                row = chr(65 + col.index(' '))
                column = columns.index(col) + 1
                move = row + str(column)
                return move
        return ""


    def block_row_win(self, board_state: BoardState) -> str:
        for label, row in zip('ABC', board_state.get_rows()):
            row_counts = { char:row.count(char) for char in row}
            if " " not in row_counts.keys():
                continue
            if row_counts[' '] == 1 and 2 in row_counts.values():
                print("row almost win detected")
                move = label + str(row.index(" ") + 1)
                print(move)
                return move
        return ""

    def block_diagonal_win(self, board_state: BoardState) -> str:
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
        return ""

    def get_col_win(self, board_state: BoardState) -> str:
        columns = board_state.get_columns()
        for col in columns:
            if col.count(' ') + col.count(self.symbol) == 3:
                row = chr(65 + col.index(' '))
                column = columns.index(col) + 1
                move = row + str(column)
                return move
        return ""


    def get_row_win(self, board_state: BoardState) -> str:
        row_dict = {
            label:row for label, row in zip("ABC", board_state.get_rows())
        }
        for label, row in row_dict.items():
            if " " in row and row.count(self.symbol) == 2:
                return label + str(row.index(" ") + 1)
        return ""


    def get_diag_win(self, board_state: BoardState) -> str:
        diagonals = zip(["ltr", "rtl"], board_state.get_diagonals())
        for diag in diagonals:
            if " " in diag[1] and diag[1].count(self.symbol) == 2:
                open_space = diag[1].index(" ")
                if open_space == 1:
                    return "B2"
                if diag[0] == "ltr":
                    if open_space == 0:
                        return "A1"
                    if open_space == 2:
                        return "C3"
                else:
                    if open_space == 0:
                        return "A3"
                    if open_space == 2:
                        return "C1"
        return ""




                
