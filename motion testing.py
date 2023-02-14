import pygame
pygame.init()
screen = pygame.display.set_mode((800,640))

#FPS = 30
#fpsClock = pygame.time.Clock()


#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#our moving object
intx = 10
inty = 10

#main game loop
running = True
while running:
    screen.fill(BLACK)
    direction='right'
    pygame.time.delay(10)
    for event in pygame.event.get():
      
       if dire ction == 'right':
          intx+=10
          if intx == 530:
            direction ='down'
       elif direction == 'down':
          inty-=10
          if inty == 300:
            direction = 'left'
       elif direction == 'left':
          intx-=10
          if intx == 100:
            direction = 'up'
       elif direction == 'up':
          inty+=10
       if event.type == pygame.QUIT:
          pygame.quit()
          running=False
      
    circle = pygame.draw.circle(screen,WHITE,(intx,inty),5)


  
    #screen.blit(circle,(intx,inty))         
    pygame.display.update()
    #fpsClock.tick(FPS)

               
