'''
this is our driver file. It will be responsible for handling user input and displaying the current gamestate object.
'''

import pygame as p
import ChessEngine   

WIDTH=HEIGHT=400
DIMENSTION=8 
SQ_SIZE=HEIGHT//DIMENSTION
MAX_FPS=15 #for animations later on
IMAGES= {}

'''
initialize a global dictionary of images. this will be called exactly once in the main
'''
def loadImages():
    pieces=['wp','wR','wB','wQ','wK','wN','bN','bp','bR','bB','bQ','bK']
    for piece in pieces:
        IMAGES[piece]=p.transform.scale(p.image.load('images/'+piece+'.png'),(SQ_SIZE,SQ_SIZE))
    # we can access an image by saying IMAGES['wp']

'''
the main driver for our code. This handle user input and updating the graphics
'''
def main():
    p.init()
    screen=p.display.set_mode((WIDTH,HEIGHT))
    clock=p.time.Clock()
    screen.fill(p.Color('white'))
    gs=ChessEngine.GameState()
    print(gs.board)
    loadImages() #only do this once, before the while loop
    running=True
    sqSelected=()#no square is selected, keep track of the last click of the user
    playerClicks=[] #keep track of player clicks 
    while running:
        for e in p.event.get():
            if e.type==p.QUIT:
                running=False
            elif e.type==p.MOUSEBUTTONDOWN:
                location=p.mouse.get_pos() #(x,y) location of mouse
                col=location[0]//SQ_SIZE
                row=location[1]//SQ_SIZE
                if sqSelected==(row,col):#user clicked the same square twice
                    sqSelected=()
                    playerClicks=[]#clear player clicks
                
                else:
                    sqSelected=(row,col)
                    playerClicks.append(sqSelected) #append for both the 1st and 2nd click
                
                if len(playerClicks)==2: #after 2nd move
                    move=ChessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected=() #reset move
                    playerClicks=[]

        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all the graphics within a current game state
'''

def drawGameState(screen,gs):
    drawBoard(screen) #draw squares on the board
    #add in piece highlighting or move suggestions (later)
    drawPieces(screen,gs.board) #draw pieces on top of those squares

'''
Draw the squares on the board
'''
def drawBoard(screen):
    colors=[p.Color('white'),p.Color('gray')]
    for r in range(DIMENSTION):
        for c in range(DIMENSTION):
            color=colors[(r+c)%2]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

'''
draw the pieces on the board using the current Gamestate.board
'''

def drawPieces(screen,board):
    for r in range(DIMENSTION):
        for c in range(DIMENSTION):
            piece=board[r][c]
            if piece!='--':
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))




if __name__=='__main__':
    main()
