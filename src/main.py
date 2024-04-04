class BoardState:
    def __init__(self):
        self.top_row: list[str]    = [" ", " ", " "]
        self.middle_row: list[str] = [" ", " ", " "]
        self.bottom_row: list[str] = [" ", " ", " "]

        self.POSITION_HASH: dict[str, list[str]] = {
            "A": self.top_row,
            "B": self.middle_row,
            "C": self.bottom_row
                    }

    def get_board_state(self) -> dict[str, list[str]]:
        """ Return the dictionary containing up to date board status (position of places X and Os) """
        return self.POSITION_HASH

    def update_board_state(self, position: str, player: str) -> None:
        """
    @param position: The position to change, in the form of A1, where the first character is A, B
    or C, and the second character is 1, 2, or 3. The first character represents the row to alter, and the second character the column.
    for Example, a position of "A1" will add an X or an O to the upper-left space.
    @param player: The symbol to place on the board (X or O)
        """
        row: str = position[0].upper()
        column: int = int(position[1]) - 1
        self.POSITION_HASH[row][column] = player

    def move_is_valid(self, position: str) -> bool:
        row: str = position[0].upper()
        column: int = int(position[1]) - 1
        if self.POSITION_HASH[row][column] != " "\
        or row not in "ABC"\
        or column not in range(0, 3):
            return False
        else:
            return True

    def game_is_over(self) -> bool:
        state = self.get_board_state()
        rows = state.values()
        for row in rows:
            row_is_won = (len(set(row)) == 1)
            row_is_empty = any([column != " " for column in row])
            if row_is_empty and row_is_won:
                return True
        for i in range(0, 3):
            column = [row[i] for row in rows]
            column_is_empty = all([e == " " for e in column])
            column_is_won = len(set(column)) == 1
            if  column_is_won and not column_is_empty:
                print(rows)
                print(column)
                return True
        return False

class Player:
    def __init__(self, symbol:str):
        self.symbol = symbol

    def take_turn(self) -> str:
        position = input("Enter the coordinates for you next move: ")
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
