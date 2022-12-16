import pygame, sys # Projekti teinud Juhan Pauklin ja Kristina Katarina Kaljumäe
import time        # Projekti tegemiseks saadi informatsiooni videotest, mis asuvad aadressil https://www.youtube.com/playlist?list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
kell = pygame.time.Clock()
screen_ratio = 0.7
screen_width = 1332 * screen_ratio
screen_height = 850 * screen_ratio

pygame.init()
win = pygame.display.set_mode([screen_width, screen_height])

# pildid on võetud aadressilt https://craftpix.net/all-game-assets/
jumping = [pygame.image.load('jump1.png'), pygame.image.load('jump2.png')]
walkRight = [pygame.image.load('R1.1.png'), pygame.image.load('R2.1.png'), pygame.image.load('R3.1.png'), pygame.image.load('R4.1.png'), pygame.image.load('R5.1.png'), pygame.image.load('R6.1.png'), pygame.image.load('R7.1.png'), pygame.image.load('R8.1.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png')]
fightRight = [pygame.image.load('FP1.png'), pygame.image.load('FP2.png'), pygame.image.load('FP3.png'), pygame.image.load('FP4.png')]
fightLeft = [pygame.image.load('FL1.png'), pygame.image.load('FL2.png'), pygame.image.load('FL3.png'), pygame.image.load('FL4.png')]
taust = pygame.image.load('Taust3.jpg')
taust = pygame.transform.scale(taust, (screen_width, screen_height))
taustFB = pygame.image.load("Taust2.jpg")
taustFB = pygame.transform.scale(taustFB, (670, 400))
keskelParem = pygame.image.load('R9.1.png')
keskelVasak = pygame.image.load("L9.png")
uks1 = pygame.image.load("Uks1.png") # kinnine uks
uks2 = pygame.image.load("Uks2.png") # lahtine uks
võti = pygame.image.load("võti.png")
R_surm = [pygame.image.load('DR.1.png'), pygame.image.load('DR.2.png'), pygame.image.load('DR.3.png'), pygame.image.load('DR.4.png'), pygame.image.load('DR.5.png'), pygame.image.load('DR.6.png')]
FB_surm =[pygame.image.load('dead (1).png'),pygame.image.load('dead (2).png'),pygame.image.load('dead (3).png'),pygame.image.load('dead (4).png'),pygame.image.load('dead (5).png'),pygame.image.load('dead (6).png'),pygame.image.load('dead (7).png'),pygame.image.load('dead (8).png'),pygame.image.load('dead (9).png'),pygame.image.load('dead (10).png'),pygame.image.load('dead (10).png'),pygame.image.load('dead (10).png'),pygame.image.load('dead (10).png'),pygame.image.load('dead (10).png'),pygame.image.load('dead (10).png'),pygame.image.load('dead (10).png')]
FB_attack = [pygame.image.load('attack (1).png'),pygame.image.load('attack (2).png'),pygame.image.load('attack (3).png'),pygame.image.load('attack (4).png'),pygame.image.load('attack (5).png'),pygame.image.load('attack (6).png'),pygame.image.load('attack (7).png'),pygame.image.load('attack (8).png'),pygame.image.load('attack (9).png'),pygame.image.load('attack (10).png'),pygame.image.load('attack (1).png')]
FB_idle = [pygame.image.load('Idle(1).png'),pygame.image.load('Idle(2).png'),pygame.image.load('Idle(3).png'),pygame.image.load('Idle(4).png'),pygame.image.load('Idle(5).png'),pygame.image.load('Idle(6).png'),pygame.image.load('Idle(7).png'),pygame.image.load('Idle(8).png'),pygame.image.load('Idle(9).png'),pygame.image.load('Idle(10).png'),pygame.image.load('Idle(1).png')]
FB_charge = [pygame.image.load('charge (1).png'),pygame.image.load('charge (2).png'),pygame.image.load('charge (3).png'),pygame.image.load('charge (4).png'),pygame.image.load('charge (5).png'),pygame.image.load('charge (6).png'),pygame.image.load('charge (7).png'),pygame.image.load('charge (8).png'),pygame.image.load('charge (9).png'),pygame.image.load('charge (10).png'),pygame.image.load('charge (1).png')]

