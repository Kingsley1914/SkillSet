import pygame
import random

pygame.init()

window = [700, 700]
screen = pygame.display.set_mode(window)
screen.fill(('#f7efe9'))

def scroll():
    if pl.rect.top < 200 and pl.vely < 0 :
        for pla in platforms:
            pla.rect.y -= pl.vely
    if pl.vely > 0 and pl.rect.y <= 200:
        pl.rect.y = 202
            
def refresh(start):
    h = 0
    x,y = 0,-300
    for i in  platforms:
        if i.rect.y < h:
            h = i.rect.y
    #print(h)
    if h == 0 and start == None:
        print('xxxx')
        for i in range(10):
            x = 0
            r = random.randint(0,4)
            if r != 1:
                for i in range(7):
                    c = random.randint(0,9)
                    if c not in [1,2,3,4,5,6,7,8,9]:
                        plat = Platform(x,y, 'n')
                        platforms.add(plat)
                    if c == 1:
                        plat = Platform(x,y, 't')
                        platforms.add(plat)
                        
                    x += 100
            y += 30        

    elif start == True:
        print('rar')
        for i in range(25):
            x = 0
            r = random.randint(0,3)
            if r != 2:
                for i in range(7):
                    c = random.randint(0,4)
                    if c == 1:
                        plat = Platform(x,y, 'n')
                        platforms.add(plat)
                    x += 100
            y += 30        
            print(y)       
                
        
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, ty):
        super(). __init__()
        self.image = pygame.surface.Surface((90, 20))
        self.ty = ty
        self.st = 'h'
        self.vely = 0
        self.acc = 0.9
        if self.ty == 'n':
            self.image.fill(('#66bb11'))
        elif self.ty == 't':
            self.image.fill(('#a98e69'))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def chk(self):
        pl_hit = pygame.sprite.spritecollide(self, players, False)
        for pl in pl_hit:
            if self.rect.bottom - pl.rect.top < 19:
                self.st = 'fall'
                
        
    def update(self):
        
        if self.st == 'fall' and self.ty == 't':
            self.vely += self.acc
            self.rect.y += self.vely
        if self.rect.y > 750:
            self.kill()
        #self.chk()
class Doodler(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(). __init__()
        self.image = pygame.surface.Surface((20, 20))
        self.image.fill(('#cac816'))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.jump = False
        self.vely = 0
        self.acc = 0.9
    def check_h(self):
        pl_hit = pygame.sprite.spritecollide(self, platforms, False)
        for pl in pl_hit:
            if self.rect.bottom - pl.rect.top < 19:
                self.rect.bottom = pl.rect.top
                if pl.ty == 't':
                    pl.st = 'fall'
                else:
                    self.jump = False
                    self.vely = 0
    def update(self):
        button = pygame.key.get_pressed()
        if self.rect.y > 600:
            self.jump = False
            self.vely = 0
        self.check_h()
        if self.jump == False:
          self.vely -= 1
          self.vely -=  20
          self.jump = True
        if button[pygame.K_RIGHT]:
            self.rect.x += 5
        if button[pygame.K_LEFT]:
            self.rect.x -= 5
        if self.rect.x > 700:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = 680
        if self.rect.y >= 200:
            self.rect.y += self.vely
        self.vely += self.acc



players = pygame.sprite.Group()
platforms = pygame.sprite.Group()


pl = Doodler(100, 200)
players.add(pl)

clock = pygame.time.Clock()
done = False
refresh(True)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(('#f7efe9'))        
    players.update()
    players.draw(screen)
    platforms.draw(screen)
    platforms.update()
    refresh(None)
    scroll()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()    
