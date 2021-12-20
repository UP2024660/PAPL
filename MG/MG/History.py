import tkinter as tk                
from tkinter import font  as tkfont 
import random
from Migration import *
from BletchleyPark import *

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, History, H_Test,  H_Revise, Migration, MedievalBritain, MB_BasicInformation, MB_JewishProsecution, MB_Diversity, MB_Attitudes, MB_QuickFireEvents, ElizabethI, NaziGermany, MakingOfAmerica, BletchleyPark, BP_R_Question1, BP_R_Question2, BP_R_Question3, BP_R_Question4, BP_R_Question5, BP_R_Question6, BP_R_Question7, BP_R_Question8, BP_R_Question9, BP_R_Question10, BP_R_Question11, BP_R_Question12, BP_R_Question13, BP_R_Question14):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class History(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        button1 = tk.Button(self, text="Test", command=lambda: controller.show_frame("H_Test"),bg="#f1c40f",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="Revise", command=lambda: controller.show_frame("H_Revise"),bg="#f1c40f",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=1,padx=5,pady=5)
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",font=(None,23,"bold"),height=2, width=11).grid(row=0,column=2,padx=5,pady=5)

class H_Test(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#f39c12")
        self.controller = controller
        button1= tk.Button(self, text="Migration",command=lambda: controller.show_frame("HTM"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button2= tk.Button(self, text="Elizabeth I",command=lambda: controller.show_frame("HTE"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button3= tk.Button(self, text="Nazi Germany",command=lambda: controller.show_frame("HTNG"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button4= tk.Button(self, text="Making of America",command=lambda: controller.show_frame("HTMoA"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button5= tk.Button(self, text="Bletchley Park",command=lambda: controller.show_frame("HTBP"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button18 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=6,column=2)

class H_Revise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        button= tk.Button(self, text="Migration",command=lambda: controller.show_frame("Migration"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Elizabeth I",command=lambda: controller.show_frame("Elizabeth"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Nazi Germany",command=lambda: controller.show_frame("NaziGermany"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button3= tk.Button(self, text="Making of America",command=lambda: controller.show_frame("MakingOfAmerica"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button4= tk.Button(self, text="Bletchley Park",command=lambda: controller.show_frame("BletchleyPark"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button6 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class ElizabethI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="ELIZABETH I", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""AGAIN, NO INFO YET....""",fg="white",bg="#f39c12")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Unit 1.1",command=lambda: controller.show_frame("H_Revise"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")           

class NaziGermany(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="NAZI GERMANY", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET, STAY TUNED....""",fg="white",bg="#f39c12")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Unit 1.1",command=lambda: controller.show_frame("H_Revise"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")
        
class MakingOfAmerica(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Making Of Britain", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""EMPTY SPACE AS OF NOW....""",fg="white",bg="#f39c12")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Medieval Britain",command=lambda: controller.show_frame("H_Revise"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")

print("History")

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()




