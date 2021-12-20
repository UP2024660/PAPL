import tkinter as tk 
from tkinter import font  as tkfont 
import random
from tkinter import *

from mathsflashcardhope import *            
from ComputerScience import *   

from Finance import *



class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")       
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,
                  Maths,
                  M_Y1 ,M_Y2,

                  M_AS,M_AS_SM,M_ALP,M_ALS,AS_A_E,AS_Q,AS_E_I,AS_G_T,AS_R1,AS_SLG,AS_C,AS_A_M,AS_B_E,AS_T_R,AS_T_I_E,AS_R2,AS_V,AS_D,AS_I,AS_E_L,AS_R3,AS_Equations,

                  AS_SM_D,AS_SM_MLS,AS_SM_RD,AS_SM_C,AS_SM_P,AS_SM_SD,AS_SM_HT,AS_SM_R1,AS_SM_MM,AS_SM_CA,AS_SM_FM,AS_SM_VA,AS_SM_R2,AS_SM_Equations,

                  AL_A_M,AL_F_G,AL_S_S,AL_B_E,AL_R1,AL_R,AL_T_F,AL_T_M,AL_P_E,AL_R2,AL_D,AL_N_M,AL_I,AL_V,AL_R3,ALP_Equations,

                  ALS_R_C_HT,ALS_C_P,ALS_N_D,ALS_R1,ALS_M,ALS_F_F,ALS_P,ALS_A_F,ALS_F_K,ALS_R2,ALS_Equations,

                  ComputerScience, CS_Revise,

                  Component1,Component2,

                  C_DS, C_LO, C_A_P, C_P_P, C_S_A, C_S_D, C_S_E, C_P_C, C_EMLE, C_H_C, C_D_T, C_DR_DT, C_O_SD, C_D_DS, C_OS, C_DT_SS_A, C_DS_IP,

                  Finance,
                  Diploma,

                  D_Unit3,

                  U3_T1,
                  U3T1_1,U3T1_2,U3T1_3,U3T1_4,U3T1_5,U3T1_6,U3T1_7,U3T1_8,

                  U3_T2,
                  U3T2_1, U3T2_2, U3T2_3,

                  U3_T3,
                  U3T3_1, U3T3_2, U3T3_3, U3T3_4 , U3T3_5, U3T3_6, U3T3_7,

                  U3_T4,
                  U3T4_1, U3T4_2, U3T4_3, U3T4_4,

                  U3_T5,
                  U3T5_1, U3T5_2, U3T5_3, U3T5_4, U3T5_5, U3T5_6, U3T5_7,

                  U3_T6,
                  U3T6_1, U3T6_2, U3T6_3, U3T6_4, U3T6_5, U3T6_6,

                  U3_T7,
                  U3T7_1, U3T7_2, U3T7_3,U3T7_4,U3T7_5,U3T7_6
                  ):


            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button1 = tk.Button(self, text="Maths", command=lambda: controller.show_frame("Maths"),bg="#3498db",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=1,column=1,padx=5,pady=5)#bg of frame is #2980b9
        button2 = tk.Button(self, text="Computing",command=lambda: controller.show_frame("ComputerScience"),bg="#3F51B5",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=1,column=2,padx=5,pady=5)#bg of frame is #303F9F
        button4 = tk.Button(self, text="Finance",command=lambda: controller.show_frame("Finance"),bg="#ff7373",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=1,column=4,padx=5,pady=5)#bg of frame is #303F9F
        

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
 




