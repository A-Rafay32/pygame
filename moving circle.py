import pygame 
pygame.init()

screen = pygame.display.set_mode((500,500))
title = pygame.display.set_caption('Self-moving circle')

#positional co-ordinates and radius of circle
x = 100 ; y = 100 
radius = 5

#main game loop 
running = True
direction = 'right'
vel = 10
while running is True :
    
  pygame.time.delay(20)
  for event in pygame.event.get():
     if event.type == pygame.QUIT:  
        running = False
  
  #if direction == 'right':
     #increment in x 
  while x < 500-radius:  
       x += vel   
  direction = 'down'
  if direction == 'down': 
    #increment in y
    while y < 500-radius:  
      y += vel 
    direction = 'left'
  if direction == 'left':
    #decrement in x
    while x > 0: 
      x -= vel
    direction = "up" 
  if direction == "up":
    #decrement in y
    while y > 0:
      y -= vel
   
  #background color
  screen.fill(( 0, 0, 0 ))
  
  #circle
  pygame.draw.circle(screen, (255, 255, 255), (x , y), radius)    
  
  #refresh screen
  pygame.display.update()
    
pygame.quit()
 
