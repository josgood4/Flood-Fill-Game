from tkinter import *

INC = 1
DEC = 2
BG_COLORS = ['maroon1', 'brown1', 'chocolate1', 'goldenrod1', 'green2', \
              'yellow', 'green4', 'blue4', 'DeepSkyBlue', 'violet']
FG_COLORS = ['black', 'black', 'black', 'black', 'black', \
              'black', 'white', 'white', 'black', 'black']

class ButtonClass():
    def __init__(self, aRow, aCol):
        self.__row = aRow
        self.__col = aCol
        self.__myText = StringVar()
        self.__myText.set(str(ButtonClass.MODEL.getVal(aRow, aCol)))
        self.__myButton = Button(ButtonClass.ROOT, textvariable=self.__myText, \
                          command=self.myCommand)
        ##print(aRow,"\t", aCol)
        self.__myButton.config(activebackground=BG_COLORS[ButtonClass.MODEL.getVal(aRow, aCol)-1], \
                               activeforeground=FG_COLORS[ButtonClass.MODEL.getVal(aRow, aCol)-1]  )
        self.__myButton.grid(row=aRow, column=aCol)
        ##print("initializing " + self.__str__())
        
        

    @classmethod
    def INIT(cls, GUI, root, model, var):
        ButtonClass.GUI = GUI
        ButtonClass.ROOT = root
        ButtonClass.MODEL = model
        ButtonClass.radVar = var

    def myCommand(self):
        ##print(type(ButtonClass.radVar.get()))
        if ButtonClass.radVar.get() == INC: #change increment()/incrementMod() here
            ButtonClass.MODEL.incrementMod( \
                (self.__row, self.__col))
        if ButtonClass.radVar.get() == DEC: #likewise with decrement()/decrementMod()
            ButtonClass.MODEL.decrementMod( \
                (self.__row, self.__col))
        ButtonClass.GUI.updateBoard()
        if ButtonClass.MODEL.didWin():
            messagebox.showinfo("You Won!", "You Won!!!")

    def updateVal(self):
        self.__myText.set(str(ButtonClass.MODEL.getVal(\
                self.__row, self.__col)))
        ##print(self.__myText.get())

    def getButton(self):
        return self.__myButton

    def getTuple(self):
        return (self.__row, self.__col)

    def __str__(self):
        return str(self.__row) + ', ' + str(self.__col) + \
                ', ' + self.__myText.get()



