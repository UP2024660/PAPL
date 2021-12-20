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


class BletchleyPark(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        button1= tk.Button(self, text="Question 1 ",command=lambda: controller.show_frame("BP_R_Question1"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button2= tk.Button(self, text="Question 2",command=lambda: controller.show_frame("BP_R_Question2"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button3= tk.Button(self, text="Question 3",command=lambda: controller.show_frame("BP_R_Question3"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button4= tk.Button(self, text="Question 4",command=lambda: controller.show_frame("BP_R_Question4"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button5= tk.Button(self, text="Question 5",command=lambda: controller.show_frame("BP_R_Question5"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button6= tk.Button(self, text="Question 6",command=lambda: controller.show_frame("BP_R_Question6"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        button7= tk.Button(self, text="Question 7",command=lambda: controller.show_frame("BP_R_Question7"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=2,column=0)
        button8= tk.Button(self, text="Question 8",command=lambda: controller.show_frame("BP_R_Question8"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=2,column=1)
        button9= tk.Button(self, text="Question 9",command=lambda: controller.show_frame("BP_R_Question9"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=2,column=2)
        button10= tk.Button(self, text="Question 10",command=lambda: controller.show_frame("BP_R_Question10"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button11= tk.Button(self, text="Question 11",command=lambda: controller.show_frame("BP_R_Question11"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button12= tk.Button(self, text="Question 12",command=lambda: controller.show_frame("BP_R_Question12"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=3,column=2)
        button13= tk.Button(self, text="Question 13",command=lambda: controller.show_frame("BP_R_Question13"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=4,column=0)
        button14= tk.Button(self, text="Question 14",command=lambda: controller.show_frame("BP_R_Question14"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=4,column=1)
        button15 = tk.Button(self, text="History Topics",command=lambda: controller.show_frame("H_Revise"),fg="white",bg="#f1c40f",width=20,font=(None,17,"bold")).grid(row=5, column=0)
        button16 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None,17,"bold")).grid(row=5, column=3)


class BP_R_Question1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="The Reasons for the location of the site within its surroundings", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="When and Why people first created the site", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="The ways in which the site changed over time", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="How the site has been used throughout History", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="The diversity of activities and people associated with the site", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="The reasons for changes to the site and to the way it was used", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question7(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="Significant times in the site's past: Peak activity, Major developments, Turning Points", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question8(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="The significance of specific features in the physical remains at the site", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question9(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="The importance of the whole site either locally or nationally, as appropiate", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question10(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="The typicality of the site based on a comparison with other similar sites", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question11(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="What the site reveals about everyday life, attitudes and values in particular periods of history", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question12(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="""How the physical remains may prompt questions about the past
and how historians frame these as valid historical enquiries""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question13(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="How the physical remains can inform artistic reconsturctions and other interpretations of the site", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

class BP_R_Question14(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="The challenges and benefits of studying the historic environment", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",fg="white",bg="#f1c40f",command=lambda: controller.show_frame("StartPage"))
        button.pack()

print("BletchleyPark")
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


