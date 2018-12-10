
import roadNetwork_c
import trafficLights_c
import random
import pygame
###################### Classes #######################################)
class world:
    def __init__(self, allCars, allTLs):
        self.allCars = allCars
        self.lights = allTLs
        self.relevant = [[10,6.5],[11.5,4], [10.5,7], [13,5.5]]
    
    def checkCars(self, x, y):
        #Loops through the list of all created cars
        for i in range(len(self.allCars)):
            if self.allCars[i].x == x:
                if self.allCars[i].y == y:
                    #returns False if a car is found at the wanted
                    #position
                    return False
        return True
    
    def checkTLights(self, x, y, d):
        #If the car reaches an intersection
        if [x, y] in self.relevant:
            if d == 'e':
                #If the east traffic lights are red stop
                if self.lights[0].current == 1:
                    return False
                #carry on
                else:
                    return True
            if d == 's':
                if self.lights[1].current == 1:
                    return False
                else:
                    return True
            if d == 'n':
                if self.lights[2].current == 1:
                    return False
                else:
                    return True
            if d == 'w':
                if self.lights[3].current == 1:
                    return False
                else:
                    return True
        return True

class car:
    def __init__(self,w,x,y,d):
        #Current position is the starting position of the car
        self.x = x
        self.y = y
        green = (0,255,0)
        red = (255,0,0)
        yellow = (255,255,0)
        self.ctrl = w
        self.timer = 100
        self.color = random.choice([red,green,yellow])
        self.direction = d
        
    def move(self):
        #Depending on the direction check with world if a car or a red light is there
        #If there isn't then go on.
        if self.direction == "e" and self.timer == 0:
            empty = self.ctrl.checkCars(self.x+1, self.y)
            green = self.ctrl.checkTLights(self.x+1, self.y, self.direction)
            if empty and green:
                self.x += 1
                self.timer = 50
            else:
                self.timer = 50
                
        if self.direction == "w" and self.timer == 0:
            empty = self.ctrl.checkCars(self.x-1, self.y)
            green = self.ctrl.checkTLights(self.x-1, self.y, self.direction)
            if empty and green:
                self.x -= 1
                self.timer = 50
            else:
                self.timer = 50
                
        if self.direction == "n" and self.timer == 0:
            empty = self.ctrl.checkCars(self.x, self.y-1)
            green = self.ctrl.checkTLights(self.x, self.y-1, self.direction)
            if empty and green:
                self.y -= 1
                self.timer = 50
            else:
                self.timer = 50
                
        if self.direction == "s" and self.timer == 0:
            empty = self.ctrl.checkCars(self.x, self.y+1)
            green = self.ctrl.checkTLights(self.x, self.y+1, self.direction)
            if empty and green:
                self.y += 1
                self.timer = 50
            else:
                self.timer = 50
        self.timer -= 5
        
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,pygame.Rect(20*self.x,20*self.y,5,5))

    def terminate(self, allCars):
        #The car removes it self from the list if the car goes
        #beyond boundries.
        if self.x < 0 :
            allCars.remove(self)
        if self.x > 30:
            allCars.remove(self)
        if self.y > 25:
            allCars.remove(self)
        if self.y < 0:
            allCars.remove(self)
 

















