#print('Hello, World!')
import pygame as pg 
from random import randint
starter = False
pg.init() 

def get_events():
    global run
    global starter
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_w:
                player_1.speed = -5
            if e.key == pg.K_s:
                player_1.speed = 5
            if e.key == pg.K_UP:
                player_2.speed = -5
            if e.key == pg.K_DOWN:
                player_2.speed = 5
            if e.key == pg.K_SPACE:
                starter = True
        if e.type == pg.KEYUP:
            if e.key == pg.K_w:
                player_1.speed = 0
            if e.key == pg.K_s:
                player_1.speed = 0
            if e.key == pg.K_UP:
                player_2.speed = 0
            if e.key == pg.K_DOWN:
                player_2.speed = 0
            if e.key == pg.K_SPACE:
                starter = True
            

class GameSprite(pg.sprite.Sprite):
    def __init__(self, image, x, y, w, h, speed):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def update(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        self.rect.y += self.speed

class Ball(GameSprite):
    def init(self):
        self.speed_x = self.speed
        self.speed_y = self.speed
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= 600:
            self.speed_y *= -1
        if self.rect.colliderect(player_1.rect) or self.rect.colliderect(player_2.rect):
            self.speed_x *= -1.1


lable2 = pg.font.SysFont('verdana', 45).render('Нажмите на Пробел что бы начать', True, (255,255,255))
win = pg.display.set_mode((1200,600))
pg.display.set_caption('PingPong')
lable = pg.font.SysFont('verdana', 65)
a = randint(0,255)
b = randint(0,255)
c = randint(0,255)
count = 0
f = randint(0,1)

if f == 0:
    f = 5
else:
    f = -5
win.fill((0,0,0))

run = True
Fin = False
clock = pg.time.Clock()

player_1 = Player('player_1.png', 20, 200, 75, 75, 0)
player_2 = Player('player_2.png', 1100, 200, 75, 75, 0)
ball = Ball('ball.png', 600, 250 , 25, 25, f)
ball.init()

while run:
    get_events()
    if not Fin:
        if count == 30:
            a = randint(0,255)
            b = randint(0,255)
            c = randint(0,255)
            count = 0
        else:
            count += 1
        win.fill((a,b,c))
        player_1.move()
        player_1.update()
        player_2.move()
        player_2.update()
        if starter:
            ball.move()
            ball.update()
        else:
            win.blit(lable2, (250,250))
        

        if ball.rect.x <= -25:
            res = ('Плауер 1 проиграл')
            Fin = True
        elif ball.rect.x >= 1215:
            res = ('Плауер 2 проиграл')
            Fin = True
    else:
        lable = pg.font.SysFont('verdana', 65).render(res, True, (255,255,255))
        win.blit(lable, (300,250))
    pg.display.update()
    clock.tick(60)