import random, pygame
class trafficLights:
    def __init__(self, updateRate = 1, delay = 0, x = 0, y = 0):
        #A traffic light would need a delay (the time the red lights
        #are on in msec), an x and y position for later positioning,
        #and an update rate so that the timing of the states stay constant
        #regardless of the update rate
        self.x = x
        self.y = y
        self.states = [1, 2, 3]
        self.current = random.choice(self.states)
        green = (0,255,0)
        red = (255,0,0)
        yellow = (255,255,0)
        self.colors = [red,yellow,green]
        self.delay = delay
        #The red and green lights stay an equal amount of time but
        #the yellow light stays half the period
        self.r_timer = delay + 4
        self.y_timer = self.r_timer/2
        self.g_timer = delay + 4
        self.upR = updateRate
    def draw(self,screen):
        pygame.draw.circle(screen, self.colors[self.current-1] , [20*self.x-5,20*self.y+10], 3)
    def updateTimer(self):
        RED = 1
        YELLOW = 2
        GREEN = 3
        #Decrementing the main timer after every call
        if self.current == RED:
            self.r_timer -= self.upR
            if self.r_timer <= 0:
                self.g_timer = self.delay + 4
                self.current = GREEN
        elif self.current == YELLOW:
            self.y_timer -= self.upR
            if self.y_timer <= 0:
                self.r_timer = self.delay + 4
                self.current = RED
        elif self.current == GREEN:
            self.g_timer -= self.upR
            if self.g_timer <= 0:
                self.y_timer = (self.delay + 4)/2
                self.current = YELLOW
