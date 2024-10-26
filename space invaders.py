import pygame
import sys
import random 
color = [0, 0, 0]

WINDOW_SIZE = [640, 700]
screen = pygame.display.set_mode(WINDOW_SIZE)


pygame.init()
class Player(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        super().__init__()
        self.image = pygame.surface.Surface((16, 16))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.fire_rate = 0
        self.life = 5
        self.side = 'player'
    def check_hit(self):
        hits = pygame.sprite.spritecollide(self,bullet_list,False)
        for col in hits:
            if col.side != self.side:
                self.life -= 1
                col.kill()
    def update (self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.rect.x += 8

        if keys[pygame.K_LEFT]:
            self.rect.x -= 8
        
        if self.rect.x > 624:
            self.rect.x = 624
        if self.rect.x < 0:
            self.rect.x = 0
    
        if keys[pygame.K_UP]:
            self.rect.y -= 15

        if keys[pygame.K_DOWN]:
            self.rect.y += 15

        if keys[pygame.K_SPACE]:
            if self.fire_rate == 0:
               bullet = Bullet(self.rect.x, self.rect.y - 10, 10, 'player')
               bullet_list.add(bullet)
               self.fire_rate = 10
        if self.fire_rate > 0:
            self.fire_rate -= 1
        self.check_hit()
        if self.life <= 0 :
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__ (self, x, y, spd, sid):
        super().__init__()
        self.image = pygame.surface.Surface((3, 9))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.speed = spd
        self.side = sid
    def update (self):
        self.rect.y -= self.speed
        if self.rect.y < 0 or self.rect.y > 700:
            self.kill()
        
class Enemy(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        super().__init__()
        self.image = pygame.surface.Surface((16, 16))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.fire_rate = 0
        self.enemylife = 2
        self.side = 'enemy'
        self.id = 0
    def check_ehit(self):
        hits = pygame.sprite.spritecollide(self,bullet_list,False)
        for coll in hits:
            if coll.side != self.side:
                self.enemylife -= 1
                coll.kill()
    def shoot(self):
                  
        bullet = Bullet(self.rect.x + 8, self.rect.y + 23, -10, 'enemy')
        bullet_list.add(bullet)
                    
        
    def update(self):
        if self.fire_rate > 0:
            self.fire_rate -= 1
        
        
        self.check_ehit()
        #print(self.enemylife)
        if self.enemylife <= 0 :
            self.kill()

enemy_list = pygame.sprite.Group()

scale = (96, 64)
x = 0
y = 0
map1 = [[ ],
        [ ],
        [ ],
        [ ],
        [ ],]
'''        [ ],
        [ ],
        [ ]]'''

for row in map1:
    for tile in range(8):
        x = 1#random.randint(0, 1)
        row.append(x)

for row in map1:
    x = 0
    for tile in row:
        if tile == 1:
            enemy = Enemy(x, y)
            enemy_list.add(enemy)
        x += scale [0]
    y += scale[1]


player_list = pygame.sprite.Group()
square = Player(100, 600)
player_list.add(square)

bullet_list = pygame.sprite.Group()

clock = pygame.time.Clock()
#print(enemy_list[0])
id1 =0
for enemy in enemy_list:
    enemy.id = id1
    id1 += 1


def shoot():
    shot = random.randint(0,len(enemy_list))
    for i in enemy_list:
        if i.id == shot:
            i.shoot()
t = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(color)
    player_list.draw(screen)
    player_list.update()

    bullet_list.draw(screen)
    bullet_list.update()
    
    enemy_list.draw(screen)
    enemy_list.update()
    
    pygame.display.flip()
    clock.tick(50)
    if t > 20:
        shoot()
        t = 0
    t += 1
