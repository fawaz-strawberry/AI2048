"""
This python file is in charge of just running a regular game with 2048 using only
user input. No AI involved here
"""
# import random
from game import GameBoard
from pynput.keyboard import Key, Listener

mainBoard = GameBoard()
mainBoard.displayBoard()

def on_release(key):
    if key == Key.up:
        mainBoard.slideUp() 
        
    if key == Key.left:
        mainBoard.slideLeft()
    if key == Key.right:
        mainBoard.slideRight()
    if key == Key.down:
        mainBoard.slideDown()

    mainBoard.displayBoard()
    if(mainBoard.checkBoard() == False):
        print("Game Over")
        exit()


# Collect events until released
with Listener(
        on_release=on_release) as listener:
    listener.join()