import tkinter as tk                
from tkinter import font  as tkfont 
import random
from A_C_C import *

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, English, E_Test, E_Revise, A_C_C, A_C_C_Stave_1, ACC_S1_Read, ACC_S1_KQ, ACC_S1_CA, ACC_S1_KT, ACC_S1_BS,A_C_C_Stave_2, ACC_S2_Read, ACC_S2_KQ, ACC_S2_CA, ACC_S2_KT, ACC_S2_BS,A_C_C_Stave_3, ACC_S3_Read, ACC_S3_KQ, ACC_S3_CA, ACC_S3_KT, ACC_S3_BS,A_C_C_Stave_4, ACC_S4_Read, ACC_S4_KQ, ACC_S4_CA, ACC_S4_KT, ACC_S4_BS, ACC_S4_C, A_C_C_Stave_5, ACC_S5_Read, ACC_S5_KQ, ACC_S5_CA, ACC_S5_KT, ACC_S5_BS, A_C_C_Full_Book, A_I_C, A_I_C_Act_1, AIC_A1_Read, AIC_A1_KQ, AIC_A1_CA, AIC_A1_KT, AIC_A1_BS,A_I_C_Act_2, AIC_A2_Read, AIC_A2_KQ, AIC_A2_CA, AIC_A2_KT, AIC_A2_BS, A_I_C_Act_3, AIC_A3_Read, AIC_A3_KQ, AIC_A3_CA, AIC_A3_KT, AIC_A3_BS,AIC_Context, A_I_C_Full_Play,Macbeth, Macbeth_Act_1, Macbeth_Act_1_Read, Macbeth_Act_1_KQ, Macbeth_Act_1_CA, Macbeth_Act_1_KT, Macbeth_Act_1_BS, Macbeth_Act_2, Macbeth_Act_2_Read, Macbeth_Act_2_KQ, Macbeth_Act_2_CA, Macbeth_Act_2_KT, Macbeth_Act_2_BS, Macbeth_Act_3, Macbeth_Act_3_Read, Macbeth_Act_3_KQ, Macbeth_Act_3_CA, Macbeth_Act_3_KT, Macbeth_Act_3_BS, Macbeth_Act_4, Macbeth_Act_4_Read, Macbeth_Act_4_KQ, Macbeth_Act_4_CA, Macbeth_Act_4_KT, Macbeth_Act_4_BS, Macbeth_Act_5, Macbeth_Act_5_Read, Macbeth_Act_5_KQ, Macbeth_Act_5_CA, Macbeth_Act_5_KT, Macbeth_Act_5_BS,Macbeth_Full_Play,Macbeth_Context, A_I_C_J_B,):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class English(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        button1 = tk.Button(self, text="Test", command=lambda: controller.show_frame("E_Test"),bg="#e67e22",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="Revise", command=lambda: controller.show_frame("E_Revise"),bg="#e67e22",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=1,padx=5,pady=5)
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e67e22",font=(None,23,"bold"),height=2, width=11).grid(row=0,column=2,padx=5,pady=5)

class E_Test(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#d35400")
        self.controller = controller
        button1= tk.Button(self, text="A Christmas Carol",command=lambda: controller.show_frame("E_T_ACC"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button2= tk.Button(self, text="An Inspector Calls",command=lambda: controller.show_frame("E_T_AIC"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button3= tk.Button(self, text="Macbeth",command=lambda: controller.show_frame("E_T_Macbeth"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button4= tk.Button(self, text="Poems",command=lambda: controller.show_frame("E_T_Poems"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button5= tk.Button(self, text="Literary Devices",command=lambda: controller.show_frame("E_T_Literary_Devices"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button6 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=6,column=2)


class E_Revise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        button1= tk.Button(self, text="A Christmas Carol",command=lambda: controller.show_frame("A_C_C"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button2= tk.Button(self, text="An Inspector Calls",command=lambda: controller.show_frame("A_I_C"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button3= tk.Button(self, text="Macbeth",command=lambda: controller.show_frame("Macbeth"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button4= tk.Button(self, text="Poems",command=lambda: controller.show_frame("Poems"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button5= tk.Button(self, text="Literary Devices",command=lambda: controller.show_frame("Literary_Devices"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button6 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e67e22",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()




