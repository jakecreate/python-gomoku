from package.graphics import *
from package.game import *

#  from game import *
# from graphics import *
# import buttonlist

# [Difficulty] --> [EASY](19x19) - [MEDIUM](9x9) - [HARD](7x7)
# options for difficulty input = "easy" - "medium" - "hard" [Capitalization does not matter]
difficulty = 'easy'

# window size
winSize = 750
column_width = winSize/5

# colors
window_color = color_rgb(247,215,157)
column_color =color_rgb(64,62,58) 
p1_color = color_rgb(64,62,58) # black
p2_color = color_rgb(246, 242, 235) # white

# window setup
win = GraphWin(title='Connect 5', width=winSize, height=winSize)
win.setBackground(window_color)                                                            

# players
player1 = Player(1, p1_color)
player2 = Player(2, p2_color)

# game setup
round = Round(win, winSize, difficulty)
round.drawLines()
dotRadius = round.getSpacing()/3
players = [player1, player2]

# round
while round.isRunning():

    # find player
    player = players[round.getTurns() % 2]
    print(f"[Turn#{round.getTurns() + 1}] Player#{players.index(player) + 1}'s turn! [{player.getColor()}]")
    print()

    # get mouse coords
    mouse = win.getMouse()
    xCord = mouse.getX()
    yCord = mouse.getY()

    # check if mouse in on board
    if xCord < winSize:
        # find slot
        slot = round.findSlot(xCord, yCord)

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

        # has five connected
        if round.hasFiveConnected(slot):
            print(f"Player#{player.getId()} Wins! Click anywhere to END")
            round.end()
            
        # if full
        if round.isFull():
            round.end()
    else:
        # have a set of buttons
        # if conds of buttons
        pass

# wait for window to close
win.getMouse()
win.close()

