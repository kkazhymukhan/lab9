import pygame, sys, os
from pygame.locals import *
import random, time
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load(os.path.join("C:/Users/kazhon/OneDrive/Рабочий стол/ff/race_game/resoursec/AnimatedStreet.png"))
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(os.path.join("C:/Users/kazhon/OneDrive/Рабочий стол/ff/race_game/resoursec/Enemy.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Coin(pygame.sprite.Sprite):
      def _init_(self):
        super()._init_() 
        self.image = pygame.image.load(os.path.join("C:/Users/kazhon/OneDrive/Рабочий стол/ff/race_game/resoursec/download.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        
        def move(self):
            global SCORE
            self.rect.move_ip(0,SPEED)
            if (self.rect.top > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 

 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(os.path.join("C:/Users/kazhon/OneDrive/Рабочий стол/ff/race_game/resoursec/Player.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
                           
P1 = Player()
E1 = Enemy()
C1 = Coin()
 

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
coins = pygame.sprite.Group()

 

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 

while True:
        
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
 
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect) 
        entity.move()

    for entity in coins:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(os.path.join("C:/Users/kazhon/OneDrive/Рабочий стол/ff/race_game/resoursec/crash.wav")).play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    coins.add(C1)

    if pygame.sprite.spritecollideany(P1, coins):
          pygame.mixer.Sound("C:/Users/kazhon/OneDrive/Рабочий стол/ff/race_game/resoursec/coins-to-table-1.wav").play()
          for entity in coins:
                entity.kill() 
                SCORE += 2
                C1 = Coin()
         
    pygame.display.update()
    FramePerSec.tick(FPS)