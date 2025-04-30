
from RetroPy.retroPy import rpy, kb, draw, disp, gameObj, LoadSpriteStr, LoadSprite, sprite, LoadMap, sMap
import os, random, time
import math
import RetroPy.AB2Cont

p_fox = LoadSprite("/rpg/assets/fox.rs8")
p_foxrun = LoadSprite("/rpg/assets/foxrun.rs8")

#p_foxattack = LoadSprite("/rpg/assets/ArcticFox_Attack.rs8")
b_burrow = LoadSprite("/rpg/assets/Burrow.rs8")
e_hare = LoadSprite("/rpg/assets/Arctic_Hare.rs8")
e_bush = LoadSprite("/rpg/assets/Berry_Bush.rs8")
e_lemming = LoadSprite("/rpg/assets/Lemming.rs8")
e_geese = LoadSprite("/rpg/assets/Geese.rs8")
e_geeseflying = LoadSprite("/rpg/assets/Geese_Flying.rs8")
e_cod = LoadSprite("/rpg/assets/Cod.rs8")
e_redfox = LoadSprite("/rpg/assets/Red_Fox.rs8")
e_redfoxattack = LoadSprite("/rpg/assets/Red_Fox_Attack(rs8).rs8")
e_owl = LoadSprite("/rpg/assets/Owl.rs8")
e_owlattack = LoadSprite("/rpg/assets/Owl_Attack.rs8")
e_eagle = LoadSprite("/rpg/assets/Eagle.rs8")
e_eagleattack = LoadSprite("/rpg/assets/Eagle_Attack.rs8")
e_bear = LoadSprite("/rpg/assets/Polar_Bear.rs8")
e_bearattack = LoadSprite("/rpg/assets/Polar_Bear_Attack.rs8")
i_health = LoadSprite("/rpg/assets/Health.rs8")
i_warmth = LoadSprite("/rpg/assets/Fire.rs8")
i_hunger = LoadSprite("/rpg/assets/Hunger.rs8")

p_tiles = LoadSprite("/rpg/TerrainTiles.rs8")
p_map = LoadMap("/rpg/map1_final.map")
xmap = sMap(p_tiles, p_map, 1)

hare, bush, lemming, geese, cod = [], [], [], [], []
redfox, owl, eagle, bear = [], [], [], []
burrows = []
health = 5
maxhealth = 10
hunger = 6
maxhunger = 10
warmth = 4
maxwarmth = 10
'''change this later'''

CurrentPhase = 1
RandomVariable = 0
player=gameObj(p_fox,112,120,70,currNdx=0, cam_mode = 1)
curr_x,curr_y=1024,1024
prevmove,move,dirr=0,0,0
disp.cam_pos(0,0)


def clampmove(x,y):
    global curr_x, curr_y
    curr_x+= x if (curr_x+x>=120) and (curr_x+x<=1790) else 0
    curr_y+= y if (curr_y+y>=120) and (curr_y+y<=1790) else 0

#def DealDamage(Object, Damage Dealt):
#    

