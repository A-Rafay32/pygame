import pygame
pygame.init()
screen=pygame.display.set_mode((640,320))
BLACK=(0,0,0,0)
CYAN=(0,255,255,0)
RED=(255,0,0)
COLOR=(123,200,150)
WHITE=(255,255,255)
screen.fill(BLACK)
pygame.draw.rect(screen,CYAN,(60,60,120,100))
pygame.draw.circle(screen,RED,(150,300),40)
Rect = pygame.Rect(320,150,50,30)
pygame.draw.rect(screen,COLOR,Rect,30)
pygame.draw.line(screen,WHITE,(10,10),(10,10),2)
pygame.draw.circle(screen,WHITE,(200,200),5)
pixObj = pygame.PixelArray(screen)
pixObj[480][280] = WHITE
pygame.display.update()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
if running is False:      
  pygame.quit()


