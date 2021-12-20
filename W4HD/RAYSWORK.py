import tkinter as tk 
from tkinter import font  as tkfont 
import random
from choose import *
from slider import *
from sliderif import *
from bestchoice import *
from results import *


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

       
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,choose,slider, sliderif, bestchoice, results):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button = tk.Button(self, text="Start", command=lambda: controller.show_frame("choose"),bg="#3498db",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=1,column=1,padx=5,pady=5)#bg of frame is #2980b9
        button2 = tk.Button(self, text="Results", command=lambda: controller.show_frame("results"),bg="#3498db",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=1,column=2,padx=5,pady=5)#bg of frame is #2980b9
        


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
 




