
from piece import Pawn , Rook, King ,Bishop,Knight,Queen

class Chess:
    
    def __init__(self, p1: str, p2: str) -> None:
        self.p1 = p1
        self.p2 = p2
        self.board_rows = [1, 2, 3, 4, 5, 6, 7, 8]
        self.board_cols = 'abcdefgh'
        self.board = [[None for _ in range(len(self.board_rows))] for _ in range(len(self.board_cols))]
        self.FEN_CODE = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

    def show(self):
        print("   +------------------------+")
        for i, row in enumerate(self.board):
            print(f" { i+1} |", end=" ")
            for piece in row:
                print(f"{str(piece) if piece else '.'} ", end=" ")
            print(f"|")
        print("   +------------------------+")
        print("     a  b  c  d  e  f  g  h")
    
    def load(self, fenCode=None):
        if fenCode is None:
            self.setFenCode(self.FEN_CODE)
        else:
            self.setFenCode(fenCode)

    def setFenCode(self, fenCode: str):
        code = fenCode.split(" ")[0]
        row = 0
        col = 0
        for c in code:
            if c == "/":
                row += 1
                col = 0
            elif c.isdigit():
                col += int(c)
            else:
                if c == 'p':
                    self.board[row][col] = Pawn(c, row, col, "black")
                elif c == 'P':
                    self.board[row][col] = Pawn(c, row, col, "white")
                elif c == 'r':
                    self.board[row][col] = Rook(c, row, col, "black")
                elif c == 'R':
                    self.board[row][col] = Rook(c, row, col, "white")
                elif c == 'n':
                    self.board[row][col] = Knight(c, row, col, "black")
                elif c == 'N':
                    self.board[row][col] = Knight(c, row, col, "white")
                elif c == 'b':
                    self.board[row][col] = Bishop(c, row, col, "black")
                elif c == 'B':
                    self.board[row][col] = Bishop(c, row, col, "white")
                elif c == 'q':
                    self.board[row][col] = Queen(c, row, col, "black")
                elif c == 'Q':
                    self.board[row][col] = Queen(c, row, col, "white")
                elif c == 'k':
                    self.board[row][col] = King(c, row, col, "black")
                elif c == 'K':
                    self.board[row][col] = King(c, row, col, "white")
                
                col += 1


    def move(self, From: str, to: str):
        from_col = ord(From[0].lower()) - 97
        from_row = int(From[1]) - 1
        to_col = ord(to[0].lower()) - 97
        to_row = int(to[1]) - 1
        
        if self.board[from_row][from_col] is None:
            print("There is no piece on that cell")
            return
        
        piece = self.board[from_row][from_col]
        possibleMoves = piece.possible_moves(self.board)
        
        if (to_row, to_col) in possibleMoves:
            self.board[to_row][to_col] = self.board[from_row][from_col]
            self.board[from_row][from_col] = None
            self.board[to_row][to_col].row = to_row
            self.board[to_row][to_col].col = to_col
            self.board[to_row][to_col].firstMove = False
        else:
            print("Invalid move")


    def checkMoves(self,From):
        from_col = ord(From[0].lower()) - 97
        from_row = int(From[1]) - 1
        if self.board[from_row][from_col] is None:
            print("There is no piece on that cell")
            return
        
        piece = self.board[from_row][from_col]
        # Here, you should call a method from the piece class to get possible moves
        # Assuming each piece class has a method called possible_moves(self, board)
        possibleMoves = piece.possible_moves(self.board)
        print(possibleMoves)