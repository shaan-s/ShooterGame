import pygame
from random import randint
pygame.init()

run = True
dif = 1
EK = 0
fbcl = 0
mfbcl = 0
mbcl = 0
bcl = 0
rdo = 0
win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Test Game")
h2font = pygame.font.SysFont("bahnschrift", 34, 0, 0)

class Player():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 2
        self.facing = 1
        self.rect = pygame.Rect(self.x,self.y,self.w, self.h)
    def draw(self, win):
        self.rect = pygame.Rect(self.x,self.y,self.w, self.h)
        pygame.draw.rect(win, (255,45,45), (rp.rect))

class Enemy():
    def __init__(self,x,y,w,h,speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.facing = 1
        self.rect = pygame.Rect(self.x,self.y,self.w, self.h)
    def draw(self, win):
        self.rect = pygame.Rect(self.x,self.y,self.w, self.h)
        pygame.draw.rect(win, (45,45,255), (self.rect))

class Bullet():
    def __init__(self,x,y,w,h,d,speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.d = d
        self.speed = speed
        self.rect = pygame.Rect(self.x,self.y,self.w, self.h)
    def draw(self,win):
        self.rect = pygame.Rect(self.x,self.y,self.w, self.h)
        pygame.draw.rect(win, (255,45,45), (self.rect))
class HomingBullet():
    def __init__(self,x,y,w,h,d,speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.d = d
        self.speed = speed
        self.rect = pygame.Rect(self.x,self.y,self.w, self.h)
    def draw(self,win):
        self.rect = pygame.Rect(self.x,self.y,self.w, self.h)
        pygame.draw.rect(win, (45,255,45), (self.rect))

rp = Player(300, 300, 40, 40)
bullets = []
enemies = []

while run:
    win.blit(h2font.render((f"Enemies Killed: {EK}"), True, (255,255,255)), (0,0))
    win.blit(h2font.render((f"Game Difficulty: {round(dif)}"), True, (255,255,255)), (300,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False

        if event.type == pygame.KEYDOWN:
            kpress = event.key

            if kpress == pygame.K_SPACE:
               if len(bullets) < 15:
                   bullets.append(Bullet(rp.x + 10,rp.y + 10,20,20,rp.facing,4))
            elif kpress == pygame.K_LSHIFT:
                bullets.append(HomingBullet(rp.x + 10,rp.y + 10,20,20,rp.facing,5))
            elif kpress == pygame.K_RETURN:
                if mbcl == 0:
                    bullets.append(Bullet(rp.x + 10,rp.y + 10,20,20,1,4))
                    bullets.append(Bullet(rp.x + 10,rp.y + 10,20,20,2,4))
                    bullets.append(Bullet(rp.x + 10,rp.y + 10,20,20,3,4))
                    bullets.append(Bullet(rp.x + 10,rp.y + 10,20,20,4,4))
                    mbcl = 500
                else:
                    rdo = 80
            elif kpress == pygame.K_RSHIFT:
                if mfbcl == 0:
                    bullets.append(Bullet(rp.x + 10,rp.y + 10,20,20,1,8))
                    bullets.append(Bullet(rp.x + 10,rp.y + 10,20,20,2,8))
                    bullets.append(Bullet(rp.x + 10,rp.y + 10,20,20,3,8))
                    bullets.append(Bullet(rp.x + 10,rp.y + 10,20,20,4,8))
                    mfbcl = 600
                else:
                    rdo = 80
            elif kpress == pygame.K_RALT:
                if fbcl == 0:
                    bullets.append(Bullet(rp.x + 10,rp.y + 10,20,20,rp.facing,8))
                    fbcl = 250
                else:
                    rdo = 80
    if fbcl != 0:
        fbcl-=1
    if mbcl != 0:
        mbcl-=1
    if mfbcl != 0:
        mfbcl-=1
    if rdo != 0:
        rdo -= 1
        win.blit(h2font.render(("You are trying this action too fast!"), True, (255,255,255)), (0,550))
    for bullet in bullets:
        bullet.draw(win)
        if bullet.speed != 5:
            if bullet.x < 600 and bullet.x > 0 and bullet.y > 0 and bullet.y < 600:
                if bullet.d == 1:
                    bullet.y -= bullet.speed
                elif bullet.d == 2:
                    bullet.x += bullet.speed
                elif bullet.d == 3:
                    bullet.y += bullet.speed
                else:
                    bullet.x -= bullet.speed
            else:
                bullets.pop(bullets.index(bullet))
        else:
            if bullet.x > enemy.x:
                bullet.x -= bullet.speed
            else:
                bullet.x += bullet.speed
            if bullet.y > enemy.y:
                bullet.y -= bullet.speed
            else:
                bullet.y += bullet.speed
    for enemy in enemies:
        if rp.rect.colliderect(enemy.rect):
            run = False
        for bullet in bullets:
            if bullet.rect.colliderect(enemy.rect):
                enemies.pop(enemies.index(enemy))
                dif*=1.2
                EK+=1
                if bullet.speed == 5:
                    bullets.pop(bullets.index(bullet))

    for enemy in enemies:
        enemy.draw(win)
        r = randint(0,2)
        if r == 1:
            if enemy.x > rp.x:
                enemy.x -= enemy.speed
            else:
                enemy.x += enemy.speed
        elif r == 2:
            if enemy.y > rp.y:
                enemy.y -= enemy.speed
            else:
                enemy.y += enemy.speed
        else:
            if randint(0,1) == 1:
                enemy.y -= randint(-1,1)
            else:
                enemy.x -= randint(-1,1)
    dif2=round(dif)
    rene = randint(1, 5000-dif2)
    if rene == 1:
        enemies.append(Enemy(0,0,10,10,1.5))
    elif rene == 2:
        enemies.append(Enemy(600,0,10,10,1.5))
    elif rene == 3:
        enemies.append(Enemy(0,600,10,10,1.5))
    elif rene == 4:
        enemies.append(Enemy(600,600,10,10,1.5))
    rene = randint(1, 2000-dif2)
    if rene == 1:
        enemies.append(Enemy(0,0,30,30,1))
    elif rene == 2:
        enemies.append(Enemy(600,0,30,30,1))
    elif rene == 3:
        enemies.append(Enemy(0,600,30,30,1))
    elif rene == 4:
        enemies.append(Enemy(600,600,30,30,1))
    rene = randint(1, 4000-dif2)
    if rene == 1:
        enemies.append(Enemy(0,0,50,50,0.7))
    elif rene == 2:
        enemies.append(Enemy(600,0,50,50,0.7))
    elif rene == 3:
        enemies.append(Enemy(0,600,50,50,0.7))
    elif rene == 4:
        enemies.append(Enemy(600,600,50,50,0.7))
    khold = pygame.key.get_pressed()
    if khold[pygame.K_UP] and rp.y - rp.speed > 5:
        rp.y -= rp.speed
        rp.facing = 1
    if khold[pygame.K_DOWN] and rp.y + rp.speed < 555:
        rp.y += rp.speed
        rp.facing = 3
    if khold[pygame.K_LEFT] and rp.x - rp.speed > 5:
        rp.x -= rp.speed
        rp.facing = 4
    if khold[pygame.K_RIGHT] and rp.x + rp.speed < 555:
        rp.x += rp.speed
        rp.facing = 2
    pygame.display.update()
    pygame.time.delay(10)
    win.fill((20,20,20))
    rp.draw(win)
pygame.quit()
