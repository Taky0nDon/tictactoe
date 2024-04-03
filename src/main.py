class BoardState:
    def __init__(self):
        self.top_row    = [" ", " ", " "]
        self.middle_row = [" ", " ", " "]
        self.bottom_row = [" ", " ", " "]

        self.POSITION_HASH = {
            "A": self.top_row,
            "B": self.middle_row,
            "C": self.bottom_row
                    }

    def update_board_state(self, position: str, player: str):
        """
:param str position: The position to change, in the form of A1, where the first character is A, B
or C, and the second character is 1, 2, or 3. The first character represents the row to alter, and the second character the column.
for Example, a position of "A1" will add an X or an O to the upper-left space.
        """
        row = position[0].upper()
        column = int(position[1]) - 1
        self.POSITION_HASH[row][column] = player

    def move_is_valid(self, position) -> bool:
        if self.POSITION_HASH[position[0].upper()][int(position[1]) - 1] != " "\
        or position[0].upper() not in "ABC"\
        or int(position[1]) not in range(1, 4):
            return False
        else:
            return True


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def take_turn(self):
        position = input("Enter the coordinates for you next move")
        return position





class BoardMaker:
    def get_current_state(self, board_state: BoardState):
        self.current_state = board_state
        top_row = board_state.top_row
        middle_row = board_state.middle_row
        bottom_row = board_state.bottom_row

        self.board_rows: list[str] = [
              f" {top_row[0]}|{top_row[1]} |{top_row[2]} ",
              f"__|__|__",
              f" {middle_row[0]}|{middle_row[1]} |{middle_row[2]} ",
              f"__|__|__",
              f" {bottom_row[0]}|{bottom_row[1]} |{bottom_row[2]} ",
              f"  |  |  "
              ]
        return self.board_rows


    def make_board(self, updated_board):
        current_board = self.get_current_state(updated_board)
        for current_row in current_board:
            print(current_row)
