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
        row = position[0]
        column = int(position[1]) - 1
        self.POSITION_HASH[row][column] = player

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


    def make_board(self):
        current_board = self.get_current_state(updated_board)
        for current_row in current_board:
            print(current_row)
