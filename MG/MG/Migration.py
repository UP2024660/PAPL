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

class Migration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        button= tk.Button(self, text= "Medieval Britain",command=lambda: controller.show_frame("MedievalBritain"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Early Modern Britain",command=lambda: controller.show_frame("EarlyModernBritain"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Industrial Britain",command=lambda: controller.show_frame("IndustrialBritain"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button3= tk.Button(self, text="Britain since 1900",command=lambda: controller.show_frame("BritainSince1900"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button4= tk.Button(self, text="Timeline",command=lambda: controller.show_frame("Timeline"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button6 = tk.Button(self, text="Revise page",command=lambda: controller.show_frame("H_Revise"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=3,column=2)

class MedievalBritain(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        button= tk.Button(self, text= "Basic Information",command=lambda: controller.show_frame("MB_BasicInformation"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button1= tk.Button(self, text="Jewish Prosecution",command=lambda: controller.show_frame("MB_JewishProsecution"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button2= tk.Button(self, text="Diversity",command=lambda: controller.show_frame("MB_Diversity"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button3= tk.Button(self, text="Attitudes",command=lambda: controller.show_frame("MB_Attitudes"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button4= tk.Button(self, text="Quick Fire Events and Facts",command=lambda: controller.show_frame("MB_QuickFireEvents"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button6 = tk.Button(self, text="Revise page",command=lambda: controller.show_frame("H_Revise"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button7 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None, 17, "bold")).grid(row=3,column=2)


class MB_BasicInformation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="Basic Information", font=controller.title_font,fg="white", bg="#f1c40f")
        label.pack(side="top", fill="x", pady=10)
        
        def clickHistoryM_MB_Info():
            try:
                file=open("History_M_MB_Info.txt","r")
                data=file.read()
                file.close()
            except IOError:
                file=open("History_M_MB_Info.txt","w+")
                file.write("The King's Lands,Church,The King's Power, Technology and Crafts, Trade and Transport, Crusades, Countryside, Plague, Towns, Rebellion")
                data=file.read()
                file.close()
            History_Events=data.split(',') 
            temp=random.choice(History_Events)
            used=[]
            used.append(temp)
            History_Events.remove(temp)
            label.configure(text=temp)
        button=tk.Button(self, text="More Information",command=clickHistoryM_MB_Info,fg="white",bg="#f1c40f",width=20,font=(None,20,"bold"))
        button.pack(side="top",padx=5,pady=5)
        button1=tk.Button(self, text="Medieval Britain",command=lambda: controller.show_frame("MedievalBritain"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold"))
        button1.pack(side="top",padx=5,pady=5)
        button2 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold"))
        button2.pack(side="top",padx=5,pady=5)
        
class MB_JewishProsecution(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Prosecution of Jewish People", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""AGAIN, NO INFO YET....""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Medieval Britains",command=lambda: controller.show_frame("MedievalBritain"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")           

class MB_Diversity(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Diversity within the Country", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""NOTHING HERE YET, STAY TUNED....""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Unit 1.1",command=lambda: controller.show_frame("MedievalBritain"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")
        
class MB_Attitudes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label=tk.Label(self, text="Attitudes towards Immigrants", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1=tk.Label(self,text="""EMPTY SPACE AS OF NOW....""",fg="white",bg="#f1c40f")
        label1.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Medieval Britain",command=lambda: controller.show_frame("MedievalBritain"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")
        button1 = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold")).pack(side="top")


class MB_QuickFireEvents(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f39c12")
        label = tk.Label(self, text="Quick Fire Events", font=controller.title_font,fg="white", bg="#f39c12")
        label.pack(side="top", fill="x", pady=10)
        
        def clickHistoryM_MB_Events():
            try:
                file=open("History_M_MB_Events.txt","r")
                data=file.read()
                file.close()
            except IOError:
                file=open("History_M_MB_Events.txt","w+")
                file.write("1250,1250 onwards,1270,1290,1325,1330s onwards,1354,1370s onwards,1436-1437,1439,1440")
                data=file.read()
                file.close()
            History_Events=data.split(',') 
            temp=random.choice(History_Events)
            used=[]
            used.append(temp)
            History_Events.remove(temp)
            label.configure(text=temp)
        button=tk.Button(self, text="Events",command=clickHistoryM_MB_Events,fg="white",bg="#f1c40f",width=10,font=(None,20,"bold"))
        button.pack(side="top",padx=5,pady=5)
        button1=tk.Button(self, text="Medieval Britain",command=lambda: controller.show_frame("MedievalBritain"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold"))
        button1.pack(side="top",padx=5,pady=5)
        button2 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#f1c40f",width=20,font=(None,20,"bold"))
        button2.pack(side="top",padx=5,pady=5)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


