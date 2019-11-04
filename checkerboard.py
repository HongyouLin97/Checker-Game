class Checkerboard:
    
    # Define the representation of the checkerboard, and its default initial state.
    def __init__(self):
        r1 = [0, 1, 0, 1, 0, 1, 0, 1]
        r2 = [1, 0, 1, 0, 1, 0, 1, 0]
        r3 = [0, 1, 0, 1, 0, 1, 0, 1]
        r4 = [0, 0, 0, 0, 0, 0, 0, 0]
        r5 = [0, 0, 0, 0, 0, 0, 0, 0]
        r6 = [-1, 0, -1, 0, -1, 0, -1, 0]
        r7 = [0, -1, 0, -1, 0, -1, 0, -1]
        r8 = [-1, 0, -1, 0, -1, 0, -1, 0]
        self.board = [r1, r2, r3, r4, r5, r6, r7, r8]
        self.turn = 1

    # Method that checks the two conditions for losing a game: 1. there is no more chess piece left for one player; 2. there are still chess pieces left, but none of them has legal move available.
    def CheckLost(self): 
        # Condition 1 -- no more chess piece left
        if self.NoPiecesLeft():
            return True
        # Condition 2 -- remaining chess pieces cannot perform legal move
        for i in range(8):
            for j in range(8):
                if self.board[i][j] / self.turn > 0 and self.MoveAvailable((i,j)): 
                    return False
        return True
    
    # Method designed for CheckLost() method, mainly checking whether there are available chess pieces left for one player or not.
    def NoPiecesLeft(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] / self.turn > 0:
                    return False
        return True

    # Method that checks wehther the given chess piece can perform legal move.
    def MoveAvailable(self, piece):
        if self.CaptureAvailable(piece):
            return True
        else:
            i = piece[0]
            j = piece[1]
            res = self.LegalMove(piece, (i + 1, j + 1)) \
                   or self.LegalMove(piece, (i + 1, j - 1)) \
                   or self.LegalMove(piece, (i - 1, j + 1)) \
                   or self.LegalMove(piece, (i - 1, j - 1))
            return res

    # Check whether there are chess pieces of the opponent that could be legally captured (eliminated) from the key board.
    def CaptureAvailable(self, piece):
        i = piece[0]
        j = piece[1]
        return self.LegalCapture(piece, (i + 2, j + 2)) \
               or self.LegalCapture(piece, (i + 2, j - 2)) \
               or self.LegalCapture(piece, (i - 2, j + 2)) \
               or self.LegalCapture(piece, (i - 2, j - 2))

    # Interactive method that obtains the two tuple inputs from the user, and check if the chess piece is allowed to move from the first tuple to the position described by the second tuple.
    def LegalMove(self, From, To):
        if self.IsCapture(From, To):
            return self.LegalCapture(From, To)
        elif self.IsNormalMove(From, To):
            piece = self.board[From[0]][From[1]]
            if self.board[To[0]][To[1]] != 0: # If the destination of the chess piece is not empty, the move is illegal.
                return False
            elif piece / self.turn == 1: # if the chess piece for moving is the one for the player at the current turn, then we make sure that this normal chess piece is moving to the next row in the correct direction.
                return To[0] - From[0] == self.turn
            elif piece / self.turn == 2: # if the chess piece is the upgraded piece, then it is allowed to move both back & forth, and wherever it is empty.
                return True
            else:
                return False
        else:
            return False

    # Check whether a capture of one chess piece of the opponent is legal to perform, and also check whether the movement associated with the capture is legal.
    def LegalCapture(self, From, To):
        if self.IsCapture(From, To):
            piece = self.board[From[0]][From[1]]
            captured = self.board[int((From[0] + To[0]) / 2)][int((From[1] + To[1]) / 2)]
            if self.board[To[0]][To[1]] != 0: 
                return False
            elif captured / self.turn >= 0: # Check whether the chess piece to capture belongs to the opponent or not.
                return False
            elif piece / self.turn == 1: 
                return To[0] - From[0] == 2 * self.turn # The movement associated with the capture is twice as far as that shown in LegalMove().
            elif piece / self.turn == 2: 
                return True
            else:
                return False
        else:
            return False

    # Check whether the movement associated with the capture is to move two rows a time such that the piece is still in the board.
    def IsCapture(self, From, To):
        if self.InTheBoard(From) and self.InTheBoard(To):
            return (To[0] - From[0] == 2 or To[0] - From[0] == -2) \
                   and (To[1] - From[1] == 2 or To[1] - From[1] == -2)
        else:
            return False

    # Check whether the movement of the chess piece taken is a normal, one-row move (no direction restricted here).
    def IsNormalMove(self, From, To):
        if self.InTheBoard(From) and self.InTheBoard(To):
            return (To[0] - From[0] == 1 or To[0] - From[0] == -1) \
                   and (To[1] - From[1] == 1 or To[1] - From[1] == -1)
        else:
            return False

    # Check whether a position represented by tuple is legal such that it is within the range of the chess board.
    def InTheBoard(self, piece):
        return 0 <= piece[0] <= 7 and 0 <= piece[1] <= 7

    # Mutate the states of the chess board by moving the chess piece, and capturing the opponent's piece.
    def Move(self, From, To):
        piece = self.board[From[0]][From[1]]
        if piece == 1 and To[0] == 7: # upgraded chess piece
            self.board[To[0]][To[1]] = 2  
        elif piece == -1 and To[0] == 0: # upgraded chess piece
            self.board[To[0]][To[1]] = -2
        else:
            self.board[To[0]][To[1]] = piece # Reassign the chess piece to the new position
        self.board[From[0]][From[1]] = 0 # Remove the chess piece from the original position
        if self.IsCapture(From, To):
            self.board[(From[0] + To[0]) / 2][(From[1] + To[1]) / 2] = 0 # The opponent's key is captured and eliminated from the chess board

    # Print out the representation of the state of the chess board everytime a player finishes his run, as well as a list of indices (on the top & left) labeling the row & column of the chess board.
    def __str__(self):
        string = ""
        index = "12345678"
        k=0
        for i in self.board:
            for j in i:
                if j >= 0:
                    string += " " + str(j)
                else:
                    string += str(j)
            string += "   " + index[k] + "\n" 
            k=k+1
        return " 1 2 3 4 5 6 7 8" + "\n" + "\n" + string # To create the row & column indices on the top & left of the chess board.
 