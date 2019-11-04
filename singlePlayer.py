import copy as cp
import random as rd

class SinglePlayer :

    # Construct the object with multiple properties: 1."state" is the list that stores the curent state of the checker board; 2."turn" stores the turn number/which side the AI is playing for the AI; 3. "pieces" stores all the available pieces; 4. "legalMoves" stores the moves as a tuple in a list such that they are legal to perform for all chess pieces; 5. "safeMoves" stores the moves as a tuple in a list such that they make sure that the chess pieces are safe after this action.
    def __init__(self):
        self.state = None
        self.turn = 0
        self.pieces = []
        self.legalMoves = []
        self.safeMoves = []

    # Method that assigns the current state of the checker board to the property of the object
    def currentState(self, checkerGame):
        self.state = checkerGame

    # Method that assigns the turn number to the AI as a property of the object -- whether the AI starts first or second
    def firstOrSecond(self, turn):
        if turn == "first":
            self.turn = -1
        else:
            self.turn = 1

    # Method that obtains and stores all the pieces available for the current state of the checker board.
    def piecesAvailable(self):
        self.pieces=[]
        for i in range(8):
            for j in range(8):
                if self.state.board[i][j] / self.turn > 0:
                    self.pieces.append((i,j))

    # Method that randomly picks a legal move for a random movable chess piece on the board.
    def justMovePiece(self):
        return rd.choice(self.legalMoves)

    # Check for a given position of a chess piece, return true if there is an opponent's chess piece available for capturing.
    def canCapture(self):
        for i in range(len(self.pieces)):
            if self.state.CaptureAvailable(self.pieces[i]):
                return True
        return False

    # Method that finds the legal move for the given chess piece.
    def justMove(self, piece):
        to = (piece[0] + rd.choice([1,-1]),piece[1] + rd.choice([1,-1]))
        while not self.state.LegalMove(piece, to):
            to = (piece[0] + rd.choice([1,-1]),piece[1] + rd.choice([1,-1]))
        return [piece, to]

    # Method that checks whether or not a legal jump/capture is allowed to perform for any piece available -- the piece that can capture is returned.
    def capturePiece(self):
        for i in range(len(self.pieces)):
            if self.state.CaptureAvailable(self.pieces[i]):
                return self.pieces[i]

    # Method that generates all positions of the movable pieces, find out all the legal moves available for these movable pieces, and stores them as a property of the object.
    def allLegalMove(self):
        self.legalMoves = []
        movable = []
        list=[1,-1]
        for i in self.pieces:
            if self.state.MoveAvailable(i):
                movable.append(i)
        for j in movable:
            for k in range(len(list)):
                for n in range(len(list)):
                    to = (j[0] + list[k],j[1] + list[len(list)-1-n])
                    if self.state.LegalMove(j,to):
                        self.legalMoves.append((j,to))

    # Method that takes all the legal moves, finds out the legal moves, and stores them as a property of the object.
    def allSafeMove(self):
        self.safeMoves = []
        Copy = cp.deepcopy(self.state)
        for i in self.legalMoves:
            self.state.Move(i[0],i[1])
            if not self.isDangerPosition(i[1]):
                self.safeMoves.append(i)
            self.state.Move(i[1],i[0])
        self.state = Copy

    # Method that finds the legal jump/capture for the given chess piece.
    def captureMove(self,piece):
        to = (piece[0] + rd.choice([2,-2]),piece[1] + rd.choice([2,-2]))
        while not self.state.LegalCapture(piece, to):
            to = (piece[0] + rd.choice([2,-2]),piece[1] + rd.choice([2,-2]))
        return [piece, to]

    # Check for a given position, if there are nearby opponent chess pieces that could capture the piece on this position.
    def isDangerPosition(self, to):
        oppTurn = cp.deepcopy(self.state) 
        oppTurn.turn = self.turn * -1
        return oppTurn.LegalCapture((to[0]-1, to[1]-1),(to[0]+1, to[1]+1)) or oppTurn.LegalCapture((to[0]+1, to[1]-1),(to[0]-1, to[1]+1)) or oppTurn.LegalCapture((to[0]+1, to[1]+1),(to[0]-1, to[1]-1)) or oppTurn.LegalCapture((to[0]-1, to[1]+1),(to[0]+1, to[1]-1))

    # Check if there is any chess piece that is in a danger position.
    def isPieceDanger(self):
        for i in range(len(self.pieces)):
            if self.isDangerPosition(self.pieces[i]):
                return True
        return False

    # Method that returns the first found chess piece that is in danger.
    def dangerPiece(self):
        for i in range(len(self.pieces)):
            if self.isDangerPosition(self.pieces[i]):
                return self.pieces[i]

    # Mutator that decides which and how the selected chess piece to move. The chess piece follows the multiple jumps rules. The chess piece that is in danger will be moved first, and the chess piece will make safe move when it is possible, then random move.
    def decisionMove(self):
        self.piecesAvailable()
        self.allLegalMove()
        self.allSafeMove()
        pieceMove = self.justMovePiece()
        if self.isPieceDanger(): # If there is a chess piece that is in danger of being captured, the AI will try to move it first; the AI will check if this in danger piece is capable of capturing the opponent's piece, then checks if it could just move if the former is false, and finally randomly moves a piece if the former two are false. 
            dangerPiece = self.dangerPiece()
            if self.state.CaptureAvailable(dangerPiece):
                captureMove = self.captureMove(dangerPiece)
                self.state.Move(captureMove[0],captureMove[1])
                print ("AI moves from " + str((captureMove[0][0]+1, captureMove[0][1]+1)) + " to " + str((captureMove[1][0]+1, captureMove[1][1]+1)))
                print ("\n")
                if self.state.CaptureAvailable(captureMove[1]):
                    self.decisionMove()
            elif self.state.MoveAvailable(dangerPiece):
                if self.safeMoves == []:
                    justMove = self.justMove(dangerPiece)
                    self.state.Move(justMove[0],justMove[1])
                    print ("AI moves from " + str((justMove[0][0]+1, justMove[0][1]+1)) + " to " + str((justMove[1][0]+1, justMove[1][1]+1)))
                    print ("\n")
                else:
                    for i in self.safeMoves:   # If there is a safe move for the in danger piece, AI will do the safe move instaed of the random move.
                        if dangerPiece in i:
                            self.state.Move(i[0],i[1])
                            print ("AI moves from " + str((i[0][0]+1, i[0][1]+1)) + " to " + str((i[1][0]+1, i[1][1]+1)))
                            print ("\n")
                            return
                    justMove = self.justMove(dangerPiece)
                    self.state.Move(justMove[0],justMove[1])
                    print ("AI moves from " + str((justMove[0][0]+1, justMove[0][1]+1)) + " to " + str((justMove[1][0]+1, justMove[1][1]+1)))
                    print ("\n")
            elif self.canCapture():
                captureMove = self.captureMove(self.capturePiece())
                self.state.Move(captureMove[0],captureMove[1])
                print ("AI moves from " + str((captureMove[0][0]+1, captureMove[0][1]+1)) + " to " + str((captureMove[1][0]+1, captureMove[1][1]+1)))
                print ("\n")
                if self.state.CaptureAvailable(captureMove[1]):
                    self.decisionMove()
            else:
                if self.safeMoves == []: # If there is no more safe moves to do, the AI has to pick a legal move.
                    self.state.Move(pieceMove[0], pieceMove[1])
                    print ("AI moves from " + str((pieceMove[0][0]+1, pieceMove[0][1]+1)) + " to " + str((pieceMove[1][0]+1, pieceMove[1][1]+1)))
                    print ("\n")
                else:
                    safeMove = rd.choice(self.safeMoves)
                    self.state.Move(safeMove[0], safeMove[1])
                    print ("AI moves from " + str((safeMove[0][0]+1, safeMove[0][1]+1)) + " to " + str((safeMove[1][0]+1, safeMove[1][1]+1)))
                    print ("\n")
        else: # If there is no chess piece that is in danger of being captured, the AI first seeks for capturing, and then seeks for a safe move, and lastly a random move.
            if self.canCapture():
                captureMove = self.captureMove(self.capturePiece())
                self.state.Move(captureMove[0],captureMove[1])
                print ("AI moves from " + str((captureMove[0][0]+1, captureMove[0][1]+1)) + " to " + str((captureMove[1][0]+1, captureMove[1][1]+1)))
                print ("\n")
                if self.state.CaptureAvailable(captureMove[1]):
                    self.decisionMove()
            else: 
                if self.safeMoves == []: # If there is no more safe moves to do, the AI has to pick a legal move.
                    self.state.Move(pieceMove[0], pieceMove[1])
                    print ("AI moves from " + str((pieceMove[0][0]+1, pieceMove[0][1]+1)) + " to " + str((pieceMove[1][0]+1, pieceMove[1][1]+1)))
                    print ("\n")
                else:
                    safeMove = rd.choice(self.safeMoves)
                    self.state.Move(safeMove[0], safeMove[1])
                    print ("AI moves from " + str((safeMove[0][0]+1, safeMove[0][1]+1)) + " to " + str((safeMove[1][0]+1, safeMove[1][1]+1)))
                    print ("\n")