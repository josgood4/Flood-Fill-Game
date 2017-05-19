from tkinter import *
#from boxClass import *
from boxClass2 import *
from ButtonClass import *
import sys
import os

BUTTON_STR = 'button'

INC = 1
DEC = 2

class mainGUI():
    def __init__(self):
        self.__model = boxClass2()
        self.__root = Tk()

        self.__dict = {}
        
        ##self.__mainLabel = Label(self.__root, text='Grid game')\
                           #.grid(row=0, column=0)
        self.__numMoveLabel = Label(self.__root, text='Number of Moves: ')
        self.__numMoveVar = StringVar()
        self.__numMoveVar.set(self.__model.getNumMoves())
        self.__numMoveLabelD = Label(self.__root, textvariable=self.__numMoveVar)

        self.__radVar = IntVar()
        self.__incButton = Radiobutton(self.__root, text="Increment", \
                                       variable=self.__radVar, value=INC)
        self.__decButton = Radiobutton(self.__root, text="Decrement", \
                                       variable=self.__radVar, value=DEC)
        self.__undoButton = Button(self.__root, text='Undo', \
                                   command=self.__undoMove)
        self.__resetButton = Button(self.__root, text='Reset', \
                                    command=self.__resetGame)
        self.__newButton = Button(self.__root, text='New Game', \
                                  command=self.__newGame)
        ##self.__setButton = Button(self.__root, text='Settings', \
                                  #command=self.__settings)
        self.__top = None
                                    

        ButtonClass.INIT(self, self.__root, self.__model, \
                         self.__radVar)
        self.__setupBoard(boxClass2.getINDEX_LIM())
        self.__gridOptions()
                                

    def __gridOptions(self):
        self.__numMoveLabel.grid(row=0, column=boxClass2.getINDEX_LIM()+1)
        self.__numMoveLabelD.grid(row=0, column=boxClass2.getINDEX_LIM()+2)
        self.__incButton.grid(row=1, column=boxClass2.getINDEX_LIM()+1)
        self.__decButton.grid(row=2, column=boxClass2.getINDEX_LIM()+1)
        self.__undoButton.grid(row=3, column=boxClass2.getINDEX_LIM()+1)
        self.__resetButton.grid(row=4, column=boxClass2.getINDEX_LIM()+1)
        self.__newButton.grid(row=5, column=boxClass2.getINDEX_LIM()+1)
        ##self.__setButton.grid(row=6, column=boxClass2.getINDEX_LIM()+1)

        
    def __setupBoard(self, numBoxes):
        for i in range(numBoxes):
            for j in range(numBoxes):
                self.__dict[(i,j)] = ButtonClass(i,j)

    def updateBoard(self):
        for i in range(boxClass2.getINDEX_LIM()):
            for j in range(boxClass2.getINDEX_LIM()):
                self.__dict[(i,j)].updateVal()
        self.__numMoveVar.set(self.__model.getNumMoves())
        ##print(self.__model)

    def __newGame(self):
        self.__model = boxClass2()
        self.__dict = {}
        ButtonClass.INIT(self, self.__root, self.__model, \
                         self.__radVar)
        self.__setupBoard(boxClass2.getINDEX_LIM())
        self.updateBoard()

    def __resetGame(self):
        self.__model.resetBoard()
        self.updateBoard()

    def __undoMove(self):
        self.__model.undoMove()
        self.updateBoard()
        
    '''
    def __settings(self):
        if not(self.__top):
            self.__top = Toplevel()
            self.__top.protocol("WM_DELETE_WINDOW", self.__onClosing)
            self.__numMaxCurrL = Label(self.__top, text='Current Limit: ')
            self.__numMaxCurrV = StringVar()
            self.__numMaxCurrV.set(boxClass2.getNUM_MAX())
            self.__numMaxCurrLD = Label(self.__top, textvariable=self.__numMaxCurrV)

            self.__numMaxL = Label(self.__top, text='Number Limit: ')
            self.__numMaxUserV = StringVar()
            self.__numMaxE = Entry(self.__top, textvariable=self.__numMaxUserV)
            self.__numMaxE.bind("<Return>", self.__setNUM_MAX)
            self.__numMaxE.config(width=5)


            self.__iLimCurrL = Label(self.__top, text='Current Limit: ')
            self.__iLimCurrV = StringVar()
            self.__iLimCurrV.set(boxClass2.getINDEX_LIM())
            self.__iLimCurrLD = Label(self.__top, textvariable=self.__iLimCurrV)            

            self.__iLimL = Label(self.__top, text='Board size: ')
            self.__iLimUserV = StringVar()
            self.__iLimE = Entry(self.__top, textvariable=self.__iLimUserV)
            self.__iLimE.bind("<Return>", self.__setI_LIM)
            self.__iLimE.config(width=5)

            #Grid calls:
            self.__numMaxCurrL.grid(row=1, column=0, sticky='E')
            self.__numMaxCurrLD.grid(row=1, column=1)
            self.__numMaxL.grid(row=2, column=0, sticky='E')
            self.__numMaxE.grid(row=2, column=1)
            
            Label(self.__top, text=' ').grid(row=3, column=0)

            self.__iLimCurrL.grid(row=4, column=0, sticky='E')
            self.__iLimCurrLD.grid(row=4, column=1)
            self.__iLimL.grid(row=5, column=0, sticky='E')
            self.__iLimE.grid(row=5, column=1)
            

            self.__instr = Label(self.__top, text=\
                                 'Type a number\n(this will', justify='right')\
                                 .grid(row=0, column=0)
            self.__instr2 = Label(self.__top, text=\
                                  'and hit <ENTER> \nreset game)', justify='left')\
                                  .grid(row=0, column=1)
            
    def __setNUM_MAX(self, e):
        if self.__numMaxUserV.get().isdigit():
            boxClass2.setNUM_MAX(int(self.__numMaxUserV.get()))
            self.__newGame()
            self.updateBoard()
            self.__numMaxCurrV.set(self.__numMaxUserV.get())
        print("hey")
        self.__numMaxUserV.set('')
        
    def __setI_LIM(self, e):
        if self.__iLimUserV.get().isdigit():
            boxClass2.setINDEX_LIM(int(self.__iLimUserV.get()))
            ##print('--------')
            
            temp = list(self.__dict.values())
            for eachButton in temp:
                print("deleting " + str(eachButton))
                eachButton.getButton().destroy()
                del self.__dict[eachButton.getTuple()]
            #self.__newGame() #:
            self.__model = boxClass2()
            self.__dict = {}
            ButtonClass.INIT(self, self.__root, self.__model, \
                             self.__radVar)
            self.__setupBoard(boxClass2.getINDEX_LIM())
            self.updateBoard()
            
            self.__newGame()
            
            self.__iLimCurrV.set(self.__iLimUserV.get())
            self.__gridOptions()
        self.__iLimUserV.set('')

    def __onClosing(self):
        self.__top.destroy()
        self.__top = None
    '''

            
        

        
        


mainGUI()
