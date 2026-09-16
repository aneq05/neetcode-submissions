class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return_1 = self.check_rows_cols(board)
        return_2 = self.check_boxes(board)
        return return_1 and return_2

    def check_boxes(self, board: List[List[str]]) -> bool:
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                seen = []
                for r in range(3):
                    for c in range(3):
                        element = board[box_r + r][box_c + c]
                        if element == '.':
                            continue
                        if element not in seen:
                            seen.append(element)
                        else:
                            return False
        return True


    def check_rows_cols(self, board: List[List[str]]) -> bool:
        for r in range(9):
            row_seen = []
            col_seen = []
            for c in range(9):
                row_el = board[r][c]
                col_el = board[c][r]
                if row_el != '.':
                    if row_el in row_seen:
                        return False
                    row_seen.append(row_el)
                if col_el != '.':
                    if col_el in col_seen:
                        return False
                    col_seen.append(col_el)
        return True
