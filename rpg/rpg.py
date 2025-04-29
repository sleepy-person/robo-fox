
from RetroPy.retroPy import rpy, kb, draw, disp, gameObj, LoadSpriteStr, LoadSprite, sprite
import os, random, time
import math
import RetroPy.AB2Cont

p_fox = LoadSprite("/rpg/assets/finalfox.rs8")
p_foxrun = LoadSprite("/rpg/assets/finalfoxrun.rs8")
e_hare = LoadSprite("/rpg/assets/Arctic_Hare.rs8")
e_bush = LoadSprite("/rpg/assets/Berry_Bush.rs8")
e_lemming = LoadSprite("/rpg/assets/Lemming.rs8")
e_redfox = LoadSprite("/rpg/assets/Red_Fox.rs8")
e_redfoxattack = LoadSprite("/rpg/assets/Red_Fox_Attack.rs8")
e_owl = LoadSprite("/rpg/assets/Owl.rs8")
e_owlattack = LoadSprite("/rpg/assets/Owl_Attack.rs8")
e_eagle = LoadSprite("/rpg/assets/Eagle.rs8")
e_eagleattack = LoadSprite("/rpg/assets/Eagle_Attack.rs8")
e_bear = LoadSprite("/rpg/assets/Polar_Bear.rs8")
e_bearattack = LoadSprite("/rpg/assets/Polar_Bear_Attack.rs8")
hare, bush, lemming = [], [], []
redfox, owl, eagle, bear = [], [], [], []

CurrentPhase = 1
RandomVariable = 0
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

    #Hare spawn rate
    if (random.random() * 100) < ((10 * 3 + CurrentPhase * 8) ** dt):
        hare.append(gameObj(e_hare, randint(128,896), randint(128,896)))
        if abs(hare[-1].pos_x - curr_x) > 320 or abs(hare[-1].pos_y - curr_y) > 320:
            hare.remove(-1)
    for h in hare:
        h.update()
        if RandomVariable % 10 == 0:
            if abs(h.pos_x - curr_x) > 320 or abs(h.pos_y - curr_y) > 320:
                hare.remove(h)

    #Lemming spawn rate
    if (random.random() * 100) < ((16 * 3 + CurrentPhase * 8) ** dt):
        lemming.append(gameObj(e_lemming, randint(128,896), randint(128,896)))
        if abs(lemming[-1].pos_x - curr_x) > 320 or abs(lemming[-1].pos_y - curr_y) > 320:
            lemming.remove(-1)
    for lemon in lemming:
        lemon.update()
        if RandomVariable % 10 == 0:
            if abs(lemon.pos_x - curr_x) > 320 or abs(lemon.pos_y - curr_y) > 320:
                lemming.remove(lemon)
                
    #Bush 
    if (random.random() * 100) < ((20 * 3 + CurrentPhase * 8) ** dt):
        bush.append(gameObj(e_bush, randint(128,896), randint(128,896)))
        if abs(bush[-1].pos_x - curr_x) > 320 or abs(bush[-1].pos_y - curr_y) > 320:
            bush.remove(-1)
    for bus in bush:
        bus.update()
        if RandomVariable % 10 == 0:
            if abs(bus.pos_x - curr_x) > 320 or abs(bus.pos_y - curr_y) > 320:
                bush.remove(bus)
                
    #RedFox spawn rate
    if (random.random() * 100) < ((4 * 3 + CurrentPhase * 5) ** dt):
        redfox.append(gameObj(e_redfox, randint(128,896), randint(128,896)))
        if abs(redfox[-1].pos_x - curr_x) > 320 or abs(redfox[-1].pos_y - curr_y) > 320:
            redfox.remove(-1)
    for rf in redfox:
        rf.update()
        if RandomVariable % 10 == 0:
            if abs(rf.pos_x - curr_x) > 320 or abs(rf.pos_y - curr_y) > 320:
                redfox.remove(rf)

    #PolarBear spawn rate
    if (random.random() * 100) < ((1 * 3 + CurrentPhase * 5) ** dt):
        bear.append(gameObj(e_bear, randint(128,896), randint(128,896)))
        if abs(bear[-1].pos_x - curr_x) > 320 or abs(bear[-1].pos_y - curr_y) > 320:
            bear.remove(-1)
    for b in bear:
        b.update()
        if RandomVariable % 10 == 0:
            if abs(b.pos_x - curr_x) > 320 or abs(b.pos_y - curr_y) > 320:
                bear.remove(b)
                
    #Owl spawn rate
    if (random.random() * 100) < ((2 * 3 + CurrentPhase * 5) ** dt):
        owl.append(gameObj(e_owl, randint(128,896), randint(128,896)))
        if abs(owl[-1].pos_x - curr_x) > 320 or abs(owl[-1].pos_y - curr_y) > 320:
            owl.remove(-1)
    for o in owl:
        o.update()
        if RandomVariable % 10 == 0:
            if abs(o.pos_x - curr_x) > 320 or abs(o.pos_y - curr_y) > 320:
                owl.remove(o)

    #Eagle spawn rate
    if (random.random() * 100) < ((2 * 3 + CurrentPhase * 5) ** dt):
        eagle.append(gameObj(e_eagle, randint(128,896), randint(128,896)))
        if abs(eagle[-1].pos_x - curr_x) > 320 or abs(eagle[-1].pos_y - curr_y) > 320:
            eagle.remove(-1)
    for e in eagle:
        e.update()
        if RandomVariable % 10 == 0:
            if abs(e.pos_x - curr_x) > 320 or abs(e.pos_y - curr_y) > 320:
                e.remove(e)    
    
    RandomVariable += 1
    

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
