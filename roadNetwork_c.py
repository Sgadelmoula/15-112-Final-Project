class road:
    def __init__(self, length, valuerep = 0):
        #A road needs a length and a value representation
        #meaning how will a road look like in the resultant map
        self.length = length
        self.fstlane = [valuerep]*length
        self.sndlane = [valuerep]*length
        self.whole = [self.fstlane, self.sndlane]

class roadNetwork:
    def __init__(self, dimensions, v_pos, h_pos):
        #Dimensions refers to the map as a whole
        self.net = []
        self.dimen = dimensions
        self.grid = []
        self.h_list = []
        self.v_list = []
        self.roadsDic = {}
        self.StAddress = 0
        self.initial = self.grid
        self.curState = list(self.grid)
        self.intersection = 0
        self.h_pos = h_pos
        self.v_pos = v_pos
    def makeMap(self):
        #This uses the dimentions to make the initial map
        #with the help of the road network class
        self.makeGrid()
        if len(self.v_pos) > 0:
            for i in self.v_pos:
                self.addRoads(posx = i, posy = 0, orient = 'v')
        if len(self.h_pos) > 0:
            for i in self.h_pos:
                self.addRoads(posx = 0, posy = i, orient = 'h')
        return self.grid
        
        
    def makeGrid(self):
        for i in range(self.dimen[0]):
            self.grid.append([1]*self.dimen[1])

    def addRoads(self, posx = 0, posy = 0, orient = 'v'):
        #Adding a road requies a position, x for vertical
        #y for horizontal
        if orient == 'v':
            for i in range(len(self.grid)):
                self.grid[i][posx] = 0
                self.grid[i][posx+1] = 0
        if orient == 'h':
            for i in range(self.dimen[1]):
                #Marking an intesection by setting its value to 5
                if self.grid[posy][i] == 0:
                    self.grid[posy][i] = 5
                    
            for i in range(self.dimen[1]):
                #Filling in with zeros
                if self.grid[posy][i] != 5:
                    self.grid[posy][i] = 0
                    self.grid[posy+1][i] = 0
    
    def getIntPos(self):
        #For the traffic placement we hve a function that returns
        #the intersection position
        intPos = []
        for i in range(self.dimen[0]):
            for k in range(1):
                for j in range(self.dimen[1]):
                    if self.grid[i][k][j] == 5:
                        intPos += [[i,k,j]]
        return intPos
    
    def getStAddress(self):
        #To fill in cars in the correct spots
        for i in range(self.dimen[0]):
            for k in range(1):
                if self.grid[i][k][0] == 0:
                    self.roadsDic['Hroad'+str(i)+str(k)] = [[i,k,0]]
        for i in range(self.dimen[1]):
            if self.grid[0][0][i] == 0:
                self.roadsDic['Vroad'+'0'+str(i)] = [[0,0,i]]
        return self.roadsDic

    def updateMap(self):
        #For easily displaying the current state of the map with
        #cars added, traffic lights, etc.
        return self.grid


