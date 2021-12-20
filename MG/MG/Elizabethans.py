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
        for F in (StartPage, History, Elizabeth, ElizabethGov, Catholics, E_Daily_Lives, Merry_England, The_Wider_World, EGOV_Elizabeth,EGOV_PC,EGOV_EoE, EGOV_PO, EGOV_LGaP, EGOV_QFE,Cath_PR, Cath_Links, Cath_Plots, Cath_Spy, Cath_Mary, Cath_Armada, Cath_War, Cath_QFE,ED_SC, ED_FL, ED_P, ED_QFE,ME_T, ME_PC, ME_W, ME_QFE,WW_I, WW_R, WW_T, WW_QFE):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class Elizabeth(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        button= tk.Button(self, text= "Elizabeth and her Government",command=lambda: controller.show_frame("ElizabethGov"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Catholics",command=lambda: controller.show_frame("Catholics"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Daily Lives",command=lambda: controller.show_frame("E_Daily_Lives"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=2)
        button3= tk.Button(self, text="Popular Culture (Merry England)",command=lambda: controller.show_frame("Merry_England"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=0)
        button4= tk.Button(self, text="The Wider World",command=lambda: controller.show_frame("The_Wider_World"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=1)

        button6 = tk.Button(self, text="Revise page",command=lambda: controller.show_frame("H_Revise"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=2)

class ElizabethGov(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        button= tk.Button(self, text= "Elizabeth",command=lambda: controller.show_frame("EGOV_Elizabeth"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Privy Council ",command=lambda: controller.show_frame("EGOV_PC"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Earl of Essex",command=lambda: controller.show_frame("EGOV_EoE"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=2)
        button3= tk.Button(self, text="Puritan Opposition",command=lambda: controller.show_frame("EGOV_PO"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=0)
        button4= tk.Button(self, text="Local Government and Propaganda",command=lambda: controller.show_frame("EGOV_LGaP"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=1)
        button5= tk.Button(self, text="Quick Fire events",command=lambda: controller.show_frame("EGOV_QFE"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=2)
        button6 = tk.Button(self, text="The Elizabethans",command=lambda: controller.show_frame("Elizabeth"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=2)

class EGOV_Elizabeth(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Queen Elizabeth I ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""Queen Elizabeth I""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Elizabeth and Government",command=lambda: controller.show_frame("ElizabethGov"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class EGOV_PC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="The Privy Council", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""The Privy Council""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Elizabeth and Government",command=lambda: controller.show_frame("ElizabethGov"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class EGOV_EoE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="The Rebellion of the Earl of Essex", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""REBELLION""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Elizabeth and Government",command=lambda: controller.show_frame("ElizabethGov"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class EGOV_PO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Puritan Opposition", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""PURITANS""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Elizabeth and Government",command=lambda: controller.show_frame("ElizabethGov"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class EGOV_LGaP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Local Government and Propaganda ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""PROPAGANDA""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Elizabeth and Government",command=lambda: controller.show_frame("ElizabethGov"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class EGOV_QFE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Quick Fire Events", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""FACTS""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Elizabeth and Government",command=lambda: controller.show_frame("ElizabethGov"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           


class Catholics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        button= tk.Button(self, text= "Enforcement of Protestant religion",command=lambda: controller.show_frame("Cath_PR"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Catholic Links abroad",command=lambda: controller.show_frame("Cath_Links"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Plots against Elizabeth",command=lambda: controller.show_frame("Cath_Plots"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=2)
        button3= tk.Button(self, text="Elizabethan Spy Network",command=lambda: controller.show_frame("Cath_Spy"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=0)
        button4= tk.Button(self, text="Mary Queen of Scots",command=lambda: controller.show_frame("Cath_Mary"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=1)
        button5= tk.Button(self, text="The Armada",command=lambda: controller.show_frame("Cath_Armada"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=0)
        button6= tk.Button(self, text="War with Spain",command=lambda: controller.show_frame("Cath_War"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=1)
        button7= tk.Button(self, text="Quick Fire events",command=lambda: controller.show_frame("Cath_QFE"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=2)
        button8 = tk.Button(self, text="The Elizabethans",command=lambda: controller.show_frame("Elizabeth"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=0)
        button9 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=2)

class Cath_PR(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Enforcement of the Protestant Religion", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""PROTESTANTS VS CATHOLICS """,fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Catholics",command=lambda: controller.show_frame("Catholics"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class Cath_Links(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Links Abroad", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""SPAIN/ETC""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Catholics",command=lambda: controller.show_frame("Catholics"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class Cath_Plots(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Plots against Queen Elizabeth", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""PLOTS """,fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Catholics",command=lambda: controller.show_frame("Catholics"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class Cath_Spy(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Spy Network", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""Spies in England""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Catholics",command=lambda: controller.show_frame("Catholics"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class Cath_Mary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Mary Queen of Scots", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""Queen Mary""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Catholics",command=lambda: controller.show_frame("Catholics"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class Cath_Armada(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="The Spanish Armada", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""ARMADA """,fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Catolics",command=lambda: controller.show_frame("Catholics"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class Cath_War(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="War with Spain", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""WAR""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Catholics",command=lambda: controller.show_frame("Catholics"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class Cath_QFE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Quick Fire Events", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""FACTS""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Catholics",command=lambda: controller.show_frame("Catholics"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           


class E_Daily_Lives(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        button= tk.Button(self, text= "The Social Contrasts",command=lambda: controller.show_frame("ED_SC"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Family Life",command=lambda: controller.show_frame("ED_FL"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Poverty",command=lambda: controller.show_frame("ED_P"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=2)
        button5= tk.Button(self, text="Quick Fire events",command=lambda: controller.show_frame("ED_QFE"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=2)
        button6 = tk.Button(self, text="The Elizabethans",command=lambda: controller.show_frame("Elizabeth"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=2)

class ED_SC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="The Social Contrast between the Rich, Middling and the Poor", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""It was bad""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Daily Lives",command=lambda: controller.show_frame("E_Daily_Lives"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class ED_FL(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Family Life", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""Family Lives""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Daily Lives",command=lambda: controller.show_frame("E_Daily_Lives"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class ED_P(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Poverty", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""'TWAS BAD""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Daily ",command=lambda: controller.show_frame("ElizabethGov"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class ED_QFE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Quick Fire Events", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""FACTS""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Daily Lives",command=lambda: controller.show_frame("E_Daily_Lives"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class Merry_England(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        button= tk.Button(self, text= "Theatres and their Opponents",command=lambda: controller.show_frame("ME_T"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="The Puritan attack on Pop Culture",command=lambda: controller.show_frame("ME_PC"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="The Persecution of Witches",command=lambda: controller.show_frame("ME_W"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=2)
        button7= tk.Button(self, text="Quick Fire events",command=lambda: controller.show_frame("ME_QFE"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=2)
        button8 = tk.Button(self, text="The Elizabethans",command=lambda: controller.show_frame("Elizabeth"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=0)
        button9 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=2)

class ME_T(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Theatres and their Opponents", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""Puritans""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Merry_England",command=lambda: controller.show_frame("Merry_England"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class ME_PC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Puritan Attack On Popular Culture", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""SPAIN/ETC""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Merry England",command=lambda: controller.show_frame("Merry_England"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class ME_W(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="The Persecution of Witches", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""PLOTS """,fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Merry England",command=lambda: controller.show_frame("Merry_England"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class ME_QFE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Quick Fire Events", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""FACTS""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Merry England",command=lambda: controller.show_frame("Merry_England"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class The_Wider_World(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        button= tk.Button(self, text= "Imperial Ambition",command=lambda: controller.show_frame("WW_I"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Roanoke",command=lambda: controller.show_frame("WW_R"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Trade",command=lambda: controller.show_frame("WW_T"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=0,column=2)
        button7= tk.Button(self, text="Quick Fire events",command=lambda: controller.show_frame("WW_QFE"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=1,column=2)
        button8 = tk.Button(self, text="The Elizabethans",command=lambda: controller.show_frame("Elizabeth"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=0)
        button9 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None, 17, "bold")).grid(row=3,column=2)

class WW_I(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Imperial Ambition : Motives and Achievements of Elizabethan Explorers", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""EXPLORATION""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Merry_England",command=lambda: controller.show_frame("Merry_England"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class WW_R(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="ROANOKE", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""FAILURE""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="The Wider World",command=lambda: controller.show_frame("The_Wider_World"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class WW_T(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Trade with the east, first contacts with India", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""TRADE """,fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="The Wider World",command=lambda: controller.show_frame("The_Wider_World"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           

class WW_QFE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Quick Fire Events", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""FACTS""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="The Wider World",command=lambda: controller.show_frame("The_Wider_World"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=25,font=(None,20,"bold")).pack(side="top")           


