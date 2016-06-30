#!usr/bin/python3
# _*_ coding : utf-8 _*_

from turtle import Turtle, Screen
import numpy as np



class turtle2DPolygon(Turtle):

    def __init__(self, name, array2d, color):
        super(turtle2DPolygon, self).__init__()

        self.vertices = array2d
        self.name = name
        self.ht()
        self.penup()
        self.speed(0)

        self.color = color
        self.pencolor = color
        self.fillcolor = color

        self.write(self.name)
        self.draw(self.vertices)

    def draw(self, vertices):
        # General draw function. It is incredibly important to get the speed of this draw function up..
        self.goto(vertices[0])
        self.pendown()
        self.begin_fill()

        self.goto(vertices[1])
        self.goto(vertices[2])
        self.goto(vertices[0])

        self.end_fill()
        self.penup()

# -- Init screen -- 

scr = Screen()
scr.delay(0)

# -- Init tut --

poly1 = turtle2DPolygon('1', np.array([[0,0], [0,100],[100,0]]),'black')
poly2 = turtle2DPolygon('2', np.array([[-100,0],[-100, 100],[0,0]]), 'red')


def scale2d(vertices):

    scaleUp = np.array([[0,0],[0,50], [0,0]])
    
    scaledVertices = vertices + scaleUp
    return scaledVertices

def translate2d(vertices):
    return 0

def rotate2d(vertices):
    return 0

def scale3d():
    return 0

def translate3d():
    return 0

def rotate3d():
    return 0 


scr.mainloop()