algus_taust = pygame.image.load("Start_taust.jpg")
võit_taust = pygame.image.load("Rüütel.jpg")
x = 200 * screen_ratio    # tegelase algkordinaadid
y = 850-64-50 * screen_ratio
width = 64
height = 64
vel = 5 * screen_ratio
knight_hp = 100
knight_dyingCount = 0

plat_x = 400 * screen_ratio # platvormi argumendid
plat_y = 600 * screen_ratio
plat_width = 150 * screen_ratio
plat_height = 50 * screen_ratio

plat2_x = 600 * screen_ratio # teine platvorm
plat2_y = 400 * screen_ratio
plat2_width = 50 * screen_ratio
plat2_height = 50 * screen_ratio

plat3_x = 800 * screen_ratio # kolmas platvorm
plat3_y = 350 * screen_ratio
plat3_width = 200 * screen_ratio
plat3_height = 50 * screen_ratio
onPlatform3 = False

plat4_x = 400 * screen_ratio
plat4_y = 600 * screen_ratio
plat4_width = 1332 * screen_ratio

vasak = False # kõndimise animatsioonid
parem = False
fight = False
viimatiParem = True
sammud = 0

isJump = False # hüppamise muutujad
jumpCount = 15
airtime = 0
onGround = True
onPlatform = False
isInTheMiddleOfJump = False
maapind = 736 * screen_ratio

uksLahti = False # ukse muutujad
uks1_x = 928 * screen_ratio
uks1_y = 272 * screen_ratio
uks2_x = 915 * screen_ratio
uks2_y = 263 * screen_ratio
avamised = 0
punktid = 0
aeg = 0 # final bossi animatsiooniks vajalik muutuja
nulli_aeg = True
lõpp = False
room2 = False
heledam1 = False
heledam2 = False
heledam3 = False
heledam4 = False
õpetus = False
rs = False # rüütli surma näitaja
run = True

# Final Boss
FB_hp = 150
FB_x = 450 * screen_ratio
FB_y = 100 * screen_ratio
FB_dir = -1 # -1 = vasak & 1 = parem
FB_idling = True
FB_charging = False
FB_attacking = False

# Siit algab kõik seondub luukerega. 'skel_' muutuja ees näitab, et seondub luukerega.   
skel_walkRight = [pygame.image.load('002.png'), pygame.image.load('004.png'), pygame.image.load('006.png'), pygame.image.load('008.png'), pygame.image.load('010.png'), pygame.image.load('012.png'),pygame.image.load('014.png'), pygame.image.load('016.png'), pygame.image.load('018.png'),pygame.image.load('020.png'), pygame.image.load('022.png'), pygame.image.load('024.png')]
skel_walkLeft = [pygame.image.load('001.png'), pygame.image.load('003.png'), pygame.image.load('005.png'), pygame.image.load('007.png'), pygame.image.load('009.png'), pygame.image.load('011.png'),pygame.image.load('013.png'), pygame.image.load('015.png'), pygame.image.load('017.png'),pygame.image.load('019.png'), pygame.image.load('021.png'), pygame.image.load('023.png')]
skel_dying = [pygame.image.load('D1.png'),pygame.image.load('D2.png'),pygame.image.load('D3.png'),pygame.image.load('D4.png'),pygame.image.load('D5.png'),pygame.image.load('D6.png'),pygame.image.load('D7.png'),pygame.image.load('D8.png'),pygame.image.load('D9.png'),pygame.image.load('D10.png'),pygame.image.load('D11.png'),pygame.image.load('D12.png'),pygame.image.load('D13.png')]
skel_attack_anim = [pygame.image.load('A1.png'),pygame.image.load('A2.png'),pygame.image.load('A3.png'),pygame.image.load('A4.png'),pygame.image.load('A5.png'),pygame.image.load('A6.png'),pygame.image.load('A7.png'),pygame.image.load('A8.png'),pygame.image.load('A9.png'),pygame.image.load('A10.png'),pygame.image.load('A11.png'),pygame.image.load('A12.png'),pygame.image.load('A13.png'),]

