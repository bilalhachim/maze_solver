from Line import *
from Point import *
class Cell:
    def __init__(self ,win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 =0
        self._x2 = 0
        self._y1 = 0
        self._y2 =  0
        self._win = win
        self.visited = False
    def get_x1(self):
        return self._x1
    def get_x2(self):
        return self._x2
    def get_y1(self):
        return self._y1
    def get_y2(self):
        return self._y2    
    def draw(self,top_left_point,bottom_right_point,fill_color):
        self._x1 = top_left_point.x
        self._x2 = bottom_right_point.x
        self._y1 = top_left_point.y
        self._y2 =  bottom_right_point.y
        top_left_point = Point(self._x1,self._y1)
        top_right_point = Point(self._x2,self._y1)
        bottom_right_point = Point( self._x2, self._y2)
        bottom_left_point = Point(self._x1,self._y2)
        if(self.has_left_wall):
            Line(top_left_point,bottom_left_point).draw(self._win,fill_color)
        else:
            Line(top_left_point,bottom_left_point).draw(self._win,"#d9d9d9")
        if(self.has_right_wall):
            Line(top_right_point,bottom_right_point).draw(self._win,fill_color)
        else:
            Line(top_right_point,bottom_right_point).draw(self._win,"#d9d9d9")
        if(self.has_top_wall):
            Line(top_left_point,top_right_point).draw(self._win,fill_color)
        else:
            Line(top_left_point,top_right_point).draw(self._win,"#d9d9d9")    
        if(self.has_bottom_wall):
            Line(bottom_left_point,bottom_right_point).draw(self._win,fill_color)
        else:
            Line(bottom_left_point,bottom_right_point).draw(self._win,"#d9d9d9")
    def draw_move(self,to_cell, canvas,undo=False):
        x1_center = (self._x1 + self._x2)/2
        y1_center = (self._y1 + self._y2)/2
        center_point1 = Point(x1_center,y1_center)
        x2_center = (to_cell.get_x1() + to_cell.get_x2())/2
        y2_center = (to_cell.get_y1() + to_cell.get_y2())/2
        center_point2 = Point(x2_center,y2_center)
        if undo:
            Line(center_point1,center_point2).draw(canvas,"gray")
        else:
            Line(center_point1,center_point2).draw(canvas,"red")
   


        