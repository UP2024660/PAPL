import tkinter as tk
from tkinter import font as tkfont
from tkinter.scrolledtext import ScrolledText
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
        for F in (StartPage, Maths,
                  M_Y1 ,

                  M_Y2,

                  M_AS,

                  M_AS_SM,M_ALP,M_ALS,AS_A_E,AS_Q,AS_E_I,AS_G_T,AS_R1,AS_SLG,AS_C,AS_A_M,AS_B_E,AS_T_R,AS_T_I_E,AS_R2,AS_V,AS_D,AS_I,AS_E_L,AS_R3,AS_Equations,

                  AS_SM_D,AS_SM_MLS,AS_SM_RD,AS_SM_C,AS_SM_P,AS_SM_SD,AS_SM_HT,AS_SM_R1,AS_SM_MM,AS_SM_CA,AS_SM_FM,AS_SM_VA,AS_SM_R2,AS_SM_Equations,

                  AL_A_M,AL_F_G,AL_S_S,AL_B_E,AL_R1,AL_R,AL_T_F,AL_T_M,AL_P_E,AL_R2,AL_D,AL_N_M,AL_I,AL_V,AL_R3,ALP_Equations,

                  ALS_R_C_HT,ALS_C_P,ALS_N_D,ALS_R1,ALS_M,ALS_F_F,ALS_P,ALS_A_F,ALS_F_K,ALS_R2,ALS_Equations) :

            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class Maths(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1 = tk.Button(self, text="YEAR ONE: AS", command=lambda: controller.show_frame("M_Y1"),bg="#3498db",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="YEAR TWO: A ", command=lambda: controller.show_frame("M_Y2"),bg="#3498db",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=1,padx=5,pady=5)
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=2,column=3,padx=5,pady=5)

class M_Y1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1 = tk.Button(self, text="YEAR ONE PURE", command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white",font=(None, 23, "bold"), height=2, width=30).grid(row=0,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="YEAR ONE STATS/MECHANICS", command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white",font=(None, 23, "bold"), height=2, width=30).grid(row=0,column=2,padx=5,pady=5)
        button3 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("Maths"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=2,column=0,padx=5,pady=5)
        button4 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=2,column=2,padx=5,pady=5)


class M_Y2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1 = tk.Button(self, text="YEAR TWO PURE", command=lambda: controller.show_frame("M_ALP"),bg="#3498db",fg="white",font=(None, 23, "bold"), height=2, width=30).grid(row=0,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="YEAR TWO STATS/MECHANICS", command=lambda: controller.show_frame("M_ALS"),bg="#3498db",fg="white",font=(None, 23, "bold"), height=2, width=30).grid(row=0,column=2,padx=5,pady=5)
        button3 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("Maths"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=2,column=0,padx=5,pady=5)
        button4 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=2,column=2,padx=5,pady=5)
            

