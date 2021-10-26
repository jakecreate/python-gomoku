from modules.graphics import *
from modules.game import *
from modules.gui import *
import time

# conditions
print("hello")
difficulty = 'test' # options for difficulty input = "easy"(19x19) - "medium"(9x9) - "hard"(7x7) [Capitalization does not matter] 
winSize = 750 # window -- size range from 250 to 900 --
gui_width = winSize/5
window_color = color_rgb(247,215,157)
column_color =color_rgb(58,61,67) 
p1_color = color_rgb(64,62,58) # black
p2_color = color_rgb(246, 242, 235) # white

# window setup
win = GraphWin(title='Gomoku', width=winSize + gui_width, height=winSize)
win.setBackground(window_color)   
# players
player1 = Player(1, p1_color)
player2 = Player(2, p2_color)

# gui setup
gui = Column(win, gui_width, column_color)
gui.drawComponents()

# game setup
round = Round(win, winSize, difficulty)
round.drawLines()
round.drawLabels()
dotRadius = round.getSpacing()/3
players = [player1, player2]

#draw text lines

# for x in range(8):
#     line = Line(Point(0,(x + 1)*winSize/12), Point(win.getWidth(),(x + 1)*winSize/12))
#     line.setFill('white')
#     l
#ine.draw(win)
# round
i = 0
previous = int(time.time())%10
while round.isRunning():

    
    # find player
    mouse = win.checkMouse()
    if mouse is not None:
        player = players[round.getTurns() % 2]
        # print(f"[Turn#{round.getTurns() + 1}] Player#{players.index(player) + 1}'s turn! [{player.getColor()}]")
        # get mouse coords
        xCord = mouse.getX()
        yCord = mouse.getY()
        # check if mouse in on board
        if xCord < winSize:

            # find slot
            slot = round.findSlot(xCord, yCord)
            print(slot.getUniq())
            if slot.isOccupied():

                print("occupied")

            else:

                # draw dot on a specific slot
                dot = Circle(Point(slot.getX(), slot.getY()), dotRadius) 
                dot.setOutline(player.getColor())
                dot.setFill(player.getColor())

                slot.occupy(player)
                slot.addDotToSlot(dot)
                dot.draw(win)
                
                round.nextTurn()

                # gui update 1
                gui.update_num_turns_display(round.getTurns())
                gui.update_turn_display(round.getTurns())
                gui.update_uniq_display(slot.getUniq())
                # gui.update_
                
            # has five connected
            if round.hasFiveConnected(slot):
                round.end()

            # if full
            if round.isFull():
                round.end()

        else:
            # have a set of buttons
            if gui.getForefitButton().ifPressed(mouse):
                round.end()
            # if conds of buttons
            pass

    else:
        print(9 - int(time.time())%10)
    
    win.update()
    
# wait for window to close
win.getMouse()
win.close()

