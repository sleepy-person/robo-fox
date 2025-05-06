from RetroPy.retroPy import rpy, kb, draw, disp, gameObj, LoadSpriteStr, LoadSprite, sprite, LoadMap, sMap, gc
import os, random, time
import math
import RetroPy.AB2Cont

p_fox = LoadSprite("/rpg/assets/fox.rs8")
p_foxrun = LoadSprite("/rpg/assets/foxrun.rs8")
p_foxattack = LoadSprite("/rpg/assets/foxattack.rs8")
b_burrow = LoadSprite("/rpg/assets/Burrow.rs8")
e_hare = LoadSprite("/rpg/assets/Arctic_Hare.rs8")
e_bush = LoadSprite("/rpg/assets/bush.rs8")
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

enemies=[]
food=[]
burrows = []
health = 100
maxhealth = 100
hunger = 75
maxhunger = 100
warmth = 750
maxwarmth = 1000
'''change this later'''

CurrentPhase = 1
RandomVariable = 0
player=gameObj(p_fox,112,120,70,currNdx=0, cam_mode = 1)
curr_x,curr_y=512,512
prevmove,move,dirr=0,0,0
disp.cam_pos(0,0)

player.clamp_x(120,904)
player.clamp_y(120,904)
    
def load(animal,sprite,chance):
    if (random.random() * 100) < ((chance * 3 + CurrentPhase * 5) ** 0.031) and len(enemies)<CurrentPhase*2:
        tempx,tempy=player.pos_x+(random.randint(-110, -80) if random.random() < 0.5 else random.randint(80, 110)),player.pos_y+(random.randint(-110, -80) if random.random() < 0.5 else random.randint(80, 110))
        screenx, screeny = tempx - (player.pos_x - 256), tempy - (player.pos_y - 256)
        enemies.append([gameObj(sprite, int(screenx), int(screeny)),animal,50 if animal=="bear" else 20,int(tempx),int(tempy)])
        #print(enemies[-1][0].pos_x-player.pos_x,enemies[-1][0].pos_y-player.pos_y)
    count=0
    
    
def poad(animal,sprite,chance):
    if (random.random() * 100) < ((chance * 3 + CurrentPhase * 8) ** 0.031) and len(food)<CurrentPhase*4:
        tempx,tempy=player.pos_x+(random.randint(-120, -20) if random.random() < 0.5 else random.randint(20, 120)),player.pos_y+(random.randint(-120, -20) if random.random() < 0.5 else random.randint(20, 120))
        food.append([gameObj(sprite, int(tempx), int(tempy)),animal,2])
        #print(food[-1][0].pos_x-player.pos_x,food[-1][0].pos_y-player.pos_y)
        
    count=0

#def DealDamage(Object, Damage Dealt):
#    

def Update(dt):
    global dtt, move, prevmove, curr_x, curr_y, dirr, hunger, warmth, health
    global CurrentPhase, RandomVariable
    player.update()
    
    move=10
    if kb.readDown == 0 and player.pos_y<904:
        player.speed_y = 50
    elif kb.readUp == 0 and player.pos_y>120:
        player.speed_y = -50
    else:
        player.speed_y = 0
        move-= 4
    if kb.readRight == 0 and player.pos_x<904:
        player.speed_x = 50
        dirr=0
    elif kb.readLeft == 0 and player.pos_x>120:
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

    if RandomVariable % 9 == 0:
        if hunger >= 7 and health < maxhealth:
            health += 1
    if RandomVariable % 9 == 0:
        if move > 5:
            hunger -= 1
        warmth -= 5

    '''if kb.readB == 0:
        for row in burrow:
            if row.collider(player):
                pass
                #go to den
        elif len(burrow) < 5:
            #change sprite
            burrow.append(gameOBj(b_burrow), curr_x, curr_y)'''
            

    
    if kb.readA == 0:
        player.sprite(p_foxattack,70)
        count=0
        for enemy in enemies:
            if enemy[0].collider(player):
                print(enemies)
                print(enemy)
                enemy[2]-=random.randint(1,4)
                if enemy[2]<=0:
                    enemies.pop(count)
                    print(0)
            count+=1
        count=0
        for foo in food:
            if foo[0].collider(player):
                print(foo)
                print(food)
                foo[2]-=random.randint(1,4)
                if foo[2]<=0:
                    food.pop(count)
                    print(2)
                    hunger+=20
                    if hunger>100:
                        hunger=100
            count+=1
         
    poad("hare",e_hare,10)

    poad("lemming",e_lemming,16)
    
    poad("bush",e_bush,20)
    

    poad("geese",e_geese,4)
                
    #RedFox spawn rate
    load("redfox",e_redfox,4)

    #PolarBear spawn rate
    load("bear",e_bear,1)
                
    #Owl spawn rate
    load("owl",e_owl,2)

    #Eagle spawn rate
    load("eagle",e_eagle,2)
    
    count=0
    for enemy in enemies:
        enemy[0].update()
        enemy[0].speed_x,enemy[0].speed_y = -player.speed_x, -player.speed_y
        if RandomVariable % 10 == 0:
            if abs(enemy[0].pos_x-player.pos_x) > 400 or abs(enemy[0].pos_y-player.pos_y) > 400:
                enemies.pop(count)
                gc.collect()
            RandomVariable=0
        count+=1
        
    count=0
    for foo in food:
        foo[0].update()
        foo[0].speed_x,foo[0].speed_y = -player.speed_x, -player.speed_y
        if RandomVariable % 10 == 0:
            if abs(foo[0].pos_x-player.pos_x) > 400 or abs(foo[0].pos_y-player.pos_y) > 400:
                food.pop(count)
                gc.collect()
            RandomVariable=0
        count+=1
    
    if health<=0 or warmth<=0 or hunger<=0:
        #rpy.quit()
        pass
    
    RandomVariable += 1
    
    

# =======================================================================================
def Draw(dt):
    global dtt, move, curr_x, curr_y
    draw.clear()
    
    xmap.draw(disp.cam_pos_x(), disp.cam_pos_y())

    player.drawCollider(8)
   
    draw.text(str(xmap.cell(player.pos_x, player.pos_y)), 500, 500, 8)
    draw.text(str(xmap.ndx_x(player.pos_x, player.pos_y)) +"," + str(xmap.ndx_y(player.pos_x, player.pos_y)), 2, 210, 7)
    #draw.text(str(curr_x) +"," + str(curr_y), 2, 220, 8)
   
    draw.text(str(disp.cam_pos_x())+", "+str(disp.cam_pos_y()), 100, 100, 8)
    #draw.text(str(player.pos_x, player.pos_y), -200, -200, 7)
    draw.text(str(dt), 200, 0, 7)
    
    for enemy in enemies:
        enemy[0].draw()
        enemy[0].drawCollider(8)
    for foo in food:
        foo[0].draw()
        foo[0].drawCollider(8)
    
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
