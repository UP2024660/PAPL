import tkinter as tk                
from tkinter import font  as tkfont 
import random


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,EPQ,EPQ_Test,EPQ_Revise,Chapter1):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class EPQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#8e44ad")
        button1 = tk.Button(self, text="Test", command=lambda: controller.show_frame("EPQ_Test"),bg="#9b59b6",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="Revise", command=lambda: controller.show_frame("EPQ_Revise"),bg="#9b59b6",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=1,padx=5,pady=5)
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#9b59b6",font=(None,23,"bold"),height=2, width=11).grid(row=0,column=2,padx=5,pady=5)

class EPQ_Test(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#8e44ad")
        self.controller = controller
        button1= tk.Button(self, text="Chapter 1",command=lambda: controller.show_frame("Chapter1"),fg="white",bg="#9b59b6",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button6 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#9b59b6",width=20,font=(None, 17, "bold")).grid(row=6,column=2)


class EPQ_Revise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#8e44ad")
        button1= tk.Button(self, text="Chapter 1",command=lambda: controller.show_frame("Chapter1"),fg="white",bg="#9b59b6",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button16 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#9b59b6",width=20,font=(None, 17, "bold")).grid(row=5,column=2)


class Chapter1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#8e44ad")
        label = tk.Label(self, text="Chapter 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#9b59b6",fg="white")
        button.pack()



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()




