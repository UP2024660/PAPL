import tkinter as tk
from tkinter import font as tkfont
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
        for F in (StartPage, French, F_Test, F_Revise,F_Module_1,F_M1_SQ,F_Module_2,F_M2_SQ,F_Module_3,F_M3_SQ,F_Module_4,F_M4_SQ,F_Module_5,F_M5_SQ,F_Module_6,F_M6_SQ,F_Module_7,F_M7_SQ,F_Module_8,F_M8_SQ,F_Module_9,F_M9_SQ,F_Module_10,F_M10_SQ,F_Module_11,F_M11_SQ,F_Grammar_Booklet):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class French(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button1 = tk.Button(self, text="Test", command=lambda: controller.show_frame("F_Test"),bg="#e74c3c",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="Revise", command=lambda: controller.show_frame("F_Revise"),bg="#e74c3c",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=1,padx=5,pady=5)
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",font=(None,23,"bold"),height=2, width=11).grid(row=0,column=2,padx=5,pady=5)


class F_Test(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#c0392b")
        self.controller = controller
        button1= tk.Button(self, text="Module 1",command=lambda: controller.show_frame("FTModule1"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button2= tk.Button(self, text="Module 2",command=lambda: controller.show_frame("FTModule2"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button3= tk.Button(self, text="Module 3",command=lambda: controller.show_frame("FTModule3"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button4= tk.Button(self, text="Module 4",command=lambda: controller.show_frame("FTModule4"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button5= tk.Button(self, text="Module 5",command=lambda: controller.show_frame("FTModule5"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button6= tk.Button(self, text="Module 6",command=lambda: controller.show_frame("FTModule6"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        button7= tk.Button(self, text="Module 7",command=lambda: controller.show_frame("FTModule7"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=2,column=0)
        button8= tk.Button(self, text="Module 8",command=lambda: controller.show_frame("FTModule8"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=2,column=1)
        button9= tk.Button(self, text="Module 9",command=lambda: controller.show_frame("FTModule9"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=2,column=2)
        button10= tk.Button(self, text="Module 10",command=lambda: controller.show_frame("FTModule10"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button11= tk.Button(self, text="Module 11",command=lambda: controller.show_frame("FTModule11"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button18 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=6,column=2)


class F_Revise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button1= tk.Button(self, text="Module 1",command=lambda: controller.show_frame("F_Module_1"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button2= tk.Button(self, text="Module 2",command=lambda: controller.show_frame("F_Module_2"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button3= tk.Button(self, text="Module 3",command=lambda: controller.show_frame("F_Module_3"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button4= tk.Button(self, text="Module 4",command=lambda: controller.show_frame("F_Module_4"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button5= tk.Button(self, text="Module 5",command=lambda: controller.show_frame("F_Module_5"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button6= tk.Button(self, text="Module 6",command=lambda: controller.show_frame("F_Module_6"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        button7= tk.Button(self, text="Module 7",command=lambda: controller.show_frame("F_Module_7"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=2,column=0)
        button8= tk.Button(self, text="Module 8",command=lambda: controller.show_frame("F_Module_8"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=2,column=1)
        button9= tk.Button(self, text="Module 9",command=lambda: controller.show_frame("F_Module_9"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=2,column=2)
        button10= tk.Button(self, text="Module 10",command=lambda: controller.show_frame("F_Module_10"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button11= tk.Button(self, text="Module 11",command=lambda: controller.show_frame("F_Module_11"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button16 = tk.Button(self, text="Grammar Booklet", command=lambda: controller.show_frame("F_Grammar_Booklet"),bg="#e74c3c",fg="white",font=(None,17, "bold"),width=20).grid(row=3,column=2)
        button17 = tk.Button(self, text="Idioms", command=lambda: controller.show_frame("F_Idioms"),bg="#e74c3c",fg="white",font=(None,17, "bold"),width=20).grid(row=4,column=0)
        button18 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=6,column=2)


class F_Module_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button= tk.Button(self, text= "Speaking Questions",command=lambda: controller.show_frame("F_M1_SQ"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key words and Phrases",command=lambda: controller.show_frame("F_M1_WaP"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Idioms",command=lambda: controller.show_frame("F_M1_Idioms"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="French Homepage",command=lambda: controller.show_frame("F_Revise"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class F_M1_SQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label1 = tk.Label(self, text="1-       Décris-moi ton/ta meilleur(e) ami(e). Describe your best friend to me.",bg="#c0392b",fg="white", font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label2 = tk.Label(self, text="2-       Tu t’entends bien avec ta famille?  Do you get on well with your family?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label3 = tk.Label(self, text="3-       Qu’est-ce que tu fais normalement avec tes amis le week-end?    What do you usually do with your friends at the weekend?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label4 = tk.Label(self, text="4-       Qu’est-ce que tu as fait le week-end dernier avec tes amis? What did you do last weekend with your friends?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label5 = tk.Label(self, text="5-       Quelles sont les qualités d’un bon ami/une bonne amie? What are the qualities of a good friend?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label6 = tk.Label(self, text="6-       Quels sont les avantages d’une famille nombreuse?  What are the advantages of a large family?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label7 = tk.Label(self, text="7-       Préfères-tu sortir avec tes amis, ou rester chez toi? Pourquoi?Do you prefer to go out with your friends or stay at home? Why?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label8 = tk.Label(self, text="8-       Qu’est-ce que tu vas faire ce week-end avec tes amis? What are you going to do this weekend with your friends??",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label9 = tk.Label(self, text="9-       Décris-moi ton/ta copain/copine idéal(e). Describe your ideal boy/girlfriend.",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label10 = tk.Label(self, text="10-	Tu es comment? Décris toi.    What are you like? Describe yourself.",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        button11 = tk.Button(self, text="Module 1",command=lambda: controller.show_frame("F_Module_1"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)
        button12 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)

        
class F_Module_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button= tk.Button(self, text= "Speaking Questions",command=lambda: controller.show_frame("F_M2_SQ"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key words and Phrases",command=lambda: controller.show_frame("F_M2_WaP"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Idioms",command=lambda: controller.show_frame("F_2_Idioms"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="French Homepage",command=lambda: controller.show_frame("F_Revise"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class F_M2_SQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label1 = tk.Label(self, text="1-	Décris-moi ta ville.Describe your home town to me.",bg="#c0392b",fg="white", font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label2 = tk.Label(self, text="2-	Qu’est-ce qu’il y a dans ta ville pour les jeunes/les touristes/sportifs?What does your town have to offer young people/tourists/sporty people?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label3 = tk.Label(self, text="3-	Qu’est-ce qu’il y a à faire dans ta ville?What is there to do in our town?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label4 = tk.Label(self, text="4-	Tu aimes habiter dans ta ville? Pourquoi/Pourquoi pas?Do you like living in your town? Why/Why not?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label5 = tk.Label(self, text="5-	Elle est comment ta ville idéale?What would your ideal town be like?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label6 = tk.Label(self, text="6-	Tu préfèrerais habiter dans une ville ou à la campagne? Pourquoi/Pourquoi pas?Would you prefer to live in a town or in the countryside? Why/Why not?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label7 = tk.Label(self, text="7-	Où es-tu allé(e) en vacances l’année dernière?Where did you go  on holiday last year?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label8 = tk.Label(self, text="8-	Qu’est-ce que tu vas faire pour les vacances cet été?What are you going to do for the holidays this summer?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label9 = tk.Label(self, text="9-	Tu préfères les vacances d’été ou les vacances d’hiver? Pourquoi?Do you prefer summer or winter holidays? Why?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label10 = tk.Label(self, text="10-	Tu préfères aller en vacances avec ta famille ou avec tes amis?Do you prefer to go on holiday with your family or friends?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        button11 = tk.Button(self, text="Module 2",command=lambda: controller.show_frame("F_Module_2"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)
        button12 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)


class F_Module_3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button= tk.Button(self, text= "Speaking Questions",command=lambda: controller.show_frame("F_M3_SQ"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key words and Phrases",command=lambda: controller.show_frame("F_M3_WaP"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Idioms",command=lambda: controller.show_frame("F_M3_Idioms"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="French Homepage",command=lambda: controller.show_frame("F_Revise"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class F_M3_SQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label1 = tk.Label(self, text="1-	Qu’est-ce que tu aimes faire au collège? What do you like to do at school?",bg="#c0392b",fg="white", font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label2 = tk.Label(self, text="2-	Qu’est-ce que tu as fait hier au collège? What did you do yesterday at school?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label3 = tk.Label(self, text="3-	Qu’est-ce que tu n’aimes pas comme matière? Pourquoi? Which subjects don’t you like? Why?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label4 = tk.Label(self, text="4-	Tu voudrais prendre une année sabbatique à l’avenir? Pourquoi/Pourquoi pas? Would you like to take a gap year in the future? Why/Why not?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label5 = tk.Label(self, text="5-	Quelles sont les différences entre l’école en France et en Angleterre? What are the differences between school in France and England?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label6 = tk.Label(self, text="6-	Qu’est-ce que tu aimerais faire comme job plus tard? What job would you like to do later on?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label7 = tk.Label(self, text="7-	Qu’est-ce que tu changerais à ton collège et pourquoi? What would you change about your school and why?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label8 = tk.Label(self, text="8-	Qu’est-ce que tu voudrais faire l’année prochaine? What would you like to do next year?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label9 = tk.Label(self, text="9-	Pourquoi as-tu choisi d’étudier le français? Why did you choose to study French?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label10 = tk.Label(self, text="10-	Tu aimerais travailler à l’étranger plus tard? Would you like to work abroad later on?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        button11 = tk.Button(self, text="Module 3",command=lambda: controller.show_frame("F_Module_3"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)
        button12 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)

        
class F_Module_4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button= tk.Button(self, text= "Speaking Questions",command=lambda: controller.show_frame("F_M4_SQ"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key words and Phrases",command=lambda: controller.show_frame("F_M4_WaP"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Idioms",command=lambda: controller.show_frame("F_4_Idioms"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="French Homepage",command=lambda: controller.show_frame("F_Revise"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class F_M4_SQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label1 = tk.Label(self, text="1-	Qu’est-ce que tu aimes faire dans ton temps libre? What do you like to do in your free time?",bg="#c0392b",fg="white", font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label2 = tk.Label(self, text="2-	Qu’est-ce que tu as fait le week-end dernier? What did you do last weekend?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label3 = tk.Label(self, text="3-	Qu’est-ce que tu as fait pour fêter ton anniversaire l’année dernière? What did you do to celebrate your birthday last year?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label4 = tk.Label(self, text="4-	Tu aimes quel genre de musique? What kind of music do you like?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label5 = tk.Label(self, text="5-	Qu’est-ce que tu aimes regarder à la télé? What do you like to watch on the TV?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label6 = tk.Label(self, text="6-	Raconte-moi un film que tu as vu récemment? Tell me about a film you saw recently?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label7 = tk.Label(self, text="7-	Quels sont tes projets pour le week-end prochain? What are your plans for next weekend?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label8 = tk.Label(self, text="8-	Tu aimes quel genre de films?What kind of films do you like?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label9 = tk.Label(self, text="9-	Qu’est-ce que tu penses des réseaux sociaux? What do you think of social media?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label10 = tk.Label(self, text="10-	Tu préfères sortir avec des amis ou rester devant l’ordinateur? Pourquoi? Do you prefer to go out with friends or stay in front of the computer? Why?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        button11 = tk.Button(self, text="Module 2",command=lambda: controller.show_frame("F_Module_4"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)
        button12 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)


class F_Module_5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button= tk.Button(self, text= "Speaking Questions",command=lambda: controller.show_frame("F_M5_SQ"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key words and Phrases",command=lambda: controller.show_frame("F_M5_WaP"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Idioms",command=lambda: controller.show_frame("F_M5_Idioms"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="French Homepage",command=lambda: controller.show_frame("F_Revise"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class F_M5_SQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label1 = tk.Label(self, text="1-	Que fais-tu pour garder la forme? What do you do to stay in shape?",bg="#c0392b",fg="white", font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label2 = tk.Label(self, text="2-	Tu manges sainement? Pourquoi/Pourquoi pas?Do you eat healthily? Why/Why not?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label3 = tk.Label(self, text="3-	Est-ce que c’est important de faire de l’exercice à ton avis? Is it important to do exercise in your opinion?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label4 = tk.Label(self, text="4-	Comment pourrais tu améliorer ta façon de manger? How could you improve the way you eat?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label5 = tk.Label(self, text="5-	Décris-moi un repas sain que tu as mangé récemment. Describe a healthy meal you had recently.",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label6 = tk.Label(self, text="6-	Selon toi, pourquoi est-ce qu’on devient végétarien(ne)? In your opinion, why do people become vegetarian?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label7 = tk.Label(self, text="7-	Qu’est-ce que tu penses du tabagisme? What do you think of smoking?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label8 = tk.Label(self, text="8-	Est-ce que tu as des mauvaises habitudes? Do you have any bad habits?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label9 = tk.Label(self, text="9-	Qu’est-ce que tu manges pendant une journée typique? What do you eat during a typical day?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label10 = tk.Label(self, text="10-	Quels sont les dangers de l’alcool pour les jeunes? What are the dangers of alcohol for young people?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        button11 = tk.Button(self, text="Module 5",command=lambda: controller.show_frame("F_Module_5"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)
        button12 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)

        
class F_Module_6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button= tk.Button(self, text= "Speaking Questions",command=lambda: controller.show_frame("F_M6_SQ"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key words and Phrases",command=lambda: controller.show_frame("F_M6_WaP"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Idioms",command=lambda: controller.show_frame("F_6_Idioms"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="French Homepage",command=lambda: controller.show_frame("F_Revise"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class F_M6_SQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label1 = tk.Label(self, text="1-	Quelle est ta fête préférée, et pourquoi? Which is your favourite holiday, and why?",bg="#c0392b",fg="white", font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label2 = tk.Label(self, text="2-	Comment as-tu fêté Noël/Eid/Diwali l’année dernière? How did you celebrate Christmas/Eid/Diwali last year?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label3 = tk.Label(self, text="3-	Décris-moi une fête française. Describe a French festival to me.",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label4 = tk.Label(self, text="4-	Est-ce que les fêtes nationales sont importantes à ton avis? Are national festivals important in your opinion?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label5 = tk.Label(self, text="5-	Qu’est-ce que tu penses des fêtes françaises? What do you think of French festivals?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label6 = tk.Label(self, text="6-	Tu es déjà allé(e) à une fête en France? Have you been to a French festival?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label7 = tk.Label(self, text="7-	Quelles sont les différences entre le Noël en France et en Angleterre? What are the differences between Christmas in France and n England?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label8 = tk.Label(self, text="8-	Comment vas-tu fêter le nouvel an? How are you going to celebrate the new year?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label9 = tk.Label(self, text="9-	Qu’est-ce que tu as reçu comme cadeaux pour ton anniversaire? What presents did you get for your birthday?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label10 = tk.Label(self, text="10-	Comment voudrais-tu fêter ton anniversaire, si tu avais le choix? How would you celebrate your birthday if you had the choice?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        button11 = tk.Button(self, text="Module 6",command=lambda: controller.show_frame("F_Module_6"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)
        button12 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)


class F_Module_7(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button= tk.Button(self, text= "Speaking Questions",command=lambda: controller.show_frame("F_M7_SQ"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key words and Phrases",command=lambda: controller.show_frame("F_M7_WaP"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Idioms",command=lambda: controller.show_frame("F_M7_Idioms"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="French Homepage",command=lambda: controller.show_frame("F_Revise"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class F_M7_SQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label1 = tk.Label(self, text="1-	Que fait ta famille pour protéger l’environnement? What do you do to protect the environment?",bg="#c0392b",fg="white", font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label2 = tk.Label(self, text="2-	À ton avis, c’est important de protéger l’environnement? In your opinion is it important to protect the environment?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label3 = tk.Label(self, text="3-	Qu’est-ce que tu as fait récemment pour aider l’environnement? What have you done recently to help the environment?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label4 = tk.Label(self, text="4-	À ton avis, quels sont les problèmes les plus graves pour l’environnement? In your opinion what are the most serious problems with the environment?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label5 = tk.Label(self, text="5-	Quels sont les effets du réchauffement de la terre? What are the effects of global warming?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label6 = tk.Label(self, text="6-	Est-ce qu’il y a trop de pollution dans ta ville à ton avis? Is there too much pollution in your town in your opinion?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label7 = tk.Label(self, text="7-	Le recyclage, c’est important pour toi? Is recycling important to you?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label8 = tk.Label(self, text="8-	Qu’est-ce que tu changerais à ton collège pour améliorer l’environnement? What would you change at your school to improve the environment?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label9 = tk.Label(self, text="9-	Est-ce qu’il y a assez d’espaces verts dans ta ville? Are there enough green spaces in your town?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label10 = tk.Label(self, text="10-	Quand tu seras plus agé(e) que feras-tu chez toi pour protéger l’environnement? When you are older, what will you do in your home to protect the environment?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        button11 = tk.Button(self, text="Module 7",command=lambda: controller.show_frame("F_Module_7"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)
        button12 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)

        
class F_Module_8(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button= tk.Button(self, text= "Speaking Questions",command=lambda: controller.show_frame("F_M8_SQ"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key words and Phrases",command=lambda: controller.show_frame("F_M8_WaP"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Idioms",command=lambda: controller.show_frame("F_8_Idioms"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="French Homepage",command=lambda: controller.show_frame("F_Revise"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class F_M8_SQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label1 = tk.Label(self, text="1-	Est-ce que tu donnes de l’argent à des organisations caritatives? Combien? Pourquoi? Do you give money to charity? How much? Why?",bg="#c0392b",fg="white", font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label2 = tk.Label(self, text="2-	Quelles organisations caritatives sont les plus importantes pour toi? Which charities are most important to you?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label3 = tk.Label(self, text="3-	Est-ce que tu as déjà donné tes affaires à un magasin qui soutient une organisation caritative? Have you ever donated anything to a charity shop?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label4 = tk.Label(self, text="4-	Est-ce que tu as déja récolté des fonds pour une organisation caritative? Comment? Have you ever raised money for charity? How?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label5 = tk.Label(self, text="5-	As-tu déjà été sponsorisé? Have you ever been sponsored?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label6 = tk.Label(self, text="6-	Que font les élèves et les profs de ton collège pour récolter des fonds pour une organisation caritative? What do the students and teachers at your school do to raise money for charity?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label7 = tk.Label(self, text="7-	Qu’est-ce que tu pourrais faire pour récolter des fonds pour une organisation caritative? What could you do to raise money for charity?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label8 = tk.Label(self, text="8-	As-tu déjà fait du bénévolat? Have you ever done any volunteering?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label9 = tk.Label(self, text="9-	Quels sont les avantages et les inconvénients du travail bénévole? What are the advantages and disadvantages of volunteer work?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label10 = tk.Label(self, text="10-	Tu voudrais faire du travail bénévole à l’étranger et où ça? Would you like to do volunteer work abroad and where?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        button11 = tk.Button(self, text="Module 8",command=lambda: controller.show_frame("F_Module_8"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)
        button12 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)

class F_Module_9(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button= tk.Button(self, text= "Speaking Questions",command=lambda: controller.show_frame("F_M9_SQ"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key words and Phrases",command=lambda: controller.show_frame("F_M9_WaP"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Idioms",command=lambda: controller.show_frame("F_9_Idioms"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="French Homepage",command=lambda: controller.show_frame("F_Revise"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class F_M9_SQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label1 = tk.Label(self, text="1-	Tu voudrais prendre une année sabbatique à l’avenir? Pourquoi/Pourquoi pas? Would you like to take a gap year in the future? Why/Why not?",bg="#c0392b",fg="white", font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label2 = tk.Label(self, text="2-	Qu’est-ce que tu aimerais faire comme job plus tard? What job would you like to do later on?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label3 = tk.Label(self, text="3-	Qu’est-ce que tu voudrais faire l’année prochaine? What would you like to do next year?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label4 = tk.Label(self, text="4-	Tu aimerais travailler à l’étranger plus tard? Would you like to work abroad later on?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label5 = tk.Label(self, text="5-	Quel serait ton travail idéal? Pourquoi? What would be your ideal job? Why?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label6 = tk.Label(self, text="6-	Où as-tu fait ton stage? Where did you do your work experience?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label7 = tk.Label(self, text="7-	Décris une journée typique pendant ton stage. Describe a typical day during your work experience.",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label8 = tk.Label(self, text="8-	Tu préfèrerais travailler seul ou dans une équipe? Pourquoi? Would you prefer to work alone or in a team? Why?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label9 = tk.Label(self, text="9-	Tu aimerais travailler à l’extérieur? Pourquoi? Would you like to work outside? Why?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label10 = tk.Label(self, text="10-	Qu’est-ce que tu voulais faire quand tu étais petit(e)? What did you want to do when you were little?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        button11 = tk.Button(self, text="Module 9",command=lambda: controller.show_frame("F_Module_9"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)
        button12 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)


class F_Module_10(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button= tk.Button(self, text= "Speaking Questions",command=lambda: controller.show_frame("F_M10_SQ"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key words and Phrases",command=lambda: controller.show_frame("F_M10_WaP"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Idioms",command=lambda: controller.show_frame("F_10_Idioms"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="French Homepage",command=lambda: controller.show_frame("F_Revise"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class F_M10_SQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label1 = tk.Label(self, text="1-	Quelle est ton émission préférée?What is your favourite programme?",bg="#c0392b",fg="white", font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label2 = tk.Label(self, text="2-	Tu regardes souvent la télé?Do you watch the TV regularly?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label3 = tk.Label(self, text="3-	Tu passes combien de temps sur Internet pendant une journée typique?How much time do you spend on the internet during a typical day?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label4 = tk.Label(self, text="4-	Qu’est-ce que tu penses des réseaux sociaux? What do you think of social media?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label5 = tk.Label(self, text="5-	Tu préfères sortir avec des amis ou rester devant l’ordinateur? Pourquoi? Do you prefer to go out with friends or stay in front of the computer? Why?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label6 = tk.Label(self, text="6-	Les jeunes passent trop de temps sur leurs portables. Tu es d’accord? Young people spend too much time on their phones. Do you agree?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label7 = tk.Label(self, text="7-	Quels sont les dangers d’Internet pour les jeunes? What are the dangers of the internet for young people?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label8 = tk.Label(self, text="8-	Tu utilises beaucoup les gadgets éléctroniques? Do you use a lot of electronic gadgets?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label9 = tk.Label(self, text="9-	Est-ce que tu pourrais vivre sans Internet?Could you live without the internet?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label10 = tk.Label(self, text="10-	À ton avis, quelle est l’invention technologique la plus importante du siècle? In your opinion, what is the most important technological invention of the century?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        button11 = tk.Button(self, text="Module 10",command=lambda: controller.show_frame("F_Module_10"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)
        button12 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)

        
class F_Module_11(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        button= tk.Button(self, text= "Speaking Questions",command=lambda: controller.show_frame("F_M11_SQ"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Key words and Phrases",command=lambda: controller.show_frame("F_M11_WaP"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Idioms",command=lambda: controller.show_frame("F_11_Idioms"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="French Homepage",command=lambda: controller.show_frame("F_Revise"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class F_M11_SQ(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label1 = tk.Label(self, text="1-	Quels sont les problèmes principaux pour les SDF?What are the main problems for homeless people?",bg="#c0392b",fg="white", font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label2 = tk.Label(self, text="2-	Est-ce qu’il y a beaucoup de gens sans domicile fixe dans ta ville?Are there many homeless people in your town?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label3 = tk.Label(self, text="3-	Pourquoi certaines personnes deviennent-elles sans-abris?Why do some people become homeless?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label4 = tk.Label(self, text="4-	Qu’est-ce que tu pourrais faire pour aider les SDF?What could you do to help homeless people?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label5 = tk.Label(self, text="5-	Faut-il construire plus de maisons pour résoudre le problème des sans-abris?Should we build more houses to solve the problem of homelessness?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label6 = tk.Label(self, text="6-	A ton avis est-qu’il y a beaucoup de pauvreté dans ta ville? In your opinion is there a lot of poverty in your town?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label7 = tk.Label(self, text="7-	Pourquoi est-ce que la pauvreté est un problème dans les pays développés?Why is poverty a problem in developed countries?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label8 = tk.Label(self, text="""8-	Est-ce que tu penses que les pays développés doivent aider les gens dans les pays en voie de développement?

Do you think that developed countries have a responsibility to help people in less developed countries?""",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label9 = tk.Label(self, text="9-	Que fait le gouvernement pour résoudre le problème de la pauvreté? What is the government doing to resolve the problem of poverty?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        label10 = tk.Label(self, text="10-	A l’avenir tu crois que le niveau de la pauvreté va augmenter? Pourquoi? In the future do you think that the level of poverty will increase? Why?",bg="#c0392b",fg="white",font=(None,13,"bold")).pack(side="top", fill="x", pady=3)
        button11 = tk.Button(self, text="Module 11",command=lambda: controller.show_frame("F_Module_11"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)
        button12 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e74c3c",width=20,font=(None, 17, "bold")).pack(side="top",pady=3)




class F_Grammar_Booklet(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#c0392b")
        label = tk.Label(self, text="Grammar Booklet", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",bg="#e74c3c",fg="white",command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    print("Main")


