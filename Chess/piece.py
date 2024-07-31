from abc import ABC, abstractmethod

class Piece(ABC):
    
    def __init__(self,char:str,row:str,col:str,color:str) -> None:
        self.row = row
        self.col = col
        self.color = color;
        self.char = char
    def __str__(self):
        return self.char
    def is_valid(self, row: int, col: int, board):
        # Check if the position is within the bounds of the board and not occupied by a piece of the same color
        if 0 <= row < 8 and 0 <= col < 8:
            piece = board[row][col]
            return piece is None or piece.color != self.color
        return False


class Pawn(Piece):
    def __init__(self, char, row, col, color):
        super().__init__(char, row, col, color)
        self.first_move = True
    
    def __str__(self):
        return self.char

    def possible_moves(self, board):
        moves = []
        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color == "white" else 1

        # Move one square forward
        if board[self.row + direction][self.col] is None:
            moves.append((self.row + direction, self.col))

        # Move two squares forward from starting position
        if self.first_move and board[self.row + 2 * direction][self.col] is None:
            moves.append((self.row + 2 * direction, self.col))

        # Capturing diagonally
        if self.col > 0 and isinstance(board[self.row + direction][self.col - 1], Piece) and board[self.row + direction][self.col - 1].color != self.color:
            moves.append((self.row + direction, self.col - 1))

        if self.col < 7 and isinstance(board[self.row + direction][self.col + 1], Piece) and board[self.row + direction][self.col + 1].color != self.color:
            moves.append((self.row + direction, self.col + 1))

        return moves


class Rook(Piece):
    def __init__(self, char, row, col, color):
        super().__init__(char, row, col, color)

    def possible_moves(self, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for d in directions:
            for i in range(1, 8):
                new_row = self.row + i * d[0]
                new_col = self.col + i * d[1]

                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None:
                        moves.append((new_row, new_col))
                    elif board[new_row][new_col].color != self.color:
                        moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break

        return moves


class Knight(Piece):
    def __init__(self, char, row, col, color):
        super().__init__(char, row, col, color)

    def possible_moves(self, board):
        moves = []
        move_offsets = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for offset in move_offsets:
            new_row = self.row + offset[0]
            new_col = self.col + offset[1]

            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))

        return moves


class Bishop(Piece):
    def possible_moves(self, board):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for d in directions:
            for i in range(1, 8):
                new_row = self.row + i * d[0]
                new_col = self.col + i * d[1]
                if self.is_valid(new_row, new_col, board):
                    moves.append((new_row, new_col))
                    if board[new_row][new_col] is not None:  # Stop if another piece is encountered
                        break
                else:
                    break
        
        return moves


class Queen(Piece):
    def possible_moves(self, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for d in directions:
            for i in range(1, 8):
                new_row = self.row + i * d[0]
                new_col = self.col + i * d[1]
                if self.is_valid(new_row, new_col, board):
                    moves.append((new_row, new_col))
                    if board[new_row][new_col] is not None:  # Stop if another piece is encountered
                        break
                else:
                    break
        
        return moves


class King(Piece):
    def possible_moves(self, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for d in directions:
            new_row = self.row + d[0]
            new_col = self.col + d[1]
            if self.is_valid(new_row, new_col, board):
                moves.append((new_row, new_col))
        
        return moves
