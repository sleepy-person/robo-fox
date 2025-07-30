from RetroPy.retroPy import rpy, kb, draw, disp, gameObj, LoadSpriteStr, LoadSprite
import os, random, time, math
from packtiles import packarray, unpackarray

tilemap=unpackarray("tilemap") #assuming file is named tilemap (binary file where 1 byte = 4 tiles)
tiles=LoadSprite("alltiles") #index determines tiles (16 tiles)

def drawtiles(x,y):
    screentiles = [row[max(0,x//32):min(128-1,(x+12)//32)+1] for row in tilemap[max(0,y//32):min(128-1,(y+8)//32)+1]]
    for row in range(len(screentiles)):
        for col in range(len(screentiles[row])):
            tiles.draw(screentiles[col][row],col*32-x,row*32-y,0)
    
if __name__ == "__main__":
    def Update(dt):        
        pass
    
    def Draw(dt):
        draw.clear()
        drawtiles()
        draw.text(str(dt), 200, 0, 7)

    rpy.run(Update, Draw)
