How to start?
1. Open the terminal.
2. Type python, hit Space, then Drag the file named Main.py into the terminal, hit Enter.
3. Follow the instructions shown by the console. Note that the coordinate must be entered as (horizontal, vertical).
4. To see codes for test cases & results. Go to the folder named Test & Demo Log.
5. To run the test file — follow the same procedure as 1 & 2 except that at last drag the file named tests.py into the terminal, Enter.
6. Once the game is over, hit any key to start again, or hit 0 to exist.

---------------------------------------------------------------------------------------------

Rules & representations of this checkerboard game:
1. The chess pieces are labeled as “1” or “-1”. “0” resembles empty space. The upgraded chess pieces are labeled as “2” or “-2”.
2. The chess pieces are only allowed to move in diagonal.
3. The chess pieces labeled as “1” or “-1” are only allowed to move towards the other side of the chess board. One step each time if there is no capture available.
4. The chess pieces could capture/eliminate a opponent’s chess piece by being able to jump over it. After this action, the opponent’s chess piece is gone and its position will become empty labeled as “0”.
5. The chess pieces are upgraded once they reach the end of the board (of the opponent’s side). These upgraded chess pieces could move in both direction (up and down) on the board such that they could be used to chase down the opponent’s chess piece.
6. A player loses the game if he does not have any chess piece left on the board, or he is unable to make any legal move in his turn.

—--------------------------------------------------------------------------------------------
Brief introduction to the three classes of codes:

1. class Checkerboard — this class defines the representation of the chessboard and the methods (accessors & mutators) as rules of the game.

init: list of list (8 x 8)
	player one: + sign, player two: - sign
	empty position: 0
	a normal piece: 1/-1
	an upgraded piece: 2/-2
	r1 = [0, 1, 0, 1, 0, 1, 0, 1]
        r2 = [1, 0, 1, 0, 1, 0, 1, 0]
        r3 = [0, 1, 0, 1, 0, 1, 0, 1]
        r4 = [0, 0, 0, 0, 0, 0, 0, 0]
        r5 = [0, 0, 0, 0, 0, 0, 0, 0]
        r6 = [-1, 0, -1, 0, -1, 0, -1, 0]
        r7 = [0, -1, 0, -1, 0, -1, 0, -1]
        r8 = [-1, 0, -1, 0, -1, 0, -1, 0]
        self.board = [r1, r2, r3, r4, r5, r6, r7, r8]
        self.turn = 1 — parameter that indicates whose turn it is (1 for player one, -1 for the other)

Accessor:
1) CheckLost(): at the beginning of a player’s turn, check if this player has lost

2) LegalMove(From(tuple), To(tuple)): from a position represented as a tuple (row1,column1) to another position (row2,column2), and check if at the current turn, a move from the position (row1,column1) to another (row2,column2) is legal (including capture and normal move)

3) CaptureAvailable(piece(tuple)): check whether at the current turn a capture is available using the given chess piece. Useful for implementing the forced-to-capture rule.

4) LegalCapture(From(tuple), To(tuple)): from a position represented as a tuple (row1,column1) to another position (row2,column2), and check if in the current turn a move from the position (row1,column1) to position (row2,column2) is a legal capture move. Useful for implementing forced—to-capture rule.

5) str: print out the matrix representing the chess board.
	
Mutator: 
1). Move(From(tuple), To(tuple)): from a position represented as a tuple (row1,column1) to another position (row2,column2), and move the piece from the position (row1,column1) to position (row2,column2).




2. class TwoPlayers

init: construct the object with the property "player" that stores players' name in a list

Accessor:
1). gameStart(checkerboard): starts the game -- give important instructions of who plays which side and shows the representation of the chess board

2). gameOver(checkerboard): takes care of deciding whehther or not a player loses the game and produces a sentence saying who is the winner.

Mutator: 
1). enterName(name1, name2): mutates the object's property by storing the names of the two players

2). checkCaptureOrMove(checkerGame,from,to): helps identify a detail required by the rule of checkerboard -- if a chess piece is allowed to perform multiple consecutive captures, it is required to perform all captures once the player decides to use this chess piece to make the first capture.

3). gameProcess(checkerboard): takes care for the gaming process where each player takes turn to move the chess piece until one player loses the game (satisfy the Checkerboard.CheckLost() accessor method).




3. class SinglePlayer

init: construct the object with multiple properties: 
	self.state — is the list that stores the curent state of the checker board; 
	self.turn — stores the turn number/which side the AI is playing for the AI; 
	self.pieces — stores all the available pieces; 
	self.legalMoves — stores the moves as a tuple in a list such that they are legal to perform for all chess pieces; 
	self.safeMoves — stores the moves as a tuple in a list such that they make sure that the chess pieces are safe after this action.

Accessor:
1). justMove(piece): finds the legal move for the given chess piece.
2). canCapture(): check for a given position of a chess piece, return true if there is an opponent's chess piece available for capturing.
3). justMovePiece(): randomly picks a legal move for a random movable chess piece on the board.
4). capturePiece(): checks whether or not a legal jump/capture is allowed to perform for any piece available -- the piece that can capture is returned.
5). captureMove(piece): finds the legal jump/capture for the given chess piece.
6). isDangerPosition(to): checks for a given position, if there are nearby opponent chess pieces that could capture the piece on this position.
7). isPieceDanger(): checks if there is any chess piece that is in a danger position.
8). dangerPiece(): returns the first found chess piece that is in danger.


Mutator:
1). currentState(checkerGame): assigns the current state of the checker board to the property of the object
2). firstOrSecond(turn): assigns the turn number to the AI as a property of the object -- whether the AI starts first or second
3). piecesAvailable(): obtain and stores all the pieces available for the current state of the checker board.
4). allLegalMove(): generates all positions of the movable pieces, find out all the legal moves available for these movable pieces, and stores them as a property of the object.
5). allSafeMove(): takes all the legal moves, finds out the legal moves, and stores them as a property of the object.
6). decisionMove(): decides which and how the selected chess piece moves. The chess piece follows the multiple jumps rules. The chess piece that is in danger will be moved first, and the chess piece will make safe move when it is possible, then random move.
