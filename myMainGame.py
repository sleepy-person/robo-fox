from RetroPy.retroPy import rpy, kb, draw, disp, gameObj, LoadSpriteStr, LoadSprite, sMap
import os, random, time, math
from RetroPy.Sprites import bombs
from myGame.myPlayer import player, doPlayer, drawPlayer, projectile
from myGame.myEnemies import enemies, doEnemies, drawEnemies
p_boss1 = LoadSprite("boss1.rs4")
p_shield = LoadSprite("shield.rs4")
p_bomb1 = LoadSpriteStr(bombs.bomb1)
p_bomb2 = LoadSpriteStr(bombs.bomb2)

boss_speed = 45
boss_life_max = 15
boss = []
boss.append(gameObj(p_boss1, -90, 10, 200, boss_speed, 0))
boss[-1].val(boss_life_max)
bombs = []

# -----------------------------------------------------------------------------
dtt = 0
# =======================================================================================
def Update(dt):
    global dtt
    dtt += dt
    
    doEnemies(dt)
    doPlayer(dt)
    for bos in boss:
        bos.update()
        if bos.pos_x>200:
            bos.speed_x=-boss_speed
        if bos.pos_x<0:
            bos.speed_x=boss_speed
        if bos.pos_x%45==0:
            for i in range(-2,2,1):
                bombs.append(gameObj(random.choice([p_bomb1,p_bomb2]),bos.pos_x+25,bos.pos_y+16))
                bombs[-1].speed_y=100
                bombs[-1].speed_x=i*30
        if bos.val()<1:
            boss.remove(bos)
    
    for b in bombs:
        b.update()
        if b.pos_y>230:
            bombs.remove(b)
        if b.collider(player):
            rpy.quit()
    for p in projectile:
        for bos in boss:
            if p.collider(bos):
                projectile.remove(p)
                bos.val(bos.val()-1)
        for e in enemies:
            if p.collider(e):
                projectile.remove(p)
                enemies.remove(e)

# =======================================================================================
def Draw(dt):
    global dtt
    draw.clear()
        
    drawEnemies()
    drawPlayer()
    for bos in boss:
        bos.draw()
        draw.filled_rect(bos.pos_x-7,bos.pos_y-4,boss_life_max*4,7,5)
        draw.filled_rect(bos.pos_x-7,bos.pos_y-4,bos.val()*4,7,11)
    for b in bombs:
        b.draw()

    draw.text(str(len(enemies)), 2, 0, 7)  # number of enemies
    draw.text(str(dt), 200, 1, 7)    # frame time
    draw.text(str(dtt), 200, 10, 7)  # total time
# =======================================================================================
# =======================================================================================               
rpy.run(Update, Draw) 
# =======================================================================================



