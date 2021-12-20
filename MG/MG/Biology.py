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
        for F in (StartPage, BiologyEquations, BiologyDefinitions, B_Test, B_Revise, BChapter1, BChapter2, BChapter3, BChapter4, BChapter5, BChapter6, BChapter7, BChapter8, BChapter9, BChapter10, BChapter11, BChapter12, BChapter13, BChapter14, BChapter15):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class Biology(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        button1 = tk.Button(self, text="Test", command=lambda: controller.show_frame("B_Test"),bg="#1abc9c",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=0,padx=5,pady=5)
        button2 = tk.Button(self, text="Revise", command=lambda: controller.show_frame("B_Revise"),bg="#1abc9c",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=1,padx=5,pady=5)
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#1abc9c",font=(None,23,"bold"),height=2, width=11).grid(row=0,column=2,padx=5,pady=5)


class B_Test(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#16a085")
        self.controller = controller
        button1= tk.Button(self, text="Chapter 1",command=lambda: controller.show_frame("BTChapter1"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button2= tk.Button(self, text="Chapter 2",command=lambda: controller.show_frame("BTChapter2"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button3= tk.Button(self, text="Chapter 3",command=lambda: controller.show_frame("BTChapter3"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button4= tk.Button(self, text="Chapter 4",command=lambda: controller.show_frame("BTChapter4"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button5= tk.Button(self, text="Chapter 5",command=lambda: controller.show_frame("BTChapter5"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button6= tk.Button(self, text="Chapter 6",command=lambda: controller.show_frame("BTChapter6"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        button7= tk.Button(self, text="Chapter 7",command=lambda: controller.show_frame("BTChapter7"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=2,column=0)
        button8= tk.Button(self, text="Chapter 8",command=lambda: controller.show_frame("BTChapter8"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=2,column=1)
        button9= tk.Button(self, text="Chapter 9",command=lambda: controller.show_frame("BTChapter9"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=2,column=2)
        button10= tk.Button(self, text="Chapter 10",command=lambda: controller.show_frame("BTChapter10"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button11= tk.Button(self, text="Chapter 11",command=lambda: controller.show_frame("BTChapter11"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button12= tk.Button(self, text="Chapter 12",command=lambda: controller.show_frame("BTChapter12"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)
        button13= tk.Button(self, text="Chapter 13",command=lambda: controller.show_frame("BTChapter13"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=4,column=0)
        button14= tk.Button(self, text="Chapter 14",command=lambda: controller.show_frame("BTChapter14"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=4,column=1)
        button15= tk.Button(self, text="Chapter 15",command=lambda: controller.show_frame("BTChapter15"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=4,column=2)
        button16 = tk.Button(self, text="Equations", command=lambda: controller.show_frame("BTEquations"),bg="#1abc9c",fg="white",font=(None, 17, "bold"),width=20).grid(row=5,column=0)
        button17 = tk.Button(self, text="Definitions", command=lambda: controller.show_frame("BTDefinitions"),bg="#1abc9c",fg="white",font=(None, 17, "bold"),width=20).grid(row=5,column=1)
        button6 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=6,column=2)


class B_Revise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        button1= tk.Button(self, text="Chapter 1",command=lambda: controller.show_frame("BChapter1"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=0,column=0)
        button2= tk.Button(self, text="Chapter 2",command=lambda: controller.show_frame("BChapter2"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=0,column=1)
        button3= tk.Button(self, text="Chapter 3",command=lambda: controller.show_frame("BChapter3"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=0,column=2)
        button4= tk.Button(self, text="Chapter 4",command=lambda: controller.show_frame("BChapter4"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=1,column=0)
        button5= tk.Button(self, text="Chapter 5",command=lambda: controller.show_frame("BChapter5"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=1,column=1)
        button6= tk.Button(self, text="Chapter 6",command=lambda: controller.show_frame("BChapter6"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=1,column=2)
        button7= tk.Button(self, text="Chapter 7",command=lambda: controller.show_frame("BChapter7"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=2,column=0)
        button8= tk.Button(self, text="Chapter 8",command=lambda: controller.show_frame("BChapter8"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=2,column=1)
        button9= tk.Button(self, text="Chapter 9",command=lambda: controller.show_frame("BChapter9"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=2,column=2)
        button10= tk.Button(self, text="Chapter 10",command=lambda: controller.show_frame("BChapter10"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=3,column=0)
        button11= tk.Button(self, text="Chapter 11",command=lambda: controller.show_frame("BChapter11"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=3,column=1)
        button12= tk.Button(self, text="Chapter 12",command=lambda: controller.show_frame("BChapter12"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=3,column=2)
        button13= tk.Button(self, text="Chapter 13",command=lambda: controller.show_frame("BChapter13"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=4,column=0)
        button14= tk.Button(self, text="Chapter 14",command=lambda: controller.show_frame("BChapter14"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=4,column=1)
        button15= tk.Button(self, text="Chapter 15",command=lambda: controller.show_frame("BChapter15"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=4,column=2)
        button16 = tk.Button(self, text="Equations", command=lambda: controller.show_frame("BiologyEquations"),bg="#1abc9c",fg="white",font=(None, 17, "bold"), width=20).grid(row=5,column=0,padx=5,pady=5)
        button17 = tk.Button(self, text="Definitions", command=lambda: controller.show_frame("BiologyDefinitions"),bg="#1abc9c",fg="white",font=(None, 17, "bold"), width=20).grid(row=5,column=1,padx=5,pady=5)
        button18 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#1abc9c",width=20,font=(None, 17, "bold")).grid(row=6,column=2)


class BChapter1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 5", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 6", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter7(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 7", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter8(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 8", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter9(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 9", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter10(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 10", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter11(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 11", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter12(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 12", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter13(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 13", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter14(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 14", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()

class BChapter15(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        label = tk.Label(self, text="Chapter 15", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"),bg="#1abc9c",fg="white")
        button.pack()



class BiologyEquations(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#16a085")
        self.controller = controller
        label = tk.Label(self, text="This is Biology", font=controller.title_font,fg="white", bg="#1abc9c")
        label.pack(side="top", fill="x", pady=10)
        
        def clickBiologyEquations():
            try:
                file=open("Biology_EQUATIONS.txt","r")
                data=file.read()
                file.close()
            except IOError:
                file=open("Biology_EQUATIONS.txt","w+")
                file.write("Photosynthesis: carbon dioxide + water = glucose + oxygen,Light Dependent Stage Equation: H2O = H+ + O2,Light Independent Stage Equation: H+ + CO2 = C6 H12 O6,Aerobic Cellular Respiration: glucose + oxygen = carbon dioxide + water + energy,Aerobic Cellular Respiration: C6 H12 O6 + 6O2 = 6CO2 + 6H2O + 36ATP,Glycolysis: glucose = 2 pyruvate + 2ATP,Krebs Cycle: pyruvate = carbon dioxide + 2ATP,Electron Transport Chain Equations: H+ + O2 = H2O ADP + P = 32ATP,Anaerobic Word Equation (Animals): glucose = lactic acid + 2ATP,Anaerobic Word Equation (Plants): glucose = ethanol + carbon dioxide + 2ATP")
                data=file.read()
                file.close()
            biology_equations=data.split(',') 
            temp=random.choice(biology_equations)
            used=[]
            used.append(temp)
            biology_equations.remove(temp)
            label.configure(text=temp)
        button=tk.Button(self, text="Equations",command=clickBiologyEquations,fg="white",bg="#1abc9c",width=10,font=(None,20,"bold"))
        button.pack(side="top",padx=5,pady=5)
        button1=tk.Button(self, text="Definitions",command=lambda: controller.show_frame("BiologyDefinitions"),fg="white",bg="#1abc9c",width=10,font=(None,20,"bold"))
        button1.pack(side="top",padx=5,pady=5)
        button2 = tk.Button(self, text="Go Back",
        command=lambda: controller.show_frame("StartPage"),fg="white",bg="#1abc9c",width=10,font=(None,20,"bold"))
        button2.pack(side="top",padx=5,pady=5)

class BiologyDefinitions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#16a085")
        S = tk.Scrollbar(self)
        T = tk.Text(self, height=4 , width =100, bg="white")
        S.pack(side="right", fill="y")
        T.pack(side="top")
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        definitions="""Abdomen:   lower region of   body. In humans it contains   digestive organs, kidneys, etc.
Acid rain: Rain that is made acidic by dissolved gases, such as sulphur dioxide, produced by   burning of fossil fuels.
Active site:   area on an enzyme where   reactants bind.
Active transport: Movement of substances against a concentration gradient and/or across a cell membrane, using energy.
Adaptation: Special feature that makes an organism particularly well suited to   environment where it lives.
Adult cell cloning: Process in which   nucleus and adult cell of one animal is fused with an empty egg from ano r animal.   embryo which results is placed inside   uterus of a third animal to develop.
Aerobic respiration: Breaking down food using oxygen to release energy for   cells.
Algal cells:   cells of algae, single-celled or simple multicellular organisms, which can photosyn sise but are not plants.
Allele:  A version of a particular gene.
Alveoli:   tiny air sacs in   lungs which increase   surface area for gaseous exchange.
Amino acids:   building blocks of a protein.
Amylase:   enzyme made in   salivary glands and   pancreas which speeds up   breakdown of starch into simple sugars.
Anaerobic respiration: Breaking down food without oxygen to release energy for   cells.
Antibiotic: Drug that destroys bacteria inside   body without damaging human cells.
Antigen: Toxins on   surface of   cell.  y are recognised by   immune system as 'self' or 'non-self'
Aorta:   main artery leaving   left ventricle carrying oxygenated blood to   body
Asexual budding: A form of asexual reproduction where a complete new individual forms as a bud on   parent organism e.g. yeast, hydra
Artery: Blood vessel which carries blood away from   heart. It usually carries oxygenated blood and it has a pulse.
Asexual reproduction: Reproduction that involves only one individual with no fusing of gametes to produce   offspring.   offspring are identical to   parent.
Atria:   small upper chambers of   heart.   right atrium receives blood from   body and   left atrium receives blood from   lungs.
Auxin; A plant hormone that controls   responses of plants to light (phototropism) and to gravity (gravitropism)
Bacteria; Single celled microorganisms that can reproduce very rapidly. Many bacteria are useful, e.g. gut bacteria and decomposing bacteria, but some cause disease.
Bacterial colony: A population of billions of bacteria grown in culture
Biconcave:   shape of   red blood cells - a disc which is dimpled inwards on both sides.
Bile: Yellowy-green liquid made in   liver and stored in   gall bladder. It is released into   small intestine and emulsifies fats.
Biodiversity:   number and variety of different organisms found in a specified area.
Biofuel: Fuel produced from biological material which is renewable and sustainable.
Biogas: Methane produced from biological material which is renewable and sustainable.
Biological detergent: Washing detergent that contains enzymes.
Biomass: Biological material from living or recently living organisms.
Bladder:   organ where urine is stored until it is released from   body.
Blood:   liquid which is pumped around   body by   heart. It contains blood cells, dissolved food, oxygen, waste products, mineral ions, hormones and o r substances needed in   body or needing to be removed from   body.
Blood circulation system:   system by which blood is pumped around   body.
Blood vessel: Tube which carries blood around   body, i.e. arteries, veins and capillaries.
Breathing: Physical movement of air into and out of   lungs. In humans this is brought about by   action of intercostal muscles on   ribs and   diaphragm.
Breathing system:   system involved in ventilation:   ribs, intercostal muscles, diaphragm as well as   lungs and   tubes which bring air into   body from   outside.
Capillaries:   smallest blood vessels which run between individual cells.  y have a thick wall which is only one cell thick.
Carbohydrase: Enzyme which speeds up   breakdown of carbohydrates.
Carbon cycle:   cycle of carbon through   living and non-living world
Carbon Neutral: A process which uses as much carbon dioxide as it produces.
Carnivore: Animal that eats o r animals.
Carrier: Individual who is heterozygous for a faulty allele that causes a genetic disease in   homozygous form.
Catalyst: speeds up chemical reaction. Remains chemically unchanged unless denatured.
Cell membrane:   controls in and out
Cell wall: A rigid structure which surrounds   cells of living organisms apart from animals.
Cellulose: A big carbohydrate molecule which makes up a plant and algal cell walls.
Central nervous system (CNS): A system made up of   brain and spinal cord where information is processed
Chlorophyll:   green pigment contained in   chloroplasts.
Chloroplasts:   organelles in which photosyn sis takes place.
Chromosome: Threadlike structure carrying   genetic information found in   nucleus of a cell.
Clone: Offspring produced by asexual reproduction which is identical to its parent organism.
Competition:   process by which living organisms compete with each o r for limited resources such as food, light or reproductive partners.
Compost heap: A site where garden rubbish and kitchen waste or decomposed by microorganisms.
Concentration Gradient:   gradient between an area where a substance is at a high concentration and an area where it is at a low concentration.
Contraceptive pill: A pill containing female sex hormones which is used to prevent conception.
Core body temperature:   internal temperature of   body.
Coronary artery: An artery that carries oxygenated blood to   muscle of   heart.
Culture medium: A substance containing   nutrients needed for microorganisms to grow.
Cuticle:   waxy covering of a leaf (or an insect) which reduces water loss from   surface.
Cystic fibrosis: A genetic disease that affects   lungs, digestive and reproductive systems. It is inherited through a recessive allele.
Cytoplasm: A water-based gel in which   organelles of all living cells are suspended.
Decomposer: Microorganism that breaks down waste products and dead bodies.
Ecology:   scientific study of   relationship between living organisms and  ir environment.
Effector organs: Muscles and glands which respond to impulses from   nervous system.
Electron microscope: An instrument used to magnify specimens using a beam of electrons.
Embryonic stem cell: Stem cell with   potential to form a number of different specialised cell types, which is taken from an early embryo.
Emulsifiers: Breaks down into tiny droplets which form an emulsion.
Endemic: Species evolved is in isolation and is found in only one place in   world; it is said to be particular to that area.
Environmental isolation: This is when   climate changes in one area where an organism lives but not in o rs.
Enzyme: Protein molecule which acts as a biological catalyst. It changes   rate of chemical reactions without being affected itself at   end of   reaction.
Epidemic: When more cases of an infectious disease are recorded than would normally be expected.
Epidermal tissue:   tissue made up of relatively unspecialised cells which line   tubes and organs of   body.
Eutrophication: Process by which excessive nutrients in water lead to very fast plant growth. When   plants die  y are decomposed and this uses up a lot of oxygen so   water can no longer sustain animal life.
Evaporation:   change of a liquid to a vapour at a temperature below its boiling point.
Evolution:   process of slow change in living organisms over a long period of time as those best adapted to survive and breed successfully.
Evolutionary relationship: Model of   relationships between organisms, often based on DNA evidence, which suggests how long ago  y evolved away from each o r and how closely related  y are in evolutionary terms.
Evolutionary tree: Model of   evolutionary relationships between different organisms based on  ir appearance, and increasingly, on DNA evidence.
Exchange surface: A surface where materials are exchanged
Extinction:   permanent loss of all   members of   species.
Extremophile: Organism which lives in environments that are very extreme.
Fatty acids: Building blocks of lipids.
Fermentation:   reaction in which   enzymes in yeast turn glucose into ethanol and carbon dioxide.
Fertile soil: A soil containing enough minerals to supply   crop plants with all   nutrients needed for healthy growth.
Fertiliser: A substance provided for plants that supplies  m with essential nutrients for growth.
Fossil fuel: Fuel obtained from long dead biological material.
FSH: Female hormone that stimulates   eggs to mature in   ovaries, and   ovaries to produce hormones, including oestrogen.
Gamete: Sex cell which has half   chromosome number of an ordinary cell.
Gaseous exchange: Exchange of gases.
Gene: A short section of DNA carrying genetic information.
Genetic disorder: Disease which is inherited.
Genetic engineering/modification: A technique for changing   genetic information of a cell.
Genetic material:   DNA which carries instructions for making a new cell or a new individual.
Geographical isolation: This is when two populations become physically isolated by geographical feature.
Glandular tissue:   tissue which makes enzymes and hormones and also secretes chemicals.
Glucagon: A hormone involved in   control of blood sugar levels.
Glycerol: Building block of lipids.
Glycogen: Carbohydrate stored in animals, including   muscles, liver and brain of   human body.
Gravitropism: Response of a plant to   force of gravity controlled by auxin.
Greenhouse effect: Trapping of infrared radiation from   sun as a result of greenhouse gas in   Earth's atmosphere. This maintains   surface of   Earth at a temperature suitable for life.
Greenhouse gas: Gases which absorb infrared radiation from   Earth, and result in   warming up of   atmosphere.
Guard Cells:   cells which surrounds stomata in   leaves of plants and control  ir opening and closing.
Haemoglobin:   red pigment which carries oxygen around   body.
Heart:   muscular organ which pumps blood around   body.
Herbicide: Chemical that kills plants.
Homeostasis:   maintenance of   internal body conditions.
Hydroponics: Growing plants in water enriched by mineral irons ra r than soil.
Hypothermia:   state when   core body temperature falls below   normal average.
Immune response: Response of   immune system to self carrying foreign antigens.
Immune system:   body system which recognises and destroys foreign cells such as invading pathogens.
Immunisation: Giving a vaccine that allows immunity to develop without exposure to   disease itself.
Immunosuppresant drugs: Drugs which suppress your immune system on   recipient of a transplanted organ to prevent rejection.
Impulse: Electrical signal carried along neurons.
Indicator species: Lichens or insects that particularly sensitive to pollution and can be used to indicate changes in   environmental pollution levels.
Inheritance of acquired characteristics: Lamarck's  ory of evolution took place.
Inherited: Passed on from parents to  ir offspring through genes.
Inoculate: To make someone immune to   disease by injecting  m with a vaccine that stimulates   immune system to make antibodies against   disease.
Insulin: Hormone involved in   control of blood sugar levels.
Intercostal muscles: Muscles between   ribs which raise and lower  m during breathing.
Internal environment: Conditions inside   body.
Ion: Charged particle produced by   loss or gain of electrons.
Isomerase: Enzyme which converts one form of a molecule to another
Isotonic: A drink or liquid containing   same concentration of salts as in   body.
Kidney: Organ which filters   blood and removes urea, excess salts and water.
Kidney tubule: Structure in   kidney where substances are reabsorbed back into   blood.
Lactic acid: One product of anaerobic respiration. It builds up in muscles with exercise. Important in yoghurt and cheese making processes.
Light microscope: Instrument used to magnify specimens using lenses and light.
Lipase: Enzyme which breaks down fats and oils into fatty acids and glycerol.
Liver: A large organ in   abdomen which carries out a wide range of functions in   body.
Malnourished: Condition when   body does not get a balanced diet.
Meiosis: Two stage process of cell division which reduces   chromosome number of   daughter cells. It is involved in making   gametes for sexual reproduction.
Menstrual cycle:   reproductive cycle in women controlled by hormones.
Mesophyll tissue:   tissue in a green plant where photosyn sis takes place.
Metabolic rate:   rate at which   reactions of your body takes place, particularly cellular respiration.
Methane: A hydrocarbon gas with   chemical formula CH4. It makes up   main flammable component of biogas.
Microorganism: Bacteria, viruses and o r organisms that can only be seen using a microscope.
Mineral ion: Chemical needed in small amounts as part of a balanced diet to keep   body healthy.
Mitochondria:   site of aerobic cellular respiration in a cell.
Mitosis: Asexual cell division were two identical cells are formed.
Molecule: Particle made up of two or more atoms bonded toge r.
Motor neuron: Neuron that carries impulses from   central nervous system to   effector organs.
MRSA: An antibiotic-resistant bacterium.
Multicellular organism: Organism which is made up of many different cells which work toge r.
Muscular tissue:   tissue which makes up   muscles.
Mutation: A change in   genetic material of an organism.
Mycoprotein: Food based on   fungus fusarium that grows and reproduces rapidly.
Natural classification system: A classification system based on   similarities between different living organisms.
Natural selection:   process by which evolution takes place. Organisms produce more offspring than   environment can support so those only which are most suited to  ir environment will survive to breed and pass on  ir useful characteristics.
Negative pressure: System when   external pressure is lower than   internal pressure.
Nerve: Balls of hundreds or even thousands of neurons
Neurons: Basic cell of   nervous system which carries minute electrical impulses around   body.
Nitrate ion: Ion which is needed by plants to make proteins.
Nucleus: An organelle found in many living cells containing   genetic information.
Obese: Very overweight, with a BMI of over 30.
Oestrogen: Female sex hormone which stimulates   lining of   womb to build up in preparation for a pregnancy.
Optic Nerve:   nerve carrying impulses from   retina of   eye to   brain.
Oral contraceptive: Hormone contraceptive which is taken by   mouth.
Organ: A group of different tissues working together to carry out a particular function.
Organ system: A group of organs working together to carry out a particular function.
Osmosis:   net movement of water from an area of high concentration to an area of low concentration through a partially permeable membrane.
Ova:   female sex cells, eggs.
Ovary: Female sex organ which contains   eggs and produces sex hormones during   menstrual cycle.
Overweight: Person which carries excess fat and has a BMI between 25 and 30.
Ovipositor: Pointed tube found in many female insects which is used to lay eggs.
Ovulation:   release of a mature egg from   ovary in   middle of   menstrual cycle.
Oxygen Debt: Extra oxygen that must be taken into   body after exercise has stopped to complete   aerobic respiration of lactic acid.
Oxyhaemoglobin: Molecule formed when haemoglobin binds to oxygen molecules.
Pancreas: Organ that produces   hormone insulin and many digestive enzymes.
Pandemic: One more cases of a disease are recorded than normal in a number of different countries.
Parasite: Organism which lives in or on o r living organisms and get some or all of it nourishment from its host organism.
Partially permeable: Allowing only certain substances to pass through.
Pathogen: Microorganism which causes disease
Perfluorocarbon: Chemical which can be used as artificial blood.
Period: Stage in   menstrual cycle when   lining of   womb is lost.
Permanent vacuole: A space in   cytoplasm filled with cell sap.
Pesticide: Chemical that kills animals.
Phloem tissue:   living transport tissue in plants which carries sugars around   plant.
Photosyn sis:   process by which plants make food using carbon dioxide, water and light energy.
Phototropism:   response of a plant to light, controlled by auxin.
Pigment:  coloured molecule.
Pituitary gland: Small gland in brain, produces range of hormones controlling body functions.
Placebo: Stents used in a clinical trial which does not contain any drugs at all.
Plasma:   clear, yellow liquid part of   blood which carries dissolved substances and blood cells around   body.
Plasmid: Extra circle of DNA found in bacterial cytoplasm.
Platelet: Fragment of cell in   blood which is vital for   clotting mechanism to work.
Polydactyly: Genetic condition inherited through a dominant allele is which results in extra fingers and toes.
Polytunnel: Large greenhouse made of plastic.
Positive pressure: A system where   external pressure is higher than   internal pressure.
Progesterone: Female sex hormone used in   contraceptive pill.
Protease: An enzyme that breaks down proteins.
Protein syn sis:   process by which proteins are made on   ribosomes based on information from genes in   nucleus.
Puberty:   stage of development when   sexual organs and   body become adult.
Pulmonary artery: Large blood vessel taking deoxygenated blood from   right ventricle of   heart to   lungs.
Pulmonary vein:   large blood vessel bringing blood into   left atrium of   heart from   lungs.
Pyramid of biomass: A model of   mass of biological material in   organisms at each level of   food chain.
Quadrat: apparatus for sampling organisms in   field.
Quantitative sampling: Sampling which records   numbers of organisms ra r than just   type.
Range:   minimum and maximum values of   independent or dependant variables; important in ensuring that any pattern is detected.
Receptor: Special sensory cell that detects changes in   environment.
Recessive:   characteristics that will show up in   offspring only if both of   alleles are inherited.
Red blood cell: Blood cell which contains pigment haemoglobin.
Reflex arc:   sense organ, sensory neuron, relay neuron, motor neuron and effector organ which bring about a reflex action.
Reflex: A rapid automatic response of   nervous system that does not involve conscious thought.
Rehydrate: To restore water to a system.
Respiration:   process by which food molecules are broken down to release energy for   cells.
Ribosome:   site of protein syn sis in a cell.
Root hair cell: Cell on   root of a plant with microscopic hairs which increases   surface area for   absorption of water from   soil.
Safe medicine: A medicine which does not cause any unreasonable side effects while curing a disease.
Salivary gland: Gland in   mouth which produces saliva containing   enzyme amylase.
Secreting: Releasing chemicals such as hormones or enzymes.
Selective reabsorption:   varying amount of water and dissolved mineral ions that are taken back into   blood in   kidney, depending on what is needed by   body.
Sense organ: Collection of special cells known as receptors which respond to changes in   surroundings.
Sensory neurone: Neurone which carries impulses from sensory organs to   central nervous system.
Sewage: A combination of bodily waste, waste water from homes and rainfall overflow from   street drains.
Sex chromosome: Chromosome which carries   information about   sex of an individual.
Sexual reproduction: Reproduction which involves   fusion of male and female gametes producing genetic variety in   offspring.
Small Intestine: Region of   digestive system where most of   digestion of   food takes place
Solute: Solid which dissolves in a solvent to form a solution.
Specialised: Adapted for a particular function.
Speciation:   formation of a new species.
Species: Group of organisms with many features in common which can breed successfully producing fertile offspring.
Stable medicine:   medicine which does not break down under normal conditions.
Statin: Drug which lowers   blood cholesterol levels and improves   balance of HDLs to LDL.
Stem cell: Undifferentiated cell with   potential to form a wide variety of different cell types.
Stent: A metal mesh placed in   artery which is used to open up   blood vessel by   inflation of a tiny balloon.
Steroid: Drug that is used illegally by some athletes to build muscles and improve performance.
Stimuli: A change in   environment that is detected by sensory receptors.
Stomata: Openings in   leaves which allow gasses to enter and leave   leaf.  y are opened and closed by   guard cells.
Sustainable food production: Methods of producing food which can be sustained over time without destroying   fertility of   land all ocean.
Synapse: Gap between   neurons where   transmission of information is chemical rather than electrical.
Territory: Area where an animal lives and feeds, which it may mark out or defend against o r animals.
Thalidomide: Drug that caused deformities in   fetus when given to pregnant women to prevent morning sickness.
Therapeutic cloning: Cloning by transferring   nucleus of an adult to cell to an empty egg to produce tissues and organs which could be used in medicine.
Thermoregulatory centre:   area of   brain which is sensitive to   temperature of   blood.
Thorax: Upper region of body
Tissue: A group of specialised cells that all carry out   same function.
Tissue culture: Using a small group of cells from a plant to make new plants.
Trachea:   main tube linked with cartilage rings which carries air from   nose and mouth down towards   lungs.
Transect: A measured line or area along which quadrats are made.
Transfusion:   transfer of blood from one person to another.
Transpiration:   loss of water vapour from   leaves of plants through   stomata when  y are opened to allow gas exchange for photosyn sis.
Tuber:  modified part of plant which is used to store food in   form of starch.
Type One Diabetes: Pancreas cannot make Insulin.
Urea: waste product formed by breakdown of amino acids in   liver.
Urine:   liquid produced by kidneys, contains metabolic waste product urea along with excess water and salts from   body.
Vaccination: Introduction of dead/ inactive pathogens into body- stimulates immune system.
Valve: prevents backflow of liquid.
Variegated: Having different colours.
Vein: carries blood away from heart
Vena Cava: Large vein into right atrium
Ventilation: Movement of air in + out of lungs.
Villi: Finger-like projections from lining of   small intestine which increase   surface area for   absorption of digested food into   blood.
Virus: Microorganisms, take over body cells, reproduce rapidly and cause disease.
White blood cells: Engulfs bacteria + makes antibodies and antitoxins.
Wilting:   plants droop if dehydrated or too hot, reduces further water loss + prevents cell damage.
Xenotransplantation: Transplanting tissues or organs from one species to another.
Urobilin: Yellow pigment, comes from breakdown of haemoglobin in liver.
    """
        T.insert(tk.END, definitions)
        button = tk.Button(self, text="Start Page",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#1abc9c",width=10,font=(None,20,"bold"))
        button.pack()
        
print("Biology")

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()



