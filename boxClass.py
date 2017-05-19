'''
Things I still want to do with this:

Replace the current getGroup() and in/decrement() methods with
  a single in/decrement method (with parameters: self, boxTuple, +/-)
  that uses the flood fill algorithm (formally).

Implement a better GUI/Interface
'''

DEFAULT_I_MAX = 10
DEFAULT_N_MAX = 10

from random import *
import copy

class boxClass():

    @classmethod
    def setNUM_MAX(cls, nMax):
        boxClass.NUM_MAX = nMax

    @classmethod
    def setINDEX_LIM(cls, iLim):
        boxClass.INDEX_LIM = iLim
        
    @classmethod
    def INIT(cls, nMax, iLim):
        boxClass.INDEX_MIN = 0
        boxClass.INDEX_LIM = iLim  #the size of the board
        boxClass.NUM_MAX = nMax   #the highest number on the board (minus 1)

        boxClass.FALSE_2D_LIST = []
        for i in range(boxClass.INDEX_LIM):
            eachRow = []
            for j in range(boxClass.INDEX_LIM):
                eachRow.append(False)
            boxClass.FALSE_2D_LIST.append(eachRow)

    @classmethod
    def getDefaults(cls):
        boxClass

    ## tuples of the form (row, column) will be used
    ## note: the grid is 0-indexed from the top-left corner

    def __init__(self):
        self.__data = []
        # vvvthe -1 below is to adjust for 0-indexing in range()vvv
        for i in range(boxClass.INDEX_LIM):
            eachRow = []
            for j in range(boxClass.INDEX_LIM):
                ##print(i, '\t', j)
                ##eachRow.append(randrange(1,boxClass.NUM_MAX+1))####CHANGE ME FOR NOT MODs
                eachRow.append(randrange(0,boxClass.NUM_MAX))    ####CHANGE ME FOR MODs
            self.__data.append(eachRow)
        self.__originalBoard = copy.deepcopy(self.__data)
        self.__lastState = copy.deepcopy(self.__data)
        self.__numMoves = 0
        self.__tempNumMoves = 0
        self.__tempList = []   ## used in the getGroup function
        ##print(self)
    '''
    ## Constructor for testing purposes:
    def __init__(self):
        row1 = [4, 4, 4, 2]
        row2 = [4, 4, 4, 4]
        row3 = [4, 4, 5, 5]
        row4 = [4, 5, 5, 5]
        self.__data = [row1, row2, row3, row4]
        self.__tempList = []   ## used in the getGroup function
    '''
    @classmethod
    def getINDEX_LIM(cls):
        return boxClass.INDEX_LIM

    @classmethod
    def getNUM_MAX(cls):
        return boxClass.NUM_MAX

    def getVal(self, row, col):
        return self.__data[row][col]
    
    def getOriginalBoard(self):
        return self.__originalBoard

    def getNumMoves(self):
        return self.__numMoves
    
    def getAdjacents(self, boxTuple):
        retList = []
        x = boxTuple[0]
        y = boxTuple[1]
        for (i,j) in [ (x-1, y), (x+1, y), (x, y-1), (x, y+1) ]:
                ##print(i, '\t', j)
                if i >= boxClass.INDEX_MIN and i < boxClass.INDEX_LIM and \
                   j >= boxClass.INDEX_MIN and j < boxClass.INDEX_LIM:
                    ##print(i, "\t", j)
                    retList.append((i,j))
        return retList

    def getSameAdjacents(self, boxTuple):
        retList = []
        x1 = boxTuple[0]
        y1 = boxTuple[1]
        for (x2,y2) in self.getAdjacents(boxTuple):
            if self.__data[x1][y1] == self.__data[x2][y2]:
                retList.append((x2,y2))
        return retList

    def getGroup(self, boxTuple):
        ## very first base cases:
        if not(self.__tempList):
            if not(self.getSameAdjacents(boxTuple)):
                ##print(boxTuple, "only one here")
                return [boxTuple]
            else:
                self.__tempList.append(boxTuple)
                for eachTuple in self.getSameAdjacents(boxTuple):
                    ##print(eachTuple, "(added)", boxTuple, "has buddies")
                    self.getGroup(eachTuple)
                    if eachTuple not in self.__tempList:
                        self.__tempList.append(eachTuple)
                retList = self.__tempList
                ##print("reseting self.__tempList now")
                self.__tempList = []
                return retList
            
        else:
            for eachTuple in self.getSameAdjacents(boxTuple):
                if boxTuple not in self.__tempList:
                    self.__tempList.append(boxTuple)
                if eachTuple not in self.__tempList:
                    ##print(eachTuple, "adding this now")
                    thisResult = self.getGroup(eachTuple)
                    if thisResult != None:
                        ##print("actually adding", eachTuple)
                        self.__tempList.append(thisResult)
                if eachTuple in self.__tempList:
                    pass
                    ##print(eachTuple, "already accounted for")

    
    def getAllGroups(self): #, boxTuple):
        groupList = []
        boolList = copy.deepcopy(boxClass.FALSE_2D_LIST)
        for i in range(boxClass.INDEX_LIM):
            for j in range(boxClass.INDEX_LIM):
                myGroup = self.getGroup((i,j))
                shouldAdd = True
                for t in myGroup:
                    if boolList[t[0]][t[1]]:
                        shouldAdd = False
                if shouldAdd:
                    groupList.append(myGroup)
                    for t in myGroup:
                        boolList[t[0]][t[1]] = True
        return groupList

    
    def didWin(self):
        if len(self.getAllGroups()) == 1:
            return True
        else:
            return False
    '''
    # alternative didWin() (that does not use getGroup())
    # simply checks if all the values in self.__data are the same
    def didWin(self):
        won = True
        tempList = []
        firstTime = True
        i = 0
        while i < boxClass.INDEX_LIM and won:
            j = 0
            while j < boxClass.INDEX_LIM and won:
                ##print(self.__data[i][j], '\t', tempList)
                if firstTime:
                    tempList.append(self.__data[i][j])
                    firstTime = False
                else:
                    if self.__data[i][j] not in tempList:
                        won = False
                    tempList.append(self.__data[i][j])
                j += 1
            i += 1
        return won
    '''
    

    def increment(self, boxTuple):
        if (self.getVal(boxTuple[0], boxTuple[1]) + 1) <= boxClass.NUM_MAX:
            self.__lastState = copy.deepcopy(self.__data)
            for (i,j) in self.getGroup(boxTuple):
                self.__data[i][j] += 1
            self.__numMoves += 1
        ##print(self)

    def decrement(self, boxTuple):
        if (self.getVal(boxTuple[0], boxTuple[1])) - 1 > 0:
            self.__lastState = copy.deepcopy(self.__data)
            for (i,j) in self.getGroup(boxTuple):
                self.__data[i][j] += -1
            self.__numMoves += 1
        ##print(self)

    def incrementMod(self, boxTuple):
        self.__lastState = copy.deepcopy(self.__data)
        for (i,j) in self.getGroup(boxTuple):
            self.__data[i][j] = (self.__data[i][j] + 1) % boxClass.NUM_MAX
        self.__numMoves += 1
        ##print(self)
        
    def decrementMod(self, boxTuple):
        self.__lastState = copy.deepcopy(self.__data)
        for (i,j) in self.getGroup(boxTuple):
            self.__data[i][j] = (self.__data[i][j] - 1) % boxClass.NUM_MAX
        self.__numMoves += 1
        ##print(self)

    def undoMove(self):
        if self.__tempNumMoves == self.__numMoves or self.__numMoves == 0:
            self.__numMoves = self.__tempNumMoves
        else:
            self.__numMoves += -1
        self.__tempNumMoves = self.__numMoves
        self.__data = copy.deepcopy(self.__lastState)
        ##print(self)

    def resetBoard(self):
        self.__lastState = copy.deepcopy(self.__data)
        self.__tempNumMoves = self.__numMoves
        self.__numMoves = 0
        self.__data = copy.deepcopy(self.__originalBoard)
        ##print(self.__originalBoard)
        ##print(self.__data)
        ##print(self)



    def __str__(self):
        retStr = "\nNumber of Moves: " + str(self.__numMoves) + "\n"
        for i in range(boxClass.INDEX_LIM):
            for j in range(boxClass.INDEX_LIM):
                retStr += str(self.__data[i][j]) + '\t'
            retStr += '\n'
        return retStr
    

def Tester():
    myBox = boxClass()
    ##print(myBox)
    #print( myBox.getGroup((1,1)) )
    #print( myBox.getGroup((3,3)) )
    #for eachVal in myBox.getAllGroups():
    #    print(eachVal, '\n')
    myBox.increment((0,0))
    for i in range(5):
        myBox.decrement((0,0))

##Tester()
boxClass.INIT(DEFAULT_N_MAX, DEFAULT_I_MAX)
 
