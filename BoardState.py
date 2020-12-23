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
        print("Insert player color, b for black or w for white")
        self._playerColor = input()

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
        for end in directionEnds:
            end == self.findValidEnd(start, end, color)
            if (end != None):
                validEnds.append(end)
        if (len(validEnds) == 0):
            return False
        for validEnd in validEnds:
            self.flipper(start, validEnd, color)
        return True


    #Returns the point along the path from start to end where a disk of color can be placed, if there is no valid it returns None
    def findValidEnd(self, start, end, color):
        if (start == end):
            return
        y = start[0]
        x = start[1]
        yEnd = end[0]
        xEnd = end[1]
        xChange = self.__getChange(x, xEnd)
        yChange = self.__getChange(y, yEnd)
        currentTile = self._board[y][x]
        #Checks if position adjacent to start is invalid(unique as adjacent tile of the same color is invalid)
        if (currentTile == "-" or currentTile == color):
            return
        while x != xEnd or y != yEnd:
            x += xChange
            y += yChange
            currentTile = self._board[y][x]
            #returns none if it hits an empty space (tiles can't be flipped in this direction)
            if (currentTile == "-"):
                return
            #returns position of valid end space
            if (currentTile == color):
                return (y, x)

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
        edgeCoords.append((y + num, x - num))
        #adding north west
        num = min(y, x)
        edgeCoords.append((y - num, x - num))
        #adding south west
        num = min(7 - y, x)
        edgeCoords.append((7 - y, x))
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
        y = start[0]
        x = start[1]
        yEnd = end[0]
        xEnd = end[1]
        count = 0
        while x != xEnd and y != yEnd:
            self._board[y][x] = color
            count += 1
            if x < xEnd:
                x += 1
            elif x > xEnd:
                x -= 1
            if y < yEnd:
                y += 1
            elif y > yEnd:
                y -= 1
        if (color == "w"):
            self._numberOfWhiteDisks += count
        else :
            self._numberOfWhiteDisks -= count
            
    #prints the current board state
    def printBoard(self):
        for list in self._board:
            for character in list:
                print(character, end=" ")
            print()
        return


def main():
    game = BoardState()
    game.printBoard()

if __name__ == '__main__':
    main()
