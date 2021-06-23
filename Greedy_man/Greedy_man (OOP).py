import pygame, sys, os
import random
import math
pygame.init()

WHITE = (240, 240, 240)
RED = (240, 0, 0)
BLUE = (122, 0, 0)
GREEN = (0, 240, 0)
BOT_SPEED = 0.040
PLAYER_SPEED = 0.080
WIDTH, HIGHT = 600, 400
# TIME = pygame.clock


man = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "theman.png")),(32,32))
man2 = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "man2.png")),(32,32))
coin = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "thecoin.png")),(16,16))
weapon1 = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "knive.png")),(32,32))
background = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "grass.png")),(600,400))



#Screen set
pygame.display.set_caption("Greedy man By Basheer")
pygame.display.set_icon(man)
screen = pygame.display.set_mode((WIDTH, HIGHT))
font1 = pygame.font.Font(os.path.join("imgs", "FreeSansBold.ttf"), 20)
pygame.mouse.set_cursor(pygame.cursors.arrow)

class Main:
    #Man1 (player)
    
    def __init__(self, x, y, speed, bot_speed, weapon_img):
        self.x = x
        self.y = y
        self.x2 = random.randint(0, WIDTH-30)
        self.y2 = random.randint(0, HIGHT-30)
        self.x3 = random.randint(0, WIDTH-30)
        self.y3 = random.randint(0, HIGHT-30)
        self.speed = speed
        self.bot_speed = bot_speed
        self.coinx = random.randint(0, WIDTH-30)
        self.coiny = random.randint(0, HIGHT-30)
        self.score = 0
        self.weapon = weapon_img
        self.weapon_x = random.randint(0, WIDTH-30)
        self.weapon_y = random.randint(0, HIGHT-30)
        self.has_weapon = False
        self.scores = [0]
   
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if self.x + self.speed <= 580:
                self.x += self.speed
        if keys[pygame.K_LEFT]:
            if self.x - self.speed >= 20:
                self.x -= self.speed
        if keys[pygame.K_UP]:
            if self.y - self.speed >= 20:
                self.y -= self.speed
        if keys[pygame.K_DOWN]:
            if self.y + self.speed <= 380:
                self.y += self.speed
        
        # mouse movement
        if pygame.mouse.get_pos()[0] < self.x:
            self.x -= PLAYER_SPEED
        elif pygame.mouse.get_pos()[0] > self.x:
            self.x += PLAYER_SPEED
        if pygame.mouse.get_pos()[1] < self.y:
            self.y -= PLAYER_SPEED
        elif pygame.mouse.get_pos()[1] > self.y:
            self.y += PLAYER_SPEED


    def look_load(self, image):
        self.image = image
        screen.blit(self.image, (self.x, self.y))

    #Man2(BOT)
    
    def move2(self):
        if self.x > self.x2:
            self.x2 += self.bot_speed
        if self.x < self.x2:
            self.x2 -= self.bot_speed
        if self.y < self.y2:
            self.y2 -= self.bot_speed
        if self.y > self.y2:
            self.y2 += self.bot_speed
   
    def look_load2(self, image2):
        self.image2 = image2
        screen.blit(self.image2, (self.x2, self.y2))
    
    #Man3(BOT)
   
    def move3(self):
        if math.sqrt((math.pow(self.x3-self.x2,2)) + (math.pow(self.y3-self.y2,2))) < 25:
            self.x3, self.y3 = random.randint(0, WIDTH-30), random.randint(0, HIGHT-30)
        if self.x > self.x3:
            self.x3 += self.bot_speed
        if self.x < self.x3:
            self.x3 -= self.bot_speed
        if self.y < self.y3:
            self.y3 -= self.bot_speed
        if self.y > self.y3:
            self.y3 += self.bot_speed
   
    def look_load3(self, image3):
        self.image3 = image3
        screen.blit(self.image3, (self.x3, self.y3))
    
    #Coins
  
    def font_render(self, font):
        self.font = font
        text = self.font.render(f'Score: {self.score}', True, RED, None)
        text2 = self.font.render(f"Max score: {max(self.scores)}", True, RED, None)
        textRect = text.get_rect()
        text2Rect = text.get_rect()
        textRect.center = (WIDTH // 12, HIGHT // 15)
        text2Rect.center = (WIDTH -100, HIGHT // 15)
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
   
    def coin_respwan(self, coin_img):
        self.coin = coin_img
        screen.blit(self.coin, (self.coinx, self.coiny))
   
    def the_score(self):
        if math.sqrt((math.pow(self.x-self.coinx,2)) + (math.pow(self.y-self.coiny,2))) < 25:
            self.score += 1
            self.coinx = random.randint(0, WIDTH-30)
            self.coiny = random.randint(0, HIGHT-30)
    
    def lost(self):
        self.d_x_x2 = math.sqrt((math.pow(self.x-self.x2,2)) + (math.pow(self.y-self.y2,2)))
        self.d_x_x3 = math.sqrt((math.pow(self.x-self.x3,2)) + (math.pow(self.y-self.y3,2)))
        if self.d_x_x2 < 25 or self.d_x_x3 < 25:
            if self.has_weapon:
                self.has_weapon = False
                self.weapon_x = random.randint(0, WIDTH-30)
                self.weapon_y = random.randint(0, HIGHT-30)
                if self.d_x_x2 < 25:
                    self.x2 = random.randint(0, WIDTH-30)
                    self.y2 = random.randint(0, HIGHT-30)
                elif self.d_x_x3 < 25:
                    self.x3 = random.randint(0, WIDTH-30)
                    self.y3 = random.randint(0, HIGHT-30)
                self.weapon = weapon1
                self.has_weapon = False
            else:
                self.x2 = random.randint(0, WIDTH-30)
                self.y2 = random.randint(0, HIGHT-30)
                self.x, self.y = (WIDTH/2)-20, (HIGHT/2)
                self.scores.append(self.score)
                self.score = 0

    def weapon_respwan(self):
        screen.blit(self.weapon, (self.weapon_x, self.weapon_y))
    
    def weapon_pickup(self):
        if math.sqrt((math.pow(self.x-self.weapon_x,2)) + (math.pow(self.y-self.weapon_y,2))) < 25:
            self.weapon_x, self.weapon_y = self.x+10, self.y+10
            self.weapon = pygame.transform.scale(self.weapon, (16,16))
            self.has_weapon = True

player = Main((WIDTH/2)-20, (HIGHT/2), PLAYER_SPEED, BOT_SPEED, weapon1)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(background, (0,0))
    player.weapon_pickup()
    player.move()
    player.move2()
    player.move3()
    player.the_score()
    player.font_render(font1)
    player.coin_respwan(coin)
    player.look_load(man)
    player.weapon_respwan()
    player.look_load2(man2)
    player.look_load3(man2)
    
    
    player.lost()

    pygame.display.flip()
