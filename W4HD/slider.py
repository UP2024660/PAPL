import tkinter as tk
import random
from tkinter import font as tkfont



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

       
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,choose,slider,sliderif,besthoice,results):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

SCALE_LABELS = {
    0: "Strongly Hate",
    1: "Hate",
    2: "Dislike",
    3: "Neither Like nor Dislike",
    4: "Like",
    5: "Love",
    6: "Strongly Love"
}





class slider(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller= controller
        label=tk.Label(self, text="How much do i like?", font=controller.title_font,fg="white",bg="#2980b9")
        label.grid(row=0,column=0,padx=5,pady=5)
        label1=tk.Label(self,text="X.example",font=controller.title_font,fg="white",bg="#2980b9")
        label1.grid(row=2,column=0,padx=5,pady=5)
        label1=tk.Label(self,text="A.example",font=controller.title_font,fg="white",bg="#2980b9")
        label1.grid(row=4,column=0,padx=5,pady=5)
      
        def scale_labels(value):
          scale.config(label=SCALE_LABELS[int(value)])
          
        def scale_labels2(value):
          scale2.config(label=SCALE_LABELS[int(value)])
        
        scale = tk.Scale(self, from_=min(SCALE_LABELS), to=max(SCALE_LABELS), orient=tk.HORIZONTAL, showvalue=False, length=300, command=scale_labels,fg="white",bg="#3498db")
        scale.grid(row=2,column=1,padx=5,pady=5)
        scale2 = tk.Scale(self, from_=min(SCALE_LABELS), to=max(SCALE_LABELS), orient=tk.HORIZONTAL, showvalue=False, length=300, command=scale_labels2,fg="white",bg="#3498db")
        scale2.grid(row=4,column=1,padx=5,pady=5)


        def show_values():
          
          if int(scale.get()) == 0:
            print("X: Strongly Hate")
          if int(scale.get()) == 1:
            print("X: Hate")
          if int(scale.get()) == 2:
            print("X: Dislike")
          if int(scale.get()) == 3:
            print("X: Neither Like nor Dislike")
          if int(scale.get()) == 4:
            print("X: Like")
          if int(scale.get()) == 5:
            print("X: Love")
          if int(scale.get()) == 6:
            print("X: Strongly Love")

          if int(scale2.get()) == 0:
            print("A: Strongly Hate")
          if int(scale2.get()) == 1:
            print("A: Hate")
          if int(scale2.get()) == 2:
            print("A: Dislike")
          if int(scale2.get()) == 3:
            print("A: Neither Like nor Dislike")
          if int(scale2.get()) == 4:
            print("A: Like")
          if int(scale2.get()) == 5:
            print("A: Love")
          if int(scale2.get()) == 6:
            print("A: Strongly Love")

        button=tk.Button(self, text='Print Values', command= show_values,fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11)
        button.grid(row=5,column=0,padx=5,pady=5)
        button1 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("choose"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=7,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="Next Page",command=lambda: controller.show_frame("sliderif"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=7,column=1,padx=5,pady=5)
        
        button3 = tk.Button(self, text="StartPage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",font=(None,23,"bold"),height=2, width=11).grid(row=7,column=2,padx=5,pady=5)
  



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    print("Main")


