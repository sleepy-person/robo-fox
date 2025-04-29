
from RetroPy.retroPy import rpy, kb, draw, disp, gameObj, LoadSpriteStr, LoadSprite, sprite
import os, random, time
import math
import RetroPy.AB2Cont

p_fox = LoadSprite("/rpg/assets/finalfox.rs8")
p_foxrun = LoadSprite("/rpg/assets/finalfoxrun.rs8")
e_redfox = LoadSprite("/rpg/assets/Red_Fox.rs8")
e_redfoxattack = LoadSprite("/rpg/assets/Red_Fox_Attack.rs8")
redfox = []
CurrentPhase = 1
player=gameObj(p_fox,112,120,70,currNdx=0)
curr_x,curr_y=1024,1024
prevmove,move,dirr=0,0,0

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

    #RedFox spawn rate
    if (random.random() * 100) < ((4 * 3 + CurrentPhase * 5) ** dt):
        redfox.append(gameObj(e_redfox, randint(128,896), randint(128,896)))
        if abs(redfox[-1].pos_x - curr_x) > 320 or abs(redfox[-1].pos_y - curr_y) > 320:
            redfox.remove(-1)
    for rf in redfox:
        rf.update()
        if abs(rf.pos_x - curr_x) > 320 or abs(rf.pos_y - curr_y) > 320:
            redfox.remove(rf)

    

# =======================================================================================
def Draw(dt):
    global dtt, move, curr_x, curr_y
    draw.clear()
    player.draw()
    draw.text(str(dt), 200, 0, 7)
    
# =======================================================================================
# =======================================================================================               
rpy.run(Update, Draw) 
# =======================================================================================
