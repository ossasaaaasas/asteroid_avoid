import pygame
from pygame.locals import *
import random

pygame.init()

FPS = 30
framesPerSec = pygame.time.Clock()

black = (0,0,0)

window = pygame.display.set_mode((500,600))
window.fill(black)
pygame.display.set_caption("Asteroid Avoid")

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Asteroid.png")
        self.surf = pygame.Surface((40,40))
        self.rect = self.surf.get_rect(center = (random.randint(40,460), 0))

    def move(self):
        self.rect.move_ip(0,10)
        if(self.rect.bottom > 600):
            self.rect.center = (random.randint(30,460), 0)
               
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceShip.png")
        self.surf = pygame.Surface((100,150))
        self.rect = self.surf.get_rect(center = (250, 525))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressedKeys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressedKeys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressedKeys[K_RIGHT]:
                self.rect.move_ip(5, 0)

P1 = Player()
E1 = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    P1.update()
    E1.move()

    window.fill(black)

    P1.draw(window)
    E1.draw(window)

    pygame.display.update()
    framesPerSec.tick(FPS)














    
            
            

    














    
        
    
