#!/usr/bin/env python

from Tkinter import *
import tkMessageBox

f = open('/Users/shaolei/Desktop/3rd year/side proj/python/testuse.txt','r')
print f.read()
f.close()

#or
with open('/Users/shaolei/Desktop/3rd year/side proj/python/testuse.txt','r') as f:
	for line in f.readlines():
		print(line.strip()) #get rid of new line char

#'rb' is for reading binary files like image or video
#'w' write file
#'w+' create file if it doesn't exist
#'r+' read and write
#'a' append
#'a+' create file it it doens't exist

#f = open('/Users/shaolei/Desktop/3rd year/side proj/python/testuse2.txt','a+')
#f.write('hello world')
#f.close()

#GUI
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()#easy layout
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()