import pygame
import sleep
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Лабіринт')

background = pygame.transform.scale(pygame.image.load('background.jpg'), (800,600))

running = True
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.play()

kick = pygame.mixer.Sound('kick.ogg')
money = pygame.mixer.Sound('money.ogg')

pygame.font.init()
font = pygame.font.SysFont("Arial", 64)

win = font.render('You win', True, 'white')
lose = font.render('You lose', True, 'white')


class GameStrite(pygame.sprite.Sprite):
    def __init__(self, image, x ,y , speed):
        self.image = pygame.transform.scale(pygame.image.load(image), (64,64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.x = x
        self.speed = speed

    def render(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameStrite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 550:
            self.rect.y += self.speed
        if keys[pygame.K_d] and self.rect.x < 750:
            self.rect.x += self.speed
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameStrite):
    diraction = 'right'
    def update(self):

        if self.rect.x >= 600:
            self.diraction = 'left'
        if self.rect.x <= 100:
            self.diraction = 'right'
        

        if self.diraction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

class Wall(pygame.sprite.Sprite):
    def __init__(self, r,g,b,x,y,widht,height):
        super().__init__()
        self.red = r
        self.g = g
        self.b = b
        self.width = widht
        self.height = height  
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((self.red, self.green, self.blue))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
w1 = Wall(255,255,255,150,150,250,50)
w2 = Wall(255,255,255,150,150,)

hero = Player('hero.png', 100,100,5)
enemy = Enemy('cyborg.png',200,200,10)
treasure = GameStrite('treasure.png',500,500,0)

while running:
    window.blit(background, (0,0))

    hero.render()
    hero.update()
    enemy.render()
    enemy.update()
    treasure.render()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        w1.draw_wall()

    player.draw()
    player.update()

    enemy.darw()
    enemy.update()

    treasure.darw()

    if pygame.sprite.collide_rect(player, enemy):
        window.blit(lose, (400, 300))
        kick.play()
        sleep(3)
        running = False

    if pygame.sprite.collide_rect(player, treasure):
        window.blit(win, (400, 300))
        money.play()
        sleep(3)
        running = False

    if pygame.sprite.collide_rect(player1, w1):
        player.rect.x = 50
        player.rect.y = 100

    pygame.display.update()
    clock.tick(60)

pygame.quit()
