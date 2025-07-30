from RetroPy.retroPy import rpy, kb, draw, disp, gameObj, LoadSpriteStr, LoadSprite, sprite
import os, random, time
import math
import RetroPy.AB2Cont
with open("/rpg/data_literal.py") as f:
    code = f.read()
exec(code)

p_fox = LoadSprite("/rpg/assets/fox.rs8")
p_foxrun = LoadSprite("/rpg/assets/foxrun.rs8")
p_foxattack = LoadSprite("/rpg/assets/foxattack.rs8")
i_health = LoadSprite("/rpg/assets/Health.rs8")
i_warmth = LoadSprite("/rpg/assets/Fire.rs8")
i_hunger = LoadSprite("/rpg/assets/Hunger.rs8")
player=gameObj(p_fox,112,120,70,currNdx=0)
curr_x,curr_y=1024,1024
prevmove,move,dirr=0,0,0
objs=[]
for obj in range(8):
    objs.append(sprite(LoadSprite(f"/rpg/tiles/tile{obj+1}.rs8")))
mapp=matrix
climate=1
despawn=0
rand=0
health = 100
maxhealth = 100
hunger = 75
maxhunger = 100
warmth = 750
maxwarmth = 1000

e_bear = LoadSprite("/rpg/assets/Polar_Bear.rs8")
e_bearattack = LoadSprite("/rpg/assets/Polar_Bear_Attack.rs8")
enemies=[]

def clampmove(x,y):
    global curr_x, curr_y
    curr_x+= x if (curr_x+x>=0) and (curr_x+x<=1790) else 0
    curr_y+= y if (curr_y+y>=0) and (curr_y+y<=1790) else 0

def Update(dt):
    global dtt, move, prevmove, curr_x, curr_y, dirr, despawn, enemies
    global health, hunger, warmth, rand, maxhunger, maxhealth, maxwarmth
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

    if (random.random() * 100) < ((1 * 3 + climate * 5) ** dt) and len(enemies)<climate:
        tempx,tempy=curr_x+(random.randint(-110, -80) if random.random() < 0.5 else random.randint(80, 110)),curr_y+(random.randint(-110, -80) if random.random() < 0.5 else random.randint(80, 110))
        print(tempx-curr_x,tempy-curr_y)
        enemies.append([gameObj(e_bear, int(tempx-curr_x), int(tempy-curr_y)),"bear",50,tempx,tempy])
    
    if rand % 9 == 0:
        if hunger >= 7 and health < maxhealth:
            health += 1
        if move > 5:
            hunger -= 1
        warmth -= 5
    
    for enemy in enemies:
        hit=0
        if (abs(enemy[3]-curr_x)<1 and abs(enemy[4]-curr_y)<1):
            health-=10
        else:
            if (enemy[3]-curr_x!=0):
                enemy[3]-=abs(enemy[3]-curr_x)//(enemy[3]-curr_x)
            if (enemy[4]-curr_y!=0):
                enemy[4]-=abs(enemy[4]-curr_y)//(enemy[4]-curr_y)
        enemy[0].pos_x,enemy[0].pos_y=int(enemy[3]-curr_x)+120, int(enemy[4]-curr_y)+120
        enemy[0].update()
        if despawn % 10 == 0:
            if abs(enemy[0].pos_x-120) > 140 or abs(enemy[0].pos_y-120) > 140:
                enemies.remove(enemy)
            despawn=0
    
    if health<=0: #or warmth<=0 or hunger<=0:
        rpy.quit()
            
    despawn+=1
    rand+=1

# =======================================================================================
def Draw(dt):
    global dtt, move, curr_x, curr_y
    draw.clear()
    
    for x in range(0,9):
        for y in range(0,9):
            objs[mapp[int(curr_x//32)+x][int(curr_y//32)+y]].draw(0,x*32-int(curr_x)%32,y*32-int(curr_y)%32,0)
    
    for enemy in enemies:
        enemy[0].draw()
    
    player.draw()
    
    sprite(i_health).draw(0,160, 180,0)
    draw.filled_rect(185,180,maxhealth*4//10,7,5)
    draw.filled_rect(185,180,health*4//10,7,11)
    sprite(i_warmth).draw(0,160, 200,0)
    draw.filled_rect(185,200,maxwarmth*4//100,7,5)
    draw.filled_rect(185,200,warmth*4//100,7,11)
    sprite(i_hunger).draw(0,160, 220,0)
    draw.filled_rect(185,220,maxhunger*4//10,7,5)
    draw.filled_rect(185,220,hunger*4//10,7,11)
    
    draw.text(str(dt), 200, 0, 7)
    
# =======================================================================================
# =======================================================================================               
rpy.run(Update, Draw) 
# =======================================================================================