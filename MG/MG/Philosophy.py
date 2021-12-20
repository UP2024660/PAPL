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
        for F in (StartPage, Philosophy, P_Test,  P_Revise, TChristianBeliefs, TChristianPractices, TChristianTeachings, TIslamBeliefs, TIslamTeachings, TIslamPractices, TB, TC, TD, TE, RChristianBeliefs, RChristianPractices, RChristianTeachings, RIslamBeliefs, RIslamTeachings, RIslamPractices, RB, RC, RD, RE, RNaturesOfGod, RNOG_Omnipotence, RNOG_Omnibenevolence, RNOG_Just):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class Philosophy(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#00796B")
        button1 = tk.Button(self, text="Test", command=lambda: controller.show_frame("P_Test"),bg="#009688",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="Revise", command=lambda: controller.show_frame("P_Revise"),bg="#009688",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=1,padx=5,pady=5)
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#009688",font=(None,23,"bold"),height=2, width=11).grid(row=0,column=2,padx=5,pady=5)

class P_Test(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller
        label1 = tk.Label(self, text = "Paper 1", fg = "white", bg = "#00796B", font = (None, 18, "bold")).grid(row = 0, column = 0)
        label2 = tk.Label(self, text = "Paper 2", fg = "white", bg = "#00796B", font = (None, 18, "bold")).grid(row = 3, column = 0)
        
        button1= tk.Button(self, text="Christian Beliefs",command=lambda: controller.show_frame("TChristianBeliefs"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=1,column=0)
        button2= tk.Button(self, text="Christian Teachings",command=lambda: controller.show_frame("TChristianTeachings"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=1,column=1)
        button3= tk.Button(self, text="Christian Practices",command=lambda: controller.show_frame("TChristianPractices"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=1,column=2)
        button4= tk.Button(self, text="Islamic Beliefs",command=lambda: controller.show_frame("TIslamBeliefs"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=2,column=0)
        button5= tk.Button(self, text="Islamic Teachings",command=lambda: controller.show_frame("TIslamTeachings"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=2,column=1)
        button6= tk.Button(self, text="Islamic Practices",command=lambda: controller.show_frame("TIslamPractices"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=2,column=2)
        button7= tk.Button(self, text="B- Life",command=lambda: controller.show_frame("TB"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=4,column=0)
        button8= tk.Button(self, text="C- Existence of God and Revelation",command=lambda: controller.show_frame("TC"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=4,column=1)
        button9= tk.Button(self, text="D- Peace and Conflict",command=lambda: controller.show_frame("TD"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=5,column=0)
        button10= tk.Button(self, text="E- Crime and Punishment",command=lambda: controller.show_frame("TE"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=5,column=1)


        
        button18 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=2)
class TChristianBeliefs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#00796B")
        label = tk.Label(self, text="God", font=controller.title_font,fg="white", bg="#00796B").grid(row=0,column=0)
        button= tk.Button(self, text= "Natures of God",command=lambda: controller.show_frame("TNaturesOfGod"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button1= tk.Button(self, text="Creation",command=lambda: controller.show_frame("TCreation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button2= tk.Button(self, text="Afterlife",command=lambda: controller.show_frame("TAfterlife"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        label1 = tk.Label(self, text="Jesus", font=controller.title_font,fg="white", bg="#00796B").grid(row=2,column=0)
        button3= tk.Button(self, text="Incarnation",command=lambda: controller.show_frame("TIncarnation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button4= tk.Button(self, text="Crucifixion",command=lambda: controller.show_frame("TCrucifixion"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button6 = tk.Button(self, text="Resurrection",command=lambda: controller.show_frame("TReserrection"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=2)
        button7 = tk.Button(self, text="Ascension",command=lambda: controller.show_frame("TAscension"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=0)
        button8= tk.Button(self, text="Sin",command=lambda: controller.show_frame("Sin"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=1)
        button9= tk.Button(self, text="Salvation",command=lambda: controller.show_frame("TSalvation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=2)
        label2 = tk.Label(self, text="Practises", font=controller.title_font,fg="white", bg="#00796B").grid(row=5,column=0)
        button10 = tk.Button(self, text="Worship Form",command=lambda: controller.show_frame("TWorship Form"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=0)
        button11 = tk.Button(self, text="Prayer",command=lambda: controller.show_frame("TPrayer"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=1)
        button12 = tk.Button(self, text="Sacraments",command=lambda: controller.show_frame("TSacraments"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=2)
        button13 = tk.Button(self, text="Pilgrimage",command=lambda: controller.show_frame("TPilgrimage"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=7,column=0)
        button14 = tk.Button(self, text="Celebrations",command=lambda: controller.show_frame("TCelebrations"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=7,column=1)
        button15 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#009688",font=(None,23,"bold"),height=2, width=11).grid(row=8,column=2,padx=5,pady=5)


class TChristianPractices(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#00796B")
        label = tk.Label(self, text="Empty", font=controller.title_font,fg="white", bg="#00796B").grid(row=0,column=0)
        button= tk.Button(self, text= "Empty",command=lambda: controller.show_frame("NaturesOfGod"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button1= tk.Button(self, text="Empty",command=lambda: controller.show_frame("Creation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button2= tk.Button(self, text="Empty",command=lambda: controller.show_frame("Afterlife"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        label1 = tk.Label(self, text="Empty", font=controller.title_font,fg="white", bg="#00796B").grid(row=2,column=0)
        button3= tk.Button(self, text="Empty",command=lambda: controller.show_frame("Incarnation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button4= tk.Button(self, text="Empty",command=lambda: controller.show_frame("Crucifixion"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button6 = tk.Button(self, text="Empty",command=lambda: controller.show_frame("Reserrection"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=2)
        button7 = tk.Button(self, text="Empty",command=lambda: controller.show_frame("Ascension"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=0)
        button8= tk.Button(self, text="Empty",command=lambda: controller.show_frame("Sin"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=1)
        button9= tk.Button(self, text="Empty",command=lambda: controller.show_frame("Salvation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=2)
        label2 = tk.Label(self, text="Empty", font=controller.title_font,fg="white", bg="#00796B").grid(row=5,column=0)
        button10 = tk.Button(self, text="Empty",command=lambda: controller.show_frame("Worship Form"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=0)
        button11 = tk.Button(self, text="Empty",command=lambda: controller.show_frame("Prayer"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=1)
        button12 = tk.Button(self, text="Empty",command=lambda: controller.show_frame("Sacraments"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=2)
        button13 = tk.Button(self, text="Empty",command=lambda: controller.show_frame("Pilgrimage"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=7,column=0)
        button14 = tk.Button(self, text="Empty",command=lambda: controller.show_frame("Celebrations"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=7,column=1)
        button15 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#009688",font=(None,23,"bold"),height=2, width=11).grid(row=8,column=2,padx=5,pady=5)
        

class TChristianTeachings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#00796B")
        label = tk.Label(self, text="God", font=controller.title_font,fg="white", bg="#00796B").grid(row=0,column=0)
        button= tk.Button(self, text= "Natures of God",command=lambda: controller.show_frame("NaturesOfGodT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button1= tk.Button(self, text="Creation",command=lambda: controller.show_frame("CreationT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button2= tk.Button(self, text="Afterlife",command=lambda: controller.show_frame("AfterlifeT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        label1 = tk.Label(self, text="Jesus", font=controller.title_font,fg="white", bg="#00796B").grid(row=2,column=0)
        button3= tk.Button(self, text="Incarnation",command=lambda: controller.show_frame("IncarnationT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button4= tk.Button(self, text="Crucifixion",command=lambda: controller.show_frame("CrucifixionT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button6 = tk.Button(self, text="Resurrection",command=lambda: controller.show_frame("ResurrectionT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=2)
        button7 = tk.Button(self, text="Ascension",command=lambda: controller.show_frame("AscensionT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=0)
        button8= tk.Button(self, text="Sin",command=lambda: controller.show_frame("SinT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=1)
        button9= tk.Button(self, text="Salvation",command=lambda: controller.show_frame("SalvationT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=2)
        label2 = tk.Label(self, text="Practises", font=controller.title_font,fg="white", bg="#00796B").grid(row=5,column=0)
        button10 = tk.Button(self, text="Worship Form",command=lambda: controller.show_frame("Worship FormT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=0)
        button11 = tk.Button(self, text="Prayer",command=lambda: controller.show_frame("PrayerT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=1)
        button12 = tk.Button(self, text="Sacraments",command=lambda: controller.show_frame("SacramentsT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=2)
        button13 = tk.Button(self, text="Pilgrimage",command=lambda: controller.show_frame("PilgrimageT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=7,column=0)
        button14 = tk.Button(self, text="Celebrations",command=lambda: controller.show_frame("CelebrationsT"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=7,column=1)
        button15 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#009688",font=(None,23,"bold"),height=2, width=11).grid(row=8,column=2,padx=5,pady=5)
class TIslamBeliefs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class TIslamTeachings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class TIslamPractices(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class TB(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class TC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class TD(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class TE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()

        label1 = tk.Label(self, text = "empty").grid()
class P_Revise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#00796B")
        label1 = tk.Label(self, text = "Paper 1", fg = "white", bg = "#00796B", font = (None, 18, "bold")).grid(row = 0, column = 0, sticky = "w")
        label2 = tk.Label(self, text = "Paper 2", fg = "white", bg = "#00796B", font = (None, 18, "bold")).grid(row = 3, column = 0, sticky = "w")
        
        button1= tk.Button(self, text="Christian Beliefs",command=lambda: controller.show_frame("RChristianBeliefs"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=1,column=0)
        button2= tk.Button(self, text="Christian Teachings",command=lambda: controller.show_frame("RChristianTeachings"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=1,column=1)
        button3= tk.Button(self, text="Christian Practices",command=lambda: controller.show_frame("RChristianPractices"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=1,column=2)
        button4= tk.Button(self, text="Islamic Beliefs",command=lambda: controller.show_frame("RIslamBeliefs"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=2,column=0)
        button5= tk.Button(self, text="Islamic Teachings",command=lambda: controller.show_frame("RIslamTeachings"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=2,column=1)
        button6= tk.Button(self, text="Islamic Practices",command=lambda: controller.show_frame("RIslamPractices"),fg="white",bg="#009688",width=29,font=(None, 17, "bold")).grid(row=2,column=2)
        button7= tk.Button(self, text="B- Life",command=lambda: controller.show_frame("RB"),fg="white",bg="#009688",width=29,font=(None, 17, "bold"), anchor = "w").grid(row=4,column=0)
        button8= tk.Button(self, text="C- Existence of God and Revelation",command=lambda: controller.show_frame("RC"),fg="white",bg="#009688",width=29,font=(None, 17, "bold"), anchor = "w").grid(row=4,column=1)
        button9= tk.Button(self, text="D- Peace and Conflict",command=lambda: controller.show_frame("RD"),fg="white",bg="#009688",width=29,font=(None, 17, "bold"), anchor = "w").grid(row=5,column=0)
        button10= tk.Button(self, text="E- Crime and Punishment",command=lambda: controller.show_frame("RE"),fg="white",bg="#009688",width=29,font=(None, 17, "bold"), anchor = "w").grid(row=5,column=1)
        
        
        button18 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=2)


class RChristianBeliefs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#00796B")
        label = tk.Label(self, text="God", font=controller.title_font,fg="white", bg="#00796B").grid(row=0,column=0)
        button= tk.Button(self, text= "Natures of God",command=lambda: controller.show_frame("RNaturesOfGod"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button1= tk.Button(self, text="Creation",command=lambda: controller.show_frame("Creation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button2= tk.Button(self, text="Afterlife",command=lambda: controller.show_frame("Afterlife"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        label1 = tk.Label(self, text="Jesus", font=controller.title_font,fg="white", bg="#00796B").grid(row=2,column=0)
        button3= tk.Button(self, text="Incarnation",command=lambda: controller.show_frame("Incarnation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button4= tk.Button(self, text="Crucifixion",command=lambda: controller.show_frame("Crucifixion"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button6 = tk.Button(self, text="Resurrection",command=lambda: controller.show_frame("Reserrection"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=2)
        button7 = tk.Button(self, text="Ascension",command=lambda: controller.show_frame("Ascension"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=0)
        button8= tk.Button(self, text="Sin",command=lambda: controller.show_frame("Sin"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=1)
        button9= tk.Button(self, text="Salvation",command=lambda: controller.show_frame("Salvation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=2)
        label2 = tk.Label(self, text="Practises", font=controller.title_font,fg="white", bg="#00796B").grid(row=5,column=0)
        button10 = tk.Button(self, text="Worship Form",command=lambda: controller.show_frame("Worship Form"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=0)
        button11 = tk.Button(self, text="Prayer",command=lambda: controller.show_frame("Prayer"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=1)
        button12 = tk.Button(self, text="Sacraments",command=lambda: controller.show_frame("Sacraments"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=2)
        button13 = tk.Button(self, text="Pilgrimage",command=lambda: controller.show_frame("Pilgrimage"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=7,column=0)
        button14 = tk.Button(self, text="Celebrations",command=lambda: controller.show_frame("Celebrations"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=7,column=1)
        button15 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#009688",font=(None,23,"bold"),height=2, width=11).grid(row=8,column=2,padx=5,pady=5)
class RChristianPractices(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()

class RChristianTeachings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label = tk.Label(self, text="God", font=controller.title_font,fg="white", bg="#00796B").grid(row=0,column=0)
        button= tk.Button(self, text= "Natures of God",command=lambda: controller.show_frame("NaturesOfGod"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button1= tk.Button(self, text="Creation",command=lambda: controller.show_frame("Creation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button2= tk.Button(self, text="Afterlife",command=lambda: controller.show_frame("Afterlife"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        label1 = tk.Label(self, text="Jesus", font=controller.title_font,fg="white", bg="#00796B").grid(row=2,column=0)
        button3= tk.Button(self, text="Incarnation",command=lambda: controller.show_frame("Incarnation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button4= tk.Button(self, text="Crucifixion",command=lambda: controller.show_frame("Crucifixion"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button6 = tk.Button(self, text="Resurrection",command=lambda: controller.show_frame("Reserrection"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=2)
        button7 = tk.Button(self, text="Ascension",command=lambda: controller.show_frame("Ascension"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=0)
        button8= tk.Button(self, text="Sin",command=lambda: controller.show_frame("Sin"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=1)
        button9= tk.Button(self, text="Salvation",command=lambda: controller.show_frame("Salvation"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=2)
        label2 = tk.Label(self, text="Practises", font=controller.title_font,fg="white", bg="#00796B").grid(row=5,column=0)
        button10 = tk.Button(self, text="Worship Form",command=lambda: controller.show_frame("Worship Form"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=0)
        button11 = tk.Button(self, text="Prayer",command=lambda: controller.show_frame("Prayer"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=1)
        button12 = tk.Button(self, text="Sacraments",command=lambda: controller.show_frame("Sacraments"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=6,column=2)
        button13 = tk.Button(self, text="Pilgrimage",command=lambda: controller.show_frame("Pilgrimage"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=7,column=0)
        button14 = tk.Button(self, text="Celebrations",command=lambda: controller.show_frame("Celebrations"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=7,column=1)
        button15 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#009688",font=(None,23,"bold"),height=2, width=11).grid(row=8,column=2,padx=5,pady=5)
class RIslamBeliefs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class RIslamPractices(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class RIslamTeachings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class RB(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class RC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class RD(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()
class RE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#00796B")
        self.controller = controller

        label1 = tk.Label(self, text = "empty").grid()


class RNaturesOfGod(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#00796B")
        button= tk.Button(self, text= "Omnipotence",command=lambda: controller.show_frame("RNOG_Omnipotence"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button1= tk.Button(self, text="Omnibenevolence",command=lambda: controller.show_frame("RNOG_Omnibenevolence"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button2= tk.Button(self, text="Just",command=lambda: controller.show_frame("RNOG_Just"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        button3= tk.Button(self, text="NOTHING HERE YET",command=lambda: controller.show_frame("NOTHING"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button4= tk.Button(self, text="NOTHING HERE YET",command=lambda: controller.show_frame("NOTHING"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button6 = tk.Button(self, text="NOTHING HERE YET",command=lambda: controller.show_frame("NOTHING"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=3,column=2)
        button7 = tk.Button(self, text="NOTHING HERE YET",command=lambda: controller.show_frame("NOTHING"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=0)
        button8= tk.Button(self, text="NOTHING HERE YET",command=lambda: controller.show_frame("NOTHING"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=1)
        button9= tk.Button(self, text="NOTHING HERE YET",command=lambda: controller.show_frame("NOTHING"),fg="white",bg="#009688",width=20,font=(None, 17, "bold")).grid(row=4,column=2)

class RNOG_Omnipotence(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#00796B")
        label  = tk.Label(self,text="For:",bg ="#00796B",fg= "grey95",  font = (None, 24)).grid(row=1, column=1, sticky="w")
        label2 = tk.Label(self, text="• \"God said 'let there be light', and there was light\"\n", fg = "white", bg ="#00796B", font = ("Palatino Linotype", 24)).grid(row = 2, column = 2, sticky = "w")
        label3 = tk.Label(self, text="• Jesus said \"with God all things are possible\"", fg = "white", bg ="#00796B", font = ("Palatino Linotype", 24)).grid(row = 3, column = 2, sticky = "w")
        button = tk.Button(self, text="NaturesOfGod",command=lambda: controller.show_frame("RNaturesOfGod"),fg="white",bg="#009688",width=20,font=(None,20,"bold")).grid(row = 4, column = 1, sticky = "w")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#009688",width=20,font=(None,20,"bold")).grid(row = 4, column = 2, sticky = "w")           
class RNOG_Omnibenevolence(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#00796B")
        label  = tk.Label(self,text="For:",bg ="#00796B",fg= "grey95",  font = (None, 24)).grid(row=1, column=1, sticky="w")
        label2 = tk.Label(self, text="• \"God so loved the world that He gave His only Son\"\n", fg = "white", bg ="#00796B", font = ("Palatino Linotype", 24)).grid(row = 2, column = 2, sticky = "w")
        label3 = tk.Label(self, text="• \"his steadfast love endures forever\"", fg = "white", bg ="#00796B", font = ("Palatino Linotype", 24)).grid(row = 3, column = 2, sticky = "w")
        button = tk.Button(self, text="NaturesOfGod",command=lambda: controller.show_frame("RNaturesOfGod"),fg="white",bg="#009688",width=20,font=(None,20,"bold")).grid(row = 4, column = 1, sticky = "w")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#009688",width=20,font=(None,20,"bold")).grid(row = 4, column = 2, sticky = "w")  
class RNOG_Just(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#00796B")
        label  = tk.Label(self,text="For:",bg ="#00796B",fg= "grey95",  font = (None, 24)).grid(row=1, column=1, sticky="w")
        label2 = tk.Label(self, text="• \"A God worthy of worship\"\n", fg = "white", bg ="#00796B", font = ("Palatino Linotype", 24)).grid(row = 2, column = 2, sticky = "w")
        label3 = tk.Label(self, text="• \"I was hungry and you gave me something to eat\"- Parable of The Sheep and the Goats", fg = "white", bg ="#00796B", font = ("Palatino Linotype", 24)).grid(row = 3, column = 2, sticky = "w")
        button = tk.Button(self, text="NaturesOfGod",command=lambda: controller.show_frame("RNaturesOfGod"),fg="white",bg="#009688",width=20,font=(None,20,"bold")).grid(row = 4, column = 1, sticky = "w")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#009688",width=20,font=(None,20,"bold")).grid(row = 4, column = 2, sticky = "w") 



