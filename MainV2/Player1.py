from socketRecSend import SockSendReceive
from TicTacToe import TicTacToe
import random
import time

plyr = random.randint(0, 1)
ttt = TicTacToe(plyr)
srs = SockSendReceive()

while True:
    # NEED TO GET MULTIPLAYER FIGURED OUT
    # NEED Another file like this for the 2nd player
    "Order goes start server with board. Board gets taken from server. Board gets sent to tic and played for that player. Then send board to next player and repeat"
    
    # Bug ONLY ONE RUN THROUH WORKS

    # Start Server with board
    srs.rec()

    time.sleep(1)

    # Send board to ttt
    ttt.board = srs.board
    ttt.run()
    srs.board = ttt.board
    
    time.sleep(1)

    # Send board to next player
    srs.send()