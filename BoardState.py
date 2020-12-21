class BoardState:
    def __init__(self):
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
        self._possibleMoves = {
            (2, 2), (2, 3), (2, 4), (2, 5),
            (3, 2), (3, 5), 
            (4, 2), (4 ,5),
            (5, 2), (5, 3), (5, 4), (5, 5),
        }
        self._numberOfWhiteDisks = 2

    #Removes (y, x) from _possibleMoves and adds the applicable indices surrounding (y, x) to _possibleMoves
    def updateEdges(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                curX = x + i
                curY = y + j
                if self._board[curY][curX] == '-':
                    self._possibleMoves.add((curY, curX))
        self._possibleMoves.remove((y, x))

    def positionChecker(self, start, end, color):
        y = start[0]
        x = start[1]
        yEnd = end[0]
        xEnd = end[1]
        xChange = self.__getChange(x, xEnd)
        yChange = self.__getChange(y, yEnd)
        x += xChange
        y += yChange
        currentTile = self._board[y][x]
        if (currentTile == "-" or currentTile == color):
            return
        count = 2
        while x < xEnd and y < yEnd:
            x += xChange
            y += yChange
            currentTile = self._board[y][x]
            if (currentTile == "-"):
                return
            if (currentTile == color):
                self.flipper(start, (x, y), color)
                if (color == "w"):
                    self._numberOfWhiteDisks += count
                else:
                    self._numberOfWhiteDisks -= count
                self.updateEdges(start[1], start[0])
                return
            count += 1
            
    @staticmethod
    def __getChange(start, end):
        if (start == end):
            return 0
        elif (start < end):
            return 1
        else:
            return -1
        
    def flipper(self, start, end, color):
        y = start[0]
        x = start[1]
        yEnd = end[0]
        xEnd = end[1]
        while x != xEnd and y != yEnd:
            self._board[y][x] = color
            if x < xEnd:
                x += 1
            elif x > xEnd:
                x -= 1
            if y < yEnd:
                y += 1
            elif y > yEnd:
                y -= 1
