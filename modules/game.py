from modules.graphics import *

class Round():

    def __init__(self, window, winSize, difficulty):
        # get window object
        self.win = window

        # set size of window
        self.winSize = winSize
        # set difficulty for distribution
        mode = {'easy' : 20, 'medium' : 10, 'hard' : 8, 'test' : 2}
        self.distribution = mode[difficulty.lower()]
        self.spacing = self.winSize/self.distribution

        # related to lines
        self.lineList = self.__generateLines()
        self.slotList = self.__generateSlots()

        # conditions of the round
        self.numTurns = 0
        self.running = True

        # extra cond
        self.currentRowIndex = 0
        self.currentColumnIndex = 0
        self.currentPlayerId = 0

    # generate line
    def __generateLines(self):
        li = []

        for x in range(self.distribution - 1):
            # get horizontal line end points
            hPoint1 = Point(self.spacing, self.spacing * (x + 1))
            hPoint2 = Point(self.winSize - self.spacing, self.spacing * (x + 1))
            
            # get vertical line end points
            vPoint1 = Point(self.spacing * (x + 1), self.spacing)
            vPoint2 = Point(self.spacing * (x + 1), self.winSize - self.spacing)

            # create line
            hLine = Line(hPoint1, hPoint2)
            vLine = Line(vPoint1, vPoint2)

            # set color to white
            hLine.setOutline(color_rgb(156,116,43))
            vLine.setOutline(color_rgb(156,116,43))

            # add to line list
            li.append(hLine)
            li.append(vLine)
        
        return li
    
    
    def __generateSlots(self):
        li = []

        for i in range(self.distribution - 1):
            row = []

            for j in range(self.distribution - 1):
                x = Slot(self.spacing*(j + 1), self.spacing*(i + 1))

                row.append(x)

            li.append(row)
        
        return li
    
    # draw lines
    def drawLines(self):   
        for x in range((self.distribution - 1)*2):
            self.lineList[x].draw(self.win)

    # find closet slot to add
    def findSlot(self, xCord, yCord):  
        column = 0
        for i in self.slotList[0]:
            
            if abs(i.getX() - xCord) < abs(self.slotList[0][column].getX() - xCord):
                column = self.slotList[0].index(i)
        
        closetYDistance = self.winSize
        chosenSlot = None
        row = 0

        for i in self.slotList:
            yDistance = abs(i[column].getY() - yCord)
            if yDistance <= closetYDistance:
                closetYDistance = yDistance
                row = self.slotList.index(i)
                chosenSlot = i[column]
        
        # set postions
        self.currentRowIndex = row
        self.currentColumnIndex = column

        return chosenSlot
        
    # game states
    def nextTurn(self): self.numTurns+=1


    def isRunning(self): return self.running


    def isFull(self):
        
        if self.numTurns == len(self.slotList)**2:
            return True
            
        else:
            return False
    
    # get
    def getSpacing(self): return self.spacing


    def getTurns(self): return self.numTurns

    # end round
    def hasFiveConnected(self, slot):

        def changeColor(listOfSlots):
            if slot.getId() == 1:
                color = "white"
            else:
                color = "black"

            for i in listOfSlots:
                dot = i.getDot()
                dot.undraw()
                dot.setOutline(color)
                dot.draw(self.win)
        
        # preset cond
        numConnected = 0
        slotsConnected = []
        row = self.slotList[self.currentRowIndex]
        
        # count right horizontal
        for i in range(1, 5):
            if self.currentColumnIndex + i < len(row):
                nextSlot = row[self.currentColumnIndex + i]

                if nextSlot.getId() == slot.getId() and numConnected < 4:
                    slotsConnected.append(nextSlot)
                    numConnected+=1
                else:
                    break
            else:
                break
        
        # check if connected
        if numConnected == 4:
            slotsConnected.append(slot)
            changeColor(slotsConnected)
            return True
        
        # count left horizontal
        for i in range(1, 5):
            if self.currentColumnIndex - i >= 0:
                nextSlot = row[self.currentColumnIndex - i]

                if nextSlot.getId() == slot.getId() and numConnected < 4:
                    slotsConnected.append(nextSlot)
                    numConnected+=1
                else:
                    break
            else:
                break
        
        # check if connected
        if numConnected == 4:
            slotsConnected.append(slot)
            changeColor(slotsConnected)
            return True

        # reset
        numConnected = 0
        slotsConnected = []
        
        # count up vertical
        for i in range(1, 5):
            if self.currentRowIndex - i >= 0:
                row = self.slotList[self.currentRowIndex - i]
                nextSlot = row[self.currentColumnIndex]

                if nextSlot.getId() == slot.getId() and numConnected < 4:
                    slotsConnected.append(nextSlot)
                    numConnected+=1
                else:
                    break
            else:
                break
        
       # check if connected
        if numConnected == 4:
            slotsConnected.append(slot)
            changeColor(slotsConnected)
            return True
        
        # count down vertical
        for i in range(1, 5):
            if self.currentRowIndex + i < len(self.slotList):
                row = self.slotList[self.currentRowIndex + i]
                nextSlot = row[self.currentColumnIndex]
        
                if nextSlot.getId() == slot.getId() and numConnected < 4:
                    slotsConnected.append(nextSlot)
                    numConnected+=1
                else:
                    break
            else:
                break
        
        # check if connected
        if numConnected == 4:
            slotsConnected.append(slot)
            changeColor(slotsConnected)
            return True

        # reset 
        numConnected = 0
        slotsConnected = []

        # count diagonal right up
        for i in range(1, 5):
            if self.currentColumnIndex + i < len(row) and self.currentRowIndex - i >= 0:
                row = self.slotList[self.currentRowIndex - i]
                nextSlot = row[self.currentColumnIndex + i]
        
                if nextSlot.getId() == slot.getId() and numConnected < 4:
                    slotsConnected.append(nextSlot)
                    numConnected+=1
                else:
                    break
            else:
                break
        
        # check if connected
        if numConnected == 4:
            slotsConnected.append(slot)
            changeColor(slotsConnected)
            return True
    
        # count diagonal down left
        for i in range(1, 5):
            if self.currentColumnIndex - i >= 0 and self.currentRowIndex + i < len(self.slotList):
                row = self.slotList[self.currentRowIndex + i]
                nextSlot = row[self.currentColumnIndex - i]
        
                if nextSlot.getId() == slot.getId() and numConnected < 4:
                    slotsConnected.append(nextSlot)
                    numConnected+=1
                else:
                    break
            else:
                break
        
        # check if connected
        if numConnected == 4:
            slotsConnected.append(slot)
            changeColor(slotsConnected)
            return True
        
        # reset
        numConnected = 0
        slotsConnected = []
        
        # count diagonal left up
        for i in range(1, 5):
            if self.currentColumnIndex - i >= 0 and self.currentRowIndex - i >= 0:
                row = self.slotList[self.currentRowIndex - i]
                nextSlot = row[self.currentColumnIndex - i]
        
                if nextSlot.getId() == slot.getId() and numConnected < 4:
                    slotsConnected.append(nextSlot)
                    numConnected+=1
                else:
                    break
            else:
                break
        
        # check if connected
        if numConnected == 4:
            slotsConnected.append(slot)
            changeColor(slotsConnected)
            return True
        
        # count diagonal down right
        for i in range(1, 5):
            if self.currentColumnIndex + i < len(row) and self.currentRowIndex + i < len(self.slotList):
                row = self.slotList[self.currentRowIndex + i]
                nextSlot = row[self.currentColumnIndex + i]
        
                if nextSlot.getId() == slot.getId() and numConnected < 4:
                    slotsConnected.append(nextSlot)
                    numConnected+=1
                else:
                    break
            else:
                break
        
        # check if connected
        if numConnected == 4:
            slotsConnected.append(slot)
            changeColor(slotsConnected)
            return True
        
        return False

    def end(self): self.running = False
    

class Player():

    def __init__(self, playerId, color):
        self.playerId = playerId
        self.color = color
    

    def getColor(self): return self.color


    def getId(self): return self.playerId


class Slot():

    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        self.slotOccupied = False

        # id is a single interger : 1 & 2 | 0 means there is no ID = no occupant of the slot
        self.occupantId = 0
        self.dot = None


    def occupy(self, player): 
        self.occupantId = player.getId()
        self.slotOccupied = True


    def getX(self): return self.x


    def getY(self): return self.y


    def getId(self): return self.occupantId

    
    def getDot(self): return self.dot
    

    def isOccupied(self): return self.slotOccupied

    # linking the Circle object to the specfied Slot object
    def addDotToSlot(self, dot): self.dot = dot

   

    
    


      
    

    


    

        
    


        