from pygame import *
 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
  
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 700
win_height = 500
display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("Background.jpg"), (700, 500))

mixer.init()
mixer.music.load("Rain On Me.mp3")
mixer.music.play()
 
game = True
finish = False
clock = time.Clock()
FPS = 60
 
racket1 = Player('Racket1.jpg', 30, 200, 4, 50, 150) 
racket2 = Player('Racket2.jpg', 600, 200, 4, 50, 150)
ball = GameSprite('Ball.png', 200, 200, 4, 50, 50)
 
font.init()
font = font.Font(None, 35)
lose1 = font.render('CHROMATICA LOSE!', True, (255, 255, 255))
lose2 = font.render('ARTPOP BALL LOSE!', True, (255, 255, 255))
 
speed_x = 3
speed_y = 3

reset_button_rect = Rect(300, 450, 100, 50)
reset_button_image = transform.scale(image.load("Reset.png"), (100, 50))
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                if reset_button_rect.collidepoint(e.pos):
                    finish = False
                    ball.rect.x = 200
                    ball.rect.y = 200
                    speed_x = 3
                    speed_y = 3
  
    if finish != True:
        window.blit(background, (0, 0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
    
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
    
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
    
        racket1.reset()
        racket2.reset()
        ball.reset()
    
    window.blit(reset_button_image, reset_button_rect)
    display.update()
    clock.tick(FPS)