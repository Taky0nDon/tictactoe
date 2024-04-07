from main import BoardState

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

    def cpu_turn(self):
        pass

    def block_win(self, board_state: BoardState):
        for label, row in board_state.POSITION_HASH.items():
            if row.count(" ") > 1:
                continue
            row_counts = {}
            for space in row:
                if space not in row_counts.keys():
                    row_counts[space] = 1
                else:
                    row_counts[space] += 1
            if " " in row_counts.keys() and 2 in row_counts.values():
                return label + str(row.index(" ") + 1)


