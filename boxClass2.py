# inspired by [2016-12-23] Challenge #296 [Hard] Flood Fill Puzzle Game
# on /r/dailyprogrammer

DEFAULT_I_MIN = 10
DEFAULT_N_MAX = 10

from random import *
import copy

class boxClass2():
    
    ##################################################
    ##----------------CLASS METHODS-----------------##
    ##################################################
    # (used mostly for implementing changeable settings)
    @classmethod
    def INIT(cls, nMax, iLim):
        boxClass2.INDEX_MIN = 0
        boxClass2.INDEX_LIM = iLim  #the size of the board
        boxClass2.NUM_MAX = nMax   #the highest number on the board (minus 1)

    @classmethod
    def getINDEX_LIM(cls):
        return boxClass2.INDEX_LIM

    @classmethod
    def getNUM_MAX(cls):
        return boxClass2.NUM_MAX

    @classmethod
    def setNUM_MAX(cls, nMax):
        boxClass2.NUM_MAX = nMax

    @classmethod
    def setINDEX_LIM(cls, iLim):
        boxClass2.INDEX_LIM = iLim

    ##################################################
    ##--------------INSTANCE METHODS----------------##
    ##################################################

    ##################################################
    ###            METHODS FOR SETUP               ###
    ##################################################
        
    def __init__(self):
        self.__data = []
        # vvvthe -1 below is to adjust for 0-indexing in range()vvv
        for i in range(boxClass2.INDEX_LIM):
            eachRow = []
            for j in range(boxClass2.INDEX_LIM):
                ##eachRow.append(randrange(1,boxClass2.NUM_MAX+1))####CHANGE ME FOR NOT MODs
                eachRow.append(randrange(0,boxClass2.NUM_MAX))    ####CHANGE ME FOR MODs
            self.__data.append(eachRow)
        self.__originalBoard = copy.deepcopy(self.__data)
        self.__lastState = copy.deepcopy(self.__data)
        self.__numMoves = 0
        self.__tempNumMoves = 0
        self.__tempList = []   ## used in the getGroup function
        ##print(self)
        
    def getVal(self, row, col):
        return self.__data[row][col]
    
    def getOriginalBoard(self):
        return self.__originalBoard

    def getNumMoves(self):
        return self.__numMoves

    ##################################################
    ###             ACTUAL GAME LOGIC              ###
    ##################################################

    def __floodFill(self, boxTuple, targetVal, replaceVal):
        #print("now checking " + str(boxTuple))
        tempVal = self.getVal(boxTuple[0], boxTuple[1])
        if tempVal != targetVal or targetVal == replaceVal:
            #print("we already filled this OR its not meant to be filled")
            return None
        #print("now changing " + str(boxTuple))
        x = boxTuple[0]
        y = boxTuple[1]
        self.__data[x][y] = replaceVal
        for (i,j) in [ (x-1, y), (x+1, y), (x, y-1), (x, y+1) ]:
            if i>=0 and j>=0 and i<boxClass2.INDEX_LIM and j<boxClass2.INDEX_LIM:
                #print("now filling " + str(i) + ", " + str(j))
                self.__floodFill((i,j), tempVal, replaceVal)

    def increment(self, boxTuple):
        newVal = self.getVal(boxTuple[0], boxTuple[1])+1
        if newVal <= boxClass2.NUM_MAX:
            self.__lastState = copy.deepcopy(self.__data)
            self.__floodFill(boxTuple, self.getVal(boxTuple[0], boxTuple[1]), \
                             self.getVal(boxTuple[0], boxTuple[1])+1)
            self.__numMoves += 1
        ##print(self)

    def decrement(self, boxTuple):
        newVal = self.getVal(boxTuple[0], boxTuple[1])-1
        if newVal > 0:
            self.__lastState = copy.deepcopy(self.__data)
            self.__floodFill(boxTuple, self.getVal(boxTuple[0], boxTuple[1]), \
                             self.getVal(boxTuple[0], boxTuple[1])-1)
            self.__numMoves += 1
        ##print(self)

    def incrementMod(self, boxTuple):
        self.__lastState = copy.deepcopy(self.__data)
        self.__floodFill(boxTuple, self.getVal(boxTuple[0], boxTuple[1]), \
                           (self.getVal(boxTuple[0], boxTuple[1]) + 1) % boxClass2.NUM_MAX)
        self.__numMoves += 1
        ##print(self)
        
    def decrementMod(self, boxTuple):
        self.__lastState = copy.deepcopy(self.__data)
        self.__floodFill(boxTuple, self.getVal(boxTuple[0], boxTuple[1]), \
                           (self.getVal(boxTuple[0], boxTuple[1]) - 1) % boxClass2.NUM_MAX)
        self.__numMoves += 1
        ##print(self)

    ##################################################
    ###        GAME CONTROL MECHANISMS             ###
    ##################################################

    def didWin(self):
        return self.__didWinHelper(0)

    def __didWinHelper(self, index):
        if index == len(self.__data)-2:
            return self.__data[index] == self.__data[index+1]
        return (self.__data[index]==self.__data[index+1]) and self.__didWinHelper(index+1)
    
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
        for i in range(boxClass2.INDEX_LIM):
            for j in range(boxClass2.INDEX_LIM):
                retStr += str(self.__data[i][j]) + '\t'
            retStr += '\n'
        return retStr    
    
boxClass2.INIT(DEFAULT_N_MAX, DEFAULT_I_MIN)

