import pygame
pygame.init()
screen = pygame.display.set_mode((640,320))
caption = pygame.display.set_caption('Text Practice')
 
#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#set font type and size (return type font object)
fonttype = pygame.font.Font('FreeSans.ttf',32)

#create text and display it on your window (pass your font to surface object)
#(return type surface object)
#1.string 2.for anti aliasing 3.text color 4.background color(invisible here)      
font_surf = fonttype.render('Hello World',True,WHITE)

#change surface object to rect object by get_rect() method
font_rect =  font_surf.get_rect()

#set position of your rect object by using one of its attributes
font_rect.center = (320,150)

#start main game loop 
while True:
   screen.fill(BLACK)
   screen.blit(font_surf,font_rect)
   for event in pygame.event.get():    
      if event.type == pygame.QUIT:
         pygame.quit()
   pygame.display.update()
