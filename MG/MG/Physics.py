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
        for F in (StartPage, PhysicsEquations, PhysicsDefinitions, Ph_Test, Ph_Revise, PhChapter1, PhChapter2, PhChapter3, PhChapter4, PhChapter5, PhChapter6, PhChapter7, PhChapter8, PhChapter9, PhChapter10, PhChapter11, PhChapter12, PhChapter13, PhChapter14, PhChapter15):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class Physics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        button1 = tk.Button(self, text="Test", command=lambda: controller.show_frame("Ph_Test"),bg="#34495e",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="Revise", command=lambda: controller.show_frame("Ph_Revise"),bg="#34495e",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=1,padx=5,pady=5)
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#34495e",font=(None,23,"bold"),height=2, width=11).grid(row=0,column=2,padx=5,pady=5)

class Ph_Test(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        button1= tk.Button(self, text="Chapter 1",command=lambda: controller.show_frame("PhTChapter1"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button2= tk.Button(self, text="Chapter 2",command=lambda: controller.show_frame("PhTChapter2"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button3= tk.Button(self, text="Chapter 3",command=lambda: controller.show_frame("PhTChapter3"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button4= tk.Button(self, text="Chapter 4",command=lambda: controller.show_frame("PhTChapter4"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button5= tk.Button(self, text="Chapter 5",command=lambda: controller.show_frame("PhTChapter5"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button6= tk.Button(self, text="Chapter 6",command=lambda: controller.show_frame("PhTChapter6"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        button7= tk.Button(self, text="Chapter 7",command=lambda: controller.show_frame("PhTChapter7"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=2,column=0)
        button8= tk.Button(self, text="Chapter 8",command=lambda: controller.show_frame("PhTChapter8"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=2,column=1)
        button9= tk.Button(self, text="Chapter 9",command=lambda: controller.show_frame("PhTChapter9"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=2,column=2)
        button10= tk.Button(self, text="Chapter 10",command=lambda: controller.show_frame("PhTChapter10"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button11= tk.Button(self, text="Chapter 11",command=lambda: controller.show_frame("PhTChapter11"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button12= tk.Button(self, text="Chapter 12",command=lambda: controller.show_frame("PhTChapter12"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=3,column=2)
        button13= tk.Button(self, text="Chapter 13",command=lambda: controller.show_frame("PhTChapter13"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=4,column=0)
        button14= tk.Button(self, text="Chapter 14",command=lambda: controller.show_frame("PhTChapter14"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=4,column=1)
        button15= tk.Button(self, text="Chapter 15",command=lambda: controller.show_frame("PhTChapter15"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=4,column=2)
        button16 = tk.Button(self, text="Equations", command=lambda: controller.show_frame("PhysicsTEquations"),bg="#34495e",fg="white",font=(None, 17, "bold"),width=20).grid(row=5,column=0)
        button17 = tk.Button(self, text="Definitions", command=lambda: controller.show_frame("PhysicsTDefinitions"),bg="#34495e",fg="white",font=(None, 17, "bold"),width=20).grid(row=5,column=1)
        button6 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=6,column=2)

class Ph_Revise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        button1= tk.Button(self, text="Chapter 1",command=lambda: controller.show_frame("PhChapter1"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button2= tk.Button(self, text="Chapter 2",command=lambda: controller.show_frame("PhChapter2"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button3= tk.Button(self, text="Chapter 3",command=lambda: controller.show_frame("PhChapter3"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button4= tk.Button(self, text="Chapter 4",command=lambda: controller.show_frame("PhChapter4"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button5= tk.Button(self, text="Chapter 5",command=lambda: controller.show_frame("PhChapter5"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button6= tk.Button(self, text="Chapter 6",command=lambda: controller.show_frame("PhChapter6"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        button7= tk.Button(self, text="Chapter 7",command=lambda: controller.show_frame("PhChapter7"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=2,column=0)
        button8= tk.Button(self, text="Chapter 8",command=lambda: controller.show_frame("PhChapter8"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=2,column=1)
        button9= tk.Button(self, text="Chapter 9",command=lambda: controller.show_frame("PhChapter9"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=2,column=2)
        button10= tk.Button(self, text="Chapter 10",command=lambda: controller.show_frame("PhChapter10"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button11= tk.Button(self, text="Chapter 11",command=lambda: controller.show_frame("PhChapter11"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button12= tk.Button(self, text="Chapter 12",command=lambda: controller.show_frame("PhChapter12"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=3,column=2)
        button13= tk.Button(self, text="Chapter 13",command=lambda: controller.show_frame("PhChapter13"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=4,column=0)
        button14= tk.Button(self, text="Chapter 14",command=lambda: controller.show_frame("PhChapter14"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=4,column=1)
        button15= tk.Button(self, text="Chapter 15",command=lambda: controller.show_frame("PhChapter15"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=4,column=2)
        button16 = tk.Button(self, text="Equations", command=lambda: controller.show_frame("PhysicsEquations"),bg="#34495e",fg="white",font=(None, 17, "bold"),width=20).grid(row=5,column=0)
        button17 = tk.Button(self, text="Definitions", command=lambda: controller.show_frame("PhysicsDefinitions"),bg="#34495e",fg="white",font=(None, 17, "bold"), width=20).grid(row=5,column=1)
        button6 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#34495e",width=20,font=(None, 17, "bold")).grid(row=6,column=2)


class PhChapter1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 5", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 6", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter7(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 7", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter8(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 8", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter9(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 9", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter10(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 10", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter11(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 11", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter12(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 12", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter13(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 13", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter14(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 14", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()

class PhChapter15(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        label = tk.Label(self, text="Chapter 15", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#34495e",fg="white")
        button.pack()


class PhysicsEquations(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#2c3e50")
        label = tk.Label(self, text="This is Physics", font=controller.title_font,fg="white", bg="blue")
        label.pack(side="top", fill="x", pady=10)
        
        def clickPhysicsEquations():
            try:
                file=open("physics_EQUATIONS.txt","r")
                data=file.read()
                file.close()
            except IOError:
                file=open("physics_EQUATIONS.txt","w+")
                file.write("Distance =  Speed x Time,Acceleration =  Velocity Difference ÷ Time,Force = Mass x Acceleration,Weight = Mass x Gravitational Field Strength,Efficiency = Useful Energy Out ÷ Total Energy In,HT Momentum = Mass x Velocity,Wave Speed = Frequency x Wavelength,Power =  Energy Transferred ÷ Time,Electrical Power = Current x Potential Difference,Electrical Power = Current^2  x Resistance,Density   =    Mass x Volume.,Work Done = Force x distance moved in direction,Change in Gravitational Potential Engergy = Mass x Gravitational Field Strength x Vertical Height Change,Kinetic Energy = ½ x mass x (speed)^2,Power = Work Done ÷ Time Taken P = E ÷ t.,Energy Transferred = Charge moved x Potential Difference E = Q x V.,Charge = Current x Time Q = I  x t.,Potential Difference = Current x Resistance V =  I   x  R.,Force exerted on a spring = Spring Constant x extension F = k x x.,Moment of a force = Force x distance normal to   direction of   force ,Pressure = Force normal to surface ÷ area of that surface")
                data=file.read()
                file.close()
            physics_equations=data.split(',') 
            temp=random.choice(physics_equations)
            used=[]
            used.append(temp)
            physics_equations.remove(temp)
            label.configure(text=temp)
        button=tk.Button(self, text="Equations",command=clickPhysicsEquations,fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button.pack(side="top",padx=5,pady=5)
        button1=tk.Button(self, text="Definitions",command=lambda: controller.show_frame("PhysicsDefinitions"),fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button1.pack(side="top",padx=5,pady=5)
        button2 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button2.pack(side="top",padx=5,pady=5)

class PhysicsDefinitions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2c3e50")
        self.controller = controller
        S = tk.Scrollbar(self)
        T = tk.Text(self, height=40, width =100,bg="white")
        S.pack(side="right", fill="y")
        T.pack(side="top")
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        definitions="""Acceleration: Rate of change of velocity (affected by mass and force).
Alternating Current (A.C.): An electric current that constantly changes direction.
Ammeter: A device which measures current in series and parallel circuits, measured in amperes (A).
Ampere (A): Unit of electric current.
Charges: These are either positive or negative;  they exert forces on one another. If an object is 'charged'  then it has a set of charges.
Condensation: When a vapour turns to a liquid on cooling, heat is given out during this change.
Direct current (D.C.): An electric current that always flows in   same direction.
Force:  Something, which can cause (1) movement, (2) change in direction (3) change in shape.
Fossil fuel: energy sources derived from remains of ancient biomass, wood turns into coal, and plankton turns into natural gas and crude oil.
Geothermal: An energy source which uses   heat energy from hot rocks which are close to   surface of   Earth.   energy can be utilized to heat water and generate electricity.
Gravitational energy: Energy that an object possesses because it is raised above   ground, for example   gravitational energy of   raised water in a hydroelectric dam.
Gravitational-potential energy:   energy an object possesses because of its position.
Gravity:  force of attraction between two objects.
Isotopes: element has two types of atom, each with different numbers of neutrons.
Joules: unit of energy (J).
Kilowatt: Power is measured in this unit; 1000 watts are equal to 1 kW.
Magnetic: A type of force exhibited by a few metals for example iron, cobalt, nickel.
Mass: amount of material a body or object possess, measure in a unit called kilogram (kg).
National grid:   collective name given to   power stations, transformers, pylons and cables which distribute electricity around   country.
Newton (N):  unit of force.
Non-renewable: Energy sources which are finite, for example coal, oil, gas.
Nuclear fission: A reaction of nucleus where a large unstable nucleus splits apart forming a smaller more stable nucleus.
Nuclear: Form of energy, things that release energy as a result of changes in the nuclei of  their atoms, (radioactive materials).
Ohm ( Ω ):  unit of resistance.
Pivot: A point about which an object can turn for example   pivot on a seesaw.
Potential difference: amount of energy (work done) per unit charge (coulomb) needed to move a charged particle between two points in an electric circuit; voltage.
Pressure:   force acting on a unit area of surface.
Renewable Energy: resources, which are not finite, for example solar, tidal, hydroelectric, wave, wind.
Repulsion: A force, which occurs between two charged objects if  y have similar charges for example 'positive and positive’ (pushing away force).
Resistance:   change in current in an electrical circuit as a result of change in resistance and/or voltage within circuits.
Specific Heat Capacity: This means amount of heat required to raise temperature of 1kg of a substance by one degree Celsius.
Terminal velocity:   constant velocity, which is reached by falling objects travelling in air and other fluids.
Transformer: Devices  which are used to increase or reduce voltage of an A.C. supply, it makes transmission more efficient.
Variable: Describes how something changes.
Velocity: speed of an object in a particular direction.
Voltage: Describes   amount of energy, carried by current.
Voltmeter: Measures voltage.
Volume: This is a measure of   amount of physical space an object possesses, and is measured in units of m3 or cm3.
Weight: A type of force so measured in newtons, it is   gravitational force of attraction between   object and earth.
Work: transfer of energy as a result of work done, ( work (J) = force (N) multiplied by distance (m)).
                    """
        T.insert(tk.END, definitions)
        
        button = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#34495e",width=10,font=(None,20,"bold"))
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()



