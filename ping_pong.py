from pygame import *  
window = display.set_mode((700, 500))  
display.set_caption("Ping Pong")  
background = transform.scale(image.load('table.jpg'), (700, 500))  
app = True
finish = False  
clock = time.Clock()  
FPS = 60  
  
class GameSprite(sprite.Sprite):  
#конструктор класса  
  def  __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):  
      #вызываем конструктор класса (Sprite):  
      sprite.Sprite.__init__(self)  
      #каждый спрайт должен хранить свойство image - изображение  
      self.image = transform.scale(image.load(player_image), (size_x, size_y))  
      self.speed = player_speed  
      #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан  
      self.rect = self.image.get_rect()  
      self.rect.x = player_x  
      self.rect.y = player_y  
#метод, отрисовывающий героя на окне  
  def reset(self):  
      window.blit(self.image, (self.rect.x, self.rect.y))  
#класс главного игрока  
  
class Player(GameSprite):  
  #метод для управления спрайтом стрелками клавиатуры  
   def update_L(self):  
       keys = key.get_pressed()  
       if keys[K_w] and self.rect.y > 5:  
           self.rect.y -= self.speed  
       if keys[K_s] and self.rect.y < 400:  
           self.rect.y += self.speed  
   def update_R(self):  
       keys = key.get_pressed()  
       if keys[K_UP] and self.rect.y > 5:  
           self.rect.y -= self.speed  
       if keys[K_DOWN] and self.rect.y < 400:  
           self.rect.y += self.speed  
ball = GameSprite('tenis_ball.png', 200, 300, 50, 50, 5)  
racket = Player('racket.png', 20, 40, 40, 80, 5)  
racket1 = Player('racket.png', 630, 80, 40, 80, 5)  
font.init()
font1 = font.SysFont('Calibri', 35)
font2 = font.SysFont('Calibri', 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font2.render('PLAYER 2 LOSE', True, (180, 0, 0))

speed_x = 3
speed_y = 3
while app:  
#событие нажатия на кнопку “Закрыть”  
    for e in event.get():  
        if e.type == QUIT:  
            app = False  
    window.blit(background, (0, 0))  
    ball.reset()  
    racket.reset()  
    racket1.reset()  
    
    
    if finish != True:
        racket.update_L()  
        racket1.update_R()  
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(racket, ball) or sprite.collide_rect(racket1, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        window.blit(lose1, (200, 200))
        finish = True
    if ball.rect.x > 650:
        window.blit(lose2, (200, 200))
        finish = True
            
        
    clock.tick(FPS)  
    display.update()
    
display.update()
