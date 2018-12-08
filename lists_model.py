
import roadNetwork
import trafficLights

###################### Classes #######################################)
class world:
    def __init__(self, dimensions, v_pos, h_pos):
        #This class takes in the dimensions of the whole map,
        #a list of all the horizontal and vertical roads positions
        #give the y coordinate for the horizontal and the x coordinate
        #for the virtical roads
        self.dimen = dimensions
        self.curState = 0
        self.initial = roadNetwork.roadNetwork(self.dimen, v_pos, h_pos).makeMap()
        self.count = 0
        self.h_pos = h_pos
        self.v_pos = v_pos
        self.intPos = 0
        self.roadsDic = {}
        
    def environment(self):
        env = roadNetwork.roadNetwork(self.dimen, self.v_pos, self.h_pos)
        self.curState = env.makeMap()
        return self.curState

    def getIntPos(self):
        #For the traffic placement we hve a function that returns
        #the intersection position
        intPos = []
        for i in range(self.dimen[0]):
            for k in range(1):
                for j in range(self.dimen[1]):
                    if self.initial[i][k][j] == 5:
                        intPos += [[i,k,j]]
        return intPos
    
    def getStAddress(self):
        #To fill in cars in the correct spots
        for i in range(self.dimen[0]):
            for k in range(1):
                if self.initial[i][k][0] == 0:
                    self.roadsDic['Hroad'+str(i)+str(k)] = [[i,k,0]]
        for i in range(self.dimen[1]):
            if self.initial[0][0][i] == 0:
                self.roadsDic['Vroad'+'0'+str(i)] = [[0,0,i]]
        return self.roadsDic
    
    def lookEast(self, start):
        s = start[0]
        current = self.curState
        if current[s[0]][s[1]][s[2]+1] != 7:
            return True
        return False


class car:
    def __init__(self, currentPos, w):
        #Current position is the starting position of the car
        self.current = currentPos
        self.body = 7
        self.ground = w.curState
        self.i = -1
        self.w = w
        
    def moveEast(self):
        ask = self.w.lookEast(self.current)
        intersect = self.w.getIntPos()
        if ask:
            if self.current[0] in intersect:
                p = 5
            else:
                p = 0
            self.ground[self.current[0][0]][self.current[0][1]][self.i+1] = p
            self.ground[self.current[0][0]][self.current[0][1]][self.i+2] = self.body
            self.i += 1
            self.current[0][2]+= 1
            



















