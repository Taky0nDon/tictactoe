PLAYER_SYMBOLS = ["o", "x"]


class BoardState:
    """
    Keeps track of the current state of the board (position of X's and O's).
    @param top_row: Holds values in the top row. list[str]
    @param middle_row: Holds values in the middle row. list[str]
    @param bottom_row: Holds values in the bottom row. list[str]
    * open_positions: a list of the coordinates that have not yet been played
    * POSITION_HASH: a dictionary that holds the current state of each row,
        assigned to string 'A', 'B', 'C'.

    Methods:
        get_board_state: returns updated POSITION_HASH
        update_board_state: updates the POSITION_HASH with latest move
        move_is_valid: checks that a given coordinate does not:
            1) exist beyond the boundaries of the board
            2) already have a piece in it
        game_is_won: checks for win conditions and draws
    """

    def __init__(self):
        self.top_row: list[str] = [" ", " ", " "]
        self.middle_row: list[str] = [" ", " ", " "]
        self.bottom_row: list[str] = [" ", " ", " "]
        self.open_positions: list[str] = [
            "A1",
            "A2",
            "A3",
            "B1",
            "B2",
            "B3",
            "C1",
            "C2",
            "C3",
        ]
        self.POSITION_HASH: dict[str, list[str]] = {
            "A": self.top_row,
            "B": self.middle_row,
            "C": self.bottom_row,
        }

    def get_rows(self) -> list[list[str]]:
        """ Return a 2D list containing the rows of the board """
        return list(self.POSITION_HASH.values())

    def get_columns(self) -> list[list[str]]:
        """ Return a 2D list containing the columns of the board """
        columns = []
        rows = self.get_rows()
        for col_num in range(3):
            column = []
            for row_index in range(3):
                column.append(rows[row_index][col_num])
            columns.append(column)
        return columns

    def get_diagonals(self) -> list[list[str]]:
        rows = self.get_rows()
        return [[rows[i][i] for i in range(3)],
                [rows[i][2 - i] for i in range(3)]
                ]

    def get_board_state(self) -> dict[str, list[str]]:
        """Return the dictionary containing up to date board status (position of places X and Os)"""
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
        if (
            self.POSITION_HASH[row][column] != " "
            or row not in "ABC"
            or column not in range(0, 3)
        ):
            return False
        else:
            return True

    def game_almost_won(self):
        state = self.POSITION_HASH

        for i in range(0, 3):
            column = [row[i] for row in state]
            col_char_count = {char: column.count(char) for char in column}
            if column.count(" ") != 1:
                continue
            elif any([count == 2 for count in col_char_count]):
                return True

        for row in state.values():
            row_char_count = {char: row.count(char) for char in row}
            if row.count(" ") != 1:
                continue
            elif any([count == 2 for count in row_char_count]):
                return True

    def game_is_won(self) -> bool:
        rows = self.get_rows()
        columns = self.get_columns()
        diagonals = self.get_diagonals()

        for row in rows:
            row_is_won = len(set(row)) == 1
            row_is_empty = all([position == " " for position in row])
            if not row_is_empty and row_is_won:
                return True

        for column in columns:
            column_is_empty = all([e == " " for e in column])
            column_is_won = len(set(column)) == 1
            if column_is_won and not column_is_empty:
                return True

        for diag in diagonals:
            diag_is_empty = all([e == " " for e in diag])
            diag_is_won = len(set(diag)) == 1
            if not diag_is_empty and diag_is_won:
                return True

        return False

    def game_is_draw(self) -> bool:
        if len(self.open_positions) < 1 and not self.game_is_won():
            return True
        else:
            return False


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
            f"  |  |  ",
        ]
        return self.board_rows

    def make_board(self, updated_board):
        current_board = self.get_current_state(updated_board)
        for current_row in current_board:
            print(current_row)
