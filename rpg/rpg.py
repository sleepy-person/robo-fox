from RetroPy.retroPy import rpy, kb, draw, disp, gameObj, LoadSpriteStr, LoadSprite, sprite
import os, random, time
import math
import RetroPy.AB2Cont

p_fox = LoadSprite("/rpg/finalfox.rs8")
p_foxrun = LoadSprite("/rpg/finalfoxrun.rs8")
player=gameObj(p_fox,112,120,70,currNdx=0)
curr_x,curr_y=1024,1024
prevmove,move,dirr=0,0,0
mapp=[[random.randint(0,2) for _ in range(64)] for _ in range(64)]
snow_snow = LoadSprite("/rpg/snow-snow.rs8")
snow=sprite(snow_snow)
lake_lake = LoadSprite("/rpg/lake.rs8")
lake=sprite(lake_lake)
br_br = LoadSprite("/rpg/branches.rs8")
br=sprite(br_br)
objs=[snow,lake,br]

def clampmove(x,y):
    global curr_x, curr_y
    curr_x+= x if (curr_x+x>=120) and (curr_x+x<=1790) else 0
    curr_y+= y if (curr_y+y>=120) and (curr_y+y<=1790) else 0

def Update(dt):
    global dtt, move, prevmove, curr_x, curr_y, dirr
    player.update()
    move=10
    if kb.readLeft==0:
        clampmove(-64*dt,0)
        dirr=1
    elif kb.readRight==0:
        clampmove(64*dt,0)
        dirr=0
    else:
        move-=4
        
    if kb.readUp==0:
        clampmove(0,-64*dt)
    elif kb.readDown==0:
        clampmove(0,64*dt)
    else:
        move-=4

    player.flip(dirr)
    
    if prevmove!=move:
        if move>5:
            player.sprite(p_foxrun,70)
        else:
            player.sprite(p_fox,70)
    
    prevmove=move

# =======================================================================================
def Draw(dt):
    global dtt, move, curr_x, curr_y
    draw.clear()
    
    for x in range(0,9):
        for y in range(0,9):
            objs[mapp[int(curr_x//32)+x][int(curr_y//32)+y]].draw(0,x*32-int(curr_x)%32,y*32-int(curr_y)%32,0)
            
    player.draw()
    draw.text(str(dt), 200, 0, 7)
    
# =======================================================================================
# =======================================================================================               
rpy.run(Update, Draw) 
# =======================================================================================
