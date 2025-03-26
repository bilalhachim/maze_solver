from Window import *
from Point import *
from Line import *
from Cell import *
from Maze import *
from random import *
win = Window(600, 600)
maze = Maze(3,3,20,20,40,40,win,23)
maze.solve()
win.wait_for_close()