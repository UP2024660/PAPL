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
        for F in (StartPage, English, E_Test, E_Revise, A_I_C, A_I_C_Act_1, AIC_A1_Read, AIC_A1_KQ, AIC_A1_CA, AIC_A1_KT, AIC_A1_BS,A_I_C_Act_2, AIC_A2_Read, AIC_A2_KQ, AIC_A2_CA, AIC_A2_KT, AIC_A2_BS, A_I_C_Act_3, AIC_A3_Read, AIC_A3_KQ, AIC_A3_CA, AIC_A3_KT, AIC_A3_BS,AIC_Context, A_I_C_Full_Play, A_I_C_J_B):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class A_I_C(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        button= tk.Button(self, text= "Act 1",command=lambda: controller.show_frame("A_I_C_Act_1"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Act 2",command=lambda: controller.show_frame("A_I_C_Act_2"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Act 3",command=lambda: controller.show_frame("A_I_C_Act_3"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button5= tk.Button(self, text="Full Play",command=lambda: controller.show_frame("A_I_C_Full_Play"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        button6= tk.Button(self, text="J.B. Priestley",command=lambda: controller.show_frame("A_I_C_J_B"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=2,column=0)
        button7= tk.Button(self, text="Context",command=lambda: controller.show_frame("AIC_Context"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=2,column=0)
        button8 = tk.Button(self, text="Topics",command=lambda: controller.show_frame("E_Revise"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button9 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class A_I_C_Act_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        button= tk.Button(self, text= "Act 1",command=lambda: controller.show_frame("AIC_A1_Read"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key Quotes",command=lambda: controller.show_frame("AIC_A1_KQ"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Character Analysis",command=lambda: controller.show_frame("AIC_A1_CA"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=0,column=2)
        button3= tk.Button(self, text="Key Themes",command=lambda: controller.show_frame("AIC_A1_KT"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=1,column=0)
        button4= tk.Button(self, text="Brief Summary of Act 1",command=lambda: controller.show_frame("AIC_A1_BS"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=1,column=1)
        button6 = tk.Button(self, text="Revise page",command=lambda: controller.show_frame("E_Revise"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=3,column=2)

class AIC_A1_Read(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        S = tk.Scrollbar(self)
        T = tk.Text(self, height=40, width =100,bg="white")
        S.pack(side="right", fill="y")
        T.pack(side="top", fill="x")
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        definitions=""" NOT HERE YET, SORRY
"""
        T.insert(tk.END, definitions)
        
        button = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e67e22",width=10,font=(None,20,"bold"))
        button.pack(side="bottom")

class AIC_A1_KQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 1 Key Quotes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class AIC_A1_CA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 1 Character Analysis", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class AIC_A1_KT(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 1 Key Themes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class AIC_A1_BS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 1 Brief Summary", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class A_I_C_Act_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        button= tk.Button(self, text= "Act 2",command=lambda: controller.show_frame("AIC_A2_Read"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key Quotes",command=lambda: controller.show_frame("AIC_A2_KQ"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Character Analysis",command=lambda: controller.show_frame("AIC_A2_CA"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=0,column=2)
        button3= tk.Button(self, text="Key Themes",command=lambda: controller.show_frame("AIC_A2_KT"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=1,column=0)
        button4= tk.Button(self, text="Brief Summary of Act 2",command=lambda: controller.show_frame("AIC_21_BS"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=1,column=1)
        button6 = tk.Button(self, text="Revise page",command=lambda: controller.show_frame("E_Revise"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=3,column=2)

class AIC_A2_Read(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        S = tk.Scrollbar(self)
        T = tk.Text(self, height=40, width =100,bg="white")
        S.pack(side="right", fill="y")
        T.pack(side="top", fill="x")
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        definitions=""" NOT HERE YET, SORRY
"""
        T.insert(tk.END, definitions)
        
        button = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e67e22",width=10,font=(None,20,"bold"))
        button.pack(side="bottom")

class AIC_A2_KQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 2 Key Quotes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class AIC_A2_CA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 2 Character Analysis", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class AIC_A2_KT(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 2 Key Themes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class AIC_A2_BS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 2 Brief Summary", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class A_I_C_Act_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        button= tk.Button(self, text= "Act 1",command=lambda: controller.show_frame("AIC_A3_Read"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key Quotes",command=lambda: controller.show_frame("AIC_A3_KQ"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Character Analysis",command=lambda: controller.show_frame("AIC_A3_CA"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=0,column=2)
        button3= tk.Button(self, text="Key Themes",command=lambda: controller.show_frame("AIC_A3_KT"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=1,column=0)
        button4= tk.Button(self, text="Brief Summary of Act 1",command=lambda: controller.show_frame("AIC_A3_BS"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=1,column=1)
        button6 = tk.Button(self, text="Revise page",command=lambda: controller.show_frame("E_Revise"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e67e22",width=10,font=(None, 17, "bold")).grid(row=3,column=2)

class AIC_A3_Read(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        S = tk.Scrollbar(self)
        T = tk.Text(self, height=40, width =100,bg="white")
        S.pack(side="right", fill="y")
        T.pack(side="top", fill="x")
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        definitions=""" NOT HERE YET, SORRY
"""
        T.insert(tk.END, definitions)
        
        button = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e67e22",width=10,font=(None,20,"bold"))
        button.pack(side="bottom")

class AIC_A3_KQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 3 Key Quotes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_3"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class AIC_A3_CA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 3 Character Analysis", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_3"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class AIC_A3_KT(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 3 Key Themes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_3"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class AIC_A3_BS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Act 3 Brief Summary", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("AIC_Act_3"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class A_I_C_Full_Play(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        S = tk.Scrollbar(self)
        T = tk.Text(self, height=40, width =100,bg="white")
        S.pack(side="right", fill="y")
        T.pack(side="top", fill="x")
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        definitions=""" NOT HERE YET, SORRY
"""
        T.insert(tk.END, definitions)
        
        button = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),bg="#e67e22",fg="white",width=10,font=(None,20,"bold"))
        button.pack(side="bottom")


class A_I_C_J_B(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Context", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("E_Revise"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class AIC_Context(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        label=tk.Label(self, text="Context", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET,
SORRY
""",fg="white",bg="deep sky blue")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",bg="#e67e22",fg="white",command=lambda: controller.show_frame("E_Revise"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#e67e22",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
 


