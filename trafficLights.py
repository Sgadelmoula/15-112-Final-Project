class trafficLights:
    def __init__(self, updateRate = 1, delay = 0, x = 0, y = 0):
        #A traffic light would need a delay (the time the red lights
        #are on in sec), an x and y position for later positioning,
        #and an update rate so that the timing of the states stay constant
        #regardless of the update rate
        self.x = x
        self.y = y
        self.states = [1, 2, 3]
        self.current = 1
        self.delay = delay
        #The red and green lights stay an equal amount of time but
        #the yellow light stays half the period
        self.r_timer = delay + 4
        self.y_timer = self.r_timer/2
        self.g_timer = delay + 4
        self.upR = updateRate
        
    def updateTimer(self):
        RED = 1
        YELLOW = 2
        GREEN = 3
        #Decrementing the main timer after every call
        if self.r_timer > 0:
            self.r_timer -= self.upR
            self.current = RED
            #Resetting the green timer for the nxt cycle
            self.g_timer = self.delay + 4
        elif self.y_timer > 0:
            self.y_timer -= self.upR
            self.current = YELLOW
        elif self.g_timer >= 0:
            self.g_timer -= self.upR
            self.current = GREEN
            if self.g_timer == 0:
                #resetting the red and yellow timer
                self.r_timer = self.delay + 4
                self.y_timer = self.r_timer/2
