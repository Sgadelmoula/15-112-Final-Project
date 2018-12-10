import lists_model_c as main
import trafficLights_c as tf
import roadNetwork_c as sub
import pygame
import random

######################Code from the model##########################
#Defining colors and lights for later use
grey = (100,100,100)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
lights = [green, yellow, red]

#Adding traffic lights to the map, e = east, w = west... 
allTrafficLights = []
allTrafficLights.append(tf.trafficLights(delay=200,x=10,y=6))##e
allTrafficLights.append(tf.trafficLights(delay=200,x=12,y=4))##s
allTrafficLights.append(tf.trafficLights(delay=200,x=11,y=7))##n
allTrafficLights.append(tf.trafficLights(delay=200,x=13,y=5))##w

#Initializing AllCars for availability detection
allCars = []
ctrl = main.world(allCars, allTrafficLights)
#making the map and updating the result
env = sub.roadNetwork([25,30], [10], [5])
env.makeMap()
result = env.updateMap()

#####################The interface################################
#Initializing the game and setting up a timer
pygame.init()
pygame.display.set_caption("first intersection")
screen = pygame.display.set_mode((600,500))
done = False
pygame.time.set_timer(pygame.USEREVENT+1, 3000)
#Draws a map using the result of th grid in the network file
def drawMap():
    for i in range(25):
            for j in range(30):
                if result[i][j] == 1:
                    pygame.draw.rect(screen,white,pygame.Rect(20*j,20*i,20,20))
                else:
                    pygame.draw.rect(screen,black,pygame.Rect(30*j,20*i,20,20))
    
clock = pygame.time.Clock()
while not done:
    screen.fill(black)
    drawMap()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        #Adding a random number of cars at every starting point.
        if event.type == pygame.USEREVENT+1:
            for i in range(random.randint(3,9)):
                allCars.append(main.car(ctrl,x=1,y=6.5,d="e"))
            for i in range(random.randint(3,9)):
                allCars.append(main.car(ctrl,x=29,y=5.5,d="w"))
            for i in range(random.randint(3,9)):
                allCars.append(main.car(ctrl,x=10.5,y=24,d="n"))
            for i in range(random.randint(3,9)):
                allCars.append(main.car(ctrl,x=11.5,y=1,d="s"))
                
    for trlgt in allTrafficLights:
        trlgt.updateTimer()
        trlgt.draw(screen)
    for car in allCars:
        car.move()
        car.draw(screen)
        car.terminate(allCars)
    pygame.display.flip()    
    clock.tick(60)