class M_AS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="Algebraic Expressions",command=lambda: controller.show_frame("AS_A_E"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="Quadratics",command=lambda: controller.show_frame("AS_Q"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="Equations and Inequalities",command=lambda: controller.show_frame("AS_E_I"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button4= tk.Button(self, text="Graphs and Transformations",command=lambda: controller.show_frame("AS_G_T"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button5= tk.Button(self, text="Review Exercise 1 ",command=lambda: controller.show_frame("AS_R1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=1,padx=10,pady=10)
        button6= tk.Button(self, text="Straight Line Graphs",command=lambda: controller.show_frame("AS_SLG"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=2,padx=10,pady=10)
        button7= tk.Button(self, text="Circles",command=lambda: controller.show_frame("AS_C"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=0,padx=10,pady=10)
        button8= tk.Button(self, text="Algebraic Methods",command=lambda: controller.show_frame("AS_A_M"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=1,padx=10,pady=10)
        button9= tk.Button(self, text="The Binomial Expansion",command=lambda: controller.show_frame("AS_B_E"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=2,padx=10,pady=10)
        button10= tk.Button(self, text="Trigonometric Ratios",command=lambda: controller.show_frame("AS_T_R"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=3,column=0,padx=10,pady=10)
        button11= tk.Button(self, text="Trigonometric Identities and Equations",command=lambda: controller.show_frame("AS_T_I_E"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=3,column=1,padx=10,pady=10)
        button12= tk.Button(self, text="Review Exercise 2 ",command=lambda: controller.show_frame("AS_R2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=3,column=2,padx=10,pady=10)
        button13= tk.Button(self, text="Vectors",command=lambda: controller.show_frame("AS_V"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=4,column=0,padx=10,pady=10)
        button14= tk.Button(self, text="Differentiation",command=lambda: controller.show_frame("AS_D"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=4,column=1,padx=10,pady=10)
        button15= tk.Button(self, text="Integration",command=lambda: controller.show_frame("AS_I"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=4,column=2,padx=10,pady=10)
        button16= tk.Button(self, text="Exponentials and Lograithms",command=lambda: controller.show_frame("AS_E_L"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=5,column=0,padx=10,pady=10)
        button17= tk.Button(self, text="Review Exercise 3 ",command=lambda: controller.show_frame("AS_R3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=5,column=1,padx=10,pady=10)
        button18 = tk.Button(self, text="Equations", command=lambda: controller.show_frame("AS_Equations"),bg="#3498db",fg="white",font=(None, 17, "bold"),width=35).grid(row=9,column=0,padx=10,pady=10)
        button19 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_Y1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=1,padx=10,pady=10)
        button20 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)

class M_AS_SM(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="Data Collection",command=lambda: controller.show_frame("AS_SM_D"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="Measures of location and Spread",command=lambda: controller.show_frame("AS_SM_MLS"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="Representations of Data",command=lambda: controller.show_frame("AS_SM_RD"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button4= tk.Button(self, text="Correlation",command=lambda: controller.show_frame("AS_SM_C"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button5= tk.Button(self, text="Probability ",command=lambda: controller.show_frame("AS_SM_P"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=1,padx=10,pady=10)
        button6= tk.Button(self, text="Statistical Distributions",command=lambda: controller.show_frame("AS_SM_SD"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=2,padx=10,pady=10)
        button7= tk.Button(self, text="Hypothesis Testing",command=lambda: controller.show_frame("AS_SM_HT"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=0,padx=10,pady=10)
        button8= tk.Button(self, text="Review Exercise 1",command=lambda: controller.show_frame("AS_SM_R1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=1,padx=10,pady=10)
        button9= tk.Button(self, text="Modelling in Mechanics",command=lambda: controller.show_frame("AS_SM_MM"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=2,padx=10,pady=10)
        button10= tk.Button(self, text="Constant Acceleration",command=lambda: controller.show_frame("AS_SM_CA"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=3,column=0,padx=10,pady=10)
        button11= tk.Button(self, text="Forces and Motions",command=lambda: controller.show_frame("AS_SM_FM"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=3,column=1,padx=10,pady=10)
        button12= tk.Button(self, text="Variable Acceleration",command=lambda: controller.show_frame("AS_SM_VA"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=3,column=2,padx=10,pady=10)
        button13= tk.Button(self, text="Review Exercise 2 ",command=lambda: controller.show_frame("AS_SM_R2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=4,column=0,padx=10,pady=10)
        button14 = tk.Button(self, text="Equations", command=lambda: controller.show_frame("AS_SM_Equations"),bg="#3498db",fg="white",font=(None, 17, "bold"),width=35).grid(row=9,column=0,padx=10,pady=10)
        button15 = tk.Button(self, text="Back", command=lambda: controller.show_frame("M_Y1"),bg="#3498db",fg="white",font=(None, 17, "bold"),width=35).grid(row=9,column=1,padx=10,pady=10)
        button16 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)

class M_ALP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="Algebraic Methods",command=lambda: controller.show_frame("AL_A_M"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="Functions and Graphs",command=lambda: controller.show_frame("AL_F_G"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="Sequences and Series",command=lambda: controller.show_frame("AL_S_S"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button4= tk.Button(self, text="Binomial Expansion",command=lambda: controller.show_frame("AL_B_E"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button5= tk.Button(self, text="Review Exercise 1 ",command=lambda: controller.show_frame("AL_R1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=1,padx=10,pady=10)
        button6= tk.Button(self, text="Radians",command=lambda: controller.show_frame("AL_R"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=2,padx=10,pady=10)
        button7= tk.Button(self, text="Trigonometric Functions",command=lambda: controller.show_frame("AL_T_F"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=0,padx=10,pady=10)
        button8= tk.Button(self, text="Trigonometry and Modelling",command=lambda: controller.show_frame("AL_T_M"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=1,padx=10,pady=10)
        button9= tk.Button(self, text="Parametric Equations",command=lambda: controller.show_frame("AL_P_E"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=2,padx=10,pady=10)
        button10= tk.Button(self, text="Review Exercise 2",command=lambda: controller.show_frame("AL_R2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=3,column=0,padx=10,pady=10)
        button11= tk.Button(self, text="Differentiation",command=lambda: controller.show_frame("AL_D"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=3,column=1,padx=10,pady=10)
        button12= tk.Button(self, text="Numerical Methods ",command=lambda: controller.show_frame("AL_N_M"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=3,column=2,padx=10,pady=10)
        button13= tk.Button(self, text="Integration",command=lambda: controller.show_frame("AL_I"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=4,column=0,padx=10,pady=10)
        button14= tk.Button(self, text="Vectors",command=lambda: controller.show_frame("AL_V"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=4,column=1,padx=10,pady=10)
        button15= tk.Button(self, text="Review Exercise 3",command=lambda: controller.show_frame("AL_R3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=4,column=2,padx=10,pady=10)
        button16 = tk.Button(self, text="Equations", command=lambda: controller.show_frame("ALP_Equations"),bg="#3498db",fg="white",font=(None, 17, "bold"),width=35).grid(row=9,column=0,padx=10,pady=10)
        button17 = tk.Button(self, text="Back", command=lambda: controller.show_frame("M_Y2"),bg="#3498db",fg="white",font=(None, 17, "bold"),width=35).grid(row=9,column=1,padx=10,pady=10)
        button18 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)

class M_ALS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="Regression,Correlation and Hypothesis Testing",command=lambda: controller.show_frame("ALS_R_C_HT"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="Conditional Probability",command=lambda: controller.show_frame("ALS_C_P"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="The Normal Distribution",command=lambda: controller.show_frame("ALS_N_D"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button4= tk.Button(self, text="Review Exercise 1",command=lambda: controller.show_frame("ALS_R1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button5= tk.Button(self, text="Moments ",command=lambda: controller.show_frame("ALS_M"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=1,padx=10,pady=10)
        button6= tk.Button(self, text="Forces and Friction",command=lambda: controller.show_frame("ALS_F_F"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=2,padx=10,pady=10)
        button7= tk.Button(self, text="Projectiles",command=lambda: controller.show_frame("ALS_P"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=0,padx=10,pady=10)
        button8= tk.Button(self, text="Application of Forces",command=lambda: controller.show_frame("ALS_A_F"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=1,padx=10,pady=10)
        button9= tk.Button(self, text="Further Kinematics",command=lambda: controller.show_frame("ALS_F_K"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=2,padx=10,pady=10)
        button10= tk.Button(self, text="Review Exercise 2",command=lambda: controller.show_frame("ALS_R2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=3,column=0,padx=10,pady=10)
        button11 = tk.Button(self, text="Equations", command=lambda: controller.show_frame("ALS_Equations"),bg="#3498db",fg="white",font=(None, 17, "bold"),width=35).grid(row=9,column=0,padx=10,pady=10)
        button12 = tk.Button(self, text="Back", command=lambda: controller.show_frame("M_Y2"),bg="#3498db",fg="white",font=(None, 17, "bold"),width=35).grid(row=9,column=1,padx=10,pady=10)
        button13 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)

#AS PURE
class AS_A_E(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Algebraic Expressions", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

x^ a x x^b = x^ a+b

x^a / x^b = x^a-b

(x^a)^b   =   x^ab

x ^ a/b = b√x^a     = ( b√x) ^ a

x ^ -a = 1/ x^a or (x/y) ^-a = (y/x) ^ a

x^0 = 1



x^ 2 - y ^2 = (x + y) (x - y)



√x   x √y = √xy

√x / √y  = (√x / y )

√x x √x   = (√x)^2 = x

(√x + √y) ( √x - √y) = x- y

Rationalising Denominators

For Fractions in the form  1/ √a , multiply the numerator and denominator by √a

for fractions in the form 1 / a + √b , multiply the numerator and denominator by a - √b

For fractions in the form 1 / a - √b , multiply the numerator and denominator by a + √b


 
""")
        mylist.pack()
        
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_Q(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Quadratics", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Quadratic Equations:

ax^2 + bx + C = 0


Quadratic formula

x = (-b +- √(b^2 - 4ac)) / 2a

Difference of Two Squares:

a^2 - b^2 = (a +b)(a-b)

Completing the Square:

x^2 + bx = ( x + b/2) ^2 - (b/2) ^2

if f(x) =a (x + p)^2 +q , the graph of y = f(x) has a turning point at (-p,q)

The Discriminant:

Discriminant = b^2 - 4ac

Zero Roots:

Zero roots if b^2 - 4ac < 0

One Root:

b^2 - 4ac = 0

Two Roots: b^2 - 4ac > 0

""")
        mylist.pack()
        
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_E_I(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Equations and Inequalities", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Linear simultaneous equations can be solved using elimination or substitution 

B^2 - 4ac > 0 two real solutions

b^2 - 4ac = 0 , one real solutions

b^2 - 4ac < 0 no real solutions


The Values of x for which the curve y = f(x) is below the curve y=g(x) satisfy f(x) < g(x)

the values of x for which the curve y = f(x) is above the curve y = g(x) satsify f(x) > g(x)


y < f(x) represents the points on the coordinate grid below the curve y = f(x)

Y > f(x) represents the point on the coordinate grid above the curve y= f(x)



""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_G_T(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Graphs and Transformations", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
If p is a root of the function f(x), then the graph of y = f(x) touches or crosses the x-axis at the point (p,0).

The graphs of y = k/x and y = k/ x^2 , where k is a real constant , have asymptotes at x = 0 and y = 0 .

The x - coordinate(s) at the piints of intersection of the curves with equations y = f(x) and y=g(x) are the solution(s) to the equation f(x) = g(x)

The graph of y = f(x) + a is a translation of the graph y = f(x) by the vector ( 0
                                                                                                            a)

The graph of y = f(x + a) is a translation of the graph y = f(x) by the vector ( -a
                                                                                                             0)

The graph of y = af(x) is a stretch of the graph y = f(x) by a scale factor of a in the vertical direction

The Graph of y = f(ax) is a stretch of the graph y = f(x) by a scale factor of 1/ a in the horizontal direction.


The graph of y =- f(x) is a reflection of the graph of y = f(x) in the x-axis

The graph of y = f(-x) is a reflection of the graph of y = f(x) in the y-axis




""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_R1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="REVIEW EXERCISE 1 ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_SLG(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Straight Line Graphs", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

The Gradient m of the line joining the point with coordinates (x1, y1) to the point with coordinates (x2,y2) can be calculated using the formula

m = y2 - y1   /  x2 - x1

The Equation of a straight line can be written in the form y  mx + c, where m is the gradient and (0, c) is the y- intercept

The Equation of a straight line can also be written in the form ax + by + c = 0, where a,b and c are integers.

The equation of a line with a gradient m that passes through the point with coordinates (x1,y1) can be written as y - y1 = m(x- x1)

Parallel Lines have the same gradient

If a line has a gradient m, a line perpendicular to it has a gradient of - 1/m

if two lines are perpendicular, the product of their gradients is -1.

You can find the distance d between (x1,y1) and (x2,y2) by using the formula d = √(x2-x1)^2 + (y2 - y1)^2

The point of intersection of two lines can be found using simultaneous equations

two quantities are in direct proportion when they increase at the same rate.
The graph of these quantities is a straight line through the origin

A mathematical model is an attempt to represent a real-life situation using mathematical concepts.
It is often necessary to make assumptions about the real-life problems in order to create a model.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()
        
class AS_C(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Circles", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


The midpoint of a line segment with endpoints
(x1,y1) and (x2,y2) is (x1 +x2 / 2 , y1 +y2/ 2 ).

The Perpendicular bisector of a line segment AB is the straight line that is perpendicular to AB and passes through the midpoint of AB.

If the gradient of AB is m then the gradient of its perpendicular bisectorm l, will be - 1/m.

The Equation of a circle with centre (0,0) and radius r is x^2 + y^2 = r^2

The equation of the circle with centre (a,b) and radius r is (x - a)^2 + (y-b)^2 = r^2

The equation of a straight line can intersect a circle once, by just touching the circle, or twice. Not all straight lunes will intersect a given circle.

A tangent to a circle is perpendicular to the radius of the circle at the point of intersection.

The perpendicular bisector of a chord will go through the centre of a circle.

If <PRQ = 90* then R lies on the circle with diameter PQ.
The angle in a semicircle is always a right angle

To find the centre of a circle given any three points:
Find the equations of the perpendicular bisectors of two different chords.
Find the coordinates of intersection of the perpendicular bisectors. 
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_A_M(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Algebraic Methods", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

When simplifying an algebraic fraction, factorise the numerator and denominator where possible and then cancel common factors.

You can use long division to divide a polynomial by (x +_ p), where p is a constant.

The factor theorem states that if f(x) is a polynomial then:
If f(p) = 0, then (x-p) is a factor of f(x)
If (x-p) is a factor of f(x), then f(p) = 0

You can prove a mathematical statement is true by deduction. This means starting from known facts or definitions, then using logical steps to reach the desired conclusion.

In a mathematical proof you must
State anyt information or assumptions you are using
Show every step of your proof clearly
Make sure that every step follows logically from the previous step
Make sure you have covered all possible cases
Write a statement of proof at the end of your working.4


To provide an identity you should
Start with the expression on one side of the identity
Manipulate that expression algebraically until it matches the other side
Show every step of your algebraic working.


You can prove a mathematical statement is true by exhaustion. This means breaking the statement into smaller cases and proving each case seperately.

You can prove a mathematical statement is not true by a counter-example. A counter-example is one example that does not work for the statement.
You do not need to give more than one example, as one is sufficient to disprove a statement.
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_B_E(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="The Binomial Expansion", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Pascal's triangle is formed by adding adjacent pairs of numbers to find the numbers on the next row.

The (n +1)th row of Pascal's triangle gives the coefficients in the expansion of (a+b)^n

n! = n x (n-1) x n(-2) x ... x 3 x 2 x 1

You can use factorial notation and your calculator to find entries in Pascal's traingle quickly.
The number of ways of choosing r items from a group of n items is written as nCr or (n   :  nCr  = (n)  =  n! /r!(n-r)!
                                                                                                                          r)                (r)


The rth entry in the nth row of Pascal's traingle is given by ^n-1Cr-1 = (n -1)
                                                                                                    (r-1)

The binomial expansion is:

(a+b)^n = a^n = (n) a^n-1 b + (n) a^n-2 b^2 + .... + (n) a^n-r b ^r + .... + b^n        (n e N) 
                       (1)                (2)                          (r)

where (n ) = n 
         (r  )      C r = n! / r! (n-r)!

In the expansion of (a+b)^n the general term is given by (n) a^n-r b^R
                                                                               (r)

If x is small, the first few terms in the binomial expansion can be used to find an approximate value for a complicated expression.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_T_R(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Trigonometric Ratios", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


This version of the cosine rule is used to find a missing side if you know two sides and the angle between them:

a^2 = b^2 + c^2 - 2bc Cos A

This version fo the cosine rule is used to find an angle if you know all three sides:

cos A = b^2 + c^2 - a^2 / 2bc

This version of the sine rule is used to find the length of a missing side:

a/ sin A = b / sinB = c / Sin C

This version of the sine rule is used to find a missing angle:

Sin A / a = Sin B / b = Sin C / c


The sine rule sometimes produces two possible solutions for a missing angle:

sin θ = sin( 180* - θ)

Area of a triangle = 1/2 ab sin C


The graphs of sine , cosine and tangent are periodic. They repeat themselves after a certain interval.

The graph of y = sinθ : repeates every 360* and crosses the x-axis at ...., -180* , 0, 180*,360*,...
Has a maximum value of 1 and a minimum value of -1

The Graph of y = cosθ: repeates every 360* and crosses the x-axis at ...., -90*,90*,270*,450*,....
Has a maximum value of 1 and a minimum value of -1

The graph of y = tanθ: repeats every 180* and crosses the x-axis at ... -180*,0*,180*,260*,....
has no maximum or minimum value
has vertical asymptotes at x= -90*, x=90*, x=270*,....


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()
        
class   AS_T_I_E(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Trigonometric Identities and Expressions", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

For a point P (x,y) on a unit circle such that OP makes an angle θ with the positive x-axis:
Cosθ = x = x-coordinate of P
sinθ = y = y-coordinates of P
tanθ = y/x = gradient of OP

You can use the quadrants to determine whether each of the trigonometric ratios is positive or negative

                                                                                                                                90*
For an Angle θ in the second quadrant, only sinθ is positive.                   Sin                    |                   All                            For an angle θ in the first quadrant, Sinθ , cosθ and tanθ are all positive.
                                                                                                 180* ------------------------------------------------------------ 0, 360*
For an angleθ in the third quadrant, only tan θ is positive                        Tan                    |                 Cos                           For an angle θ in the fourth quadrant, only cosθ is positive
                                                                                                                                270*

You can use these rules to find sin, cose, or tan of any positive or negative angle using the corresponding acute angle made with the x-axis, θ

sin(180* - θ) = sinθ
cose(180* - θ) = -cosθ               S                           |                                          A
tan(180* - θ) = -tanθ                                               |
                                                                            |
                                ------------------------------------------- |--------------------------------------------
                                                                            |
sin(180* + θ) = -sinθ                                               |                                                       sin(360* - θ) = -sinθ
cos(180* + θ) = -cosθ              T                             |                                                       cos(360* -θ) = cosθ
tan(180* +θ) = tanθ                                                |                                       C              tan(360* - θ) = -tanθ

The Trigonometric ratios of 30*,45* and 60* have exact forms:

sin 30* = 1/2            cos 30* =  √3 / 2       tan30* = 1/ √3 = √3 / 3

sin45* = 1/ √2 = √2 /2       cos45* = 1/ √2  = √2/2           tan45* =1

sin60* = √3 / 2                  cos60* = 1/2                       tan60* = √3

For all values of θ, sin^2θ + cos^2θ = 1

For all values of θ such that cos θ =/ 0 , tan θ = sin θ / cosθ

Solutions to sinθ = k and cosθ = k only exist when -1 <_ k <_ 1
Solutions to tanθ = p exist for all values of p

When you use the inverse trigonometric functions on your calculator, the angle you get is called the principal value

Your calculator will give principal values in the following ranges:

cos^-1 in the range 0 <_ θ <_ 180*

sin^-1 in the range -90* <_ θ <_ 90*

tan^-1 in the range -90* <_ θ <_ 90*


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_R2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Review Exercise 2 ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,""" 
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_V(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Vectors", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


If -> PQ = -> RS then the line segments PQ and RS are equal in length and are parallel.

->AB = ->-BA as the line segment AB is equal in length , parallel and in the opposite direction to BA

Triangle Law for vector addition: -> AB + -> BC = -> AC
if -> AB =a , ->BC = b , and -> AC = c , then a+b = c

Subtracting a vector is equivalent to 'adding a negative vector': a-b = a + (-b)

Adding the vectors ->PQ and -> QP gives the zero vector 0: ->PQ = ->QP = 0

Any vector parallel to the vector a may be written as λa , where λ is a non-zero scalar.

To multiply a column vector by a scalar, multiply each component by the scalar: λ (p) = (λp)
                                                                                                                       (q)    (λq)

To add two column vectors, add the x-components and the y-components (p) + (r) = (p+r)
                                                                                                           (q)    (s)   (q+s)

A unit vector is a vector of length 1. The unit vectors along the x- and y-axes are usually denoted by i and j respectively. i = (1)      j =(0)
                                                                                                                                                                                 (0)           (1)
                                                                                                                                                                                 
For any two-dimensional vector: (p) = pi + qj
                                               (q)

For the vector a = xi + yj = (x) , the magnitude of the vector is given by: |a|   = √x^2 + y^2
                                        (y)

A unit vector in the direction of a is a/ |a|

in general, a point P with coordinates (p,q) has position vector:

-> OP = pi + qj = (p)
                         (q)


->AB = ->OB --- ->OA , where ->OA and ->OB are the position vectors of A and B respectively.

If the point P divides the line segment AB in the ratio λ: u , then

->OP = ->OA + λ / λ +u ->AB

= ->OA + λ / λ+u  (->OB - ->OA)

If a and b are two non-parallel vectors and pa + qb = ra + sb then p = r and q=s



""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_D(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Differentiation", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

The gradient of a curve at a given point is defined as the gradient of the tangent to the curve at that point.

The gradient function, or derivative, of the curve y= f(x) is written as f'(x) or dy/dx
f'(x)= lim h->0 f(x+h) - f(x) / h
The gradient function can be used to find the gradient of the curve for any value of x.

For all real values of n, and for a constant a:

If f(x) = x^n then f'(x) = nx^n-1       if f(x) = ax^n then f'(x) = anx^n-1
if y = x^n then dy / dx = nx^n-1     9f y = ax^n then dy/dx = anx^n-1

For the quadratic curve with equation y = ax^2 + bx + c , the derivative is givem by dy/dx  = 2ax +b

If y =f(x) +_ g(x) then dy/ dx = f'(x) +_ g'(x)

The tangent to the curve y = f(x) at the point with coordinates (a, f(a)) has equation y -f(a) = f'(a)(x-a)

The normal to the curve y=f(x) at the point with coordinates (a, f(a)) has equation y- f(a) = -1 /f'(a) (x-a)

The function f(x) is increasing on the interval [a,b] if f'(x) _> o for all values of x such that a < x < b
The function f(x) is decreasing on the interval [a,b] if f'(x) <_ 0 for all values of x such that a < x < b

Differentiating a function y = f(x) twice gives you the second order derivative , f "(x) or d^2y / dx^2

At any point on the curve y = f(x) where f'(x) = 0 is called a stationary point. For a small positive value h:


Type of stationary point |   f '(x-h)         | f '(x)    |      f'(x+h)
Local maximum            |  Positive       |   0       |     Negative
Local minimum             |  Negative      |   0       |     Positive
-----------------------------------|--------------------|------------|------------------
                                   | Negative       |   0       |     Negative
Point of Inflection          |   Positive         |   0    |        Positive


If a function f(x) has a stationary piint when x = ax, then:

if f " (a) > 0 , the point is a local minimum
if f " (a) < 0 , the point is a local maximum

if f " (a) = 0, the point could be a local minimum, a local maximum or a point of inflection.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AS_I(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Integration", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

If dy / dx = x^n , then y = 1 / n^n+1 +c , n =/ -1
using function notation, if f '(x) = x^n , then f(x) = 1/  n+1 x^n+1 + C , N=/ -1

If dy/dx = kx^n , then y = k / n+1  x^n+1 + c , n =/ -1
using function notation, if f'(x) = kx^n , then f(x) = k/ n+1 x ^n+1 +c ,  n =/ -1
when integrating polynomials, apply the rule of integration seperately to each term.

∫ f' (x)dx = f(x) +c

∫ (f(x) = g(x)) dx = ∫f(x) dx + ∫g (x) dx

To find the constant of integration, c
Integrate the function
substitute the values (x,y) of a point on the curve, or the value of the function at a given point f(x) = k into the integrated function
solve the equation to find c
                                                                                                                                                         b                       b
If f' (x) is the derivative of f(x) for all values of x in the interval [a,b] , then the definite integral is defined as ∫a   f '(x) dx = [f(x)]a = f(b) - f(a)

The area between a positive curve, the x-axis and the lines x = a and x = b is given by
            b
Area = ∫a ydx
where y = f(x) is the equation of the curve.


When the area bounded by a curve and the x-axis is below the x-axis , ∫ ydx gives a negative answer.

You can use definite integration together with areas of trapeziums and traingles to find more complicated areas on graphs.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()


class AS_E_L(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Exponentials and Logarithms", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

For all real values of x:
if f(x) = e^x then f'(x) = e^x
if y = e^x then dy/ dx = e^x

For all real values of x and for any constant k:
if f(x) = e^kx then f'(x) = ke^kx
if y = e^kx then dy / dx = ke^kx

log a N = x is equivalent to a^x = n ( a=/ 1)

The laws of logarithms:

log a x + log a y = loga xy  ( multplication law)
loga x - loga y = loga (x/y)                division law
loga (x^k) = k loga x                         power law

log a ( 1/x ) = log a (x^-1)  = -log a x               the power law whne k = -1
log a a =1                     a > 0, a =/ 1
loga1 = 0                     a > 0, a =/1

Whenever f(x) = g(x), loga f(x) = loga g(x)

e^lnx  = ln (e^x) = x

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()


class AS_R3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Review Exercise 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,""" 
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()
        
class AS_Equations(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#2c3e50")
        mylist = ScrolledText(self)
        mylist.insert(0.0, "ugh")
        mylist.pack()
       
        def clickMathsEquations():
            try:
                file=open("Maths_EQUATIONS.txt","r")
                data=file.read()
                file.close()
            except IOError:
                file=open("Maths_EQUATIONS.txt","w+")
                file.write("Area of Rectangle: l x w, Area of Parrallelogram: b x h, Area of a Triangle: (b x 0.5) x h, Area of a Trapezium: 0.5((a+b)x h), Volume of a cuboid: l x w x h, Volume of a Prism: Area of cross section x length, Volume of a cylinder: pi x(rxr) x h, Volume of a pyramid: 1/3 x area of base x height, Circumference: pi x diameter ( C= pi x d), Circumference: 2 x pi x radius  (C= 2 x pi x r), Area of a circle: pi x radius squared (A= pi x (rxr)), Pythagoras' Theorem: Right angled Triangle: (axa) + (bxb) = (cxc),sin x= opposite/hypotoneuse, cos x= adjacent/hypotoneuse, tan x = opposite/hyponeuse, ax (squared) + bx + c= 0, Speed = distance/time, Density = Mass/volume,Sine rule = a/sinA = b/sinB = c/sinC, Cosine Rule: (axa) = (bxb)+(cxc) -2bc cos(A), area of a triangle: 1/2(ab sin C)")
                data=file.read()
                file.close()
            Maths_equations=data.split(',') 
            temp=random.choice(Maths_equations)
            used=[]
            used.append(temp)
            Maths_equations.remove(temp)
            mylist.delete('1.0','end')
            mylist.insert('end',temp)
        button=tk.Button(self, text="Equations",command=clickMathsEquations,fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button.pack(side="top",padx=5,pady=5)
        button2 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button2.pack(side="top",padx=5,pady=5)



#AS STATS/ MECHANICS



class AS_SM_D(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        
        label = tk.Label(self, text="Data Collection", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        mylist = ScrolledText(self)
        mylist.insert(0.0,""" Census :
Collecting indformation from the entire population

ADVANTAGES:

accurate information

Unbiasded


DISADVANTAGES:

Expensive

Time Consuming

Cannot be used if survey damages/ consumes the population


Sampling:

Collecting information from a sample of the population

Advantages:

Cheaper

Quicker

DISADVANTAGES:

Sample Selection can introduce Sample Bias ( doesn't represnt the population




SAMPLING TECHNIQUES

RANDOM SAMPLING:
Each member of the sample set is chosen at random

Stratified Sampling:

The Population is divided into categories

The sample is selected so that it has the same proportion of each category as the population

Members are selected from each category at random

Quota Sampling:

The population is divided into categories

A quota is set for each category so that the proportion in each category is the same as in the population

Members of the population are selected in order and are only rejected if their category has already met the quota.

Systematic Sampling:

Every nth member of the population is selected (usually starting at a random number less than n)


Opportunity (Convenience) Sampling:

The sample is selected from members of the population which are present in a particular time or place""")
        mylist.pack()
        
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()

class AS_SM_MLS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Measures of location and Spread.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,""" Mean: x̄ = Σx / n

Variance, σ^2 : Variance = Sxx / n

Standard Deviation, σ : σ = √variance

Formula Sheet Equations:

Sxx: Sxx = Σ(Xi - x^-)^2 = ΣXi^2 - (ΣXi)^2 / n

Standard Deviation, σ  : σ  = √Sxx / n = √(Σx^2)/n -  x̄ ^2

Formulae with Frequency:

Mean, x̄ : x̄ =  Σfx/ Σf

Sxx: Sxx = ΣFi(Xi -  x̄ )^2 = ΣFiXi^2 - (ΣFiXi)^2 / ΣFi

For grouped Data:


Use the mid-point of each class as the x-value

n = ΣF = total number of values in the data set
x= the values
f = frequency


Mode: The most common value

Median: The middle Value

Percentiles: xth percentile = (x/100 x n)th value of an ordered list

Quartiles: Lower Quartile ; Q1 = n/4 th value

              Median: Q2 = n/2 th value

              Upper Quartile: Q3 = 3n/4 th value

For discrete data:

if n/4 / n/2 / 3n/4 is a whole number : Find the midpoint of the n/4th / n/2 th / 3n/4th value and the next value

If n/4 / n/2 / 3n/4 is not a whole number: Round up the n/4 /n/2 / 3n/4 and pick this value from the list

Range: Range = Maximum Value - Minimum Value

Interquartile Range, IQR : IQR = Q3- Q1

Interpercentile Range: Xth to Yth interpercentile range = (Yth percentile) - (Xth Percentile)

Coding: A variable x can be coded to y using the following equation:       y = x-a / b

Mean:       ȳ =  x̄  - a / b

Standard Deviation:    σy = σx / b

Converting coded data back into original data:

Rearrange the coding equation to make x the subject:

            x = a + by

             x̄  = a + b ȳ

             σx = bσy



""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()

class AS_SM_RD(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Representations of Data", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Histograms:

Frequency Density = Frequency / Class Width

Area of bar = Frequency

Remember: The class boundaries must meet - you must extend the classes if they do not already meet

Frequency Polygon:

Remember: Use the midpoint of the top of the histogram bars as the coordinates for the crosses


Cumulative Frequency Diagrams:

Remember: Use the Upper Class Boundary as the X-coordinate of each cross

Box Plots:

| -----------------------------|_ _ |____ | ----------------------|                     x x x
minimum value         Q1  Q2    Q3        Maximum value             outliers

The minimum and Maximum values are the highest and lowest values excluding any outliers. 

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()

class AS_SM_C(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Correlation", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Scatter Diagram:
Regression Line: y= ax + b , a= gradietn, b = y-intercept

Explanatory (Independent) Variable: The variable that is causing an effect/ being controlled

Response (Dependent) Variable :  The variable that is affected by the explanatory variable

Interpolation and Extrapolation:

Interpolation: Using a regression line to predict values within the current data range ( usually very reliable)

Extrapolation: Using a regresssion line to predict values outside of the current data range (this may be unreliable)

CORRELATION DOES NOT IMPLY CAUSATION

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()

class AS_SM_P(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Probability", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Probability:

P(A or B) = P(A) +P(B) - P( A and B)

P (not A) = 1 - P(A)

P(A and B) = P(A) x P(B)     (if A and B are independent)

P(A and B) = 0 (if A and B are mutually exclusive)

Venn Diagram:

The total of all the numbers on the venn diragram must add up to 1

Mutually Exclusive:

A and B cannot both occur

Tree Diagrams:

    Spin 1        Spin 2

                    P(R)         R      P(R,R) = P(R) x P(R)
    P(R)     R <
                    P(G)         G    P(R,G) = P(R) x P(G)

        <
                        P(R)       R  P(G,R) = P(G) x P(R)

        P(G)    G <
                        P(G)      G P(G,G)   = P(G) x P(G)

Remember:

P(R and G) = P(R,G) + P(G,R)

P(R) + P(G) = 1

P(R,R) +P(R,G) +P(G,R) + P(G,G) = 1



""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()

class AS_SM_SD(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Statistical Distributions", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Probability Distributions:

DIscrete Variables: Can only take specific Values

Continuous Variables: Can take any value in a given range

Sum: ΣP(X=x) = 1 , the probabilities of all the possible values must add up to 1

Cumulative Distribution Function, F(x):

F(X0) = P(X <_ X0) , add up the probabilities of all x values less than or equal to X0

Discrete Union Distribution:

Every value has the same probability of occuring , P(X=x) = 0.25, x=1,2,3,4

Notation:
              0.1      x=1.2      x     | 1   |  2   | 3  |  4 
P(X=x) = 0.3      x=3      P(X=x)| 0.1| 0.1 |0.3   | 0.5
              0.5      x=4       F(x)   | 0.1| 0.2 | 0.5 | 1


Binomial Distribution:


Notation:

The random variable X with n trials and probability of success, p , is binomially distributed:    X - B(n,p)

Expected Value:  Expected Value = np

Conditions:

1. The number of trials, n , is fixed
2. All of the trials are independent of each other
3. There are only two possible outcomes (success/failure)
4. The probability of succes, p, is constant

Binomial Probability Function:

                        (n)   r        n-r
P(X=r) =           ( r ) p  (1-p)

where: r = number of successes, n = number of trials
p = probability of success, (1-p) = probability of failure
                                                        n        n
P(X=r) = probability of r successes,     r    =     Cr = n! / r!(n-r)!

Binomial Cumulative Distribution Function:

To calculate P(X <_ x):

1. Use statistical tables in the formula book
2. Use your calculator 

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()
        
class AS_SM_HT(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Hypothesis Testing", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Hypothesis Testing:

Level of Significance:

The threshold probability for the test ( the question will usually state this)

The null hypothesis should be rejected if a result falls within a tail which has a probability lower than the signifcance level

For 2-tail tests: remember to halve the level of significance for each tail

Actual Significance Level:

The probability of incorrectly rejecting the null hypothesis
This is the probability of getting a value within the critical region

Acceptance Region:

The set of results for which you would not reject the null hypothesis, e.g. 5<X<_20

Critical Region:

The set of results for which you would reject the null hypothesis , e.g. 0<_ X <_ 4

Critical Value:

The first value which falls inside the critical region, e.g. X=4

IMPORTANT:

watch out for questions which state that the probability of rejection in each tail should be as close to the level of significance as possible (instead of less than it)

Hypthoses:

1 - Tail Tests : Use this if the probability is suspected to have increased )or decreased)| H0: p = 0.2 | H1: p > 0.2 (or p <0.2)

2- Tail Tests : Use this if the probability is suspected to have changed | H0: p = 0.2 | H1: P != 0.2

Where:

P = probability of event occuring
H0 = null hypothesis
H1 = alternative hypothesis

Important: always define what p is before writing your hypothesis

Conclusions:

If the observation falls within the critical region:

There is evidence at the 5% level of significance to reject the null hypothesis and adopt the alternative hypothesis

If the observation falls within the acceptance region:

There is insufficient evidence at the 5% level of significance to reject the null hypothesis

Follow this statement with a description of what this actually mean.
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()

class AS_SM_R1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Review Exercise 1 ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,""" """)
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()

class AS_SM_MM(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Modelling in Mechanics", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Model                                                                                                                                      Modelling assumptions

Particle - Dimensions of the object are negligible                                                                          Massof the object is concentrated at a single point / Rotational forces and air resistance can be ignored

Rod- All dimensions but one are negligible, like a pole or beam                                                     Mass is concentrated along a line/ No thickness / Rigid (does not bend or buckle)

Lamina - Object with area but negligible thickness, like a sheet of paper                                         Mass is distributed across a flat surface

Uniform Body - Mass is distributed evenly.                                                                                  Mass of the object is concentrated at a single point at the geometrical centre of the body - the Centre of Mass

Light Object - Mass of the object is small compared to other masses, like a string or a pulley         Treat object as having zero mass/ Tension the same at both ends of a light string

Inextensible String - A string that does not stretch under load                                                        Acceleration is the same in objects connected by a taut inextensible string

Smooth Surface                                                                                                                       Assume that there is no friction between the surface and any object on it

Rough Surface - If a surface is not smooth, it is rough                                                                 Objects in contact with the surface experience a frictional force if they are moving or acted on by a force

Wire - Rigid thin length of metal                                                                                                Treated as One-Dimensional

Smooth and Light Pulley - all pulleys you consider will be smooth and light                                  Pulley has no mass / Tension is the same on either side of the bead

Bead - Particle with a hole in it for threading on a wire or string                                                    Moves freely along a wire or string / Tension is the same on either side of the bead

Peg - A support from which a body can be suspended or rested                                                   Dimensionless and fixed / Can be rough or smooth as specified in the question

Air resistance - Resisitance experienced as an object moves through the air                                 Usually modelled as being Negligible

Gravity - Force of attraction between all objects. Acceleration due to gravity is denoted by g.          Assume that all objects with mass are attracted towards the earth / Earth's Gravity is uniform and acts vertically downwards / G is constant and is taken as 9.8 ms^-2, unless otherwise stated in the question.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()

class AS_SM_CA(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Constant Acceleration", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Speed :            If acceleration is zero: Speed = Distance / Time

Acceleration:    Change in velocity per unit time: a = v-u / t

SUVAT Equations:

1. s= 1/2 (u+v) t

2. s = ut + 1/2 at ^2

3. s = vt - 1/2 at ^2

4. v = u + at

5. v^2 = u^2 + 2as

where:
s = displacement (in m)
u = initial velocity (in ms^-1)
v + Final Velocity (in ms^-1)
a = acceleration ( in ms^-2)
t = time (in s)




Velocity
   ^                      t
 v |---------------------------------------------------
   |                                      _____ / |
   |        gradient = a ________/          |
   |   __________/                              |    at or (v-u)
   | _____/                                        |
u |/---------------------------------------------------|
   |                                                   |
   |                                                   |
   |_____________________________|____> Time
                                                       t

Displacement = Area of Trapezium
A = 1/2(a+b)h
s = 1/2 (u+v) t


Displacement = Area (bottom rectangle) + Area (traingle under gradient)
s = (u x t) = (1/2 x t x at)
s = ut + 1/2 at^2

Displacement = Area (large rectangle ) - Area (traigle above gradient)
s = (v x t) - (1/2 x t x at)
s= vt - 1/2 at^2

With straight line euqation:

Y = mx + c

v =  at +u

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()
        
class   AS_SM_FM(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Forces and Motions", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Equations:

Fnet = ma

W = mg

Fnet = net/resultant force (N), m = mass(Kg), a = acceleration

W = weight (N), g = acceleration due to gravity (usually 9.8 ms^-2)

Weight, W: Acts vertically downwards on any object with mass

Normal Reaction, R: Acts on any 2 objects which are in contact/ Acts Perpendicular to the surface in contact

Resistance to Motion (Friction, for example): Acta in the opposite direction to the motion ( or potential motion) of an object
Rough surfaces experience friction; smooth surfaces do not.
Asssume that a surface is rough unless you are told it's smooth

Tension, T (and Thrust/Compression):  Acts along the rod/ string/ wire  / Rod/ String/ Wire exerts the same force on both of the objects that it is attched to.
Tension acts away from the object; thrust / compression acts towards the object.







""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()

class AS_SM_VA(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Variable Acceleration ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Differentiation:

V = ds/dt i.e differentiate displacement to get velocity

a = dv/dt, i.e. differentiate velocity to get acceleration

a = d^2s / dt^2 i.e differentiate displacement twice to get acceleration

Integration:

s = S v dt , i.e. integrate velocity to get displacement

v = S a dt , i.e. integrate acceleration to get velocity

Summary:

S differentiate -> V differentiate -> a

S <- intergate    V <- integrate      a

With respect to t

s = displacement
v= velocity
a = acceleration
t=time







""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()

class AS_SM_R2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Review Exercise 2 ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,""" 
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),bg="#3498db",fg="white")
        button.pack()

class AS_SM_Equations(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#2c3e50")
        mylist = ScrolledText(self)
        mylist.insert(0.0, "ugh")
        mylist.pack()
       
        def clickMathsEquations():
            try:
                file=open("Maths_EQUATIONS.txt","r")
                data=file.read()
                file.close()
            except IOError:
                file=open("Maths_EQUATIONS.txt","w+")
                file.write("Area of Rectangle: l x w, Area of Parrallelogram: b x h, Area of a Triangle: (b x 0.5) x h, Area of a Trapezium: 0.5((a+b)x h), Volume of a cuboid: l x w x h, Volume of a Prism: Area of cross section x length, Volume of a cylinder: pi x(rxr) x h, Volume of a pyramid: 1/3 x area of base x height, Circumference: pi x diameter ( C= pi x d), Circumference: 2 x pi x radius  (C= 2 x pi x r), Area of a circle: pi x radius squared (A= pi x (rxr)), Pythagoras' Theorem: Right angled Triangle: (axa) + (bxb) = (cxc),sin x= opposite/hypotoneuse, cos x= adjacent/hypotoneuse, tan x = opposite/hyponeuse, ax (squared) + bx + c= 0, Speed = distance/time, Density = Mass/volume,Sine rule = a/sinA = b/sinB = c/sinC, Cosine Rule: (axa) = (bxb)+(cxc) -2bc cos(A), area of a triangle: 1/2(ab sin C)")
                data=file.read()
                file.close()
            Maths_equations=data.split(',') 
            temp=random.choice(Maths_equations)
            used=[]
            used.append(temp)
            Maths_equations.remove(temp)
            mylist.delete('1.0','end')
            mylist.insert('end',temp)
        button=tk.Button(self, text="Equations",command=clickMathsEquations,fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button.pack(side="top",padx=5,pady=5)
        button2 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS_SM"),fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button2.pack(side="top",padx=5,pady=5)


#A LEVEL PURE

class AL_A_M(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Algebraic Methods", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

To prove a statement by contradiction you start by assuming it is not true. You then use logical steps to show that this assumption leads to something impossible
(either  a contradiction of the assumption or a contradiction of a fact you know to be true). You can conclude that your assumption was incorrect, and original statement was true.

A rational number can be written as a/b , where a and b are integers
An irrational number cannot be expressed in the form s/b , where a and b are integers.

To multiply fractions, cancel any common factors, then multiply the numerators and multiply the denominators.

To divide two fractions, multiply the first fraction by the reciprocal of the second fraction.

A single fraction with two distinct linear factors in the denominator can be split into two seperate fractions with linear denominations. This is called splitting it into partial fractiions:

5/ (x+1)(x-4)            = A / x+1  + B / x-4

The method of partial fractions can also be used when there are more than two distinct linear factors in the denominator:

7 / (x-2)(x+6)(x+3)  = A / x-2 + B / x +6 + c / x+3

A single fractiion with a repeated linear factor in the denominator can be split into two or more seperate fractions:

2x + 9 / (x-5)(x+3)^2          = A / (x-5) + B / (x +3) = C / (x+3)^2

An improper fraction is one whose numerator has a degree equal to or larger than the denominator. An improper fraction must be converted to a mixed fraction before you can express it in partial fractions.

You can either use:
Algebraic division
or the Relationship F(x) = Q(x) x divisor + remainder

to convert an improper fraction into a mixed fraction.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_F_G(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Functions and Graphs", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

A modulus function is , in general,  function of the type y = | f(x) |.
When f (x) _> 0, | f(x)| = f(x)
when f(x) < 0, | f(x)| = -f(x)

To sketch the graph of y = | ax +b|, sketch y = ax + b then reflect the section of the graph below the x-axis in the x-axis.

A mapping is a function if every input has a distinct output. Functions can either be one-to-one or many-to-one.

fg (x) means apply g first, then apply f. fg(x) = f(g(x))

Functions f(x) and f^-1(x) are inverses of each other. ff^-1 (x) = x and f^-1 f(x) = x.

The graphs of y = f(x) and y = f^-1(x) are reflections of each another in the line y = x

The domain of f(x) is the range of f^-1 (x)

The range of f(x) is the domain of f ^-1 (x)

To sketch the graph of y = f | f(x) |
Sketch the graph of y = f(x)
reflect any parts where f(x) < 0 (parts below the x-axis) in the x-axis
remove the parts below the x-axis.


To sketch the graph of y = f(|x|)
sketch the graph of y = f(x) for x _> 0
reflect this in the y- axis.

f(x+a) is a horizontal translation of -a

f(x) + a is a vertical translation of a'

f(ax) is a horizontal stretch of scale factor 1/a

af(x) is a vertical stretch of scale factor a

f(-x) reflects f(x) in the y-axis

-f(x) reflects f(x) in the x-axis.




""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_S_S(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Sequences and Series", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


In an arithmetic sequence, the difference  between consecutive terms is constant.

The formula for the nth term of an arithmetic sequence is un = a + (n-1)d , where a is the first term and d is the common difference

An arithmetic series is the sum of the terms of an arithmetic sequence.
The sum of the first n terms of an arithemtic series is given by sn = n/2 (2a + (n-1)d), where a is the first term and d is the common difference.
You can also write this formula as Sn = n/2 (a+l) where l is the last term.

A geometric sequnce has a common ratio between consecutive terms.

The formula for the nth term of a geometric sequence is un = ar ^ n-1 , where a is the first term and r is the common ratio.

The sum of the first n terms of a geometric series is given by Sn = a(1-r^n) / 1-r , r != 1 or Sn = a(r^n - 1) / r - 1 , r != 1
where a is the first term and r is the common ratio.

A geometric series is convergent if and oly if |r| < 1, where r is the common ratio.
The sum to infinity of a convergent series is given by Sn = u / 1- r

The greek capital letter 'sigma' is used to signify a sum. You write it as ∑. You write limits on the top and bottom to show which terms you are summing.

A recurrence relation to the form Un+1 = f(Un) defines each term of a sequence as a function of the previous term.

A sequence is increasing if Un+1 > Un for all n e N
A sequence is decreasing if Un+1 < Un for all n e N

A sequence is periodic if the terms repeat in a cycle. For a periodic sequence there is an integer k such that Un+k = Un for all n e N.
This value k is called the order of the sequence.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_B_E(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Binomial Expansion", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

This form of the binomial expansion can be applied to negative or fractional values of n to obtain an infinite series:

(1+x)^n = 1 + nx + n(n-1)x^2 / 2!    + n(n-1)(n-2)x^3 / 3! + ... + n(n-1)...(n-r+1)x^r / r!  + ...
The expansion is valid when |x| < n e R.

The expansion of (1 + bx)^n , where n is negative or a fraction, is valid for |bx| < 1 , or |x| < 1/b

The expansion of (a + bx)^n, where n is negative or a fraction, is valid for | b/a x| < 1 or |x| < |a / b|
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_R1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Review Exercise 1 ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,""" 
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_R(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Radians", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

2 π radians = 360* , π radians = 180*  , 1 radian = 180* / π

30* = π / 6 radians , 45* = π / 4 radians , 60* = π / 3 radians
90* = π / 2 radians , 180* = π radians , 360 =*  2π radians.

You need to learn the exact values of the trigonometric ratios of these angles measured in radians.

sin π/6 = 1/2 , cos π/6 = √3 / 2  , tan π/6 = 1/ √3 = √3 / 3
sin π/3 = √3/2,  cos π/3 = 1/2 ,   tan π/3 = √3
sin π/4 = 1/√2 = √2 / 2 , cos π/4 = 1/ √2 = √2/2 , tan π/4 = 1

You can use these rules to find sin, cos or tan of any positive or negative angle measured in radians using the corresponding acute angle made with the x-axis, THETA.
sin(π - θ) = sinθ
sin(π + θ) = -sinθ
sin(2π - θ) = -sinθ

cos(π - θ) = -cosθ
cos(π + θ) = -cosθ
cos(2π - θ) = cos θ

tan(π - θ) = -tanθ
tan(π + θ) = tanθ
tan(2π - θ) = -tanθ

To find the arc length l of a sector of a circle use the formula l = rθ, where r is the radius of the circle and θ is the angle, in radiansm contained by the sector.

To find the area A of a sector of a circle use the formula  A = 1/2 r^2 θ, where r is the radius of the cirlce and θ is the angle, in raidans, contained by the sector.

The area of a segment ina  circle of radius r is A = 1/2 r^2(θ - sinθ)

When θ is small and measured in radians:

sinθ roughly = θ , tanθ roughly = θ , cosθ roughly = 1 - θ^2 /2 

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()
        
class AL_T_F(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Trigonometric Functions", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


sec x = 1 / cos x (undefined for values of x for which cos x = 0)
cosec x = 1/ sin x  ( undefined for values of x for which sin x = 0)
cot x = 1/ tan x (undefined for values of x for which tan x =0)

The graph of y = sec x, x e R, has symmetry in the y-axis and has period 360* or 2 PI radians.
It has vertical asymptotes at all the values of x for which cos x = 0.

The domain of y = sec x is x e R , x != 90* , 270* , 450*,.... or any odd multiple of 90*.
In radians the domain is x e R, x != PI / 2 , 3Pi / 2 , 5PI/ 2, ... or any odd multiple of PI / 2.
The range of y = sec x is y <_ -1 or y _> 1

The graph of y = cosec x , x e R has period 360* or 2 PI radians. It has vertical asymptotes at all the values of x for which sin x = 0.

The domain of y = cosec x is x e R, x != 0*, 180* , 360*, or any mutliple of 180*
In radians the domain is x e R , x != 0, PI, 2 PI , ... or any multiple of PI.
The range of y = cosec x is y <_ -1 or y _> 1.

The graph of y = cot x , x e R, has period 180* or PI radians. It has vertical asymptotes at all the values of x for which tan x = 0.

The domain of y = cot x is x e R , x != 0*, 180*, 360*, .. .. or any multiple of 180*.
In radians the domain is x e R , != 0, PI, 2 PIm ... or any multiple of PI.
The range of y = cot x is y e R.

Sec x = k and cosec x = k have no solutions for -1 < k < 1

You can use the identity sin^2 x + cos^2 x = 1 to probve the following identities:
1 + tan^2 x = sec^2 x
1 + cot^2 x = cosec^2 x

The inverse function of sin x is called arcsin x
The domain of y = arcsin x is - PI / 2 <_ arcsin x <_ PI / 2 or -90* <_ arcsin x <_ 90*

The inverse function of cos x is called arccos x.
The domain of y = arccos x is -1 <_  x <_ 1
The range of y = arccos x is 0 <_ arccos <_ PI or 0* <_ arccos x <_ 180*

The inverse function of tan x is called arctan x
The domain of y = arctan x is x e R
the range of y = arctan x is - PI / 2 <_ arctan x <_ PI/ 2 or -90* <_ arctan x <_ 90*

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_T_M(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Trigonometry and Modelling", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

The addition (or compound-angle) formulae are:

sin(A + B) = sinAcosB + cosAsinB , sin(A-B) = sinAcosB - cosAsinB
cos(A + B) = cosAcosB - sinAsinB , cos(A-B) = cosAcosB + sinAsinB
tan(A +B) = tan A + tanB / 1- tanAtanB , tan(A-B) = tanA - tanB / 1+ tanAtanB

The double angle formulae are:

Sin2A = 2SinAcosA
cos2A = cos^2A - sin^2A = 2cos^2 A -1 = 1 - 2sin^2A
tan 2A = 2tanA / 1 - tan^2A

For positive values of a and b,

asin x +_ b cos x can be expressed in the form Rsin( x +_ALPHA)
a cos x +_ b sin x can be expressed in the form R cos(x -+ ALPHA)

with R > 0 and 0< ALPHA < 90* ( or PI / 2)
where R cos ALPHA = a m and R sin ALPHA = b , and R = RT(a^2 +b^2)

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_P_E(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Parametric Equations", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

A curve can be defined using parametric equations x = p(t) and y = q(t). Each value of the paramtere, t, defines a point on the curve with coordinates (p(t), q(t)).

You can convert between parametric equations and Cartesian equations by using subtitution to eliminate the parameter.

For parametric equations x =p(t) and y =q (t) with Cartesian equation y = f(x):
The domain of f(x) is the range of p(t)
The range of f(x) is the range of q(t)

You can use parametric equations to model real-life situations. In mechanics you will use parametric equations with time as a parameter to model motion in two dimensions.
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_R2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Review Exercise 2 ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,""" 
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()
        
class   AL_D(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Differentiation ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


For small angles, measured in radians:
sinx roughly = x
cos x roughly = 1 - 1/2x^2

if y = sin kx, then dy/dx = k cos kx
if y = cos kx, then dy/dx = - k sin kx

If y = e^kx, then dy/dx = ke^kx
if y = ln x , then dy/dx = 1/x

If y = a^kx , where k is a real constant and a > 0, then dy/dx = a^kx k ln a

The chain rule is: dy/dx = dy/du x du/dx
where y is a function of u and u is another function of x

The chain rule enables you to differentiate a function of a function. In general,
if y = (f(x))^n then dy/dx = n(f(x))^n-1 f'(x)
if y = f(g(x)) then dy/dx = f'(g(x))g'(x)

dy/dx = 1/ dx/dy

The Product rule:
if y = uv then dy/dx = u dv/dx + v du/dx, where u and v are functions of x.
if f(x) = g(x)h(x) then f' (x) = g(x)h'(x) = h(x)g'(x)

The quotient rule:
if y = u/v then dy/dx = (v du/dx - u dv/dx ) / v^2 where u and v are functions of x.
if f(x) = g(x) / h(x)' then f'(x) = h(x)g'(x) - g(x)h'(x) / (h(x))^2

If y = tan kx, then dy/dx = k sec^2 kx
If y = cosec kx , then dy/dx = -k cosec kx cot kx
If y = sex kx, then dy/dx = k sec kx tan kx
if y = cot kx , then dy/dx = -k cosec^2 kx


if y = arcsin x, then dy/dx = 1/ RT 1-x^2
if y = arccos x , then dy/dx = - 1/ RT 1-x^2
if y = arctan x, then dy/dx  = 1 / 1 +x ^2

If x and y are given as functions of a paramter, t: dy/dx = dy/dt / dx/dt

d/dx (f(y)) = f ' (y) dy/dx
d/dx (y^n) = ny ^n-1 dy/dx
d/dx (xy)  = x dy/dx +y

The function f(x) is concave on a given interval if and only if f"*(x) <_ 0 for every value of x in that interval.
The function f(x) is comvex on a given interval if and only if f " (x) _> 0 for every value of x in that interval.

A point of inflection is a point at which f " (x) changes sign

You can use the chain rule to connect rates of change in situations involving more than two variables.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_N_M(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Numerical Methods", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

If the function f(x) is continuous on the interval [a,b] and f(a) and f(b) have opposite sign, then f(x) has at least one root,x , which satisfies a < x < b

To solve an equation of the form f(x) = 0 by an iterative method, rearrange f(x) = 0 into the form x = g(x) and use the iterative formula Xn+1 = g(Xn)

The Newton-Raphson formula for approximating the roots of a function f(x) is:

Xn+1 = Xn -    (  f(Xn) / f ' (Xn) )
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_I(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Integration", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

∫x^n dx = x^n+1 / n + 1 + c , ∫e^x dex = e^x + c, ∫ 1/x dx = ln |x| + c
∫cos x dx = sin x  + c , ∫ sin x dx = - cos x + c , ∫ sec^2 x = tan x + c
∫cosec x cot x dx = -cosec x + c , ∫cosec^2x dx = -cot x + c , ∫sec x tan x dx = sec x + c

∫ f ' (ax + b) dx = 1/a f(ax +b) +c

Trigonometric identities can be used to integrate expressions. This allows an expression that cannot be integrated to be replaced by an identical expression that can be integrated.

To integrate expressions of the form ∫k f' (x) / f(x) dx , try ln | f(x) | and differentiate to check, and then adjust any constant.

To integrate an expression of the form ∫ kf ' (x) (f(x))^n dx, try (f(x))^n+1 and differentiate to check, and then any adjust any constant.

Sometimes you can simplify an integral by changing the variable, This process is similar to using the chain rule in differentiation and is called integration by substitution.

The integration by parts formula is given by: ∫ u dv / dx = uv - ∫ v du/dx dx

Partial fractions can be used to integrate algebraic fractions.

The area bounded by two curves can be found using integration:
                    b                         b              b
Area of R = ∫a  (f(x) - g(x)) dx = ∫a f(x) dx - ∫a g(x) dx

The trapezium rule is:
             b
            ∫a   y dx ~~ 1/2 h (Y0 + 2(Y1 +Y2 ... + Yn-1) + Yn)
            where h = b-a / n and Yi = f(a + ih)

when dy/dx = f(x)g(y) you can write

∫1/ g(y)  dy = ∫ f(x) dx.



""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_V(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Vectors", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

The distance from the origin to the point (x,y,z) is RT (x^2 + y^2 + z^2 )

The distance between the points (x1,y1,z1) an (x2,y2,z2) is RT ( (x1-x2)^2 + (y1 - y2)^2 + (z1-z2)^2 )

The unit vectors along the x- , y- and z- axes are denoted by i, j and k respectively,

i = (1)    j = (0),  k = (0)
     (0)         (1)        (0)
     (0)        (0)         (1)

Any 3D vector can be written in column form as pi + qj + rk = (p)
                                                                                         (q)
                                                                                         (r)

if the vector a = xi + yj + zk makes an angle THETA , with the positive x-axis then cos THETAx =   x / |a| and
similarly for angkes THETA y and THETA z.

if a, b and c are vectors in three dimensions which do not all lie in the same plane then you can compare their coefficients on both sides of an equation.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class AL_R3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Review Exercise 3 ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,""" 
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()


class ALP_Equations(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#2c3e50")
        mylist = ScrolledText(self)
        mylist.insert(0.0, "ugh")
        mylist.pack()
       
        def clickMathsEquations():
            try:
                file=open("Maths_EQUATIONS.txt","r")
                data=file.read()
                file.close()
            except IOError:
                file=open("Maths_EQUATIONS.txt","w+")
                file.write("Area of Rectangle: l x w, Area of Parrallelogram: b x h, Area of a Triangle: (b x 0.5) x h, Area of a Trapezium: 0.5((a+b)x h), Volume of a cuboid: l x w x h, Volume of a Prism: Area of cross section x length, Volume of a cylinder: pi x(rxr) x h, Volume of a pyramid: 1/3 x area of base x height, Circumference: pi x diameter ( C= pi x d), Circumference: 2 x pi x radius  (C= 2 x pi x r), Area of a circle: pi x radius squared (A= pi x (rxr)), Pythagoras' Theorem: Right angled Triangle: (axa) + (bxb) = (cxc),sin x= opposite/hypotoneuse, cos x= adjacent/hypotoneuse, tan x = opposite/hyponeuse, ax (squared) + bx + c= 0, Speed = distance/time, Density = Mass/volume,Sine rule = a/sinA = b/sinB = c/sinC, Cosine Rule: (axa) = (bxb)+(cxc) -2bc cos(A), area of a triangle: 1/2(ab sin C)")
                data=file.read()
                file.close()
            Maths_equations=data.split(',') 
            temp=random.choice(Maths_equations)
            used=[]
            used.append(temp)
            Maths_equations.remove(temp)
            mylist.delete('1.0','end')
            mylist.insert('end',temp)
        button=tk.Button(self, text="Equations",command=clickMathsEquations,fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button.pack(side="top",padx=5,pady=5)
        button2 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_ALP"),fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button2.pack(side="top",padx=5,pady=5)


# A LEVEL STATS

class ALS_R_C_HT(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Regression, Correlation and Hypothesis Testing", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Product Moment Correlation Coefficient (PMCC):
The degree of linear association between two variables.

PMCC,r            Notes
r= +1                Strong Positive Correlation; all points lie exactly on the line

r < +1               Weak(er) positive correlation

r = 0                 No Correlation

r > -1                Weak(er) negative correlation

r = -1                Strong Negative correlation; all points lie exactly on the line


Finding the critical region(s) and Value(s):

1. Use the Critical Values for Correlation Coefficients table

2. Look up the Critical Value in the Product Moment Coefficient section using the sample size and significance level given in the question
        Remember to halve the significance level for a two- tail test


3a. State the Critical Region(s) as follows:

H1                Critical Region(s)

p > 0            r >_ Critical Value

p< 0             r<_ - Critical Value

p =/ 0          r>_ Critical Value AND r<_ - Critical Value

3b.  State the Critical Value(s) as follows:

H1                Critical Value(s)

p > 0             Use the value from the table

p < 0             Use the negative of the value from the table

p =/            There are two critical values:
                 Use the positive of the value from the table
                 And the negative of the value from the table.


PMCC - Hypotheses:

1- Tail Test        Use this if you are testing for a positive ( or negative) correlation                 H0 : p =0
                                                                                                                                    H1: p > 0 (or p<0)

2- Tail Test         Use this if you are testing for any correlation                                           H0: p = 0
                         (i.e. Either Positive or Negative)                                                              H1: p =/ 0

Where: p = Population product Moment Correlation Coefficient
            H0 = Null Hypothesis
            H1 = Alternative Hypothesis

Important: Your Hypotheses must always compare p to zero

PMCC - Conclusions:

If value of r given in question falls inside critical region:

There is evdidence at the 5% level of significance to reject the null hypothesis and adopt the alternative hypothesis

If Value of r given in question falls outside critical region:

There is insufficient evidence at the 5% level of significance to reject the null hypothesis

Follow this statemenrt with a description of what this actually means
e.g, "so there is evidence at the 5% level of significance that the number of hours of revision is positively correlated with the mark achieved in the exam"

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class ALS_C_P(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Conditional Probability", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
General Equations           P(AUB) = P(A) + P(B) - P(A n B)
                                      P(A') = 1 - P(A)

Independent Events         P(A n B) = P(A) x P(B)
                                     P(B|A) = P(B)
                                     Only use this if you are told that the events are independent

Conditional Events           P(A n B)= P(A) X P(B|A)
                                     Use this equation if the events are not independent

Mutually Exclusive Events   P(A n B) = 0
                                        Use this equation if events A and B cannot both occur

Remember:
P(A') is the probability that event A does not occur
P(B|A) is the probability that event B occurs, given that event A also occurs


                                                 B              P(A n B) = P(A) x P(B|A)
                                P(B|A)

                A         <
                                P(B'|A)       B'             P(A n B') =     P(A) X P(B'|A)

P(A)  <                     P(B|A')        B             P(A' n B)  =   P(A') X P(B|A')
                A'         <
                                P(B'|A')       B'           P(A' n B')    =     P(A') X P(B' | A')

Remember:

P(B) = P(B|A) + P(B| A')

P(B') = P(B'|A) + P(B'|A@)
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class ALS_N_D(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="The Normal Distribution", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Notation:
The Variable, D, normally distributed with mean u , and standard deviation, σ, (or variance, σ^2) is written as:
                        X- N ( μ,σ^2)

Normal Distribution:

X - N ( μ, σ^2)

Standard Distribution:
Z - N (0,1)

Equation:         Z = X - μ /  σ

Points of inflection occur at: X = μ +_ σ

P(Z< z1) = 1 - P(Z> z1)                      P(Z<-z1) = P(Z> z1)

Approximation:

A binomial Dostrobution, X - B (n,p), can be approximated to a normal distribution, Y - N (np, np[1-p])

i.e. let the mean of the normal distribution μ = np let the variance of normal distribution σ^2 = np[1-p]

Conditions:

The approximation is valid when:

n is large

p = 0.5

Continuity Correction:

When using a normal distribution, Y, as an approximation to a binomial distribution, X, you must apply one of the following contuinity corrections:

P(X < a) - > P(Y<a - 0.5)
P(X _< a) -> P(Y < a + 0.5)
P(X >_ a) ----> P(Y> a -0.5)
P(X>a) -----> P(Y>a +0.5)
P(X=a) ----> P(a - 0.5 < Y < a + 0.5)



The Sample Mean of  a Normal DIstribution:

For a normally distributed variable, X - N(μ,σ^2) , the mean of a sample of n X-Values,x̄ , is normally distributed with mean, μ, and standard deviation,σ/ √ n :



x̄  - N (μ,σ^2/n)

When calculating the probability of a tail using the cumulative distribution function on your calculator you should enter the Established Mean when asked for the mean and σ/√ n when asked for the standard deviation

Transforming to a standard Normal Distribution:
You can transform the mean of sample,x̄ , into a value on the standard normal distribution, z :

z = (x̄  - μ) / σ/ √ n

This is useful if you have used the Percentage Points of the Normal Distribution table in the date booklet to determine the critical region, as this table gives values for a standard normal distribution

μ = Established mean of X , σ = standard deviation of X
n = Number of X - Values in sample

Population Mean - Hypotheses:

1 - Tail test Use this if the mean is suspected to have increased ( or decreased)              H0: μ = a
                                                                                                                                 H1 : μ > a
                                                                                                                                (or μ <a)

2 - Tail Test  Use this if the mean is suspected to have changed                                    H0: μ = a
                                                                                                                                H1 : μ =/ a

where: μ = the actual mean
           a = the established mean
           H0 = null hypothesis
           H1 = Alternative Hypothesis

Population Mean - Conclusions:

If the mean of the sample falls inside the critical region:
There is evidence at the 5% level of significance to reject the null hypothesis and adopt the alternative hyopthesis

If the mean of the sample falls oitside the critical region:

There is insufficient evidence at the 5% level of significance to reject the null hypothesis

Follow this statement with a description of what this actually means e.g. "so there is evidence at the 5% level of significance that the mean spead of motorists has increased"


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class ALS_R1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Review Exercise 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class ALS_M(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Moments ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Moment Definition:

Moment = Force x Perpendicular Distance

Principle of Moments:

For a rigid object in equilibrium:

Σ Clockwise moments = Σ Anticlockwise Moments



""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class ALS_F_F(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Forces and Friction", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Vector Components:



F = ( Fcosθ)  = (Fcosθ)i + (Fsinθ)j

Important: You must draw a right angle triangle with the original vector as the hypotenuse; the cos θ component is always adjacent to the angle, the sinθ component is always opposite the angle

Resultants and Angles:

Resultant = √Fa^2 = Fb^2

θ = tan ^-1 (Fa/ Fb)


Friction

Friction occurs on rough surfaces
Friction doesn't occur on smooth surfaces,

Friction always acts in the opposite direction to the velocity of the object


Dynamic Friction : for an object that is moving :  F= uR#

Static Friction: For an object which is stationary: <_ uR

F = Fricitional FOrce , u = Coefficient of Friction
R = Normal Reaction between object and the surface.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()
        
class ALS_P(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Projectiles", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Horizontal Motion of a projectile is moddelled as having constant velocity (a=0).

s = vt

The Vertical motion of a projectile is modelled as having constant acceleration due to gravity (a = g)

When a Particle is projected with initial velocity U, at angle α above the horizontal:

The Horizontal Component of the intial Velocity is U cosα

The Vertical Component of the intial velocity is U sin α

A projectile reaches its point of greatest height when the vertical component of its velocity is equal to 0

For a patcile which is projected from a point on a horizontal plane with an initial velocity U at an angle α above the horizontal, and that moves freely under gravity:

Time of Flight : 2 Usin α / g

Time ot reach greatest height:    Usinα / g

Range on horizontal plane = U^2 sin2α / g

Equation of Trajectory: y = x tan α  - gx^2 (1+tan^2 α) / 2 U^2

where y is the vertical height of the particle , x is the horizontal distance from the point of projection, and g is the acceleration due to gravity.
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class ALS_A_F(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Application of Forces", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Static Particles

A particle or rigid body is in static equilibrium if it is at rest and the resultant force acting on the particle is zero.

Friction and Static Particles

The maximum value of the Frictional Force Fmax = uR is reached when the body you are considering is on the point of moving. The body is then said to be in limiting equilibrium

In General, the force of friction F is such that F <_ uR, and the direction of the Frictional Force is opposite to the direction in which the body would move if the frictional force were absent.

For a Rigid Body in static Equilibrium :

The Body is stationary
The Resultant force in any direction is zero
The Resultant moment is zero
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class ALS_F_K(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Further Kinematics", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


If a particle starts from the point with position vector r0, and moves with constant velocity v, then its displacement from its intial position at time t is vt and its

position vector r is given by r = r0 + vt.

For an object moving in a plane with constant acceleration:

v = u + at , r = ut + 1/2 at ^2

where:

U is the initial velocity
A is th acceleration
v is the velocity at time t
r is the displacement at time t


if r = xi + yj , then v = dr / dt = r* = x* i = y* j

and a = dv/ dt = d^2 r / dt^2 = r** = x** i + y**j

 v =  ∫a dt and r =  ∫v dt

 
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()

class ALS_R2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        label = tk.Label(self, text="Review Exercise 2 ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,""" 
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_AS"),bg="#3498db",fg="white")
        button.pack()
        

class ALS_Equations(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#2c3e50")
        mylist = ScrolledText(self)
        mylist.insert(0.0, "ugh")
        mylist.pack()
       
        def clickMathsEquations():
            try:
                file=open("Maths_EQUATIONS.txt","r")
                data=file.read()
                file.close()
            except IOError:
                file=open("Maths_EQUATIONS.txt","w+")
                file.write("Area of Rectangle: l x w, Area of Parrallelogram: b x h, Area of a Triangle: (b x 0.5) x h, Area of a Trapezium: 0.5((a+b)x h), Volume of a cuboid: l x w x h, Volume of a Prism: Area of cross section x length, Volume of a cylinder: pi x(rxr) x h, Volume of a pyramid: 1/3 x area of base x height, Circumference: pi x diameter ( C= pi x d), Circumference: 2 x pi x radius  (C= 2 x pi x r), Area of a circle: pi x radius squared (A= pi x (rxr)), Pythagoras' Theorem: Right angled Triangle: (axa) + (bxb) = (cxc),sin x= opposite/hypotoneuse, cos x= adjacent/hypotoneuse, tan x = opposite/hyponeuse, ax (squared) + bx + c= 0, Speed = distance/time, Density = Mass/volume,Sine rule = a/sinA = b/sinB = c/sinC, Cosine Rule: (axa) = (bxb)+(cxc) -2bc cos(A), area of a triangle: 1/2(ab sin C)")
                data=file.read()
                file.close()
            Maths_equations=data.split(',') 
            temp=random.choice(Maths_equations)
            used=[]
            used.append(temp)
            Maths_equations.remove(temp)
            mylist.delete('1.0','end')
            mylist.insert('end',temp)
        button=tk.Button(self, text="Equations",command=clickMathsEquations,fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button.pack(side="top",padx=5,pady=5)
        button2 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("M_ALS"),fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button2.pack(side="top",padx=5,pady=5)













if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    print("Main")

        


