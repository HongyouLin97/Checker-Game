from checkerboard import Checkerboard
from twoPlayers import TwoPlayers
from singlePlayer import SinglePlayer

next="1"
# Main file for running the checker game -- everything gets "assembled" as a whole here:
while next == "1":
    game = Checkerboard()
    mode = input("Welcome to checkers. Please input A for two players mode and B for single player mode: ")
    if mode == "A":
        twoPlayersGame = TwoPlayers()
        Name1 = input("Enter the name for the player who will go first: ")
        Name2 = input("Enter the name for the player who will go second: ")
        twoPlayersGame.enterName(Name1, Name2)
        twoPlayersGame.gameStart(game)
        twoPlayersGame.gameProcess(game)
        twoPlayersGame.gameOver(game)
        next = input("Type 0 to exist the game; type any other key to continue: ")
        if next == "0":
            break
        else:
            next="1"
            continue # continue the while loop and restart the game.
    elif mode == "B":
        AI = SinglePlayer()
        Player = TwoPlayers()
        player = raw_input("Enter your name: ")
        turn = raw_input("Do you want to go first (using chess piece '1') or second (using chess piece '-1')? ")
        while turn!="first" and turn!="second":
            print ("Invalid input. Please enter first or second.")
            turn = raw_input("Do you want to go first or second? ")
        print ("\n")
        AI.firstOrSecond(turn)
        print(game)
        while game.CheckLost() == False:
            if game.turn == AI.turn:
                print ("This is the AI's move: ")
                AI.currentState(game)
                AI.piecesAvailable()
                AI.allLegalMove()
                if AI.legalMoves != [] or AI.canCapture(): # If AI can not make any more legal moves nor captures, the AI loses the game. This is just an unnecessary double check for the condition specified by the while loop.
                    AI.decisionMove()
                else:
                    break
                game = AI.state
                game.turn = game.turn * -1
                print(game)
            else:
                f1 = raw_input(player + " choose the piece that you want to move: ")
                t1 = raw_input("Where do you want to move the piece to: ")
                while len(f1)!=5 or len(t1)!=5 or f1[0]!='(' or t1[0]!='(' or f1[2]!=',' or t1[2]!=',' or f1[4]!=')' or t1[4]!=')' or not f1[1].isdigit() or not f1[3].isdigit() or not t1[1].isdigit() or not t1[3].isdigit() or not game.LegalMove((int(f1[1])-1, int(f1[3])-1),(int(t1[1])-1, int(t1[3])-1)):
                    print ("Illegal move! Do it again.")
                    f1 = raw_input(player + " choose the piece that you want to move: ") # Keep asking inputs until they are correcty entered by the players.
                    t1 = raw_input("Where do you want to move the piece to: ")         
                f1 = (int(f1[1])-1, int(f1[3])-1)
                t1 = (int(t1[1])-1, int(t1[3])-1)
                if game.LegalCapture(f1,t1):
                    game.Move(f1,t1)
                    Player.checkCaptureOrMove(game,f1,t1) # The method that takes care of the multiple capture features of the checker game for a player.
                else:
                    game.Move(f1,t1)
                game.turn = game.turn * -1 # This parameter controls which turn it is for each player.
                print(game)
        print ("The game is Over.")
        if game.turn == AI.turn:
            print ("Woooh the human " + str(player)+ " wins!")
        else:
            print ("HAHA AI is the best!")
        next = raw_input("Type 0 exist the game; type any other key to continue: ")
        if next == "0":
            break
        else:
            next="1"
            continue # continue the while loop and restart the game.
    else:
        print ("Invalid input.")


