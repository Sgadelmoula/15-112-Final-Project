import lists_model as main
import trafficLights as tf
import roadNetwork as sub
import pygame

######################Code from the model##########################
#Defining colors for later use
grey = (100,100,100)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
lights = [green, yellow, red]


env = sub.roadNetwork([25,30], [10,4, 20], [5, 9, 15])
env.makeMap()
result = env.updateMap()
tlights = tf.trafficLights(delay = 200)
for i in range(len(result)):
    for j in range(2):
        print result[i][j]

#####################The game interface############################
pygame.init()
pygame.display.set_caption("first intersection")
screen = pygame.display.set_mode((600,500))
done = False

tileWidth = 10
def drawMap():
    for i in range(25):
            for k in range(2):
                for j in range(30):
                    if result[i][k][j] == 1 or result[i][1][j] == 2:
                        pygame.draw.rect(screen,white,pygame.Rect(20*j,20*i,20,15))
                        pygame.display.flip()
                    if result[i][k][j] == 5 and result[i][k][j+1] == 5:
                        pygame.draw.circle(screen, red, [20*j,20*i+10], 3)
                        if tlights.current == 3:
                            color = red
                        elif tlights.current == 1:
                            color = green
                        elif tlights.current == 2:
                            color = yellow
                        pygame.draw.circle(screen, color , [20*j,20*i+10], 3)
                        tlights.updateTimer()
                        pygame.display.flip()
while not done:
    drawMap()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()














