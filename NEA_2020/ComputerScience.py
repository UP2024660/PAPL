import tkinter as tk                
from tkinter import font  as tkfont
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
        for F in (StartPage,CS_Revise, Component1,Component2, C_DS, C_LO , C_A_P , C_P_P ,  C_S_A , C_S_D , C_S_E , C_P_C , C_EMLE , C_H_C , C_D_T , C_DR_DT , C_O_SD , C_D_DS , C_OS , C_DT_SS_A , C_DS_IP):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class ComputerScience(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        button2 = tk.Button(self, text="Revise", command=lambda: controller.show_frame("CS_Revise"),bg="#3F51B5",fg="white",font=(None, 23, "bold"), height=2, width=11).grid(row=0,column=1,padx=5,pady=5)
        button = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3F51B5",font=(None,23,"bold"),height=2, width=11).grid(row=0,column=2,padx=5,pady=5)

class CS_Revise(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        button3= tk.Button(self, text="Component 1",command=lambda: controller.show_frame("Component1"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=0,column=0)
        button4= tk.Button(self, text="Component 2",command=lambda: controller.show_frame("Component2"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=0,column=2)
        button6 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=3,column=2)


class Component1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        button= tk.Button(self, text= "Data Structures",command=lambda: controller.show_frame("C_DS"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button1= tk.Button(self, text="Logical Operations",command=lambda: controller.show_frame("C_LO"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button2= tk.Button(self, text="Algorithms and Programs",command=lambda: controller.show_frame("C_A_P"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button3= tk.Button(self, text="Principles of Programming",command=lambda: controller.show_frame("C_P_P"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button4= tk.Button(self, text="System Analysis",command=lambda: controller.show_frame("C_S_A"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=1,column=1,padx=10,pady=10)
        button5= tk.Button(self, text="System Design",command=lambda: controller.show_frame("C_S_D"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=1,column=2,padx=10,pady=10)
        button6= tk.Button(self, text="Software Engineering",command=lambda: controller.show_frame("C_S_E"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=2,column=0,padx=10,pady=10)
        button7= tk.Button(self, text="Program Construction",command=lambda: controller.show_frame("C_P_C"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=2,column=1,padx=10,pady=10)
        button8= tk.Button(self, text="Economic, Moral, Legal, Ethical,Cultural issues",command=lambda: controller.show_frame("C_EMLE"),fg="white",bg="#3F51B5",width=37,font=(None, 17, "bold")).grid(row=3,column=1,padx=10,pady=10)
        button9= tk.Button(self, text="Go Back",command=lambda: controller.show_frame("CS_Revise"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=4,column=0,padx=10,pady=10)
        button10 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=4,column=2,padx=10,pady=10)



class C_DS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Data Structures", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Data structures are organised stores of data in a computer's memory. Each data structure has its own strengths and weaknesses that make it suitable for a given situation.

Arrays hold data of a single type in rows and columns; they have one or more dimensions.

The different sections in an array are called 'elements' and are accessed using an index (which usually stats from 0).

A record is a data structure that allows items of data of different types to be stored together in a single file.

Data is removed from linked lists by deleting the node and pointing the item behind it to the item in front of it.

Stacks are  Last-In, First-Out data structures that hold data in the order in which it was entered.

Data is removed or added at the top of the stack.

Queues are First-in, First-Out data structures in which the last piece of data entered is the last of data retrieved.

Tree data structures consist of nodes (leaves) and bracnhes. Nodes contain data and the branches link nodes together.

Linked lists represent each piece of data as a node which holds the data and a link to the next piece of data in the list

Hash tables use mapping functions to calculate where in the table a new piece of data should be stored.


""")
        mylist.pack()
        button = tk.Button(self, text="GO BACK",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")
        
class C_LO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Logical Operations", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Conjunction: both sides of the proposition must be true
Disjunction: Either side of the proposition can be true
Negation: Reverses the truth of a proposition.
Implication: If something is true then we can infer that something else is also true
Commutation: the order does not matter when usinhg conjunction or disjunction
Association: The order does not matter when we link multiple conjunctions or multiple disjunctions; this does not hold true if we start mixing conjunctions and disjunctions.
Double Negation: Two negations cancel each other out
De Morgan's Law: The Negation of disjunctions is the conjunction of the negations.

Commutation law for conjunction P.Q <-> Q.P
Commutation law for disjunction P + Q <-> Q +P
Association law for conjunction T.(P.Q) <-> (T.Q).P
Association law for disjunction T + (P +Q) <-> (T +Q) + P
Distribution law 1            T.(P+Q) <-> (T.P) + (T.Q)
Distribution law 2         T + (P.Q) <-> (T+P).(T+Q)
De Morgan's law for disjunction ---         -- --
                                             P+Q <->P.Q

De Morgan's law for conjunction -------    ---      ----
                                                P.Q <-> P + Q


double negative law =
                            p   <-> P
""")
        mylist.pack()
        button = tk.Button(self, text="GO BACK",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")           

class C_A_P(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Algorithms and Programs", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
       
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Algorithms are a set of mechanical steps which will take a given input and deterministically produce an output.

Pseudocode is a method of representing algorithms whihc is not language specific

Flowcharts are another method of representing algorithms in a diagrammatic format and tend to be used for smaller algorithms

Variables are programming constructs which use identifiers to store information in RAM

The key difference between constants and variables is that once a constant has been assigned a value it cannot change while the program is running.

Local scoped variables will only exits in the code block where they were defined.

Global scoped variables are available throughout the program.

Self-documenting code is code which uses sensible identifiers, good layout and clear code to reduce the need for comments and other forms of documentation.

Parameters provide input into procedures and functions; they become variables within the functions to allow the programmer access.

Procedures do not return values while functions do.

Passing parameters by value will create a copy of the value.

Passing by reference means that if the parameter is changed then the original will also change.

Recursions are functions which call themselves, a type of iteration.

Validation occurs while data is being inputted into a computer system. The common validation  rules are:
    Character check
    Length Check
    Range Check
    Formate Check
    Existence Check
    Check Digit.

Verification occurs after the data has been inputted. The two main methods are double enmtry and proof reading.


Big O is a method of comparing algorithms together and measures the growth in terms of time or space.

The order of growth in Big O, from smallest to largetst, is shown in the table below.

Algorithm                      Time Complexity                 Space complexity
Bubble Sort                      O(n^2)                                     O(1)
Insertion Sort                    O(n^2)                                      O(1)
Quicksort                          O(n log2 n )                             O(log2 n)
Linear Search                      O(n)                                       O(1) 
Binary Search                      O(log2 n)                               O(log2 n)
Dijkstra Graph Search         O(|V|^2 + |E|)                          O(|E| log2 |V|).

The main sorting algorithms are bublle sort, insertion sort and quicksort.

There are two main search algorithms: linear search and binary search.

Dijkstra's shortest path algorithm will find the shortest route in a give map if each edge has a weight.

Sequence is the order in which programming statements are executed.

Selection will choose one of two paths to follow based ona  condition.

Repetition or iteration will repeat a block of code until a condition is met. The three main types of iteration are for, while and repeat/ until loops.

Counters can be used to keep track of where in a loop we have reached and is commonly used as a method of stopping iteration.

Rogue values can also be used to stop iteration by assigning an abnormal value to delimit a string of text or a list of data.

Logical operators are used as part of condiitoms and will form part of a logical expression.

Data compression will reduce the size of data. There are two types of compression; lossy, where data is lost so we get an approximation of the original data and lossless, where no data is lost.

Run length encoding will replace strings of the same characters with a character count.

Dictionary encoding will create a list of commonly occuring sequences and replace all occurenced with a shorter reference in the dictionary.

Huffman encoding will use shorter binary values to represent letters which occur more frequently/






""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")
        
class C_P_P(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Principles of Programming", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

There are many different programming paradigms, each with their own strengths and weaknesses.

Procedural programming languages describe which steps to take to solve a problem and how to completeve each step.

Assembly language instructions consist of two distinct sections; operators, such as ADD or SUB, and operands, which are usually memory addresses.

Visual languages allow code to be created through drag and drop. They are commonly used for learning programming by students.

Event-Driven lamnguages will run functions depending on what events are happening in the system, normally triggered by the user.

Software standards define how code should be written with regard to the structure, naming of identifier and how modules are created. They may also define the specifics of how a language works, but leave the implementation up to other vendors.

Examples of standards include HTML and JavaScript

Object Oriented Languages describe the solution to a problem by creating objects that represent real-world entities.

Classes are templates for real-world objects which have attributes and methods.

Objects are instances of classes and represent a real-world object.

Methods are actions that classes or objects can perform, for example SpinWheel().

Attributes are properties of a class or object such as radius or colour.

Classes can inherit attributes and methods from a Vehicle class. In this example, Car would be a subclass and Vehicle a supercalsss.

Backus Naur Form (BNF) is a way of representing syntax as a context-free grammar. Bnf Contains a number of key elements:
The rule written as <rulename> ::=
Concatenation: elements of the BNF are written next to each other.
<IF> ::= IF <expressions> THEN <statement>
Disjunction: elements are seperated by the symbol | symbol and effectively offer a choice of options
<digit>::= 0|1|2|3|4|5|6|7|8|9
Recursion: allows rules to be iterative
<digits> ::= <digit> | <digit><digits>






""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class C_S_A(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="System Analysis", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

A stakeholder is anyone who has a vested interest in the development of a system, Common Stakeholders include:
User
Programmer
Porject Manager
SYstem Analyst.

Analysis of a computing system will include:
Porblem defintion: The current problems with the system will be investigated and initially agreed upon.

Feasability: An investigation to ensure that the project is feasible by checking the followig factors:
Economic: Is there enough money to pay for the system?
Time: Can the project be done in the timescales allowed?
Technical: Is the technology and expertise neeeded to produce the system available>
Legal: Will the project comply with the laws of the countries it will be released in?

Fact Finding: Gather information needed to accurately define the new system to be built, using the following methods:
Obeservation
Questinnaire
Interview
Collecting documentation

Requirements specification will be produced at the end of analysis

Design is based on requirements specification and is broken down into input, output, processing and storage design.

Testing is where the system is put through its paces to ensure that it has met the requirements and most of the bugs have been fixed.

Part of the deliverables of a project include documentation:
User documentation: A manual on using the system provided to the end user
Technical documentation: Information to allow the system to be maintained

When a project is implemented, one of the followinh methods is used:
Direct
Phased
Pilot
Parallel

Once the system has been deployed, it must be maintained through one of the following methods:
Corrective
Adaptive
Perfective

When devloping systems, different methodologies will be used to implement the systems lifecycle:

Program development techniques cover the various approraches to the design, writing and testing of the programs. Some of the more common ones are:

Incremental Development is where the entire system is broken  down into modules which are designed, implemented and tested before being added to the final product.

Iterative Development will provide a full system upfront but then build upon the functionality as time goes on.

Prototyping is where only a small number of features are implemented combining both Incremental and Iterative approaches.

Systems Lifecycle methodologies are the different ways in which stages of the systems lifecycle can be combined and implemented.

The Waterfall model is a linear approach to the systems lifecycle where each phase is completed fully before moving onto the next.

Agile development is focused on producing software rather than documentation and places value on communication and collaboration. Team meetings are favoured over documentation

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")
        
class C_S_D(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self,text="System Design", font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Common Interface devices, including keyboards and ice, are still in widespread use but are starting to be superseded by other human-computer interaction methods.

Voice input makes use of spoken lamnguage to allow interaction with a computer. It has a number of drawbacks:
Commands have to be phrased in a specific way
Current software is not always able to judge the context or have the knowledge to answe the user.
Acdents or background noise can impact understanding
Slang will not always be interpreted.

Touch screens are a feature of most new devices and can take advantage of gestures.

Force Feedback offers haptic feedback to the user which is adding a new dimension to human-comouter interactions.

Virtual reality uses headsets to immerse the end user in an alternative world where they can interact by moving their bodies. Sensors track a user's movement and translate it into changes in the world the user is seeing.

Augmented reality overlays details onto a live camera feed or projects onto glass.
It will make use of sensors and other data to give the user a more immersive experience.

New system design must be validated before being used to ensure that its implementation will match the requirements.

Prototypes can be used to test out an interface design.

Feedback in initial stages of a new design can be used to improve it before implementation.

Evaluation allows the development company and the customer to decide whether a project has been successful. the key issues that need to be part of any evaluation are:
Ensuring the requirements are met.
Ensuring the system responds in an acceptable timeframe.
Ensuring the product is robust.
Review if the product was developed on cost and on time.
Assess how useable the system is by the end user.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class C_S_E(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Software Engineering", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Software development can be supported by using CASE tools; Computer-Aided Software Engineering.

Analysis and planning tools enable the devloper to create diagrams quickly (for example using UML - Unified Modeling Language), validate requirements and collaborate on every part of analysis.

Design tools allow mock-ups of software to be produced for verification purposes.

Test plans and bug repositories have CASE tools, which help large-scale projects keep track of which tests were run and what bugs were produced.

IDEs offer additional tools to the devloper, such as debugging,  coding frameworks and the ability to manage larger code projects.

Version management will monitor changes to code and will manage how code files are merged back into the master branch to avoid conflicts.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")




class C_P_C(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Program Construction", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Translators take source code and turn into machine code. There are three main types: compliers, assemblers and interpreters.

Intepreters will read, tranlaste and execute the code line by line.

Intermediate Code is produced by a complier but requires an interpretor to run. It allows code to be both compiled and interpreted to provide the benefits of both.

Machine code imnstructions are made up of an opcode and operand.

Assembly langauge uses mnemonics where each one represents a single machine code instruction.

Assemblers will take a two-phase approach:
Phase one - turn symbols into memory addresses and store this in a symbol table
Phase Two - Convert assembly mnemonics into machine code.

Compilers perform the following phases:
Lexical Analysis - removes comments and white space before producing a token stream.
Syntax Analysis - Checks the order of expressions using the token stream .
Machine Code Generation - Matches parts of the syntax to machine code; it will optomise the generated machine code.
Linking - Links the generated machine code to library software; it will add loaders to the code to enable dynamic library linking.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class C_EMLE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Ethical, Moral, Legal and Cultural issues relating to Computer Science", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


The Data Protection Act sets out how those who collect personal and private data may use it. It also covers where this information can be sent and how long it can be kept for.

The Computer Misuse Act makes it illegal to access a computer without consent as well as establishing the penalties for doing so.

The copyright Deisgn and Patents Act sets out who has the right to make money from a particular creative work and how long those rights last.

The regulation of investigatory Powers Act sets out the rules that govern how the UK Government can collect information on its Citizens.

Computers have had an enormous impact on almost every work place imaginable. Some see this impact as a negative one costinng jobs and reducing wages.
Others see it as a very positive one that has created whole new industries.

Advances in Artificial Intelligence have given rise to the prospect of automated decision making. Many are happy that impartial machines will make decisions formerly made by failable humans;
others are dismayed by the idea that a computer could make life-or-death decisions.

Computers have made it easier to publicise the environmental impact of the actions of industies and individuals. But computers themselves require huge amounts of electricity and rare minerals to create and mantain.

The internet has provided a wonderful forum for debate and free exchange of ideas. However, some governments view this freedom of expression as a threat and seek to censor it.

Computers allow us not only to hold vast amounts of personal indformation, but also to analyse it to spot trends and patterns. For some this is useful, for others it is a serious invasion of privacy.

Piracy and offensive communications began long before the invention of the computer but the advent of the internet means that it is quicker and easier than ever before to distribute offensive and illegal materials.

The internet has made the world a c much smaller place. This presents a unique set of challenges to those who are trying to communicate with everyone in this vast global marketplace.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

        
class Component2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        button= tk.Button(self, text= "Hardware and Communication",command=lambda: controller.show_frame("C_H_C"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button1= tk.Button(self, text="Data Transmission",command=lambda: controller.show_frame("C_D_T"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button2= tk.Button(self, text="Data Representation and Data Types",command=lambda: controller.show_frame("C_DR_DT"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button3= tk.Button(self, text="Organisation and Structure of Data",command=lambda: controller.show_frame("C_O_SD"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button4= tk.Button(self, text="Databases and Distributed systems",command=lambda: controller.show_frame("C_D_DS"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=1,column=1,padx=10,pady=10)
        button5= tk.Button(self, text="The Operating System",command=lambda: controller.show_frame("C_OS"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=1,column=2,padx=10,pady=10)
        button6= tk.Button(self, text="Different types of software systems, their attributes",command=lambda: controller.show_frame("C_DT_SS_A"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=3,column=0,padx=10,pady=10)
        button7= tk.Button(self, text="Data Security and Integrity Processes",command=lambda: controller.show_frame("C_DS_IP"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=2,column=0,padx=10,pady=10)
        button8 = tk.Button(self, text="BACK",command=lambda: controller.show_frame("CS_Revise"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=4,column=0,padx=10,pady=10)
        button9 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3F51B5",width=35,font=(None, 17, "bold")).grid(row=4,column=2,padx=10,pady=10)

class C_H_C(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Hardware and Communication", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

A CPU is made up of the following components:
ALU - Arithmetic Logic Unit
Registers
CU - Control Unit.

Machine Code instructions are written in binary and are made up of an opcode and data.

Little Man Computer is a simplified architecture used to help learners understand the basics of low-level programming.

The Fetch-Decode-Execute (FDE) cycle will fetch instructions from memory to be run on the CPU. During the cycle the following registers are used:
MAR - Memory Address Register, which stores the address of the instruction to fetch.
MDR - Memory Data Register, which stores the data or instruction once fetched.
PC - Program Counter, which stores the address of the next insturction to fetch.
CIR - Current Instruction Register, from where the instruction will be decoded and executed.
ACC - Accumulator, which is used to store the results of a calculation.

Cache is fast memory that sits between memory and the CPU. it is used to help remove the impacy of the Von Neumann Bottleneck.

Processors, to improve  the throughput of instructions, perform parts of the FDE cycle concurrently, which is known as pipelining.

A multi-core system is a common architecture where processors have more than one core, allowing multiple processes to be run concurrently.

Parallel systems are made up of multiple processors which can perform multiple operations concurrently. Code must be written in such a way as to take advantage of any parallelism.

Random-Access Memory (RAM) stores the currently running programs, operating systems and user files.

Read-Only Memory (ROM) stores the boot-up software required to initialise the hardware, load settings and initiate the operating system (OS).

Input devices provide data for processing and come in the form of scanners, optical character recognition, optical mark recognition, barcodes, magnetic ink recognition, touch screens and sensors.

Storage Devices store data and programs when the computer is powered down.
The main types of storage Device are:
Magnetic - Back-Up Tape and hard drives.
Optical - CD, DVD and Blu-Ray
Solid State - Solid State hard drives, memory sticks and Secure Digital (SD) cards.

Redundant Arry of Independent Discs (RAID) arrays are used in servers and for more data-critical systems. They allow multiple drives to be connected together to form a single drive.
RAID arrays can provide fault tolerance in the form of mirroring and parity bits.

Storage Area Networks (SAN) can connect numerous different types of storage device as a single device.

Virtual Storage will abstract the type of storage device in a SAN, allowing devices to be added and removed without having to administer the individual devices.

Networks rely on the use of protocols and standards to ensure that communication between devices can occur even if those devices were produced by different companies.

Client-Server-Based architecture is where a powerful computer (known as a server) provides functionality to the rest of the network (a service). This can include providing files, websites or databases.

Peer-To-Peer networks have no server; rather each computer has the same status as the other. These networks are commonly used for file sharing.

Error detection ensures that packets arriver at their destination without corruption.
Common Erro detection methods include:
Parity Bits: Adding additional bits to make the number of ones odd or even, depending on the type of parity chosen.
Echo: Packets are returned from the destination and then compared by the sender.
Checksum: Calculations are performed on the packet generating a checksum that is sent with the packet; this calculation is repeated and the checksums compared.

Protocols are a set of rules that govern communication.

Handshaking is a process that devices undertake when a connection is set up. This is where the set of protocols to be used is agreed.

Protocol stacks allow the seperation of logic for each protocol, enabling different parts of the stack to be swapped.

Transmission Control Protocol/Internet Protocol (TCP/IP) stack is the most common protocol stack used in networking.

HyperText Transfer Protocol (HTTP) is used for the transmission of webpages and webpage components. HTTP uses port 80.

HTTPS (secured) is a secure version of HTTP and communicates over port 443. Certificates and the Secure Sockets Layer (SSL) protocol are used to secure communication.

File Transfer Protocol (FTP) uses port 21 and allows files to be transmitted.

The Transport layer of TCP/IP uses either of TCP or UDP:
TCP provides a streamlike communication with error detetction, ordering of packets and confirmation that packets have been recieved.
UDP (User Datagram Protocol) is a fire-and-forget approach with minimal protections.

IP is a network layer protocol that provides routing. It uses the end-to-end principle where each node is considered to be unreliable and therefore each node is asked to perfom routing.

Common Networking Hardware includes:
Network Interface Card: allows a computer to connect to the network.
Hub: connects multiple computers and packets are broadcast to all connected devices.
Switch: Allows multiple devices to be connected and provides routing by Media Access Control (MAC) address.
Router: Connects different networks together and uses IP addresses for routing; Commonly used to connect to the internet.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class C_D_T(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Data Transmission", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

When data is transmitted over a network it is broken down into packets. Each packet will have a header and footer attached which is generated by the protocols employed to transmit that packet.

Duplex mode signifies which direction packets can travel at any given time:
Duplex ( or Full Duplex); both ways at the same time
Half Duplex: both ways but not at the same time
Simplex: one direction only.

Bit Rate is the measure of how much data can be transmitted in a second. Measured as Mbps, or Megabits per second.

Packet switching is where each packet will take an independent route through a network.

Circuit switching is where all packets will follow the same route.

""")
        mylist.pack()

        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class C_DR_DT(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Data Representation and Data Types", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

File sizes are measured using magnitudes of bytes, from smallest to largest; byte, kilobyte, megabyte, gigabyte , terabyte, and petabyte.

Binary is base 2 and can be used to represent numbers; every column can be determined by the formula 2^n , where n is the column number starting at 0.

Hexadecimal is base 16 and uses the letters A-F to represent values 10-15.

Characters are encoded by giving each of them a number. That number can then converted into binary.

ASCII uses 7 bits to store characters while unicode uses 16 bits. Unicode can be used to represent symbols from other languages such as Japanese.

The Key data types are character, string, Boolean, integer and real.

Two's complement and sign-magnitude are methods of storing negative numbers in Binary. Both use the most significant bit to represent negative numbers. 1 always means negative.

Binary addition uses carries if the result of the addition is greater than 1.

Binary subtraction is easier if yoiu convert the number to be subtracted into a negative two's complement number.

Floating point numbers are made up of a mantissa and an exponent.

Normalised floating point numbers will always start with either 01 or 10.

Overflow is when a number is too large for the number of bits being used to represent it.

Underflow is whne a number is too small for the number of bits being used to represent it.




""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class C_O_SD(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Organisation and Structure of Data", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Fixed length records are made up of a number of fields, each one having a specific data type and size.

Common data types include integer, float, string, date and Boolean.

Estimating file size requires the size of single records to be calculated, multiplied by the number of records and 10% added on for metadata.

Files are opened in one of three modes: Append, Read and Write.

Files are read by iterating over records using end of file (EOF) to end the loop.

Serial files store records by a primary key field.

Indexed sequential files will have an index which will points to groups of related records.

Inserting and deleting from sequential and index sequential files require a new file to be created and the file to be re-organised

Multi-level indexes can speed up access to groups of records in larger files.

Random  access files are broken into block of records.

Records are added to blocks by using a hash function.

Hash functions take a key and calculate a block number. Their key design goal is to ensure a wide spread of blocks for any given set of inputs.

By looking at the bumber of collisions, you can compare hash functions.

Master files store all data while transaction files store data currently being worked on.

Transaction files are used to speed up access for day-to-day processing of data.

Backing up files will be based on a policy set up by a  company. It will consider how often the back-up will occur, when it should be taken, how long it will be kept and where it will be stored.

Archiving is the process of moving old files to a seperate system in order to speed up the main one.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")
        
class C_D_DS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Databases and Distributed Systems", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


Flat file databases store information in a single large table.

relational databases store data in many smaller tables, linked otgether using keys.

Primary keys are unique attributes that can be used to identify a record ina  table.

Foreign keys are the primary keys form another table and are used to link tables together.

Entity relationship models visually describe the relationships between the different entities in a database.

Normalisation is the process of converting a flat file database into a relational one.

An index is a data structure used to shorten the length of time it takes to search a database.

There are different stages of  Normalisation. The nost common is third normal form (3NF). A table is in third normal form if it contains no transitive dependencies.

Structured Query Language (SQL) is used to create, edit and delete data in databases.

Referential Integrity is needed to ensure that the foreign keys in one table refer to a primary key in another.

Data mining and predictive analytics allow analysis of big data to uncover patterns and predict future outcomes.

Database views allow a restricted view of the entire database for performance and security reasons.

Database management systems allow users and databases to be managed.
They also implement the data dictionary which stores all of the metadata of the database.

Distributed databases split an organisation's data need between multiple database servers.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class C_OS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="The Operating System", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

System software manages the hardware and software of the computer.

The operating system is responsible for memory management, process management and managing devices.

A range of utility software is available to help mantain the system. These include file management, compression, task manager and anti-virus software.

Memory management is done through two mechanisms: Paging and Segmentation.

Pages are blocks of memory of fixed size that are referenced through a paging table. The Paging table contains the page number and offset to physical memory.

Each process has a virtual address space which is translated by the memory unit to physical address by the formula

Address = page number * page size + offset

Segmentation allows blocks of memory to be used, which are variable in size.

Each segment is stored in a segmentation table and will record the ID, start address and length for each segment.

Segments are commonly used to store library software or other blocks of data that are shared across multiple processes.

Virtual memory is where the hard drive is used as additional memory in order to increase the number of processes that can be active at once.

When a process is saved into virtual memory it is suspended.  When loaded back into RAM for processing it is restored.

Page tables will record which processes are located in RAM or in virtual memory.

An interrupt is an electronic signal (Hardware Interrupt) or a process-generated signal (Software Interrupt) that is sent to the CPU to inform it that a device or process requries attention.

Common interrupts are triggered by storage devices, timers, peripherals and failure of power, software or hardware.

Buffers are used on devices to allow the CPU to perform other tasks while data is being processed.

Interrupt service routines (ISR) are bits of code that are automatically run when an interrupt occurs; these are normally within a device driver.


A process can be in one of the following states:
Running - currently has CPU time
Blocked - Waiting for an operation to complete.
Ready to Run - Waiting for the CPU.

Processes are swapped by storing both special and general registers into a process control block. This can then be used to restore the process.

The main design goal of scheduling is to maximise the throughput of processes. To do this, it must minimise starvation and eliminate deadlock.

Threading is the technique of splitting a process into multiple smaller processes to take advantage of multiple cores.

There are a number of different types of operating system:

Single-user
Multi-User
Real time. 
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class C_DT_SS_A(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Different types of Software Systems and their attributes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Open source software  tends to be free and will always give access to the source code for people to read, edit and share.

Closed source software will not give access to the source code, but may be free to use.

Proprietary software is also referred to as closed source.

Off-The-Shelf software can be bought immediately but may not be able to offer the same level of functionality that custom built software can.

Safety critical systems are classified as any system which could lead to death injury or loss to company assets.

Safety critical systems must have fail-safes and fault tolerance and are much harder to produce than regular software.

Knowledge based systems, also known as expert systems, are broken into four parts; Knowledge base, Rule Base, Inference ENgine and GUI.

Utilities are software which help the user accomplish tasks and tend to come shipped as part of the operating system.

The modern trend in software is moving towards a higher number of smaller specialised apps rather than larger monolithic  applications.

Applications such as 3D ray tracers can produce detailed computer-generated images and animation.

Weather forecasting is based on mathematical models and is backed by vast amounts of data.

Computer automation makes use of sensors to record the physical environmental and actuators to control it.

Computer-Aided Design allows designers to try ideas out on the computer, including modelling hwo the product will react in different scenarios and simulations, without having to build expensive prototypes.

Computer Aided Manufacture will take designs and produce exactly the same product using an assembly line.

Search engines give greated access to a wider range of information.

The PageRank algorithm will determine where a website appears in search results.

A company's online reputation must be carefully managed as negative information can have an impact on sales.



""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")
        
class C_DS_IP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Data Security and Integrity Processes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Security risks to modern systems include outside access of files, corruption of data, unauthorised reading or duplication and loss or deliberate deleting.

Policies ensure that staff use data responsibly and minimise risk of data loss.

Passwords need to be strong in order to protect data and files.

Access levels restrict which users can access sensitive files and data.

In symmetric encryption the process of decryption is the opposite of the process used to encrypt. The Caesar cipher is an example of symmetric encryption.

In asymmetric encryption algorithms the encryption and decryption keys are different.

Cryptographic mehtods can be compared by looking at how well they diffuse information and how hard they are to break by brute force.

Biometric data uses human metrics to identify individuals.

Common biometric methods include facial recognition, finger prints, iris scans, DNA and palm prints.

Biometric data is unique to indibiduals, which makes it very difficult to impersonate.

Biometric data can be inaccurate if recorded in sub-optmal conditions.

Privacy concerns arise as a result of using Biometric data

Black hat hackers will break into systems for their own ends while white hat hackers use their skills to identify and fix security flaws.

Malicious software comes in many forms including Viruses, Trojans, Spyware, Ransom-ware and Botnets.

Contingency planning allows companies to develop disaster recovery procedures. The plans must be tested and constantly updated to ensure the businesse has limited exposure to down time.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("Component2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


