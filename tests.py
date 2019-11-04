from checkerboard import Checkerboard
from twoPlayers import TwoPlayers
from singlePlayer import SinglePlayer

def Gameover1():
    game = Checkerboard()
    r1 = [0, 0, 0, 0, 0, 0, 0, 0]
    r2 = [0, 0, 0, 0, 0, 0, 0, 0]
    r3 = [0, 0, 0, 0, 0, 0, 0, 0]
    r4 = [0, 0, 0, 0, 0, 0, 0, 0]
    r5 = [0, 0, 0, 0, 0, 0, 0, 0]
    r6 = [-1, 0, -1, 0, -1, 0, -1, 0]
    r7 = [0, -1, 0, -1, 0, -1, 0, -1]
    r8 = [-1, 0, -1, 0, -1, 0, -1, 0]
    game.board = [r1, r2, r3, r4, r5, r6, r7, r8]
    game.turn = 1
    Test1 = TwoPlayers() 
    Test1.enterName("A","B") # The first player A (first one who enters the name) corresponds to chess piece labeled as 1, who loses this game. The second player B (second one who enters the name) corresponds to chess piece labeled as -1, who wins the game.
    Test1.gameProcess(game) # Should not do anything other then print "The game is over. " because clearly the player A loses the game by losing all his chess pieces.
    Test1.gameOver(game) # Should print out "B won the game!"


def Gameover2():
    game = Checkerboard()
    r1 = [0, 0, 0, 0, 0, 0, 0, 0]
    r2 = [0, 2, 0, 0, 0, 2, 0, 0]
    r3 = [0, 0, 1, 0, 1, 0, 0, 0]
    r4 = [0, 0, 0, -2, 0, 0, 0, 0]
    r5 = [0, 0, 2, 0, 1, 0, 0, 0]
    r6 = [0, 1, 0, 0, 0, 1, 0, 0]
    r7 = [0, 0, 0, 0, 0, 0, 0, 0]
    r8 = [0, 0, 0, 0, 0, 0, 0, 0]
    game.board = [r1, r2, r3, r4, r5, r6, r7, r8]
    game.turn = -1
    Test2 = TwoPlayers() 
    Test2.enterName("A","B") # The first player A (first one who enters the name) corresponds to chess piece labeled as 1, who wins this game. The second player B (second one who enters the name) corresponds to chess piece labeled as -1, who loses the game.
    Test2.gameProcess(game) # Should not do anything other then print out "The game is over. " because clearly the player B loses the game by not being able to move his chess piece for his turn.
    Test2.gameOver(game) # Should print out "A won the game!"

def MultipleJumps():
    game = Checkerboard()
    r1 = [0, 0, 1, 0, 0, 0, 0, 0]
    r2 = [0, 0, 0, -1, 0, 0, 0, 0]
    r3 = [0, 0, 0, 0, 0, 0, 0, 0]
    r4 = [0, 0, 0, 0, 0, -1, 0, 0]
    r5 = [0, 0, 0, 0, 0, 0, 0, 0]
    r6 = [0, 0, 0, 0, 0, 0, 0, 0]
    r7 = [0, 0, 0, 0, 0, 0, 0, 0]
    r8 = [0, 0, 0, 0, 0, 0, 0, 0]
    game.board = [r1, r2, r3, r4, r5, r6, r7, r8]
    game.turn = 1
    Test3 = TwoPlayers()
    Test3.enterName("A","B")
    print (game)
    Test3.gameProcess(game) # Should have an interactive process asking A to "choose the piece to move" and "where to move the piece to", and a multiple captures/multiple jumps process is required if the player choose the do the first capture.
    # This test of multiple jumps/captures is shown by the log file of the game too.
    Test3.gameOver(game) # SHould print "A won the game! " after the interactive process.

def AIMultipleJumps():
    game = Checkerboard()
    r1 = [0, 0, 1, 0, 0, 0, 0, 0]
    r2 = [0, 0, 0, -1, 0, 0, 0, 0]
    r3 = [0, 0, 0, 0, 0, 0, 0, 0]
    r4 = [0, 0, 0, 0, 0, -1, 0, 0]
    r5 = [0, 0, 0, 0, 0, 0, 0, 0]
    r6 = [0, 0, 0, 0, 0, 0, 0, 0]
    r7 = [0, 0, 0, 0, 0, 0, 0, 0]
    r8 = [0, 0, 0, 0, 0, 0, 0, 0]
    game.board = [r1, r2, r3, r4, r5, r6, r7, r8]
    game.turn = 1
    Test4 = SinglePlayer()
    Test4.state = game
    Test4.turn = game.turn
    Test4.decisionMove() # AI should make the decision of double capturing as requierd by the rule of the game.
    print (Test4.state) # Print out the final result after AI's move, which should be only the chess piece 1 moving from (1,3) to (5,7).

def AIAvoidBeingCaptured():
    game = Checkerboard()
    r1 = [0, 0, 0, 0, 0, 0, 0, 0]
    r2 = [0, 0, -1, 0, 0, 0, 0, 0]
    r3 = [1, 0, 0, 0, 0, 0, 0, 0]
    r4 = [0, 1, 0, 0, 0, 0, 0, 0]
    r5 = [0, 0, -1, 0, 0, 0, 0, 0]
    r6 = [0, 0, 0, 0, 0, 0, 0, 0]
    r7 = [0, 0, 0, 0, 0, 0, 0, 0]
    r8 = [0, 0, 0, 0, 0, 0, 0, 0]
    game.board = [r1, r2, r3, r4, r5, r6, r7, r8]
    game.turn = -1
    Test5 = SinglePlayer()
    Test5.state = game
    Test5.turn = game.turn
    print (game)
    Test5.decisionMove() # AI should make the decision of always moving the -1 chess piece at (5,3) to (4,4) because it is in danger of being captured.
    print (Test5.state) # Print out the final result. 
    

def AIHaveToMoveRealSituation():
    game = Checkerboard()
    r1=[0, 0, 0, 0, 0, 0, 0, 0]
    r2=[1, 0, 1, 0, 1, 0, 1, 0]
    r3=[0, 1, 0, 1, 0, 1, 0, 1]
    r4=[1, 0, -1, 0, 0, 0, 1, 0]
    r5=[0, -1, 0, -1, 0, -1, 0, 1]
    r6=[0, 0, -1, 0, -1, 0, -1, 0]
    r7=[0, -1, 0, -1, 0, -1, 0, 0]
    r8=[0, 0, 0, 0, -1, 0, 0, 0]
    game.board = [r1, r2, r3, r4, r5, r6, r7, r8]
    game.turn = 1
    Test6 = SinglePlayer()
    Test6.state = game
    Test6.turn = game.turn
    print (Test6.state)
    print ("This is the AI's move: ")
    print ("\n")
    Test6.decisionMove() # The AI only have to choices here -- to either move the chess piece at (3,4) or the one at (3,6) to the position (4,5). This is not a safe move, but AI does not have choice so has to do it.
    print (Test6.state) # Print out the final result.
    

Gameover1()
print ("\n")

Gameover2()
print ("\n")

MultipleJumps()
print ("\n")

AIMultipleJumps()
print ("\n")

AIAvoidBeingCaptured()
print ("\n")

AIHaveToMoveRealSituation()