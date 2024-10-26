import pygame
import sys
color = [243,234,255]
need = [0,0,0]
WINDOW_SIZE = [700, 500]
score = [0,0]
time = [0,0]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.init()
text = pygame.font.Font('freesansbold.ttf', 30)

text2 = pygame.font.Font('freesansbold.ttf', 20)
info2 = text.render(f'{time[0]}:{time[1]}', True, [0,0,0])



class Bat(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        super().__init__()
        self.image = pygame.surface.Surface((10, 50))
        #self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y



    def update (self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.rect.y -= 15
        
        if keys[pygame.K_s]:
            self.rect.y += 15
        if self.rect.y > 450:
            self.rect.y = 450
        if self.rect.y < 0:
            self.rect.y = 0


class Ball(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        super().__init__()
        self.image = pygame.surface.Surface((8, 8))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.xspeed, self.yspeed = -6,-6
        self.angle = 0
    def check_hit(self):
        hits = pygame.sprite.spritecollide(self,bat_list,False)
        for bat in hits:
            if self.rect.right > bat.rect.left:
                self.xspeed *= -1
            elif self.rect.left < bat.rect.right:
                self.xspeed *= -1
        wall_hits = pygame.sprite.spritecollide(self,bound_list,False)
        for bat in wall_hits:
            self.xspeed *= bat.x_change
            self.yspeed *= bat.y_change
          
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.y < 0:
            self.rect.y = 0

        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 495:
            self.rect.y = 495
        self.check_hit()    



class Bat2(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        super().__init__()
        self.image = pygame.surface.Surface((10, 50))
        #self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y

    
    def update (self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.rect.y -= 15
        
        if keys[pygame.K_DOWN]:
            self.rect.y += 15
        if self.rect.y > 450:
            self.rect.y = 450
        if self.rect.y < 0:
            self.rect.y = 0
            
class Boundary(pygame.sprite.Sprite):
    def __init__ (self, x, y, w, h, xc, yc):
        super().__init__()
        self.image =pygame.surface.Surface((w*2, h))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.x_change = xc
        self.y_change = yc
        
class Controller():
    def __init__ (self):
        self.function = 'control'
    def check_hit(self):
        for Ball in ball_list:
            hits = pygame.sprite.spritecollide(Ball, bound_list, False)
            for bound in hits:
               if bound.rect.x == 0:
                  score[0] += 1
               if bound.rect.x == 680:
                   score[1] += 1
                   
    def update(self):
        self.check_hit()
bat_list = pygame.sprite.Group()
strike = Bat(50, 300)
strike2 = Bat2(600, 300)
bat_list.add(strike, strike2)

ball_list = pygame.sprite.Group()
roll = Ball(250, 250)
ball_list.add(roll)

bound_list = pygame.sprite.Group()
bound1 = Boundary(0, 0, 10, 500, -1, 1)

bound2 = Boundary(10, 490, 700, 10, 1, -1)

bound3 = Boundary(680, 0, 10, 500, -1, 1)

bound4 = Boundary(10, 0, 680, 10, 1, -1)

bound_list.add(bound1,bound2,bound3,bound4)


clock = pygame.time.Clock()
control = Controller()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(color)
    bat_list.draw(screen)
    bat_list.update()
    info = text.render(f'{score[0]}:{score[1]}', True, [0,0,0])
    screen.blit(info, (325, 10))

    screen.blit(info2, (20, 10)) 
    bound_list.draw(screen)
    bound_list.update()
    control.update()
    
    ball_list.draw(screen)
    ball_list.update()

    pygame.display.flip()
    clock.tick(50)    
 
