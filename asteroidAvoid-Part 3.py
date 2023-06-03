import pygame, time, sys
from pygame.locals import *
import random

pygame.init()

FPS = 30
framesPerSec = pygame.time.Clock()

black = (0,0,0)
red = (255, 0, 0)

window = pygame.display.set_mode((500,600))
window.fill(black)
pygame.display.set_caption("Asteroid Avoid")

speed = 10

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

from pygame import mixer
mixer.init()
mixer.music.load("space.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Asteroid.png")
        self.surf = pygame.Surface((30,30))
        self.rect = self.surf.get_rect(center = (random.randint(40,460), (random.randint(-100,0))))

    def move(self, score, destroyed):
        self.rect.move_ip(0,speed)
        if(self.rect.bottom > 600) or destroyed == True:
            self.rect.center = (random.randint(30,460), (random.randint(-100,0)))
            score += 1

        return score
               
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceShip.png")
        self.surf = pygame.Surface((54,118))
        self.rect = self.surf.get_rect(midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

    def draw(self, surface):
        surface.blit(self.image, (self.rect.centerx-45, self.rect.centery - 90))

    def update(self):
        pressedKeys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressedKeys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressedKeys[K_RIGHT]:
                self.rect.move_ip(5, 0)



class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load("bullet.png")
        self.surf = pygame.Surface((10,10))
        self.rect = self.surf.get_rect(center = (player.rect.midtop))
        self.fired = False

    def fire(self, player):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys [K_SPACE] and self.fired == False:
            self.rect = self.surf.get_rect(center = (player.rect.midtop))
            self.fired = True

        if self.fired == True:
            window.blit(self.image, self.rect)
            self.rect.move_ip(0,-5)

            if (self.rect.top < 1):
                self.rect.top = 600
                self.fired = False

    def resetPos(self):
        self.rect.top = 600
        self.fired = False


class Background():
    def __init__(self):
        self.backgroundImage = pygame.image.load("backgroundImage3.png")
        self.rectBGimage = self.backgroundImage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = -self.rectBGimage.height
        self.bgX2 = 0

        self.moveSpeed = 5


    def update(self):
        self.bgY1 += self.moveSpeed
        self.bgY2 += self.moveSpeed

        if self.bgY1>self.rectBGimage.height:
            self.bgY1 = -self.rectBGimage.height

        if self.bgY2>self.rectBGimage.height:
            self.bgY2 = -self.rectBGimage.height
    

    def render(self):
        window.blit(self.backgroundImage,(self.bgX1, self.bgY1))
        window.blit(self.backgroundImage,(self.bgX2, self.bgY2))



background = Background()


INCREASE_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_SPEED, 3000)

        

P1 = Player()
E1 = Enemy()
E2 = Enemy()
E3 = Enemy()
B1 = Bullet(P1)

enemyGroup = pygame.sprite.Group()
enemyGroup.add(E1)
enemyGroup.add(E2)
enemyGroup.add(E3)

bullets = pygame.sprite.Group()
bullets.add(B1)



font = pygame.font.SysFont("Verdana", 40)
gameOver = font.render("Game Over", True, black)

score = 0
destroyed = False

while True:
    scoreRender = font.render("Score: " +str(score), True, red)
    background.update()
    background.render()
    window.blit(scoreRender, (0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == INCREASE_SPEED:
            speed+= 0.5

    if pygame.sprite.spritecollideany(P1, enemyGroup):
        window.fill(red)
        window.blit(gameOver, (100,300))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()

    for entity in bullets:
        entity.fire(P1)
    

    for enemy in enemyGroup:
        if pygame.sprite.spritecollideany(enemy, bullets, False):
            destroyed = True
            score = score + 5
            enemy.move(score, destroyed)
            window.blit(enemy.image, enemy.rect)
            B1.resetPos()
            destroyed = False

    for enemy in enemyGroup:
        score = enemy.move(score, destroyed)
        enemy.draw(window)

    P1.update()
    P1.draw(window)

    pygame.display.update()
    framesPerSec.tick(FPS)














    
            
            

    














    
        
    
