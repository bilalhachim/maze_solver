from Cell import*
from time import *
import random
class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win,seed = None):
        if seed != None : 
            random.seed(seed)
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells =[[None for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        self._create_cells()

    def _create_cells(self):
       
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j] = Cell(self._win)         
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
        self._break_entrance_and_exit()
        self._draw_cell(0,0)
        self._draw_cell(self._num_rows-1,self._num_cols-1)
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    def _draw_cell(self, i, j):
            top_left_x = self._x1 + (i * self._cell_size_x)
            top_left_y = self._y1 + (j * self._cell_size_y )
            bottom_right_x = top_left_x +self._cell_size_x
            bottom_right_y = top_left_y + self._cell_size_y
            self._cells[i][j].draw(Point(top_left_x,top_left_y),Point(bottom_right_x,bottom_right_y),"black")
            self._animate()
            
    def _animate(self):
        self._win.redraw()
        sleep(0.03)
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall = False
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            lst = []
            if  ((i-1>=0 and i-1 <= self._num_cols-2) and ( j>=0 and  j < self._num_rows)) and ( not self._cells[i-1][j].visited):
                lst.append((i-1,j,1))
            if  ((j-1>=0 and j-1 <= self._num_rows-2) and ( i>=0 and  i < self._num_cols)) and ( not self._cells[i][j-1].visited):
                lst.append((i,j-1,2))   
            if  ((i+1>=1 and i+1<self._num_cols) and ( j>=0 and  j < self._num_rows)) and ( not self._cells[i+1][j].visited):
                lst.append((i+1,j,3))  
            if  ((j+1>=1 and j+1<self._num_rows) and ( i>=0 and  i < self._num_cols)) and ( not self._cells[i][j+1].visited):
                lst.append((i,j+1,4))   

            if len(lst) == 0:
                return    
            else:
                wall_to_break = lst[random.randrange(0,len(lst))]
                if wall_to_break[2]==1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                if wall_to_break[2]==2:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall=False
                if wall_to_break[2]==3:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                if wall_to_break[2]==4:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False

                self._draw_cell(i,j)
                self._break_walls_r(wall_to_break[0],wall_to_break[1])
    def _reset_cells_visited(self):
           for i in range(self._num_cols):
            for j in range(self._num_rows):
               if  self._cells[i][j].visited == True:
                   self._cells[i][j].visited = False 
    def solve(self):
        self._solve_r(0,0)
    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j]== self._cells[self._num_rows-1][self._num_cols-1]:
            return True
        
        if ((i-1>=0 and i-1 <= self._num_cols-2) and ( j>=0 and  j < self._num_rows))  and self._cells[i][j].has_left_wall == False and self._cells[i-1][j].visited==False:
            self._cells[i][j].draw_move(self._cells[i-1][j],self._win)
            if self._solve_r(i-1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j],self._win,True)

        if ((j-1>=0 and j-1 <= self._num_rows-2) and ( i>=0 and  i < self._num_cols))and self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited==False:
            self._cells[i][j].draw_move(self._cells[i][j-1],self._win)
            if self._solve_r(i,j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1],self._win,True)         

        if((i+1>=1 and i+1<self._num_cols) and ( j>=0 and  j < self._num_rows))  and self._cells[i][j].has_right_wall == False and self._cells[i+1][j].visited==False:
            self._cells[i][j].draw_move(self._cells[i+1][j],self._win)
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j],self._win,True)   

        if ((j+1>=1 and j+1<self._num_rows) and ( i>=0 and  i < self._num_cols)) and self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].visited==False:
            self._cells[i][j].draw_move(self._cells[i][j+1],self._win)
            if self._solve_r(i,j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1],self._win,True)    
        return False                       