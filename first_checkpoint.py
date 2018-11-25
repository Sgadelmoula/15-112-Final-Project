import pygame
import random

pygame.init()
pygame.display.set_caption("first intersection")
screen = pygame.display.set_mode((500,500))
#Defining colors for later use
grey = (100,100,100)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)
lights = [green, yellow, red]
screen.fill(grey)
done = False
#choose = range(100,500,100)

#Drawing the intersection
#x = random.choice(choose)
#choose.remove(x)
x=200
pygame.draw.line(screen, black, [x,0], [x, 500], 50)
pygame.draw.line(screen, white, [x,0], [x, 500], 1)
pygame.draw.line(screen, black, [0,x+20], [500, x+20], 50)
pygame.draw.line(screen, white, [0,x+20], [500, x+20], 1)
pygame.draw.circle(screen, black, [x, x+20], 25)
#Starting up a timer
#clock = pygame.time.Clock()
    
#Making a border of "a road" around the later intersection
pygame.draw.line(screen, black, [0,0], [0, 500], 100)
pygame.draw.line(screen, black, [0,500], [500, 500], 100)
pygame.draw.line(screen, black, [0,0], [500, 0], 100)
pygame.draw.line(screen, black, [500,0], [500, 500], 100)
pygame.draw.line(screen, white, [475,0], [475, 500], 1)
pygame.draw.line(screen, white, [0,25], [500, 25], 1)
pygame.draw.line(screen, white, [25,0], [25, 500], 1)
pygame.draw.line(screen, white, [0,475], [500, 475], 1)
pygame.display.flip()

#Covering up
pygame.draw.rect(screen,black,pygame.Rect(0,0,50,50))
pygame.draw.rect(screen,black,pygame.Rect(175,0,50,50))
pygame.draw.rect(screen,black,pygame.Rect(450,0,50,50))
pygame.draw.rect(screen,black,pygame.Rect(0,200,50,50))
pygame.draw.rect(screen,black,pygame.Rect(0,450,50,50))
pygame.draw.rect(screen,black,pygame.Rect(175,450,50,50))
pygame.draw.rect(screen,black,pygame.Rect(450,450,50,50))
pygame.draw.rect(screen,black,pygame.Rect(450,200,50,50))
pygame.display.flip()

class trafficLights:
    def __init__(self, timer, x, y = 0):
        self.offSet = x
        self.add = y
        self.clock = timer
    def wholePack(self):
        #All traffic lights are red at the start
        pygame.draw.circle(screen, red, [self.offSet-30, self.offSet+30], 2)
        pygame.draw.circle(screen, red, [self.offSet-10, self.offSet-10], 2)
        pygame.draw.circle(screen, red, [self.offSet+30, self.offSet+10], 2)
        pygame.draw.circle(screen, red, [self.offSet+15, self.offSet+50], 2)
        pygame.display.flip()
        #The first one changes to green then yellow then red again
        pygame.draw.circle(screen, green, [self.offSet-30, self.offSet+30], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, yellow, [self.offSet-30, self.offSet+30], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, red, [self.offSet-30, self.offSet+30], 2)
        pygame.display.flip()
        self.clock.tick(3)
        #The second one changes to green then yellow then red again
        pygame.draw.circle(screen, green, [self.offSet-10, self.offSet-10], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, yellow, [self.offSet-10, self.offSet-10], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, red, [self.offSet-10, self.offSet-10], 2)
        pygame.display.flip()
        self.clock.tick(3)
        #The third one changes to green then yellow then red again
        pygame.draw.circle(screen, green, [self.offSet+30, self.offSet+10], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, yellow, [self.offSet+30, self.offSet+10], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, red, [self.offSet+30, self.offSet+10], 2)
        pygame.display.flip()
        self.clock.tick(3)
        #The fourth one changes to green then yellow then red again
        pygame.draw.circle(screen, green, [self.offSet+15, self.offSet+50], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, yellow, [self.offSet+15, self.offSet+50], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, red, [self.offSet+15, self.offSet+50], 2)
        pygame.display.flip()
        self.clock.tick(3)

    def leftLight(self):
        pygame.draw.circle(screen, red, [self.offSet-30, self.offSet+30+self.add], 2)
        #The first one changes to green then yellow then red again
        pygame.draw.circle(screen, green, [self.offSet-30, self.offSet+30+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, yellow, [self.offSet-30, self.offSet+30+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, red, [self.offSet-30, self.offSet+30+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
    def upperLight(self):
        pygame.draw.circle(screen, red, [self.offSet-10, self.offSet-10+self.add], 2)
        #The second one changes to green then yellow then red again
        pygame.draw.circle(screen, green, [self.offSet-10, self.offSet-10+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, yellow, [self.offSet-10, self.offSet-10+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, red, [self.offSet-10, self.offSet-10+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
    def rightLight(self):
        pygame.draw.circle(screen, red, [self.offSet+30, self.offSet+10+self.add], 2)
        #The third one changes to green then yellow then red again
        pygame.draw.circle(screen, green, [self.offSet+30, self.offSet+10+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, yellow, [self.offSet+30, self.offSet+10+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, red, [self.offSet+30, self.offSet+10+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
    def bottomLight(self):
        #The fourth one changes to green then yellow then red again
        pygame.draw.circle(screen, green, [self.offSet+15, self.offSet+50+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, yellow, [self.offSet+15, self.offSet+50+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
        pygame.draw.circle(screen, red, [self.offSet+15, self.offSet+50+self.add], 2)
        pygame.display.flip()
        self.clock.tick(3)
clock = pygame.time.Clock()
clockS1 = pygame.time.Clock()
# main loop
while not done:
    centerI = trafficLights(clock, 200)
    centerI.wholePack()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()















