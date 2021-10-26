from modules.graphics import *
from modules.game import *
import time
class Column():

    def __init__(self, winObj, column_width, column_color):
        self.win = winObj
        self.column_width = column_width
        self.column_color = column_color

        self.column_block = self.__gen_column_block()

        self.num_turns_display = self.__gen_num_moves_display(0)

        
        self.turnText = self.__gen_turn_text()
        self.turn_display = self.__gen_turn_display("black")

        self.previous_move_text = self.__gen_previous_move_text()
        self.previous_move_display = self.__gen_previous_move_display('XX')

        self.forefeit_button = self.__gen_forefeit_button()

    # generate
    def __gen_column_block(self):
        column_block = Rectangle(Point(self.win.getHeight(), 0), Point(self.win.getWidth(), self.win.getHeight()))
        column_block.setFill(self.column_color)
        column_block.setOutline(self.column_color)

        return column_block
   

    def __gen_num_moves_display(self, numTurns):
        
        box_color = color_rgb(41, 44, 48)
        text_color = 'white'
        spacing = self.column_width/16
        

        x1_disp = self.win.getWidth() - self.column_width + spacing
        y1_disp = spacing

        x2_disp = self.win.getWidth() - spacing
        y2_disp = self.win.getHeight()/12 - spacing

        box = TextBox(Point(x1_disp, y1_disp), Point(x2_disp, y2_disp))
        box.setOutline(box_color)
        box.setFill(box_color)
        
        box.setText("Move : " + str(numTurns))
        box.setTextSize(int(self.column_width/8))
        box.setTextColor(text_color)

        return box
    

    def __gen_turn_text(self):
        spacing = self.column_width/16
        box_color = color_rgb(41, 44, 48)

        x1_disp = self.win.getWidth() - self.column_width + spacing
        y1_disp = self.win.getHeight()/12 + spacing

        x2_disp = self.win.getWidth() - self.column_width/2 + spacing
        y2_disp = (self.win.getHeight()/12)*2 - spacing

        box = TextBox(Point(x1_disp, y1_disp), Point(x2_disp, y2_disp))
        box.setOutline(box_color)
        box.setFill(box_color)
        
        box.setText('Turn:')
        box.setTextSize(int(self.column_width/9))
        box.setTextColor('white')
        return box


    def __gen_turn_display(self, turnColor):
        
        box_color = turnColor
        text_color = "black"
        if turnColor == "black":
            text_color = "white"
       
        spacing = self.column_width/16
        

        x1_disp = self.win.getWidth() - self.column_width/2 + spacing
        y1_disp = self.win.getHeight()/12 + spacing

        x2_disp = self.win.getWidth() - spacing
        y2_disp = (self.win.getHeight()/12)*2 - spacing

        box = TextBox(Point(x1_disp, y1_disp), Point(x2_disp, y2_disp))
        box.setOutline(box_color)
        box.setFill(box_color)
        
        box.setText(f'{turnColor}')
        box.setTextSize(int(self.column_width/10))
        box.setTextColor(text_color)

        return box


    def __gen_previous_move_text(self):
        spacing = self.column_width/16
        color = color_rgb(41, 44, 48)

        x1_disp = self.win.getWidth() - self.column_width + spacing
        y1_disp = self.win.getHeight()/6 + spacing*3
        x2_disp = self.win.getWidth() - spacing
        y2_disp = self.win.getHeight()/6 + self.win.getHeight()/12

        box = TextBox(Point(x1_disp, y1_disp), Point(x2_disp, y2_disp))
        box.setOutline(color)
        box.setFill(color)

        box.setText('Previous Move')
        box.setTextSize(int(self.column_width/10))
        box.setTextColor('white')

        return box


    def __gen_previous_move_display(self, uniq):
        spacing = self.column_width/16
        color = color_rgb(41, 44, 48)

        x1_disp = self.win.getWidth() - self.column_width + spacing
        y1_disp = self.win.getHeight()/4 
        x2_disp = self.win.getWidth() - spacing
        y2_disp = self.win.getHeight()/4 + self.win.getHeight()/12 - spacing*3

        box = TextBox(Point(x1_disp, y1_disp), Point(x2_disp, y2_disp))
        box.setOutline(color)
        box.setFill(color)

        box.setText(uniq)
        box.setTextSize(int(self.column_width/10))
        box.setTextColor('white')

        return box


    def __gen_forefeit_button(self):
        color = color_rgb(231, 108, 108)
        spacing = self.column_width/4

        x1_disp = self.win.getWidth() - self.column_width + spacing
        y1_disp = self.win.getHeight() - self.win.getHeight()/5 + spacing
        x2_disp = self.win.getWidth() - spacing
        y2_disp = self.win.getHeight() - spacing
        
        button = Button(Point(x1_disp, y1_disp), Point(x2_disp, y2_disp))
        button.setOutline(color)
        button.setFill(color)
        button.setText('QUIT')
        button.setTextSize(int(self.column_width/10))
        button.setTextColor('white')

        return button


    # update
    def update_num_turns_display(self, numTurns):
        box = self.__gen_num_moves_display(numTurns)        
        box.draw(self.win)
        
        self.num_turns_display.undraw()
        self.num_turns_display = box
    

    def update_turn_display(self, numTurns):
        turnColor = 'white'
        if numTurns % 2 == 0:
            turnColor = 'black'
        
        box = self.__gen_turn_display(turnColor)       
        box.draw(self.win)
        
        self.turn_display.undraw()
        self.num_turns_display = box
    
    def update_uniq_display(self, uniq):
        box = self.__gen_previous_move_display(uniq)        
        box.draw(self.win)
        
        self.previous_move_display.undraw()
        self.previous_move_display = box
    # draw
    def drawComponents(self):
        self.column_block.draw(self.win)
        

        self.num_turns_display.draw(self.win)
        self.turnText.draw(self.win)
        self.turn_display.draw(self.win)

        self.previous_move_text.draw(self.win)
        self.previous_move_display.draw(self.win)

        self.forefeit_button.draw(self.win)
        
    # get
    def getForefitButton(self):
        return self.forefeit_button
 
    

class TextBox():

    def __init__(self, p1, p2):
        self.rec = Rectangle(p1, p2);
        self.text = None

        self.leftX = self.rec.getP1().getX()
        self.rightX = self.rec.getP2().getX()

        self.topY = self.rec.getP1().getY()
        self.botY = self.rec.getP2().getY()

        self.centerPoint = self.rec.getCenter()


    def draw(self, window):
        if self.text is not None:
            self.rec.draw(window)
            self.text.draw(window)
        else:
            self.rec.draw(window)


    def undraw(self):
        if self.text == None:
            self.rec.undraw()
            
        else:
            self.rec.undraw()
            self.text.undraw()
    

    def setText(self, strLine):
        self.text = Text(self.centerPoint, strLine)
    

    def setTextSize(self, size):
        self.text.setSize(size)


    def setTextColor(self, colors):
        self.text.setTextColor(colors)


    def setOutline(self, colors):
        self.rec.setOutline(colors)


    def setFill(self, colors):
        self.rec.setFill(colors)


    def getWidth(self):
        return self.leftX - self.rightX


class Button(TextBox):

    def __init__(self, p1, p2):
        super().__init__(p1, p2)


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


   
    


