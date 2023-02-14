import pygame
from pygame.locals import *
# activate the pygame library , initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object of specific dimension..e(500, 500).
win = pygame.display.set_mode((500, 500))

# set the pygame window name
pygame.display.set_caption("Moving rectangle")

# object1 and object2 current co-ordinates
x1 = 0 ; y1 = 0
x2 = 500-10 ; y2 = 0


# dimensions of the object
width1 = 10 ; height1 = 50
width2 = 20 ; height2 = 50


# velocity / speed of movement
vel = 10

# Indicates pygame is running
run = True

# infinite loop
while run:
    # creates time delay of 10ms
    pygame.time.delay(10)	
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
       # if event object type is QIUT
       # then quitting the pygame and program both.
       if event.type == pygame.QUIT:
        # it will make exit the while loop
        run = False
    # stores keys pressed
    keys = pygame.key.get_pressed()

    # if up arrow key is pressed
    if keys[pygame.K_UP] and y1>0:
       # decrement in y co-ordinate
       y1 -= vel
    # if down arrow key is pressed
    if keys[pygame.K_DOWN] and y1<500-height1:
       # increment in y co-ordinate
       y1 += vel
    if keys[pygame.K_w] and y2>0:
       y2 -= vel
    if keys[pygame.K_s] and y2<500-height2:	
       y2 += vel
 	
    # completely fill the surface object
    win.fill((0, 0, 0))
    # drawing objects on screen which is rectangle here
    pygame.draw.rect(win, (255, 255, 255), (x1, y1, width1, height1))
    pygame.draw.rect(win, (255, 255, 255), (x2, y2, width2, height2))

    #division line
    x3 = 250 ; y3 = 0
    width3 = 5 ; height3 = 500 
    pygame.draw.rect(win, (0, 0, 255), (x3, y3, width3, height3)
                     )  
    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()
