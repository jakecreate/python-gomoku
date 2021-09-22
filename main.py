from game import *
from graphics import *
import buttonlist



print("""
                            [CONNECT 5]
[How To Play]: Just like the title, you need to 'Connect 5' linear dots
in order to win! The 5 dots can be horizontal, vertical, and diagonal.
You will need 1 other player to play with. You will take turns placing 
dots on the intersections of lines on the graph and compete against eachother to be 
the first one to connect 5 dots. 
""")


print('[Difficulty] --> [EASY](19x19) - [MEDIUM](9x9) - [HARD](7x7)')
# options for difficulty input = "easy" - "medium" - "hard" [Capitalization does not matter]
difficulty = input("What is your preferred difficulty (ex: 'easy'): ")
print()
player1 = Player(1, color_rgb(246, 242, 235))
player2 = Player(2, color_rgb(64, 62, 58))
winSize = 700

# window setup
win = GraphWin(title='Connect 5', width=winSize, height=winSize)
win.setBackground(color_rgb(247,215,157))
print(type(win))

# buttons setup
s_button = buttonlist.getStart(winSize)
s_button.draw(win)

while True:

    if s_button.ifPressed(win.getMouse()):
        s_button.undraw()
        break
    else:
        pass


# game setup
round = Round(win, difficulty)
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

# wait for window to close
win.getMouse()
win.close()

