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


    def block_column_win(self, board_state: BoardState):
        opponent = [s for s in PLAYER_SYMBOLS if s != self.symbol][0]
        columns = board_state.get_columns()
        col_map = { "1": columns[0],
                   "2": columns[1],
                   "3": columns[2]
                   }
        for col_nbr, col in col_map.items():
            if col.count(' ') + col.count(opponent) == 3:
                row = chr(65 + col.index(' '))
                column = col_nbr
                move = row + str(column)
                return move


    def block_row_win(self, board_state: BoardState):
        for label, row in zip('ABC', board_state.get_rows()):
            row_counts = { char:row.count(char) for char in row}
            if row_counts[' '] == 1 and 2 in row_counts.values():
                print("row almost win detected")
                move = label + str(row.index(" ") + 1)
                print(move)
                return move

    def block_diagonal_win(self, board_state: BoardState):
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


                
