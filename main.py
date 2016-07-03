#!usr/bin/python3
# _*_ coding : utf-8 _*_

import Tkinter
import numpy as np

# Tkinter master object
polyview = Tkinter.Tk()

# -- Initialize essentials -- 
wh = 720
ww = 1200

whc = 720/2
wwc = 1200/2
cvn = Tkinter.Canvas(polyview, bg='white', height=wh, width=ww)
# -------------------------


class Triangle2d():

	def __init__(self, offsetx=0, offsety=0, color='black', scale=0):

		self.origo = [wwc + offsetx, whc + offsety]

		self.vert1 = [self.origo[0]-100, self.origo[1]]
		self.vert2 = [self.origo[0]+100, self.origo[1]]
		self.vert3 = [self.origo[0], self.origo[1]-100]

		self.updateverts()

		self.color = color
		self.scale = scale

		self.createpoly()


	def createpoly(self):
		self.name = cvn.create_polygon(self.vertices, fill=self.color)
		return 0

	def updateverts(self):
		self.vertices = [self.vert1[0], self.vert1[1],
						 self.vert2[0], self.vert2[1],
						 self.vert3[0], self.vert3[1]]
		print('New Position: ' + str(self.vertices))

	def updatepos(self, one=[0,0], two=[0,0], three=[0,0]):

		self.vert1 = [sum(x) for x in zip(self.vert1, one)]
		self.vert2 = [sum(x) for x in zip(self.vert2, two)]
		self.vert3 = [sum(x) for x in zip(self.vert3, three)]

		self.updateverts()

		cvn.delete(self.name)
		cvn.create_polygon(self.vertices)

	def translate(self):
		return 0

	def rotate(self):
		return 0

	def scale(self):
		return 0

# Canvas object

tri1 = Triangle2d(-100,-100)
tri2 = Triangle2d(100,100)
tri2.updatepos([-200, 0], [-200, 0], [-200, 0])
tri2.updatepos([-200, 0], [-200, 0], [-200, 0])

# packs up the Canvas object and retains the Tkinter mainloop
cvn.pack()
polyview.mainloop()

