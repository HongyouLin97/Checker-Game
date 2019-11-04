
class TwoPlayers:

    # Construct the object with the property "player" that stores players' name in a list
    def __init__(self):
        self.Player = []

    # This method mutates the object's property by storing the names of the two players
    def enterName(self, Name1, Name2):
        self.Player.append(Name1)
        self.Player.append(Name2)

    # This method starts the game -- give important instructions of who plays which side and shows the representation of the chess board
    def gameStart(self, checkerGame):
        print ("Game start! " + str(self.Player[0]) + " goes first, and please uses the chess pieces label as 1; " + str(self.Player[1] + " goes second, and please uses the chess piece labeled -1."))
        print (checkerGame)

    # This method helps identify a detail required by the rule of checkerboard -- if a chess piece is allowed to perform multiple consecutive captures, it is required to perform all captures once the player decides to use this chess piece to make the first capture.
    def checkCaptureOrMove(self,checkerGame,f,t):
        if checkerGame.CaptureAvailable(t):
            print ("You have more than 2 captures avaiable, please continue with the previous chess piece.")
            print (checkerGame)
            newf=t                
            newt = input("Where do you want to move the piece to: ")  
            while len(newt)!=5 or newt[0]!='(' or newt[2]!=',' or newt[4]!=')' or not newt[1].isdigit() or not newt[3].isdigit() or not checkerGame.LegalCapture(newf,(int(newt[1])-1, int(newt[3])-1)):
                print ("Illegal move! Do it again.")
                newt = input("Where do you want to move the piece to: ")     # Keep asking for input if the input does not satisfy the required conditions  to break the while loop.
            newt = (int(newt[1])-1, int(newt[3])-1) 
            checkerGame.Move(newf,newt)   
            self.checkCaptureOrMove(checkerGame,newf,newt)    # Recusion such that the consecutive captures are forced to be executed until no more captures are available.

    # This method takes care for the gaming process where each player takes turn to move the chess piece until one player loses the game (satisfy the Checkerboard.CheckLost() accessor method).
    def gameProcess(self, checkerGame):
        while checkerGame.CheckLost() == False:
            if checkerGame.turn == 1:                
                f1 = input(str(self.Player[0]) + " choose the piece that you want to move: ")
                t1 = input("Where do you want to move the piece to: ")
                while len(f1)!=5 or len(t1)!=5 or f1[0]!='(' or t1[0]!='(' or f1[2]!=',' or t1[2]!=',' or f1[4]!=')' or t1[4]!=')' or not f1[1].isdigit() or not f1[3].isdigit() or not t1[1].isdigit() or not t1[3].isdigit() or not checkerGame.LegalMove((int(f1[1])-1, int(f1[3])-1),(int(t1[1])-1, int(t1[3])-1)):
                    print ("Illegal move! Do it again.")
                    f1 = input(str(self.Player[0]) + " choose the piece that you want to move: ") # Keep asking inputs until they are correcty entered by the players.
                    t1 = input("Where do you want to move the piece to: ")         
                f1 = (int(f1[1])-1, int(f1[3])-1)
                t1 = (int(t1[1])-1, int(t1[3])-1)
                if checkerGame.LegalCapture(f1,t1):
                    checkerGame.Move(f1,t1)
                    self.checkCaptureOrMove(checkerGame,f1,t1) # The method that takes care of the multiple capture features of the checker game.
                else:
                    checkerGame.Move(f1,t1)
                checkerGame.turn = checkerGame.turn * -1 # This parameter controls which turn it is for each player.
                print(checkerGame)
            else:
                f2 = input(str(self.Player[1]) + ", choose the piece that you want to move: ")
                t2 = input("Where do you want to move the piece to: ")
                while len(f2)!=5 or len(t2)!=5 or f2[0]!='(' or t2[0]!='(' or f2[2]!=',' or t2[2]!=',' or f2[4]!=')' or t2[4]!=')' or not f2[1].isdigit() or not f2[3].isdigit() or not t2[1].isdigit() or not t2[3].isdigit() or not checkerGame.LegalMove((int(f2[1])-1, int(f2[3])-1),(int(t2[1])-1, int(t2[3])-1)):
                    print ("Illegal move! Do it again.")
                    f2 = input(str(self.Player[1]) + ", choose the piece that you want to move: ")
                    t2 = input("Where do you want to move the piece to: ")
                f2 = (int(f2[1])-1, int(f2[3])-1)
                t2 = (int(t2[1])-1, int(t2[3])-1)
                if checkerGame.LegalCapture(f2,t2):
                    checkerGame.Move(f2,t2)
                    self.checkCaptureOrMove(checkerGame,f2,t2)
                else:
                    checkerGame.Move(f2,t2)
                checkerGame.turn = checkerGame.turn * -1
                print(checkerGame)
        print ("The game is over. ")


    # This method takes care of deciding whehther or not a player loses the game and produces a sentence saying who is the winner.
    def gameOver(self, checkerGame):
        if checkerGame.CheckLost() == True:
            if checkerGame.turn == 1:
                print (str(self.Player[1]) + " won the game!")
            else:
                print (str(self.Player[0]) + " won the game!")
                    
                    
