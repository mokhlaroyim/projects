#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image as PImage, ImageTk as PImageTK 
from tkinter import *
from tkinter.ttk import *
from python import *

# this class inherits Frame widget from tkinter
class Example(Frame):
    # create constructor
    def __init__(self): 
        super().__init__() 
        self.initUI() # automatically call the initUI function 
    
    #initUI funtion    
    def initUI(self):
        self.master.title("Main") # the title of the Window 
        self.style = Style().configure("TFrame", background="#333"), # Query the default value of the specified option in style
        self.pack(fill=BOTH, expand=True) # make the widget fill the entire parent and enable expand 
        
        topFrame = Frame(self)# create the self Frame
        topFrame.pack(side=TOP)# pack widgets side by side, in our case TOP

        bottomFrame = Frame(self)# create the self Frame
        bottomFrame.pack(side=TOP, pady=50)# pack widgets at top with padding y=50

        image_0 = PhotoImage(file="woman_1.png")  # read file 
        #create Button, specify parameters and in case of click call open_dialog function
        btn_open_dialog = Button(self, 
                                 text = "Captain Marvel", 
                                 command = lambda: self.open_dialog("woman_1.png"), 
                                 compound = TOP, 
                                 image = image_0,
                                 cursor='hand2')
        btn_open_dialog.image = image_0
        btn_open_dialog.pack(in_=topFrame, side=LEFT, padx=15) # pack widgets at top left with padding x=15 

        image_1 = PhotoImage(file = "thor.png")  # read file 
        #create Button, specify parameters and in case of click call open_dialog function
        btn_open_dialog = Button(self, 
                                 text = "Thor", 
                                 command = lambda: self.open_dialog("thor.png"), 
                                 compound = TOP, 
                                 image = image_1,  
                                 cursor='hand2')
        btn_open_dialog.image = image_1
        btn_open_dialog.pack(in_=topFrame, side=LEFT, padx=15)# pack widgets at top left with padding x=15 

        image_2 = PhotoImage(file = "dr_strange.png") # read file 
        #create Button, specify parameters and in case of click call open_dialog function
        btn_open_dialog = Button(self, 
                                 text = "Dr. Strange", 
                                 command = lambda: self.open_dialog("dr_strange.png"),
                                 compound = TOP, 
                                 image = image_2, 
                                 cursor='hand2')
        btn_open_dialog.image = image_2
        btn_open_dialog.pack(in_=topFrame, side=LEFT, padx=15)# pack widgets at top left with padding x=15 

        image_3 = PhotoImage(file = "black_widow.png") # read file 
        #create Button, specify parameters and in case of click call open_dialog function
        btn_open_dialog = Button(self, 
                                 text = "Black Widow", 
                                 command = lambda: self.open_dialog("black_widow.png"),
                                 compound = TOP, 
                                 image = image_3,  
                                 cursor='hand2')
        btn_open_dialog.image = image_3
        btn_open_dialog.pack(in_=topFrame, side=LEFT, padx=15)# pack widgets at top left with padding x=15 
        
        #display text with specified font & place it in the bottom of the Frame
        text_down = Label(self, 
                          text="Choose Character", 
                          font=('Verdana', 30))
        text_down.pack(in_=bottomFrame)

        text_up = Label(self, 
                        text= "1. Click on Image", 
                        font=('Verdana', 15))
        text_up.pack(in_=bottomFrame)

        text_up = Label(self, 
                         text="2. When camera is on, Press on 'Space'", 
                         font=('Verdana', 15))
        text_up.pack(in_=bottomFrame)

        text_up = Label(self, 
                        text = "3. After 'Space', Press on 'Esc'", 
                        font =('Verdana', 15))
        text_up.pack(in_=bottomFrame)
    
    #open_dialog function which takes one parameter 
    def open_dialog(self, pic): 
        capture_img(pic) #call funtion from python.py
    
def main():
    root = Tk() #create instance of class Tk of module tkiner  
    root.geometry("990x550+100+50") #specify the dimention 990x550 with x=100 and y=50
    root.resizable(False, False) # disable resize of Window

    app = Example() # create the instance of class Example
    
    root.mainloop() #keep Windon open

if __name__ == '__main__': 
    main()


# In[ ]:




