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
<<<<<<< HEAD
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
=======
        opponent = [s for s in PLAYER_SYMBOLS if s != self.symbol][0]
        print(f"{opponent=}")
        columns = board_state.get_columns()
        col_map = { "1": columns[0],
                   "2": columns[1],
                   "3": columns[2]
                   }
        for col_nbr, col in col_map.items():
            if col.count(' ') + col.count(opponent) == 3:
                print(f"Column {col_nbr} almost win detected")
                row = chr(65 + col.index(' '))
                column = col_nbr
                move = row + str(column)
                print(f"{move=}")
>>>>>>> was-working
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
        diags = {
                label: diag for label, diag in zip\
                        (
                            ("ABC", "CBA"),
                            board_state.get_diagonals()
                        ) 
                }
        
        opp_symbol = [symbol for symbol in PLAYER_SYMBOLS if symbol != self.symbol] 
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
        pass
        if current_diag.count(self.symbol) == 2:
            return 


                
