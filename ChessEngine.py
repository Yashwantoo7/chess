'''
This calss is responsible for storing all the information about the current state of a chess game. it will also be responsible 
for determining the valid moves at the current state. It will also keep a move log.
'''
class GameState():
    def __init__(self):
        #'--'empty
        self.board=[
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bp','bp','bp','bp','bp','bp','bp','bp'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['wp','wp','wp','wp','wp','wp','wp','wp'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR'],
        ]
        self.whiteToMove=True 
        self.moveLog=[]
    
    '''
    Take a move as parameter and executes it (this will not work for castling, pawn promotion, and en-passant)
    '''
    def makeMove(self,move):
        self.board[move.startRow][move.startCol]='--'
        self.board[move.endRow][move.endCol]=move.pieceMoved
        self.moveLog.append(move) #log the move  so we can use it later
        self.whiteToMove=not self.whiteToMove #swap turn
    
    '''
    Undo the last move
    '''
    def undoMove(self):
        if len(self.moveLog):
            move=self.moveLog.pop()
            self.board[move.startRow][move.startCol]=move.pieceMoved
            self.board[move.endRow][move.endCol]=move.pieceCaptured
            self.whiteToMove=not self.whiteToMove #swap turn

    '''
    All moves considering checks
    '''
    def getValidMoves(self):
        return self.getAllPossibleMoves() #for now we will not worry about checks
    
    def getAllPossibleMoves(self):
        moves=[Move((6,4),(4,4),self.board)]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn=='b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece=='p':
                        self.getPawnMoves(r,c,moves)
                    elif piece=='R':
                        self.getRookMoves(r,c,moves)
        return moves

    def getPawnMoves(self,r,c,moves):
        pass

    def getRookMoves(self,r,c,moves):
        pass
 
class Move():
    #maps keys to value
    #key : value
    ranksToRows={'8':0,'7':1,'6':2,'5':3,'4':4,'3':5,'2':6,'1':7}
    rowsToRanks={v:k for k,v in ranksToRows.items()}

    filesToCols={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    colsToFiles={v:k for k,v in filesToCols.items()}

    def __init__(self,startSq,endSq,board):
        self.startRow=startSq[0]
        self.startCol=startSq[1]
        self.endRow=endSq[0]
        self.endCol=endSq[1]
        self.pieceMoved=board[self.startRow][self.startCol]
        self.pieceCaptured=board[self.endRow][self.endCol]
        self.moveId = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol
        print(self.moveId)

    '''
    overriding the equals method
    '''
    def __eq__(self,other):
        if isinstance(other,Move):
            return self.moveId == other.moveId
        return False

    def getChessNotation(self):
        #you can add to make this like real chess  notation
        return self.getRankFile(self.startRow,self.startCol)+self.getRankFile(self.endRow,self.endCol)
    
    def getRankFile(self,r,c):
        return self.colsToFiles[c]+self.rowsToRanks[r]