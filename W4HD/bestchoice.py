import tkinter as tk
import random
from tkinter import font as tkfont
from choose import *
from slider import *
from sliderif import *
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
        for F in (StartPage,choose,slider,sliderif,besthoice,results):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class bestchoice(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller= controller
        label=tk.Label(self, text="Your Best Choice is....?", font=controller.title_font,fg="white",bg="#2980b9").grid(row=0,column=0,padx=5,pady=5)
        button1 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("sliderif"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=7,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="StartPage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=7,column=3,padx=5,pady=5)
  



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    print("Main")


