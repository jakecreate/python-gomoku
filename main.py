from modules.graphics import *
from modules.game import *
from modules.gui import *
import time
import math
# interchangable conditions
print("hello")
difficulty = 'test' # options for difficulty input = "easy"(19x19) - "medium"(9x9) - "hard"(7x7) [Capitalization does not matter] 
winSize = 750 # window -- size range from 250 to 900 --
gui_width = winSize/5
amountTime = 5*60 # seconds
window_color = color_rgb(247,215,157)
column_color =color_rgb(58,61,67) 


# window setup
win = GraphWin(title='Gomoku', width=winSize + gui_width, height=winSize)
win.setBackground(window_color) 

# time setup
start_time = time.time() # seconds
time_gone = 0 # seconds
time_statement = ""
# players
player1 = Player(1, "black")
player2 = Player(2, "white")

# gui setup
gui = Column(win, gui_width, column_color, amountTime)
gui.drawComponents()

# game setup
round = Round(gui, win, winSize, difficulty)
round.drawComponents()

dotRadius = round.getSpacing()/3
players = [player1, player2]
player = None
# draw text lines
# for x in range(8):
#     line = Line(Point(0,(x + 1)*winSize/12), Point(win.getWidth(),(x + 1)*winSize/12))
#     line.setFill('white')
#     line.draw(win)

while round.isRunning() or gui.isRunning():
    # find player
    mouse = win.checkMouse()
    if mouse is not None:
        
        # get mouse coords
        xCord = mouse.getX()
        yCord = mouse.getY()
        # check if mouse in on board
        if xCord < winSize and round.isRunning():
            
            # find slot
            slot = round.findSlot(xCord, yCord)
            print(slot.getUniq())

            if slot.isOccupied():

                print("occupied")

            else:
                player = players[round.getTurns() % 2]

                # draw dot on a specific slot
                dot = Circle(Point(slot.getX(), slot.getY()), dotRadius) 
                dot.setOutline(player.getColor())
                dot.setFill(player.getColor())

                slot.occupy(player)
                slot.addDotToSlot(dot)
                dot.draw(win)
                
                round.nextTurn()

                # gui update
                gui.update_num_turns_display(round.getTurns())
                gui.update_turn_display(round.getTurns())
                gui.update_uniq_display(slot.getUniq())
                
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
                gui.end()
            
            if gui.getRestartButton().ifPressed(mouse):
                round.restart()
                player = None
            
            

    
    #time display / check if 1 second has passed
    if time.time() - start_time >= 1 and player is not None and round.isRunning():
        # change current player time
        temp_player_id = players[players.index(player) - 1].getOccupantId()
        gui.setTime(temp_player_id, gui.getTime(temp_player_id) - 1)
        gui.update_timer_display(temp_player_id)

        # update previous time
        start_time = time.time()

        # ran out of time
        if gui.getTime(temp_player_id) == 0:
            if temp_player_id == 1:
                print("Black wins!")
            else:
                print("White wins!")
            
            round.end()
    
    
       
    
        
        
    win.update()
    
# wait for window to close
win.close()

