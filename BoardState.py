class BoardState:
    def __init__(self):
        #Saves the current board state
        #"-" represents an empty square
        #"w" represents a white disk
        #"b" represents a black disk
        self._board = [
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "w", "b", "-", "-", "-"],
            ["-", "-", "-", "b", "w", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"]
            ]
        #List storing the index of all possible moves (not specific to a player)
        self._possibleMoves = [
            (2, 2), (2, 3), (2, 4), (2, 5),
            (3, 2), (3, 5), 
            (4, 2), (4 ,5),
            (5, 2), (5, 3), (5, 4), (5, 5),
        ]
        self._numberOfWhiteDisks = 2
        #print("Insert player color, b for black or w for white")
        #self._playerColor = input()

    #Removes (y, x) from _possibleMoves and adds the applicable indices surrounding (y, x) to _possibleMoves
    def updateEdges(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                curX = x + i
                curY = y + j
                if self._board[curY][curX] == '-':
                    self._possibleMoves.append((curY, curX))
        self._possibleMoves.remove((y, x))

    #Checks if a tile can be placed in the current position, returns false if it can't be placed, updates board if it can and returns true
    def positionChecker(self, start, color):
        directionEnds = self.generateEdges(start)
        validEnds = []
        for directionEnd in directionEnds:
            returnedEnd = self.findValidEnd(start, directionEnd, color)
            if (returnedEnd != None):
                validEnds.append(returnedEnd)
        if (len(validEnds) == 0):
            return False
        print(f"Valid ends: {validEnds}")
        for validEnd in validEnds:
            self.flipper(start, validEnd, color)
        return True


    #Returns the point along the path from start to end where a disk of color can be placed, if there is no valid it returns None
    def findValidEnd(self, start, end, color):
        if (start == end):
            return
        print()
        print(f"current directional: {end}")
        y = start[0]
        x = start[1]
        yEnd = end[0]
        xEnd = end[1]
        xChange = self.__getChange(x, xEnd)
        yChange = self.__getChange(y, yEnd)
        print(f"xChange: {xChange}, yChange: {yChange}")
        #Checks if position adjacent to start is invalid(unique as adjacent tile of the same color is invalid)
        x += xChange
        y += yChange
        currentTile = self._board[y][x]
        if (currentTile == "-" or currentTile == color):
            print(F"Adjacent was invalid {(y, x)}")
            return 
        while True:
            x += xChange
            y += yChange
            currentTile = self._board[y][x]
            #returns none if it hits an empty space (tiles can't be flipped in this direction)
            if (currentTile == "-"):
                print(f"Hit an empty space at {(y, x)}")
                return
            #returns position of valid end space
            if (currentTile == color):
                print(f"returning valid end: {(y, x)}")
                return (y, x)
            #Hit the ends and couldn't find a valid end
            if (x == xEnd and y == yEnd):
                print("Hit end")
                return

    #returns a list of end points to check based off start
    @staticmethod
    def generateEdges(start):
        y = start[0]
        x = start[1]
        #adds cardinal directions
        edgeCoords = [(0, x), (7, x), (y, 0), (y, 7)]
        #Adding north east
        num = min(y, 7-x)
        edgeCoords.append((y - num, x + num))
        #adding south east
        num = min(7 - y, 7 - x)
        edgeCoords.append((y + num, x + num))
        #adding north west
        num = min(y, x)
        edgeCoords.append((y - num, x - num))
        #adding south west
        num = min(7 - y, x)
        edgeCoords.append((y + num, x - num))
        return edgeCoords
        

    #Defines the amount that a path should be indexed by (negative for left and up, positive for right and down)
    @staticmethod
    def __getChange(start, end):
        if (start == end):
            return 0
        elif (start < end):
            return 1
        else:
            return -1

    #Makes all entries between start and end be the input color   
    def flipper(self, start, end, color):
        print(f"Flipper called. start: {start} end: {end} color: {color}")
        y = start[0]
        x = start[1]
        yEnd = end[0]
        xEnd = end[1]
        xChange = self.__getChange(x, xEnd)
        yChange = self.__getChange(y, yEnd)
        count = 0
        while x != xEnd or y != yEnd:
            self._board[y][x] = color
            y += yChange
            x += xChange
            count += 1
        if (color == "w"):
            self._numberOfWhiteDisks += count
        else:
            self._numberOfWhiteDisks -= count - 1
            
    #prints the current board state
    def printBoard(self):
        print("  0 1 2 3 4 5 6 7")
        row = 0
        for list in self._board:
            print(row, end=" ")
            for character in list:
                print(character, end=" ")
            print()
            row += 1
        print()

    #Runs the game
    def play(self):
        isWhitesTurn = True
        self.printBoard()
        while True:
            if (isWhitesTurn):
                print("White's turn")
            else:
                print("Black's turn")
            print("input y position")
            y = input()
            print("input x position")
            x = input()
            position = (int(y), int(x))
            print("Attempting input at ", end="")
            print(position)
            if isWhitesTurn == True:
                result = self.positionChecker(position, "w")
            else:
                result = self.positionChecker(position, 'b')
            if (result):
                print()
                print(f"Number of white disks: {self._numberOfWhiteDisks}")
                self.printBoard()
                if (isWhitesTurn):
                    isWhitesTurn = False
                else:
                    isWhitesTurn = True
            else:
                print("invalid position")
                self.printBoard()

def main():
    game = BoardState()
    game.play()

if __name__ == '__main__':
    main()
