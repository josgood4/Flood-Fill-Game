from boxClass import *

def processTuple(givenStr):
    retTuple = list(givenStr)
    for i in range(2):
        retTuple[i] = int(retTuple[i])
    return tuple(retTuple)

def main():
    model = boxClass()
    print(model)
    print("type two numbers next to each other for the tuple \n" + \
          "for example: 02 would be the 0th row, 2nd element \n" + \
          "note: the board is 0-indexed from the top-left corner \n"+\
          "hit <ENTER> to quit (when prompted for a tuple)\n")
    tupleStr = input("Give me a tuple:")

    while tupleStr:
        doStr = input("i or d? (r, u, n?)")
        if doStr.lower() == 'i':
            ##model.increment(processTuple(tupleStr))
            model.incrementMod(processTuple(tupleStr))
            print(model)
        if doStr.lower() == 'd':
            ##model.decrement(processTuple(tupleStr))
            model.decrementMod(processTuple(tupleStr))
            print(model)
        if doStr.lower() == 'r':
            model.resetBoard()
            print(model)
        if doStr.lower() == 'u':
            model.undoMove()
            print(model)
        if doStr.lower() == 'n':
            model = boxClass()
            print(model)
        if model.didWin():
            print("you won!!!")
            doStr = input("keep playing? (y/n)")
            if doStr == 'y':
                model.resetBoard()
                print(model)
            else:
                break
        tupleStr = input("Give me a tuple:")

main()
