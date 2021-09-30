from tkinter.constants import RIGHT
from modules.graphics import *
from modules.game import *
class Column():

    def __init__(self, winObj, column_width, column_color):
        self.win = winObj
        self.column_width = column_width
        self.column_color = column_color


        self.numTurns = 0
        self.forefeit_button = self.__gen_forefeit_button()
        self.counterDisplay = None
        
       

    def __gen_forefeit_button(self):
        color = color_rgb(231, 108, 108)
        spacing = self.column_width/4
        x1_disp= self.win.getWidth() - self.column_width + spacing
        y1_disp = self.win.getHeight() - self.win.getHeight()/5 + spacing
        
        x2_disp = self.win.getWidth() - spacing
        y2_disp = self.win.getHeight() - spacing
        
    
        button = Button(Point(x1_disp, y1_disp), Point(x2_disp, y2_disp))
        button.setOutline(color)
        button.setFill(color)
        button.setText('QUIT', int(self.column_width/10))
        button.setTextColor('white')

        return button

    # def __gen_column_block(self):
    #     rec = Rectangle(Point(self.win.getWidth()))   
    def drawComponents(self):
        column_block = Rectangle(Point(self.win.getHeight(), 0), Point(self.win.getWidth(), self.win.getHeight()))
        column_block.setFill(self.column_color)
        column_block.setOutline(self.column_color)
        
        column_block.draw(self.win)
        self.forefeit_button.draw(self.win)

    def __gen_display_counter(self):
        pass

    def getForefitButton(self):
        return self.forefeit_button
 
        


class Button():

    def __init__(self, p1, p2):
        self.rec = Rectangle(p1, p2);
        self.text = None

        self.leftX = self.rec.getP1().getX()
        self.rightX = self.rec.getP2().getX()

        self.topY = self.rec.getP1().getY()
        self.botY = self.rec.getP2().getY()

        self.centerPoint = self.rec.getCenter()


    def ifPressed(self, p):
        
        insideX = False
        insideY = False

        if p.getX() > self.leftX and p.getX() < self.rightX:
            insideX = True
        
        if p.getY() > self.topY and p.getY() < self.botY:
            insideY = True

        if insideX and insideY:
            return True
        else:
            return False


    def draw(self, window):
        print('it ran')
        if self.text is not None:
            print('rec and text')
            self.rec.draw(window)
            self.text.draw(window)
        else:
            print('rect')
            self.rec.draw(window)


    def undraw(self):
        if self.text == None:
            self.rec.undraw()
            
        else:
            self.rec.undraw()
            self.text.undraw()
    

    def setText(self, strLine, size):
        self.text = Text(self.centerPoint, strLine)
        self.text.setSize(size)
    

    def setTextColor(self, colors):
        self.text.setTextColor(colors)


    def setOutline(self, colors):
        self.rec.setOutline(colors)


    def setFill(self, colors):
        self.rec.setFill(colors)

    def getWidth(self):
        return self.leftX - self.rightX
    

    