def Update(dt):
    global dtt, move, prevmove, curr_x, curr_y, dirr
    global CurrentPhase, RandomVariable
    player.update()
    
    move=10
    if kb.readDown == 0:
        player.speed_y = 50
    elif kb.readUp == 0:
        player.speed_y = -50
    else:
        player.speed_y = 0
        move-= 4
    if kb.readRight == 0:
        player.speed_x = 50
        dirr=0
    elif kb.readLeft == 0:
        player.speed_x = -50
        dirr=1
    else:
        player.speed_x = 0
        move-= 4
    player.flip(dirr)
    disp.cam_pos(player.pos_x - 120, player.pos_y - 120)
        
    if prevmove!=move:
        if move>5:
            player.sprite(p_foxrun,70)
        else:
            player.sprite(p_fox,70)
    if prevmove!=move:
        if move>5:
            player.sprite(p_foxrun,70)
        else:
            player.sprite(p_fox,70)
    
    prevmove=move

    if RandomVariable // (16 / dt) == 0:
        if hunger >= 7:
            health += 1
    if RandomVariable // (10 / dt) == 0:
        if move > 5:
            hunger -= 1

    '''if kb.readB == 0:
        for row in burrow:
            if row.collider(player):
                pass
                #go to den
        elif len(burrow) < 5:
            #change sprite
            burrow.append(gameOBj(b_burrow), curr_x, curr_y)'''
            

    
    '''if kb.readA == 0:
        player.sprite(p_foxattack,70)
        for h in hare:
            if h.collider(player):
                DealDamage(hare[h], random.randint(1,4))
        for lemon in lemming:
            if lemon.collider(player):
                DealDamage(lemming[lemon], random.randint(1,4))
        for bus in bush:
            if bus.collider(player):
                DealDamage(bush[bus], random.randint(1,4))
        for gee in geese:
            if gee.collider(player):
                DealDamage(geese[gee], random.randint(1,4))
        for rf in redfox:
            if rf.collider(player):
                DealDamage(redfox[rf], random.randint(1,4))
        for bea in bear:
            if bea.collider(player):
                DealDamage(bear[bea], random.randint(1,4))
        for ow in owl:
            if ow.collider(player):
                DealDamage(owl[ow], random.randint(1,4))
        for ag in eagle:
            if ag.collider(player):
                DealDamage(eagle[ag], random.randint(1,4))
    '''            
    
    #Hare spawn rate
    if (random.random() * 100) < ((10 * 3 + CurrentPhase * 8) ** dt):
        hare.append(gameObj(e_hare), randint(128,896), randint(128,896))
        if abs(hare[-1].pos_x - curr_x) > 320 or abs(hare[-1].pos_y - curr_y) > 320:
            hare.remove(-1)
        #Read tile its on
    for h in hare:
        h.update()
        if RandomVariable % 10 == 0:
            if abs(h.pos_x - curr_x) > 320 or abs(h.pos_y - curr_y) > 320:
                hare.remove(h)

    #Lemming spawn rate
    if (random.random() * 100) < ((16 * 3 + CurrentPhase * 8) ** dt):
        lemming.append(gameObj(e_lemming), randint(128,896), randint(128,896))
        if abs(lemming[-1].pos_x - curr_x) > 320 or abs(lemming[-1].pos_y - curr_y) > 320:
            lemming.remove(-1)
        #Read tile its on
    for lemon in lemming:
        lemon.update()
        if RandomVariable % 10 == 0:
            if abs(lemon.pos_x - curr_x) > 320 or abs(lemon.pos_y - curr_y) > 320:
                lemming.remove(lemon)
                
    #Bush 
    if (random.random() * 100) < ((20 * 3 + CurrentPhase * 8) ** dt):
        bush.append(gameObj(e_bush), randint(128,896), randint(128,896))
        if abs(bush[-1].pos_x - curr_x) > 320 or abs(bush[-1].pos_y - curr_y) > 320:
            bush.remove(-1)
        #Read tile its on
    for bus in bush:
        bus.update()
        if RandomVariable % 10 == 0:
            if abs(bus.pos_x - curr_x) > 320 or abs(bus.pos_y - curr_y) > 320:
                bush.remove(bus)

    #Geese 
    if (random.random() * 100) < ((4 * 3 + CurrentPhase * 8) ** dt):
        geese.append(gameObj(e_geese), randint(128,896), randint(128,896))
        if abs(geese[-1].pos_x - curr_x) > 320 or abs(geese[-1].pos_y - curr_y) > 320:
            geese.remove(-1)
        #Read tile its on
    for gee in geese:
        gee.update()
        if RandomVariable % 10 == 0:
            if abs(gee.pos_x - curr_x) > 320 or abs(gee.pos_y - curr_y) > 320:
                geese.remove(gee)
                
    #RedFox spawn rate
    if (random.random() * 100) < ((4 * 3 + CurrentPhase * 5) ** dt):
        redfox.append(gameObj(e_redfox), randint(128,896), randint(128,896))
        if abs(redfox[-1].pos_x - curr_x) > 320 or abs(redfox[-1].pos_y - curr_y) > 320:
            redfox.remove(-1)
    for rf in redfox:
        rf.update()
        if RandomVariable % 10 == 0:
            if abs(rf.pos_x - curr_x) > 320 or abs(rf.pos_y - curr_y) > 320:
                redfox.remove(rf)

    #PolarBear spawn rate
    if (random.random() * 100) < ((1 * 3 + CurrentPhase * 5) ** dt):
        bear.append(gameObj(e_bear), randint(128,896), randint(128,896))
        if abs(bear[-1].pos_x - curr_x) > 320 or abs(bear[-1].pos_y - curr_y) > 320:
            bear.remove(-1)
    for b in bear:
        b.update()
        if RandomVariable % 10 == 0:
            if abs(b.pos_x - curr_x) > 320 or abs(b.pos_y - curr_y) > 320:
                bear.remove(b)
                
    #Owl spawn rate
    if (random.random() * 100) < ((2 * 3 + CurrentPhase * 5) ** dt):
        owl.append(gameObj(e_owl), randint(128,896), randint(128,896))
        if abs(owl[-1].pos_x - curr_x) > 320 or abs(owl[-1].pos_y - curr_y) > 320:
            owl.remove(-1)
    for o in owl:
        o.update()
        if RandomVariable % 10 == 0:
            if abs(o.pos_x - curr_x) > 320 or abs(o.pos_y - curr_y) > 320:
                owl.remove(o)

    #Eagle spawn rate
    if (random.random() * 100) < ((2 * 3 + CurrentPhase * 5) ** dt):
        eagle.append(gameObj(e_eagle), randint(128,896), randint(128,896))
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
    
    xmap.draw(disp.cam_pos_x(), disp.cam_pos_y())

    player.drawCollider(8)
   
    draw.text(str(xmap.cell(player.pos_x, player.pos_y)), 2, 200, 7)
    draw.text(str(xmap.ndx_x(player.pos_x, player.pos_y)) +"," + str(xmap.ndx_y(player.pos_x, player.pos_y)), 2, 210, 7)
    draw.text(str(player.pos_x) +"," + str(player.pos_y), 2, 220, 8)
    draw.text(str(curr_x) +"," + str(curr_y), 2, 200, 8)
   
    draw.text(str(disp.cam_pos_x())+", "+str(disp.cam_pos_y()), 2, 0, 7)
    draw.text(str(dt), 200, 0, 7)

    
    player.draw()
    
    '''i_health.draw(160, -180)
    draw.filled_rect(180,-180,maxhealth*4,7,5)
    draw.filled_rect(180,-180,health*4,7,11)
    i_warmth.draw(160, -200)
    draw.filled_rect(180,-200,maxwarmth*4,7,5)
    draw.filled_rect(180,-200,warmth*4,7,11)
    i_hunger.draw(160, -220)
    sraw.filled_rect(180,-220,maxhunger*4,7,5)
    draw.filled_rect(180,-220,hunger*4,7,11)'''
    
    draw.text(str(dt), 200, 0, 7)

    
# =======================================================================================
# =======================================================================================               
rpy.run(Update, Draw) 
# =======================================================================================