skel_hp = 100
skel_x = 600*screen_ratio
skel_y = 680*screen_ratio
skel_width = 128
skel_height = 128
skel_end = 800*screen_ratio
path = [skel_x, skel_end]
skel_walkcount = 0
skel_vel = 3
skel_died = False
skel_dyingCount = 0
skel_attackcount = 0

def skel_move(): # paneb luukere kõndima edasi-tagasi
    global skel_vel
    global skel_x
    global path
    global skel_walkCount
    global skel_attackcount
    
    skel_attackcount = 0
    if skel_vel > 0:
        if skel_x  + skel_vel < path[1]:
            skel_x += skel_vel
        else:
            skel_vel = skel_vel * -1
            skel_walkCount = 0
    else:
        if skel_x - skel_vel > path[0]:
            skel_x += skel_vel
        else:
            skel_vel = skel_vel * -1
            skel_walkCount = 0
            
def skel_draw(win): # Luukere kõndimise animatsioon
    global skel_walkcount
    global skel_hp
    skel_move()
    if skel_walkcount + 1 >= 36:
        skel_walkcount = 0
    if skel_vel > 0:
        win.blit(skel_walkRight[skel_walkcount // 3], (skel_x, skel_y))
        skel_walkcount += 1
    else:
        win.blit(skel_walkLeft[skel_walkcount // 3], (skel_x, skel_y))
        skel_walkcount += 1
    pygame.draw.rect(win, "red", pygame.Rect(skel_x, skel_y, skel_hp, 10))
    
def skel_attack(): # Luukere ründamise animatsioon
    global skel_attackcount
    global skel_hp
    pygame.draw.rect(win, "red", pygame.Rect(skel_x, skel_y, skel_hp, 10))
    if skel_attackcount + 1 >= 65:
        skel_attackcount = 0
    if skel_vel > 0:
        win.blit(skel_attack_anim[skel_attackcount // 5], (skel_x, skel_y))
        skel_attackcount += 1

    elif skel_vel < 0:
        win.blit(pygame.transform.flip(skel_attack_anim[skel_attackcount // 5], True, False), (skel_x, skel_y))
        skel_attackcount += 1

        
def skel_spot(): # Kontrollib kas rüütel on läheduses ning animatsiooniga kooskõlas (õigete sprite'ide ajal) vähendab rüütli elusid 
    global knight_hp
    if skel_vel > 0:
        if x >= skel_x+48 and x <= skel_x + 112 and y > maapind-128:
            if skel_attackcount > 20 and skel_attackcount < 30 or skel_attackcount > 40 and skel_attackcount < 50:
                knight_hp -= 1
            return True
        else:
            return False
    elif skel_vel < 0:
        if x <= skel_x+48 and x >= skel_x - 64 and y > maapind-128:
            if skel_attackcount > 20 and skel_attackcount < 30 or skel_attackcount > 40 and skel_attackcount < 50:
                knight_hp -= 1
            return True
        else:
            return False

def FB_animations(win): # Final Bossi tegevus ja animatsioonid 
    global FB_idling
    global FB_charging
    global FB_attacking
    global aeg
    global FB_dir
    global FB_x
    global knight_hp
    
    if FB_idling == True:
        if FB_dir == 1:
            win.blit(FB_idle[aeg // 5], (FB_x, FB_y+128))
        else:
            win.blit(pygame.transform.flip(FB_idle[aeg // 5], True, False), (FB_x, FB_y+128))
        if aeg // 5 == 10:
            FB_idling = False
            aeg = 0
            FB_charging = True
            
    elif FB_charging == True:
        if FB_x+140 < x+32 < FB_x+150 and FB_y+25 < y+64:
            knight_hp -= 3
        if FB_dir == 1:
            win.blit(FB_charge[aeg // 5], (FB_x, FB_y))
        else:
            win.blit(pygame.transform.flip(FB_charge[aeg // 5], True, False), (FB_x, FB_y))
        FB_x = FB_x + (FB_dir * 5)
        if aeg // 5 == 10:
            FB_charging = False
            aeg = 0
            FB_attacking = True
            FB_dir = FB_dir * -1
            
    elif FB_attacking == True: 
        if FB_dir == 1:
            win.blit(FB_attack[aeg // 5], (FB_x-70, FB_y+20))
            if FB_x+64 < x+32 < FB_x+192 and y > FB_y+100 and 5<aeg//5<11:
                knight_hp -= 2
        else:
            win.blit(pygame.transform.flip(FB_attack[aeg // 5], True, False), (FB_x-40, FB_y+20))
            if FB_x < x+32 < FB_x+128 and y > FB_y+100 and 5<aeg//5<11:
                knight_hp -= 2
        if aeg // 5 == 10:
            FB_attacking = False
            aeg = 0
            FB_idling = True
        
def attack(): # Rüütli rünnak
    global skel_hp
    global FB_hp
    if viimatiParem:
        if x+64 >= skel_x+16 and x+64 <= skel_x+128-16 and y > skel_y-32:
            skel_hp -= 5
        if room2:
            if FB_x<x+64<FB_x+128:
                FB_hp -= 5
    elif not viimatiParem: 
        if x >= skel_x+16 and x <= skel_x+128-16 and y > skel_y-32:
            skel_hp -= 5
        if room2:
            if FB_x<x<FB_x+128:
                FB_hp -= 5
            
def knight_death(): # Rüütli surm
    global knight_dyingCount
    global rs
    global run
    if vel > 0:
        win.blit(R_surm[knight_dyingCount // 6], (x, y))
        if knight_dyingCount // 6 == 5:
            rs = True
            time.sleep(1)
            run = False
    elif vel < 0:
        win.blit(pygame.transform.flip(R_surm[knight_dyingCount // 6], True, False), (x, y))
        if knight_dyingCount // 6 == 5:
            rs = True
            time.sleep(1)
            run = False
    if knight_dyingCount < 35:
        knight_dyingCount += 1 

def kujundus(): # MAIN loopi kujundus enne ukse avamist
    global punktid
    global sammud
    global uksLahti
    global skel_hp
    global rs
    
    pygame.display.set_caption("Mäng")
    win = pygame.display.set_mode([screen_width, screen_height])
    win.blit(taust, (0,0))
    pygame.draw.rect(win, "green", pygame.Rect(x, y-24, knight_hp, 10))
    
    pygame.draw.rect(win, (100 * screen_ratio, 65 * screen_ratio, 30 * screen_ratio), (plat_x, plat_y, plat_width, plat_height)) # Platvormid
    pygame.draw.rect(win, (100 * screen_ratio, 65 * screen_ratio, 30 * screen_ratio), (plat2_x, plat2_y, plat2_width, plat2_height))
    pygame.draw.rect(win, (100 * screen_ratio, 65 * screen_ratio, 30 * screen_ratio), (plat3_x, plat3_y, plat3_width, plat3_height))
    
    if punktid > 8: # Ukse avamine
        uksLahti = True
        win.blit(uks2,(uks2_x-16, uks2_y-16))
    elif 8 > punktid > 4:
        uksLahti = False
        win.blit(võti,(900 * screen_ratio, 736 * screen_ratio))
        win.blit(uks1,(uks1_x-16, uks1_y-16))
    else:
        uksLahti = False
        win.blit(uks1,(uks1_x-16, uks1_y-16))
    
    if sammud + 1 >= 32: # Animatsioonide jaoks
        sammud = 0
    
    if knight_hp > 0:
        if isInTheMiddleOfJump: # Hüppamine
            if viimatiParem:
                win.blit(jumping[0], (x,y))
            else:
                win.blit(pygame.transform.flip(jumping[0], True, False), (x,y))
        elif onGround == False and onPlatform == False: # Langemine
            if viimatiParem:
                win.blit(jumping[1], (x,y))
            else:
                win.blit(pygame.transform.flip(jumping[1], True, False), (x,y))
            
        else:
            if fight and viimatiParem: # Võitlemine
                win.blit(fightRight[sammud//8], (x,y))
                sammud = sammud + 2
            elif fight and not viimatiParem:
                win.blit(fightLeft[sammud//8], (x,y))
                sammud = sammud + 2
            elif parem:
                win.blit(walkRight[sammud//4], (x,y))
                sammud = sammud + 1
            elif vasak:
                win.blit(walkLeft[sammud//4], (x,y))
                sammud = sammud + 1
            else:
                if viimatiParem:
                    win.blit(keskelParem, (x,y))
                else:
                    win.blit(keskelVasak, (x,y))
    else:
        knight_death()
            
    global skel_dyingCount # Luukere tegevus elusana
    if skel_hp > 0:
        if skel_spot() == False:
            skel_draw(win)
        elif skel_spot() == True:
            skel_attack()
    elif skel_hp <= 0 and skel_dyingCount < 39: # Luukere surm
        punktid = 5
        if skel_vel > 0:
            win.blit(skel_dying[skel_dyingCount // 3], (skel_x, skel_y))
            skel_dyingCount += 1
        else:
            win.blit(pygame.transform.flip(skel_dying[skel_dyingCount // 3], True, False), (skel_x, skel_y))
            skel_dyingCount += 1  
    pygame.display.update()     

def kujundusFB():  # MAIN loopi kujundus peale ukse avamist
    global sammud
    global aeg
    global paus
    global lõpp
    global knight_hp
    global knight_dyingCount
    global run
    global rs
    global nulli_aeg
    
    pygame.init()
    win = pygame.display.set_mode([670, 400])
    pygame.display.set_caption("Final boss")
    win.blit(taustFB, (0,0))
    pygame.draw.rect(win, "green", pygame.Rect(x, y-24, knight_hp, 10)) # Rüütli elude riba
    
    if lõpp == False and FB_hp>0: # Final Bossi tegevuse realiseerimine
        pygame.draw.rect(win, "red", pygame.Rect(FB_x+100, FB_y+50, FB_hp, 10))
        FB_animations(win)            
    elif lõpp == False:
        if nulli_aeg == True:
            aeg = 0
            nulli_aeg = False 
        win.blit(FB_surm[aeg//5],(FB_x-17,FB_y+88))
        if aeg//5 >= 15: # Kui FB surmaanimatsioon on lõppenud saab mäng läbi
            lõpp = True
            time.sleep(1)
            run = False
    aeg += 1
    if sammud + 1 >= 32:
        sammud = 0
    
    if knight_hp > 0:
        if isInTheMiddleOfJump:
            if viimatiParem:
                win.blit(jumping[0], (x,y))
            else:
                win.blit(pygame.transform.flip(jumping[0], True, False), (x,y))
        elif onGround == False and onPlatform == False:
            if viimatiParem:
                win.blit(jumping[1], (x,y))
            else:
                win.blit(pygame.transform.flip(jumping[1], True, False), (x,y))
            
        else:
            if fight and viimatiParem:
                win.blit(fightRight[sammud//8], (x,y))
                sammud = sammud + 2
            
            elif fight and not viimatiParem:
                win.blit(fightLeft[sammud//8], (x,y))
                sammud = sammud + 2
            elif parem:
                win.blit(walkRight[sammud//4], (x,y))
                sammud = sammud + 1
                
            elif vasak:
                win.blit(walkLeft[sammud//4], (x,y))
                sammud = sammud + 1
            
            else:
                if viimatiParem:
                    win.blit(keskelParem, (x,y))
                else:
                    win.blit(keskelVasak, (x,y))
    else:
        if vel > 0: # Rüütli srum
            win.blit(R_surm[knight_dyingCount // 6], (x, y))
            if knight_dyingCount // 6 == 5:
                rs = True 
                time.sleep(1)
                run = False
        elif vel < 0:
            win.blit(pygame.transform.flip(R_surm[knight_dyingCount // 6], True, False), (x, y))
            if knight_dyingCount // 6 == 5:
                rs = True
                time.sleep(1)
                run = False
        if knight_dyingCount < 35:
            knight_dyingCount += 1 
    pygame.display.update()

def algus(): # Mänguvälised menüüd 
    global heledam1
    global heledam2
    pygame.init()
    win = pygame.display.set_mode([474, 474])
    pygame.display.set_caption("algus")
    win.blit(algus_taust, (0,0))
    
    fontpk = pygame.font.SysFont('bahnschrift', 70)
    fontn =pygame.font.SysFont('bahnschrift', 35)
    pealkiri = fontpk.render('Rüütliseiklus', False, (192, 192, 192))
    nupp1 = fontn.render('Mängi', False, (0, 0, 0))
    nupp1_teine = fontn.render('Mängi', False, (192, 192, 192))
    nupp2 = fontn.render('Kuidas mängida?', False, (0, 0, 0))
    nupp2_teine = fontn.render('Kuidas mängida?', False, (192, 192, 192))
    win.blit(pealkiri, (30,50))
    
    if heledam1:
        pygame.draw.rect(win, (192, 192, 192), (180, 200, 120, 50))
        win.blit(nupp1, (190, 200))
    else:
        pygame.draw.rect(win, (0, 0, 0), (180, 200, 120, 50))
        win.blit(nupp1_teine, (190, 200))
    if heledam2:
        pygame.draw.rect(win, (192, 192, 192), (90, 300, 300, 50))
        win.blit(nupp2, (110, 300))
    else:
        pygame.draw.rect(win, (0, 0, 0), (90, 300, 300, 50))
        win.blit(nupp2_teine, (110, 300))
    pygame.display.update()
 
def juhend():
    pygame.init()
    win = pygame.display.set_mode([474, 474])
    pygame.display.set_caption("Kuidas mängida?")
    win.blit(algus_taust, (0,0))
    font = pygame.font.SysFont('bahnschrift', 35)
    fonttekst = pygame.font.SysFont('bahnschrift', 25)
    tekst1 = fonttekst.render("Mängu eesmärk on jõuda final boss'ini", False, (192, 192, 192))
    tekst2 = fonttekst.render("ja teda võita. Final bossini jõuab läbi", False, (192, 192, 192))
    tekst3 = fonttekst.render("ukse, mis avaneb peale luukere võitmist.", False, (192, 192, 192))
    tekst4 = fonttekst.render("Paremale ja vasakule liikumiseks saab", False, (192, 192, 192))
    tekst5 = fonttekst.render("kasutada noolenuppe, hüppamiseks", False, (192, 192, 192))
    tekst6 = fonttekst.render("tühikuklahvi ning võitlemiseks tuleb", False, (192, 192, 192))
    tekst7 = fonttekst.render("hoida all "'"w"-d.', False, (192, 192, 192))
    tekst8 = fonttekst.render("Edu! ;)", False, (192, 192, 192))
    win.blit(tekst1, (20,50))
    win.blit(tekst2, (20,90))
    win.blit(tekst3, (20,130))
    win.blit(tekst4, (20,210))
    win.blit(tekst5, (20,250))
    win.blit(tekst6, (20,290))
    win.blit(tekst7, (20,330))
    win.blit(tekst8, (20,370))
    nupp3 = font.render('Mängi', False, (0, 0, 0))
    nupp3_teine = font.render('Mängi', False, (192, 192, 192))
    if heledam3:
        pygame.draw.rect(win, (192, 192, 192), (300, 400, 120, 50))
        win.blit(nupp3, (310, 400))
    else:
        pygame.draw.rect(win, (0, 0, 0), (300, 400, 120, 50))
        win.blit(nupp3_teine, (310, 400))
    pygame.display.update()
def kaotus():
    pygame.init()
    win = pygame.display.set_mode([474, 220])
    pygame.display.set_caption("Kaotus")
    win.blit(algus_taust, (0,0))
    font = pygame.font.SysFont('bahnschrift', 35)
    k_tekst = font.render('Kahjuks ei õnnestunud', False, (192, 192, 192))
    k_tekst2 = font.render('sul seekord võita ;(', False, (192, 192, 192))
    win.blit(k_tekst, (40,40))
    win.blit(k_tekst2, (40,90))
    nupp4 = font.render('OK', False, (0, 0, 0))
    nupp4_teine = font.render('OK', False, (192, 192, 192))
    if heledam4:
        pygame.draw.rect(win, (192, 192, 192), (190, 150, 100, 50))
        win.blit(nupp4, (210, 150))
    else:
        pygame.draw.rect(win, (0, 0, 0), (190, 150, 100, 50))
        win.blit(nupp4_teine, (210, 150))
    pygame.display.update()
def võit():
    pygame.init()
    win = pygame.display.set_mode([512, 512])
    pygame.display.set_caption("Võit")
    win.blit(võit_taust, (0,0))
    font = pygame.font.SysFont('bahnschrift', 35)
    k_tekst = font.render('Palju õnne!!!', False, (0, 0, 0))
    k_tekst2 = font.render('Sa võitsid Final bossi :)', False, (0, 0, 0))
    win.blit(k_tekst, (230,40))
    win.blit(k_tekst2, (140,90))
    nupp4 = font.render('OK', False, (0, 0, 0))
    nupp4_teine = font.render('OK', False, (192, 192, 192))
    if heledam4:
        pygame.draw.rect(win, (192, 192, 192), (310, 270, 100, 50))
        win.blit(nupp4, (330, 270))
    else:
        pygame.draw.rect(win, (0, 0, 0), (310, 270, 100, 50))
        win.blit(nupp4_teine, (330, 270))
    pygame.display.update()
    
running = True
while running:
    algus()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 300 >= hiir[0] >= 180 and 250>= hiir[1] >= 200:
                running = False
            elif 390 >= hiir[0]>= 90 and 350 >= hiir[1] >= 300:
                running = False
                õpetus = True
    hiir = pygame.mouse.get_pos()
    if 300 >= hiir[0] >= 180 and 250>= hiir[1] >= 200:
        heledam1 = True
        heledam2 = False
    elif 390 >= hiir[0]>= 90 and 350 >= hiir[1] >= 300:
        heledam1 = False
        heledam2 = True
    else:
        heledam2 = False
        heledam1 = False

while õpetus:
    juhend()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            õpetus = False
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and 420 >= hiir[0] >= 300 and 450 >= hiir[1] >= 400:
            õpetus = False
    hiir = pygame.mouse.get_pos()
    if 420 >= hiir[0] >= 300 and 450 >= hiir[1] >= 400:
        heledam3 = True
    else:
        heledam3 = False
        
while run: # MAIN LOOP
    if room2 == False:
        kujundus()
    else:
        kujundusFB()
    
    kell.tick(32)     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        
    keys = pygame.key.get_pressed()
    
    if knight_hp > 0:
        if room2 == False:
            if keys[pygame.K_LEFT] and x > vel: # paremale ja vasakule liikumine
                x -= vel
                vasak = True
                parem = False
                viimatiParem = False
                if not keys[pygame.K_w]:
                    fight = False
            elif keys[pygame.K_RIGHT] and x < screen_width - 69 - vel:
                x += vel
                vasak = False
                parem = True
                viimatiParem = True
                if not keys[pygame.K_w]:
                    fight = False
            elif keys[pygame.K_w]:
                fight = True
                if sammud//8>2:
                    attack()

            else:
                fight = False
                vasak = False
                parem = False
                sammud = 0
        else:
            if keys[pygame.K_LEFT] and x > vel: # Paremale ja vasakule liikumine
                x -= vel
                vasak = True
                parem = False
                viimatiParem = False
                if not keys[pygame.K_w]:
                    fight = False
            elif keys[pygame.K_RIGHT] and x < 670 - 69 - vel:
                x += vel
                vasak = False
                parem = True
                viimatiParem = True
                if not keys[pygame.K_w]:
                    fight = False
            elif keys[pygame.K_w]: # Rüütli rünnak
                fight = True
                if sammud//8>2:
                    attack()

            else:
                fight = False
                vasak = False
                parem = False
                sammud = 0

        # Hüppamine    
        if not(isJump): # Et ei saaks uuesti hüpata hüppamise tsükli ajal.
            if keys[pygame.K_SPACE]: # kui space-bari vajutatakse
                isJump = True
                vasak = False
                parem = False
                sammud = 0
        else:
            if jumpCount >= 0 and (onGround == True or onPlatform == True or isInTheMiddleOfJump == True): # Saab hüpata kui oled maa peal või platvormi peal.
                isInTheMiddleOfJump = True                                                                 # Hüppamise tsükkel jätkub kuni seda on 15 korda läbitud.
                y -= round((jumpCount ** 2) * 0.15, 4)                                                    # Hüppamise tüskkel saab jätkuda siis kui hüppamist on alustatud.
                jumpCount -= 1                                                                             # isInTheMiddleOfJump = et õhkutõusu jätkataks
            else:                                                                                          # isJump = et ei saaks uuesti hüpata hüppamise tsükli ajal.
                jumpCount = 15
                isJump = False
                isInTheMiddleOfJump = False
            
    if y < maapind: # Kui oled kõrgemal kui maapind, ei ole sa maa peal
        onGround = False

    if y < maapind and isInTheMiddleOfJump == False and onPlatform == False: # Kukkumine
        y += airtime
        airtime += 1
    elif y == maapind: # Kukud kuni oled maapinnal
        airtime = 0
        onGround = True
    elif y > maapind: # Kui kukud maapinnas läbi, satud tagasi maapinnale
        y = maapind
    if x+32>=plat_x and x+32<=plat_x+plat_width and y+height>=plat_y and y+height<plat_y+height and isInTheMiddleOfJump == False and room2 == False: # Platvormile sattumine
        y = plat_y -64
        onPlatform = True
        airtime = 0
    else:
        if x+32>=plat2_x and x+32<=plat2_x+plat2_width and y+height>=plat2_y and y+height<plat2_y+height and isInTheMiddleOfJump == False and room2 == False: #teine platvorm
            y = plat2_y -64
            onPlatform = True
            airtime = 0
        else:
            if x+32>=plat3_x and x+32<=plat3_x+plat3_width and y+height>=plat3_y and y+height<plat3_y+height and isInTheMiddleOfJump == False and room2 == False: #kolmas platvorm
                y = plat3_y -64
                onPlatform = True
                onPlatform3 = True
                airtime = 0
            else:
                onPlatform = False
                onPlatform3 = False
    
    if skel_hp <= 0 and x >= 875 * screen_ratio:
        punktid = 10
        
    
    if uksLahti and x + 32 >= uks2_x and onPlatform3 and avamised == 0: # avamised on selleks, et seda lauset mitu korda ei tehtaks, sest siis hakkab display vilkuma
        avamised = 1
        pygame.display.quit() # Minnakse üle uude "ruumi" (uus taustapilt)
        room2 = True
        maapind = 370 * screen_ratio
        x = 50 * screen_ratio
        y = 300 * screen_ratio

    
while rs:
    kaotus()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rs = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 290 >= hiir[0] >= 190 and 200>= hiir[1] >= 150:
                rs = False
    hiir = pygame.mouse.get_pos()
    if 290 >= hiir[0] >= 190 and 200 >= hiir[1] >= 150:
        heledam4 = True
    else:
        heledam4 = False
while lõpp:
    võit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lõpp = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 410 >= hiir[0] >= 310 and 320 >= hiir[1] >= 270:
                lõpp = False
    hiir = pygame.mouse.get_pos()
    if 410 >= hiir[0] >= 310 and 320 >= hiir[1] >= 270:
        heledam4 = True
    else:
        heledam4 = False

pygame.quit()