from abc import ABC, abstractmethod

class Piece(ABC):
    
    def __init__(self,col:str,row:str,color:str) -> None:
        self.row = chr(row+97);
        self.col = col+1;
        self.color = color;
    @abstractmethod
    def possible_moves(self):
        pass
    
    @abstractmethod
    def isCheckMate(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class Pawn(Piece):
    def __init__(self,c,col,row,color) -> None:
        self.char = c
        self.initialPos = f'{chr(row+97)}{col+1}'
        self.possibleMoves = [];
        self.firstMove = False;
        super().__init__(col,row,color)
    def __str__(self):
        return self.char
    
    def possible_moves(self):
        self.possibleMoves=[]
        if(self.color == 'black'):
            if(not self.firstMove):
                self.possibleMoves.append(f'{self.row}{self.col+1}')
                self.possibleMoves.append(f'{self.row}{self.col+2}')
            else:
                self.possibleMoves.append(f'{self.row}{self.col+1}')
        else:
            if(not self.firstMove):
                self.possibleMoves.append(f'{self.row}{self.col-1}')
                self.possibleMoves.append(f'{self.row}{self.col-2}')
            else:
                self.possibleMoves.append(f'{self.row}{self.col-1}')
        return self.possibleMoves
    
    def isCheckMate(self):
        pass

   
    def attack(self):
        pass


class Rook(Piece):
    def __init__(self,c,col,row,color) -> None:
        self.char = c
        self.initialPos = f'{chr(row+97)}{col+1}'
        self.possibleMoves = [];
        
        super().__init__(col,row,color)
    def __str__(self):
        return self.char
    
    def possible_moves(self):
        self.possibleMoves=[]
        if(self.color == 'black'):
            if(not self.firstMove):
                # forword move
                self.possibleMoves.append(f'{self.row}{self.col+1}')
                self.possibleMoves.append(f'{self.row}{self.col+2}')
            else:
                self.possibleMoves.append(f'{self.row}{self.col+1}')
        else:
            if(not self.firstMove):
                self.possibleMoves.append(f'{self.row}{self.col-1}')
                self.possibleMoves.append(f'{self.row}{self.col-2}')
            else:
                self.possibleMoves.append(f'{self.row}{self.col-1}')
        return self.possibleMoves
    
    def isCheckMate(self):
        pass

   
    def attack(self):
        pass