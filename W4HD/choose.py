import tkinter as tk
import random
from tkinter import font as tkfont

from slider import *

from sliderif import *



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

       
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,choose,slider,sliderif,bestchoice,results):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class choose(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller= controller
        label=tk.Label(self, text="Help Me Choose?", font=controller.title_font,fg="white",bg="#2980b9").grid(row=0,column=0,padx=5,pady=5)
        label1=tk.Label(self,text="X and Y.example",font=controller.title_font,fg="white",bg="#2980b9").grid(row=2,column=0,padx=5,pady=5)
        label1=tk.Label(self,text="A and B.example",font=controller.title_font,fg="white",bg="#2980b9").grid(row=4,column=0,padx=5,pady=5)


        def decisionA():
          print("Chose X and Y.example")
        def decisionB():
          print("Chose A and B.example")

        button=tk.Button(self, text='X and Y.example', command= decisionA,fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=20)
        button.grid(row=2,column=2,padx=5,pady=5)
        button1=tk.Button(self, text='A and B.example', command=decisionB,fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=20)
        button1.grid(row=4,column=2,padx=5,pady=5)
        button2 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=7,column=0,padx=5,pady=5)
        button3 = tk.Button(self, text="Next Page",command=lambda: controller.show_frame("slider"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=7,column=3,padx=5,pady=5)
 



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    print("Main")


