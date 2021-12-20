import tkinter as tk                
from tkinter import font  as tkfont 
import random
from tkinter.scrolledtext import ScrolledText

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

class Finance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        button= tk.Button(self, text= "Diploma",command=lambda: controller.show_frame("Diploma"),fg="white",bg="#e67e22",width=25,font=(None, 17, "bold")).grid(row=0,column=0)
        button9 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#e67e22",width=25,font=(None, 17, "bold")).grid(row=3,column=2)

class Diploma(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#d35400")
        button1= tk.Button(self, text="Unit 3",command=lambda: controller.show_frame("D_Unit3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="Unit 4",command=lambda: controller.show_frame("D_Unit4"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button19 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("Finance"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=1,padx=10,pady=10)
        button20 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)

class D_Unit3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="Topic 1 ",command=lambda: controller.show_frame("U3_T1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="Topic 2",command=lambda: controller.show_frame("U3_T2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="Topic 3 ",command=lambda: controller.show_frame("U3_T3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button4= tk.Button(self, text="Topic 4",command=lambda: controller.show_frame("U3_T4"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button5= tk.Button(self, text="Topic 5",command=lambda: controller.show_frame("U3_T5"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=1,padx=10,pady=10)
        button6= tk.Button(self, text="Topic 6",command=lambda: controller.show_frame("U3_T6"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=2,padx=10,pady=10)
        button7= tk.Button(self, text="Topic 7",command=lambda: controller.show_frame("U3_T7"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=0,padx=10,pady=10)
        button19 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("Diploma"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=1,padx=10,pady=10)
        button20 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)



class U3_T1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="1.1",command=lambda: controller.show_frame("U3T1_1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="1.2",command=lambda: controller.show_frame("U3T1_2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="1.3 ",command=lambda: controller.show_frame("U3T1_3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button4= tk.Button(self, text="1.4",command=lambda: controller.show_frame("U3T1_4"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button5= tk.Button(self, text="1.5",command=lambda: controller.show_frame("U3T1_5"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=1,padx=10,pady=10)
        button6= tk.Button(self, text="1.6",command=lambda: controller.show_frame("U3T1_6"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=2,padx=10,pady=10)
        button7= tk.Button(self, text="1.7",command=lambda: controller.show_frame("U3T1_7"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=0,padx=10,pady=10)
        button8= tk.Button(self, text="1.8",command=lambda: controller.show_frame("U3T1_8"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=1,padx=10,pady=10)
        button19 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("D_Unit3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=1,padx=10,pady=10)
        button20 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)


class U3T1_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="The Importance of Sustainable Personal Finances", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""Sustainable Personal Finances are important for both individuals and the future financial and economical health of the country.

Much of the blame for 2008 , was attributed to namkers who encouraged people to take out loans and debts that they couldn’t repay.

Many economists would also say consumers who took advantage of these should also share the blame.

Total Personal Debt doubled between 1994 (400billion) to 800 billion in 2002, and hit a peak in 2008 at 1,400 billion.

The Credit Crunch , tightening of the conditions to take out a loan, brought an almost complete halt to the increase in year-on-year personal debt.

Levels of debt may be manageable as long as the economy is growing and unemployment is low, but due to the recession, unemployment figures rose. Jan 2008, 1.62milllion , which increased to 2.12 in march 2009, while peaking in November 2011 at 2.7 million.

Many people have faced legal action from lenders due to getting far into debt, resulting in them getting a County Court Judgement (CCJ) against them, properties were repossessed.

Insolvency grew from 2003 (35,604) to 2006 (107,288), and peaking in 2010 (135,045)

Rapid increases in insolvency is attributed to households taking on further levels of debt from early 2000s

Properties that were repossessed grew from 8,000 in 2004 to a peak of 49,000 in 2009.

Government agencies have been formed due to rising unemployment, such as Money Advice Service and Non-Government Agencies such as Citizens Advice and Stepchange.

Debt Problems have changed in the last few years , with credit problems being overtaken by arrears or household bills. Credit has fallen due to debt issues, with a rise of Payday loans.

Financial Capability has now been added to schools. 

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T1_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Individual Budgeting and Financial Planning", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""A budget can simply be the amount of money that someone has available to spend.

Government produces an Annual Budget , which simply is , what goes in against what goes out. 

Businesses often do the same.

For individuals it’s best to think of all the income , and start a budget by detailing what mandatory expenditure they have, and things that are discretionary expenditure, as in not necessary purchases. 

It’s best to have a Short Term Budget, Medium Term , and Long Term Budget.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T1_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Flexible Financial Planning", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""Financial Planning means planning future expenditure and deciding how it’ll be financed.

Many people use their current account statements to make sure they know what direct debits, standing orders or regular payments will be taken each month.

Looking much further ahead, Long Term financial plans will take into account the cost of starting a family , going on holiday or other expensive aspirations.

It’s Best to Expect the Unexpected; Always have an emergency fund.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T1_4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="The Characteristics of a Flexible Financial Plan", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""A Detailed budget for a certain time period, i.e., Daily, Weekly, Monthly , and 6 monthly.

Informed and Accurate information

Ability to adapt to changing products and services

Fluidity in changes

It has to be Realistic.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T1_5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Setting Priorites", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""The First step in drawing up a new financial plan is to make a list of all goods and services that you may spend money on. 

These Can be grouped between Needs, Wants and Aspirations

Mandatory Expenditure covers the costs that you have a legal obligation to pay

Essential expenditure covers costs that have to be paid to make basic needs

Discretionary expenditure is Non-Mandatory , i.e, gym subscriptions.

For those on low income, they may have to rank what needs are more important than others.

Divide surplus between Savings and Spendings.

Distinguish between the different types of savings , i.e. Pensions (Mandatory), Savings (discretionary)

1.5.1 Cash Flow Modelling

Modelling can be done through apps, spreadsheets and other software

This gives people freedom to be able to change their spending.
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T1_6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="The Obstacles to Sustainable Personal Finances", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""There are a number of obstacles that can prevent individuals from having sustainable personal finances.

These Obstacles can be:

    Failing to make Short-Term, Medium-Term, Long-Term plans that are flexible

    Failing to compare actual weekly/monthly income and expenditure with the amounts predicted

    Failing to amend plans when circumstances change or when differences occur

    Failing to take appropriate steps, such as trying to increase income, reducing spending , or borrowing

    Failing to make adequate contingency plans to deal with unexpected changes in income or expenditure
""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T1_7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Contingency Planning", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""Sustainable personal financial plans need to evolve as an indiviudals’ circumstances change. Unforeseen events should be included and expected.

Contingency planning should be used for both favourable and unfavourable events

Favourable events : Getting a Job, Salary Increase

Unfavourable Events: Losing a job, salary decrease

Due to the 2008 crisis, contingency plans were used by both businesses and governments involved. 


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T1_8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Financial Products and Services ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""The Full range of products and services offered from banks, building societies and other provides, offer many opportunities to maintain sustainable personal finances. The most important ones are:


1.8.1 Current Accounts 

Banks and Building Societies are the main providers of Current accounts, which are safe ways to store money and can be used in different ways. In addition to depositing and withdrawing holders can make payment by using:

Cheques/ Standing Orders / Direct Debits / Debit Cards / Telephone Banking / Internet Banking / Mobile Banking

With the widespread availability of online banking services in recent years has made it easier for customers to monitor their accounts regularly. Up-To-The-Minute receipts are one of the ways customers are able to spot deviances from their short term plans.

1.8.2 Savings Accounts

By opening a savings account with a bank, building society or Credit Union customers are effectively lending money to the institution , so that they can in turn use to fund loans, overdrafts and credit cards.

There are many different types of savings accounts available:

Regular (Monthly) Savings accounts;

Notice Savings accounts

Fixed-term, Fixed-interest savings bonds or deposit accounts;

Credit Union Savings Accounts;

Christmas or other festive saving clubs’

National Savings and Investments (NS&I) 

Direct Saver

Income Bonds

Investment Account

Premium Bonds

DIrect ISA

Investment Account

Guaranteed Growth Bonds

As an aid to sustainable personal finances , instant or easy access savings accounts are ideal products to use for an emergency fund. 


1.8.3 Borrowing Products

Majority of people will borrow money from a bank, building society or other lender. If borrowing is unplanned , and the borrower hasn’t put much thought into it, it can lead to very serious problems. 

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T1"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")



class U3_T2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="2.1",command=lambda: controller.show_frame("U3T2_1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="2.2",command=lambda: controller.show_frame("U3T2_2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="2.3 ",command=lambda: controller.show_frame("U3T2_3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button19 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("D_Unit3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=1,padx=10,pady=10)
        button20 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)


class U3T2_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Understanding the Need for State Welfare", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

The system of benefits payable to people who are temporarily or permanently in need of financial help is designed to be a financial ‘safety net’ to help those who:

have unexpectedly lost their main source of income

have a low level of income, eg from a minimum wage or part-time job

are not able to earn an income at all


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T2_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="The Benefits System", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Two types of benefit; contributory and non contributory.
Contributory -  paid to eligible claimants provided that they have paid the required number of National Insurance contributions (NICs). Employers automatically deduct NICs (and income tax) from employees’ salaries, but self employed workers have to make arrangements to pay their own NICs.
Non-contributory - paid to those eligible claimants who either have not paid enough NICs to claim contributory benefits or who need a ‘top-up’ payment because the contributory benefits that they receive do not meet their income needs.

Help for people out of work or unable to work full time
 - Jobseeker’s allowance.
Contributions-based JSA - aged between 18 and retirement age, not full time student, work on average less than 16 hours a week, able to work and fully available for work, willing to attend JSA interview every two weeks to show you have been trying to find work.
Income-based JSA - income-based JSA is not subject to a time limit, must have less than £16,000 in savings, your partner should be working less than 24 hours a week.

Sickness and disability benefits
-  Statutory sick pay (SSP)
employer has to pay you at least SSP if you have been off sick for four or more days, a fixed weekly amount that is paid for a maximum of 28 weeks,
- employment and Support Allowance (ESA)
standard weekly benefit for the first 13 weeks for all claimants aged 25 or over and at a lower rate for those under the age of 25. After 13 weeks, claimants are assessed and allocated to one of two categories
work-related activity group - illness or disability is not considered too severe to prevent them from returning to work, attend regular meetings with advisers
support group - illness or disability seriously limits the work that they can do, can talk to an adviser if they need to.
- Disability and carer benefits
Personal Independence Payment (PIP) - payable to those aged between 16 and 64 who have a long-term illness or disability that means they are unable to perform basic daily living activities or have limited mobility.
People over the age of 65 can claim attendance allowance instead.

Housing benefits
- Housing benefit
Pay rent, single under 35 if they live in a single room in a house or flat they share with other people. Can be reduced if:
you are paying an ‘unreasonably’ high rent to a private landlord
you are in social housing or you have savings of more than £6000
- support for mortgage interest (SMI) - who needs help with interest payments on their mortgage
Additional benefits
Those eligible for JSA, ESA and / or Housing Benefit may also be able to claim a variety of additional benefits and discounts, such as Council Tax Reduction and Cold Weather Payments.

Income support
weekly cash benefit, for those who work under 16 hours and are not eligible for JSA or ESA.

Help for those in retirement
-  State pension
Contributory benefit paid to everyone who has reached state pension age and who has paid sufficient NICs. 10 qualifying years of NIC contributions, 35 qualifying years to get the full new state pension.

Help for those who work full time 
Working tax credit & child tax credit 
can be claimed by eligible low-paid workers and each provides an additional income designed to top up wages to an amount that ensures that claimants are better off working.
partner who works the most hours each week normally receives the Working Tax Credit payment, - Child Tax Credit is paid to the one who spends the most time caring for the child.

Help for families
- Statutory Maternity Pay (SMP) and Statutory Paternity Pay (SPP)
employer must pay SMP for up to 39 weeks so that she can take maternity leave to look after the baby.
Eligible fathers are also entitled to SPP, but this is paid for only one or two weeks unless the mother chooses to return to work before using the full 39 weeks of maternity leave
- Child benefit
flat-rate cash benefit paid to all families or single parents with dependent children.
everyone receives the same amount. an additional tax charge that any individual earning over £50,000 a year will have to pay if they or their partner receives Child Benefit.

Help for those ‘exceptional circumstances’
- The ‘benefits cap’ - benefit claimants aged 16–64 have been subject to a payment ‘cap’ on the total amount of income that they can receive from benefits.
- Personal Independence Payment (PIP) -  benefit replaced Disability Living Allowance (DLA) from April 2013 for those aged 16–64.
- Changes to Housing Benefit - households entitled to Housing Benefit have seen their benefit cut if they are renting council-owned or housing association properties that are larger than they need. (one bedroom for each adult or couple)

Universal credit (2013) - simplify the benefits system by replacing six existing benefits with a single monthly payment for those living on a low income, Paid once a month rather than every week
A flat-rate benefit paid to all those who met the eligibility requirements, regardless of their income.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T2_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Sources of Financial Advice", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Money advice service (MAS)

urgent need to improve the general public’s knowledge and understanding of personal finance after the financial crisis, too many people were ‘financially illiterate’

Financial Services Act 2010 introduced measures designed to improve financial literacy.

provide the information and advice that people need to make broad financial decisions.

- Citizens advice (national debt and money advice charity)

offers information, advice, calculators and other interactive tools.

site offers advice on dealing with benefits and help to those who have built up unsustainable debts

- Money Advice Trust (MAT) (charity)

helps people across the UK to tackle their debts and manage their money.

Local council debt counselling services
Local authorities also provide their own local services. (BIrmingham City Council)

Other non government sources of help and advice
StepChange Debt Charity - national charity offering free debt advice and debt management service, both online and by telephone.
Payplan - free online debt management service. It is not a charity but it receives donations from all the lenders with which it arranges debt management plan.

Provider debt advice 
Corporate social responsibility (CSR)
Most providers therefore now publish a detailed corporate social responsibility (CSR) report each year, and these will include information on the donations that the business has made to debt and money advice charities, as well as how it is directly helping customers who get into financial difficulties


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T2"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3_T3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="3.1",command=lambda: controller.show_frame("U3T3_1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="3.2",command=lambda: controller.show_frame("U3T3_2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="3.3 ",command=lambda: controller.show_frame("U3T3_3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button4= tk.Button(self, text="3.4",command=lambda: controller.show_frame("U3T3_4"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button5= tk.Button(self, text="3.5",command=lambda: controller.show_frame("U3T3_5"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=1,padx=10,pady=10)
        button6= tk.Button(self, text="3.6",command=lambda: controller.show_frame("U3T3_6"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=2,padx=10,pady=10)
        button7= tk.Button(self, text="3.7",command=lambda: controller.show_frame("U3T3_7"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=2,column=0,padx=10,pady=10)
        button19 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("D_Unit3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=1,padx=10,pady=10)
        button20 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)


class U3T3_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Political Factors", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

When we refer to political factors in PESTEL analysis in the context of financial services, we are referring primarily to the various ways in which the policies of a government affect the products and services offered by financial providers, and the impact that these policies have on individuals. 
P - Political 
E - Economic 
S - Social 
T - Technological
L - Legal 
E-  Environmental
 
3.1.1 Regulation 


The importance of effective systems of regulation of the activities of financial services providers was clearly demonstrated by the 2007–08 global financial crisis. 

widely accepted that failings in the regulation of banking and finance worldwide were a key factor among those that caused the crisis; at the very least, it is agreed that better regulation may have helped to prevent the crisis.

governments reviewed  their regulation systems and followed this with reform, aiming to make the systems more suitable to sustainable global financial services industry and properly protecting consumers’ interests.

the UK has also had to abide by European legislation, much of which affects providers and consumers of financial services. The EU Withdrawal Act 2018 ensures most of this law continues after the UK’s exit from the EU. 
Since the crisis, the EU has also made it a priority to create a new financial system for Europe (European Commission, 2014).

A central part of EU policy is that there should be a high level of competition between a range of financial providers. The aim is to ensure that consumers can choose the products and services that meet their needs, and which offer the best value for money.

Putting EU policy into practice When the effects of the financial crisis in the UK led to the creation of the Lloyds Banking Group EU regulators demanded that LBG reduce the size of Lloyds TSB.



Overall, the system of regulation sets out exactly what financial services providers are allowed to do – and what they are not allowed to do. 

Why regulate banking and finance?  
It protects consumers from dishonest, incompetent or financially unstable providers,  more sustainable, enhancing individual and corporate financial stability, and reducing the likelihood of any future financial crises.
It gives people confidence in the financial system and encourages them to use  financial solutions  It requires providers to run their businesses prudentlyIt requires providers to ensure that consumers are fully informed 

The products and services that financial services providers offer are often complicated and can be confusing to the ordinary consumer. 

3.1.2 The regulators 

The present regulatory system was established in April 2013 under the Financial Services Act 2012. The Act returned overall responsibility for regulating financial services and maintaining the long-term sustainability of the industry to the Bank of England.

The three bodies that replaced the Financial Services Authority (FSA) after the 2007–08 financial crisis are:  the Bank of England’s Financial Policy Committee (FPC); an interim FPC met in 2011 and the full committee was established in April 2013;  the Financial Conduct Authority (FCA); and  the Prudential Regulation Authority (PRA). These are  responsible for enforcing the system of regulation that governs the financial services industry, for maintaining the stability of the industry and of individual providers, and for ensuring that consumers are fairly treated and have their interests protected.

3.1.3 Consumer protection 

Consumers do not always buy the right products or services to meet their needs. This might be because they do not fully understand what they are buying, or because the provider has made a mistake, or because the provider does not make it clear exactly what the product will cost. 

In recent years, there have been cases of financial products being ‘mis-sold’ by providers. The biggest and best-known case of mis-selling was the widespread selling of payment protection insurance (PPI) to customers taking out loans who either did not need PPI or would be ineligible to claim on some sections of the policy.

Mis-selling PPI Payment protection insurance is designed to cover the monthly loan repayments of an employed person who stops working as a result of sickness or redundancy. Many banks, building societies and other lenders have been found to have persuaded borrowers to buy PPI even if they were not employed (eg people who were self-employed or retired) – and who were therefore not eligible to claim on the policy.

These providers have since been forced to pay billions of pounds in compensation to the affected customers. In addition, the lenders involved have been sanctioned with large fines imposed first by the FSA and, more recently, by the FCA.

The FCA now has responsibility for regulating consumer credit – ie loans and hire purchase arrangements, which retailers often use to help consumers finance the purchase of furniture, domestic appliances, cars, etc. In addition, the following also play a role in protecting financial service consumers 

The Financial Ombudsman Service is an independent official body, the role of which is to investigate consumer complaints and to resolve disputes between financial services consumers and providers. The FOS is funded by an annual levy that every provider covered by the scheme is obliged to pay, and case fees paid by providers if the complaints about them referred to the FOS exceed a certain number.

The Financial Services Compensation Scheme provides a safety net if a bank, building society or certain other financial services business cannot pay its customers’ claims because it has gone out of business. All businesses authorised by the FCA are covered. The FSCS is also, like the FOS, funded by the providers who are members of the scheme and this includes the cost of any compensation payouts.

In addition to these organisations, the new Competition and Markets Authority (CMA), Citizens Advice and local authority trading standards offices also have powers and responsibilities for consumer protection more generally across all industries and businesses. 

3.1.4 The political agenda
There is another set of government policies – known collectively as the political agenda – that is focused more directly on helping to ensure that every individual has access to the benefits that financial products and services can provide.


3.1.4.1  Social exclusion and social inclusion 

A key policy within this agenda is ‘social inclusion’. If certain groups of people or individuals in certain situations are denied access to the benefits enjoyed by most people in their society, they may be said to be ‘socially excluded’. A society in which there is full social inclusion is therefore one in which all members of society:
can participate fully in community life;
can influence decisions affecting them;
are able to take some responsibility for what goes on in their communities;
can exercise a right of access to the information and support that they may need to do all of these things; and
have more equal access to services and facilities.
 

Unfortunately, the reality is often very different from this ideal. Many people find themselves socially excluded to a greater or lesser degree, perhaps because they:
have a physical or mental illness or disability;
have poor basic skills (ie literacy and / or numeracy);
live in a deprived urban area or a remote rural area;
have a low income because they work in low-paid jobs;
are not working because they have been unable to find work;
are homeless or have no fixed address to give to an employer or a bank; and / or
are (illegally) discriminated against on grounds of ethnicity, religion, gender, age or disability.
Social exclusion is a complex and multi-dimensional process. It involves the lack or denial of resources, rights, goods and services, and the inability to participate in the normal relationships and activities, available to the majority of people in a society . . . It affects both the quality of life of individuals and . . . society as a whole.


3.1.4.2  Financial exclusion and financial inclusion 

 Financial exclusion can be caused by the same issues as social exclusion, such as mental health issues or being unable to afford financial products, but there is an additional factor: the individual’s financial literacy. The term ‘financial literacy’ refers to an individual’s level of knowledge and understanding of financial matters. One measure of financial exclusion is the number of people who do not have a bank current account.  

If someone has no bank account, not only is that person unable to make use of the numerous ways in which a current account allows its holder to make and receive payments and transfers, but also their access to other financial services is restricted.
For those relying on government benefits, not having a current account became a particular problem when the government began to change the way in which it made these payments.

The result was a ‘universal banking’ policy: essentially, a commitment by the banks and building societies to offer stripped-down ‘basic bank accounts’ to any applicant, regardless of that applicant’s status. A basic bank account typically offers no overdraft facility or cheque book (although account holders may be offered a cash card or debit card); some cannot be accessed online and some cannot be used to make payments by direct debit or standing order.
In addition to basic bank accounts, another option became available to those without a bank account: the Post Office Card Account. This operates in the same way as a basic bank account, except that access to the account is through a local post office, which means that those who are used to cashing their benefit or pension cheques in this way are able to continue to get cash from the same place, rather than having to set up an account at a bank or building society branch (Post Office, undated).
 
The introduction proved to be very successful, bringing the percentage of low-income families without a current account down from almost 25 per cent in 1999–2000 to only 5 per cent by 2008–09 . Even with this improvement, however, in 2010 there remained 1.75m people in the UK without a current account – which prompted the government at that time to declare its intention to impose on banks a legal obligation to provide basic bank accounts for everyone. While this intention was never implemented, it had the effect of encouraging banks to do more to promote basic bank accounts – and this resulted in a further fall in the numbers of people without an account to around 1m by November 2013
 
Consumer rights campaigners believe, however, that many providers still do not publicise their basic bank accounts enough – suggesting that this is because the accounts are costly for them to operate and because there are no compensating profits from cross-selling other products to account holders.

3.1.4.3  Combating social and financial exclusion 

The consequences of financial exclusion have been recognised by successive governments, which have introduced a number of other policy initiatives aimed at promoting social inclusion in general and financial inclusion in particular.
The Money Advice Service  is one such initiative .

The government has also encouraged banks and other providers to:
offer a range of products (in addition to basic bank accounts) aimed at the financially excluded, products that are relatively simple and straightforward, and therefore easy to understand;
provide information on products in a way that is accessible to everyone – eg offering versions in languages other than English, or in Braille for people with visual difficulties; and

make their own efforts to promote inclusion through financial education, to help people to understand how financial products can help them and to encourage people to make more use of appropriate products.

In response to this last requirement, several banks, building societies and credit unions have developed their own financial education resources.

 the internet has played a part in reducing financial exclusion – something that the government has also encouraged by means of policies aiming to make broadband available to the majority of the population.
Another way in which the internet has helped to reduce financial exclusion is by offering a means of accessing financial services to those who:
are housebound and unable to get to a bank branch;
have a disability (eg visually handicapped people can use screen readers and voice synthesisers);
work shifts or unsocial hours and may not be able to phone or visit their financial providers during normal working hours; or
are intimidated by the office of a financial provider and / or feel uncomfortable with sales staff, preferring to research providers and products in their own home and in their own time.
 
3.1.5 The impact on individuals’ personal finances

 Most of the decisions that politicians take in Parliament have the potential to affect individuals directly – and a political decision relating to financial services can have a particularly significant impact on an individual’s personal finances.
In an unregulated, ‘free market’ financial world, individual consumers would be exposed to unscrupulous, dishonest or incompetent providers whose only objective would be to maximise their short-term profits by selling as many products as they could at the highest prices possible.

The legislation and regulation that protects consumers in general is not extensive enough to ensure consumer protection in the context of financial services.
The major banking and finance ‘scandals’ that have hit the headlines over the past few years have shown that, even with a strong regulatory system, the financial services industry is still by no means a perfect market. That system therefore has to be revised and updated constantly to deal with failings as they become apparent.

By thoroughly reforming the way in which financial services are regulated, the government hopes to restore consumer confidence in the effectiveness of the regulatory system – and hence to restore customers’ trust in financial services providers – which is essential if individuals are to maintain their personal financial stability.
 
The costs of compliance

 While regulation brings many benefits for individual consumers of financial services, it is not without its costs. 

As the number or scope of regulations with which providers have to comply increases, so too does the amount that they must spend. New legislation can also increase providers’ costs if they have to redesign products, product literature and advertisements, and retrain sales and administrative staff.

It is inevitable that these additional costs will have an impact on the individual. The company may accept lower profits, but this will mean cutting dividends distributed to its shareholders. Major changes in the regulatory system have even led some providers to leave the industry entirely because they are unable to make a profit.
Consumers too end up carrying the costs of regulation by paying higher prices for the products that they need or by going without products they cannot afford. They may also suffer if providers reduce the range of products and services that they offer, leaving consumers with fewer choices.

Regulation and consumer protection are essential if consumers are to enjoy the benefits that financial products bring – but governments must ensure that the costs do not outweigh these benefits.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T3"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T3_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Economical Factors", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
 we refer to changes in:
interest rates, which are related to: − inflation; − house prices (and thus activity in the housing market); and − savings and investments;
economic activity, government spending and unemployment; and
the global economy and exchange rates.
These factors affect how businesses (including financial services providers) operate and make decisions, and can either directly or indirectly affect consumers and have an impact on sustainable personal finances.
 

3.2.1 Interest rates and inflation 

Interest rates can be described very simply as ‘the price of money. Interest rates are also used as a central tool of government and central bank economic policy.  At the beginning of 2008, however, the financial crisis of 2007–08 and the economic recession that followed prompted the Bank of England’s Monetary Policy Committee (MPC) to cut Bank rate dramatically in March 2009 to an unprecedented 0.5 per cent, where it stayed for over seven years.

In August 2016, Bank rate was lowered further to 0.25 per cent, as a result of uncertainty following the UK’s decision to leave the European Union. The MPC increased Bank rate back to 0.5 per cent in November 2017 and then to 0.75 per cent in August 2018.

The reason for these changes in interest rates is that changing Bank rate is the way in which the Bank of England tries to manage inflation.
Basic economic theory tells us that if there is ‘too much’ spending  prices will tend to rise as businesses take advantage of the excess demand to boost their profits. If this happens on a widespread basis, the result is a general trend of rising prices, otherwise known as inflation.

In May 1997, the government gave the Bank of England the power to set Bank rate independently of government – a change later formalised under the Bank of England Act 1998. The Bank was also given responsibility for using Bank rate to deliver ‘price stability’ – ie to maintain the annual rate of inflation at around 2 per cent.

When Bank rate goes up, most lenders will automatically increase the interest rates that they charge on loans, credit cards, mortgages, overdrafts, etc.  one of the MPC’s objectives in increasing the Bank rate: to reduce consumer spending. Lower spending will reduce overall demand for products and services, which will, in turn, put pressure on businesses to reduce their prices.

For many individuals, a high and rising rate of inflation will mean having to spend a larger proportion of their income on the goods and services that they regularly consume.  Increasing interest rates to keep inflation in check therefore helps those living on a fixed income with little or no debt by ensuring that their income continues to cover their expenditure. Those with high levels of debt, however, are better off if interest rates are kept low and inflation is allowed to rise.
 

3.2.2 Interest rates and house prices

 When interest rates are rising, some people will inevitably find it harder than others to meet their monthly mortgage payments and will begin to fall into arrears. The higher cost of mortgages will also reduce demand for houses and flats.  The housing market is such a large part of the national economy that changes in house prices and demand for housing have a significant impact on economic activity as a whole.


3.2.2.1  The housing market and the national economy 


Before the financial crisis of 2007–08, interest rates had been relatively low since the mid-1990s: it was widely felt that inflation had been brought under control and was no longer a serious threat to the economy. Banks and building societies were able to borrow money easily and cheaply on the money markets, and were therefore able to make mortgage loans cheap and easily available, requiring that prospective borrowers put down little or no cash deposit. Demand for houses consequently increased and house prices rose rapidly.

Although these higher prices began to make buying a house or flat more expensive for first-time buyers, who needed to save up more money for even a small deposit and who needed to make higher monthly repayments on their mortgages, those who already owned a home were able to use the increase in the value of the home that they were selling to put down a bigger deposit on the more expensive house that they wanted to buy. The willingness of banks and building societies to lend 100 per cent of the value of the property – with some even offering 125 per cent – and up to a multiple as high as seven times buyers’ annual incomes meant that many people were able to borrow more than they could sensibly afford – and this kept demand high.
Many people now saw buying a home as a major investment that would provide a lump sum of capital to help them through their retirement years and which they might eventually pass on to their children.
In both instances, homeowners were able to convert this equity into cash by borrowing from banks and building societies on the basis of secured loans or second mortgages – commonly known as ‘equity loans’ or ‘mortgage equity withdrawal’.


Banks and building societies were willing to lend in this way because the loan was secured on the increased value of the house. They believed that there was little chance that they would lose their money even if the borrower were to default, 

 Because interest rates on secured loans are always lower than those charged for unsecured personal loans, hire purchase or credit cards, some consumers simply saw equity loans as a cheaper way of borrowing money. 


Lenders rarely pointed out to customers that taking out an additional secured loan cost the customer more than doing so using a personal loan in the long run, because they would be paying interest on the secured loan for so much longer.


In this booming housing market, there was also increased demand for other complementary financial products. Borrowers needed to take out buildings and contents insurance; they also bought life assurance to cover the financial consequences to their families should they die before paying off their mortgages.


If house prices had continued to rise year on year in the United States, Europe and other Western economies, the banks and their customers might have continued to enjoy these benefits – but the house price ‘bubble’ burst. 

It is the collapse of the US sub-prime housing market – that is often seen as the event that triggered the 2007–08 global financial crisis. 

At the end of 2006, house prices began to fall dramatically in the United States, and those in the UK and Europe followed suit throughout 2008 and 2009 (Christie, 2006).

As the financial crisis bit deeply, central banks in the United States, UK and Europe dramatically cut Bank rate to try to stop the crisis from causing a deep economic recession, which meant that the cost of borrowing money also fell. 

Anxious to avoid the risks involved in making mortgages too easy to obtain, banks and other mortgage lenders tightened their lending criteria: the ‘credit crunch’. 

They reduced their maximum loan-to-value ratios  to 75 per cent or less; 

they dropped mortgage income multiples back down to three times gross salary or less; they tightened up their credit scoring procedures. 

People who now could not get mortgages as easily either had to buy cheaper houses or had to withdraw from house purchase altogether – a situation that began to ease only in 2013.

3.2.2.2  The impact on personal finances 

If fewer people are buying or moving house, it not only reduces demand for new builds, but also for goods, such as new furniture, and for the services of builders, decorators, plumbers, electricians, estate agents, surveyors, solicitors, etc. People start to lose their jobs and others become afraid that their jobs may be under threat. Many people in this situation will reassess their personal finances in order to protect themselves against the prospect of losing their job and the income that they are used to having.


A typical reaction among the majority of people in the face of the financial crisis was to try to reduce personal debts (mortgage, loans, credit cards, etc), to increase regular savings and try to build an adequate emergency fund, and to avoid taking on any new debts. 

The homeowners worst affected by the crisis and subsequent economic recession were those who had used high loan-to-value mortgages to buy their properties or had taken advantage of mortgage equity withdrawal, and who now faced the prospect of ‘negative equity’ – ie of the amount of money that they still owed on their mortgage loan being greater than the market value of their property. 

Those affected who can still manage to meet the monthly loan repayments on the mortgage are generally able to manage this situation by simply staying put until the market improves – but those who default on their repayments take a double blow: not only may they be forced to leave their home , may find that they still owe money to the lender when the forced sale fails to cover the debt in full.


By cutting Bank rate as far as possible, the Bank of England undoubtedly helped millions of mortgage holders to keep up to date with their monthly payments and avoid getting into arrears.
 
just managing to pay even at a lower interest rate and who will be unable to meet even a small increase in monthly repayments when interest rates begin to rise once more.


3.2.3  Interest rates and savings and investments 

While rising interest rates causes problems for borrowers, it is a different story for savers. When Bank rate rises, banks and building societies can increase the interest rates that they charge to borrowers and increase the interest rates that they pay to those who have deposited savings without having to narrow profit margins. The main beneficiaries will be retired people and others who rely on their savings to provide an income. Paying higher interest rates to savers may also affect people’s attitudes to saving and borrowing – encouraging them to save more of their income rather than to spend it 
 
Interest changes can also affect investors, because the prices of shares listed on the stock market may fall after a rise in interest rates. 

Remember that when the Bank of England’s Monetary Policy Committee (MPC) increases Bank rate, it is hoping that increasing the cost of borrowing will reduce consumer and corporate spending, thereby reducing the overall (or ‘aggregate’) demand for goods and services.

 If demand for goods and services does fall, however, sales revenues will fall.

A fall in the stock market generally affects the wealth of many people and businesses. Those who have invested directly in the stock market will suffer an immediate reduction in wealth; many other individuals are also indirectly exposed to what happens in the market as a result of the effects on pension fund and insurance company fund investments. 

A period of economic growth in the five years before the financial crisis saw a steady rise in share prices: the FTSE 100 index, for example, increased from 3940 in 2002 to almost 6500 by 2007. But the global financial crisis caused a dramatic stock market crash, which cut the FTSE 100 back down to just under 4500 by the end of 2008 
One effect of these huge changes was that many people lost faith in investment products. They began to look for alternative places to keep their money 

Providers responded to these changes in consumers’ attitudes to risk by developing new ‘structured products’, which (it is claimed) offer a safer home for people’s savings than the stock market, while still allowing them to benefit from share price growth.

 
Reshaping investment risk and reward 

Guaranteed growth or guaranteed capital plans use complex investments called derivatives to offer investors a return linked to the stock market over a set period of years.  If the stock market goes up in value, investors get their money back plus growth based on the amount by which the stock market has gone up.  If the stock market falls, they either get back only their original investment (hence ‘guaranteed capital’), or get back their original investment plus a minimum growth amount, eg 4 per cent (hence ‘guaranteed growth’).

But these products cannot entirely eliminate risk: their complex structure means that they are not covered by the Financial Services Compensation Scheme (FSCS) – and that means that investors risk losing their money if the bank goes bust

3.2.4 Economic activity, government spending and unemployment 

3.2.4.1  Economic activity 

A healthy, balanced economy is one in which demand for goods and services is high enough to keep unemployment at an acceptably low level, but is not so high that it causes unacceptable levels of inflation. Economic activity in the UK is fuelled by demand for the goods and services from four main sources:  
consumer demand refers to the amount that individuals are spending on the goods and services that they are consuming, spending that is funded by consumers’ incomes, savings and borrowings;  

corporate demand is the amount that businesses are spending on the goods and services that they are consuming, spending that is funded by a business’s revenue, savings and borrowing, and by capital injections from its investors;  

government spending is the amount that national and local government departments and agencies are spending on the goods and services that they are consuming, which spending is funded by tax revenues and government borrowings; and  

demand for exports refers to the goods and services produced in the UK, but sold overseas.

One of the government’s key roles and objectives is to use the economic tools available to it to achieve and maintain full employment and low inflation.  On the other hand, when prices are stable and unemployment is growing because of a lack of demand, interest rates may be reduced to make it cheaper for individuals and businesses to borrow money to spend on goods and services, thus increasing consumer and corporate demand. This manipulation of interest rates is known as ‘monetary policy’.
 
The Bank of England’s ‘forward guidance’ statement

 Mark Carney, formerly governor of the Bank of Canada, was appointed as governor of the Bank of England in July 2013. One of his first actions was to issue a ‘forward guidance’ statement setting out what the Bank expected to happen to interest rates in the future.
The statement formally linked interest rates with the rate of unemployment, as well as inflation, when Carney said that Bank rate would not be increased until unemployment fell to 7 per cent. This would not apply, however, if the rate of inflation – which, at 2.7 per cent, was above the 2 per cent target, but stable – were to threaten to spiral out of control.

3.2.4.2  Government spending

 As well as using monetary policy, it is equally important for the government to manage the amount of money that it raises in taxation, the amount that it borrows on the financial markets, and the overall amount that it spends. This is known as ‘fiscal policy’.
Whenever the government changes its policies on taxation, borrowing and / or spending, this has the potential to affect economic activity.  Put simply, if the amount spent by the government each year is more than the amount raised through taxation, then the government’s budget is said to be running a deficit, which has to be financed by government borrowing. 

Any borrowing that is not immediately repaid is added to the overall government debt. The aim of most governments is to ‘balance’ the budget (ie for spending to be equal to tax revenue) or to achieve an annual surplus (ie revenue greater than spending).

Most people accept, however, that many governments – like consumers – were encouraged by low interest rates and easily available credit to borrow more and more in the years running up to the financial crisis (leading to increasing budget deficits and outstanding debt). They used these borrowings to finance significant expansion in government spending – especially on education, public transport and the health service.
 
The Labour government, in power from 1997 until 2010, believed that it was right to increase government borrowing and debt to improve public services and to maintain full employment. Government borrowing grew at an even faster pace after 2007, in the wake of the global financial crisis and recession, when the government faced:

the need to ‘bail out’ the failing banks with injections of funds, to save them from going bust and triggering a failure of the banking system as a whole;

rising unemployment, which led to increasing numbers of claims for state benefit payments (eg Jobseeker’s Allowance and Housing Benefit); and

the negative effects of that rising unemployment and of less activity in the housing market on government revenues from income tax, National Insurance contributions (NICs), value added tax (VAT), stamp duty, etc.

Labour promised to reduce government borrowing slowly by maintaining public spending to combat the recession
The Conservatives believed in an ‘austerity’ policy, which involved substantial cuts in public spending to reduce the amount that the government needed to borrow each year to cover the annual deficit and quickly restore a ‘balanced budget’ in which the deficit would be reduced to zero.

The coalition government largely introduced Conservative austerity policies, meaning that, each year, government spending has faced serious cuts, which have led to thousands of jobs being lost in the public sector. The cuts were not enough to stop total government debt from growing – from £530bn in 2008 to £1,457.2bn in November 2014. 
 
3.2.4.3  Unemployment 

The level of unemployment can undoubtedly have an impact on individuals’ personal finances, and on their choice of products and services.

High employment can lock people into a high-consuming lifestyle and it encourages a consumer culture. It also enables people to save money if they earn enough to have a surplus after they have satisfied their needs and everyday wants.

High unemployment makes for a very different market. The long-term unemployed have to rely on state benefits for their income and do not have the resources to buy financial products, even though they may still need them. At times of high unemployment, even those who have a job probably feel uncertain about the future.  

3.2.5 The global economy and exchange rates

 The last of the economic factors  are changes in exchange rates (ie the purchasing power of the pound sterling against other currencies) and changes in the global economy. 

3.2.5.1  The global economy

 The 2007–08 global financial crisis, yet again, illustrates clearly the impact of globalisation. 

A hundred years ago, the collapse of the US sub-prime market in mortgage lending might have affected only banks and investors in the United States; in the present day, globalisation has resulted in an international financial services industry comprising many multinational banks, insurance companies and other providers with offices scattered across the globe providing services and selling financial products to an enormous customer base. 

The extent of the connections between these providers  is considered to be one of the reasons why the US collapse was so contagious: many banks in the UK and Europe were ‘exposed’ because they had invested their money in ‘toxic’ collateralised mortgage obligations (CMOs) – a way of repackaging mortgage debts into investment products.

Many European banks were so badly affected that they had to be rescued by government bailouts. Many European governments had already increased their public spending and borrowing substantially during the ‘boom’ years

The impact that the economic policies adopted by foreign governments, and the conduct of foreign banks and other financial services providers, can have on the national economy and on individuals’ personal finances has never before been as clear as it has become in recent years.
 

3.2.5.2  Exchange rates

 Further factors that illustrate globalisation are the extent to which people regularly travel abroad.  All of this activity has an impact on foreign currency exchange rates – particularly the value of the pound sterling (£) against the euro (€) and the US dollar ($). 

Individuals and businesses consequently need financial providers to supply:

foreign exchange services, eg people who want holiday spending money will want to buy travellers’ cheques or pre-paid foreign currency cash cards;

buy-back guarantees, which mean that purchasers can sell any unspent currency at the same rate at which they bought it, meaning that they are protected against adverse currency movements;

credit and debit cards that will be accepted abroad, including in cash machines; and

products that help businesses to manage exchange rate risk, so that they will not lose if exchange rates move against them.
In the past, many governments fixed the exchange rates of their currencies, rather than allowing them to ‘float’ – ie to be determined by the forces of demand and supply in the currency markets, which is largely what happens now.

 
The euro and the UK 
In 1999, the euro replaced the national currencies of a number of European countries that had chosen to adopt it. Of the 28 member countries of the European Union, 19 have adopted the euro. Business carried out between two eurozone countries is all done in the same currency and there is therefore no exchange rate risk.

The UK chose not to join the euro – but People in the UK can  be directly affected by changes in euro–sterling exchange rates
.
With floating exchange rates, there is an interaction between interest rates and exchange rates: 
if interest rates are generally higher in the UK than in other countries  will have an incentive to buy UK government and corporate bonds.  The higher demand for sterling on the currency exchange markets will tend to increase the price of the pound, causing the value of sterling to strengthen.

Individuals should therefore be aware that taking on debt in a foreign currency carries a significant exchange rate risk, which they should take into account when drawing up their financial plans. 

The same consideration should also be given to making investments in other currencies (such as buying shares in foreign companies that cannot be bought and sold on the London Stock Exchange)

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T3"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T3_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Social Factors", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
When we refer to social factors in the context of financial services, we are referring to a wide range of cultural aspects, including changes in demographics, levels of employment and home ownership. Trends in social factors have a big impact on the type of goods and services – including financial services – that individuals demand.

3.3.1 Cultural issues

 When we speak of cultural issues, we are referring not only to people’s ethnic and religious backgrounds, but also more generally to the social groups to which they belong or in which they were brought up. 

Cultural Backgrounds  affect people’s needs, wants and aspirations, and ultimately their behaviour, including their financial behaviour.
 

3.3.1.1  Multiculturalism 

Large sections of the UK population have family origins elsewhere in the world. Their values, attitudes and beliefs may be very different from those of people with other cultural backgrounds  this means that there is a risk that they will be excluded from using certain financial products and services unless providers take cultural differences into account when they are designing, marketing and delivering those products and services.

3.3.1.2  Religion 

In many religions, lending and borrowing money is seen as an acceptable activity provided that lenders treat borrowers fairly and borrowers do not build up unsustainable levels of debt. Others, however, see debt as something to be avoided at all costs. They believe that it is wrong to lend someone money if you charge interest on the loan, and that it is equally wrong to borrow money and pay interest on the loan.

Complying with Sharia Under Islamic law, known as Sharia, it is forbidden to charge or pay interest (Riba). If an urgent need arises for someone to pay for something and they do not have enough money to do so, the options available to them are to borrow only from members of their own family group or to use a Sharia-compliant financial product.
There are now six stand-alone Islamic banks operating in the UK, and these provide Sharia-compliant home purchase plans, loans and savings.
In 2014, however, Britain became the first non-Muslim country to offer Shariacompliant government bonds (Sukuk). 
A Sharia-compliant home purchase plan is a way in which devout Muslims can access money to buy a property without technically borrowing or paying interest. There are two widely used types of Sharia home purchase plan (Ijara and Murabaha); in both cases, the bank will buy the property in which the customer wants to live and allow the customer to repay in instalments. 

Islam (and some other religions) also prohibits drinking alcohol and gambling in all of its forms. This means that Muslim customers must avoid certain investment products that might indirectly link to the stock market, such as investment funds, pensions or life assurance policies.
 

3.3.1.3  Youth culture

 ‘Youth culture’ is the term used to describe the values shared by people in their teens and early 20s. 

It embraces everything from what you believe in to how you spend your leisure time and money. Changes in youth culture can affect how young adults manage their finances, and the kind of financial products and services that they use.

The rise in social networking sites and smartphone apps offers new opportunities for marketing to the innovative financial services provider.

3.3.1.4  Grey culture

 ‘Grey culture’ refers to the older section of the population – ie those in late middle age and older stages in the financial life cycle 

This group of people has specific financial needs – for pensions, insurance, savings accounts and income-producing investments – and will often share certain values, such as respect for tradition, and the need for security and trustworthiness. 
 

People in the older stages of the financial life cycle are an important and growing market for providers of financial services.


3.3.1.5  Consumer culture

 In the latter half of the twentieth century, as standards of living rose and people in the industrialised world found themselves with more disposable income, a consumer culture emerged.
 A consumer culture, or consumer society, is ‘[a] society in which the buying and selling of goods and services is the most important social and economic activity’

The trend was reversed in the immediate aftermath of the financial crisis of 2007–08. Since 2012 there have been signs that consumer spending is increasing – not least in terms of the housing market. However, in 2017 UK consumer spending hit its lowest level in five years as a result of stagnant wages and inflation rises.


3.3.2 Demographics

 Demographics involve analysing a population in terms of age, sex, ethnicity, culture, social status and geography.  The demographic structure of a population and changes in that structure play a key role in the way in which providers design and market their products.
Demographics also tell providers a lot about the financial solutions that a target population is likely to need. Age is an important facet of demographics

Changing and ageing populations 

As populations grow in size, financial providers see a rise in demand for their products. Population growth usually happens because health and life expectancy have improved. Many countries therefore now have an ageing population. 
The impact of this on the individual is that younger people need to plan their finances wisely (particularly pensions, insurance, long-term savings and investments) if they are to ensure that they will have sufficient income to live comfortably through a much longer period of retirement than previous generations have ever enjoyed.
 
Other demographic changes can also alter a population’s demographic mix. The following are a small sample of such changes:
Changes in birth rates
Migration

The impact that these factors have on individuals and their implications for sustainable personal financial planning are complex, and emerge over a long period of time. The following are, however, some of the likely effects.
Most mothers now go out to work, and this affects the financial products and services that they need

Because people have smaller families, they can spend more on each child. Children and teenagers now consume many goods and services, and have income from pocket money and part-time jobs. 

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T3"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T3_4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Technological Factors", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Technological factors include matters such as increased automation, the rate of technological change and the influence of technology on outsourcing decisions. 

Technological shifts can affect costs and quality of service, and can lead to product innovation.

The processes that lend themselves to automation are those that are rules-based. 

A computer that works to a set of rules can make straightforward decisions based on those rules and it can put borderline cases in a separate list, to be referred to someone who can exercise judgement and make a decision. 

Credit scoring is an example of an automated way of making decisions about whether or not to lend to someone. A credit scoring system can be set up so that it will refer all borderline declines and acceptances to senior management. The system effectively separates out cases that are clear-cut and indicates a decision on them, while sending complicated cases to a person for a decision.

Some computers can ‘learn’, building up experience that helps them to make better decisions in the future, based on what has happened in the past. This sort of technology is of most value where there is a lot of data on which the system can base its experience 

Financial institutions routinely process masses of information about their customers, This information can be used to detect any deterioration in an account holder’s behaviour.. Such a system might typically flag up a pattern of declining balances or a situation in which someone’s overdraft gets bigger and is added to earlier each month.

Within the finance industry, automation has had the following results.

Increasing speed and efficiency 

Less face-to-face advice and sales – as computers take over jobs that used to be carried out by people, there are fewer opportunities for people to discuss their financial needs and plans with an adviser face to face. 

Technology such as the internet, email and smartphones means that relationships seem less personal nowadays – and yet, in other ways, relationships are closer than before. Providers’ huge information-processing capabilities mean that they amass large amounts of data about existing and potential customers, and form a clear picture of their needs, wants and habits

The digital divide It is important to remember,  that is widening between those who are computer literate and have full access to the internet and those who are not and do not. In 2018, the ONS reported that approximately 90 per cent of UK households had access to the internet (ONS, no date a). 

. E-commerce has changed the face of customer–provider relationships in the last decade, offering an electronic link  between supply (the provider) and demand (the customer). 

Technological factors thus directly determine the ways in which providers sell their products and the ways in which people manage their finances. The computer revolution has also been the single most fundamental factor in the rise and spread of globalisation, and the ever-increasing interdependence of financial providers and markets.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T3"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T3_5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Environmental Factors", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

 the vast majority of environmental experts believe that the things we do and use every day are causing serious problems for the long-term sustainability of the environment. 

Waste products from production processes and from the consumption of goods can cause pollution; waste heat and ‘greenhouse gas’ emissions contribute to global warming

These environmental factors must be considered in relation to sustainable personal finances because  the financial products and services that they buy will inevitably have an environmental impact. Financial services providers are being encouraged to make their products more environmentally friendly. 

Some have argued that it is too easy for companies to adopt so-called ‘greenwashing’ policies – ie to mask their products with ‘green’ (environmentally friendly) window dressing, when in truth they are only paying lip service to environmental issues. 

Changing perceptions of environmental issues have therefore undoubtedly affected individual finances in recent years – in both positive and negative ways.
 

Companies that supply renewable energy could benefit from favourable lending terms.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T3"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T3_6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Legal Factors", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

 there are other legal factors that can have an impact on providers and consumers of financial products and services. These include laws relating to discrimination, consumer protection, employment, and health and safety. 

3.6.1 UK legislation

 Financial providers wanting to set up in business need to ensure that they can comply with all applicable laws before they do so and, in particular, with financial legislation, such as the Financial Services and Markets Act 2000, the Consumer Credit Acts 1974 and 2006, the Banking Act 2009 and the Financial Services Act 2012.

The Banking Act 2009 established a permanent statutory regime for dealing with failing banks and makes new provisions for the governance of the Bank of England.

The Financial Services Act 2012 amends the Bank of England Act 1998, the Financial Services and Markets Act 2000, and the Banking Act 2009. It also includes other provisions about financial services and markets, which were described earlier in this topic.

In addition, companies must comply with the following legal requirements.

Company law – this covers many aspects of how companies are set up and run, and how they report on their affairs. There is also partnership law for those businesses that operate as partnerships.

Employment legislation – this sets out rules on how employers must treat their workers and what rights the workers have.

Tax laws – these govern the taxes that individuals and businesses must pay, and how they are calculated.

Proceeds of crime and anti-terrorism legislation – these laws aim to stop criminals from laundering money (ie from using 
financial services to hide the proceeds of crimes), and to stop terrorists from using financial services to collect and move their 
funds around.

Accounting standards – financial services providers must draw up their annual financial statements in accordance with International Accounting Standards (IASs).

As consumers of financial products and services, individuals are also protected by more generic consumer protection laws that give them rights, for example, to return faulty goods to the shop from which they bought them and get a full refund.
 
Until April 2014, the Office of Fair Trading (OFT) and the Competition Commission were the government agencies responsible for enforcing the relevant consumer protection provisions and were divided between the Financial Conduct Authority (FCA) and a new agency: the Competition and Markets Authority (CMA). 

This change was brought about under the Enterprise and Regulatory Reform Act 2013.

[The CMA is] responsible for:  investigating mergers which could restrict competition;  conducting market studies and investigations where there may be competition and consumer problems;  investigating where there may be breaches of UK or EU [competition laws];  bringing criminal proceedings against individuals who commit [an offence];  enforcing consumer protection legislation to tackle practices and market conditions that make it difficult for consumers to exercise choice;  co-operating with sector regulators and encouraging them to use their competition powers;  considering regulatory references and appeals. 
 
The area of responsibility that most directly affects consumers is the enforcement of the consumer protection provisions contained in the Consumer Protection from Unfair Trading Regulations 2008. 


The work of the CMA includes investigating individual cases in which consumers have suffered because of a lack of effective competition in the market for a particular product or service. 

If consumers have been sold a financial product or service in breach of the provisions of the Distance Selling Regulations (which regulate the sale of goods and service via the internet) or the Consumer Rights Act, they can take advantage of complaints procedures and ‘cooling-off’ periods during which they are entitled to change their minds about purchases; their local trading standards office will also take up any individual cases of bad practice and take steps to resolve the problem. 

This regime of consumer protection is, of course, additional to that specifically provided for consumers of financial services by the Financial Services Compensation Scheme (FSCS), the Financial Conduct Authority (FCA) and the Financial Ombudsman (FOS). 

If all else fails, consumers also have the option of bringing a civil action against a provider. When a court case between a customer and a financial services provider goes against the provider, other customers who have similar cases are likely also to take it to court: the first decision will establish judicial authority, which means that the court actions of other dissatisfied customers will have a greater chance of success. 

The need for legal regulation of financial services was demonstrated by the problems that occurred as a result of changes in the law in the 1980s, which swept away many of the regulations that had until then prevented financial services providers from widening the range of products and services that they could offer.  Deregulation freed these two types of firm from many of the legal constraints that stopped them from competing in similar areas. Generally speaking, this increased competition is seen to be a good thing, because it helps to ensure that prices are kept as low as possible. After the global financial crisis of 2007–08, however, high-profile cases of mis-selling and fixing interest rates came to light – and were considered to be the consequences of deregulation
 
The new legislation and new regulatory system brought in under the Banking Act 2009 and the Financial Services Act 2012 can therefore be seen as an acceptance by government that deregulation was damaging – that individual consumers will suffer if banks and other financial services providers are not properly and effectively regulated.


3.6.2 European legislation

Brexit 

At the time of writing in early 2019, the government is planning the process to exit the European Union (known as ‘Brexit’).

Membership of the European Union also has implications for a country’s legislation, because the institution itself makes laws. These take the form of either regulations or directives, and they have to be applied in all of the member countries.
Regulations are directly applicable in member countries, which means  that they become law in all EU member countries as soon as they come into force, and that people and businesses must comply with them immediately. Such regulations apply to all EU members equally, with no variation of the law from one country to another.

Directives can be seen as instructions issued by the European Commission to the governments of the EU member countries. Each member has to enact its own laws to meet the requirements of the directive within a set period (usually two years). The exact rules can differ from one member country to another, as long as they fulfil the requirements of the directive. In other words, the directive sets out what is to be achieved and the member country can decide for itself how to achieve it.

A huge number of UK laws have originated in the European Union, eg the Data Protection Act 1998 and the Consumer Credit Act 2006. In December 2010, the deposit compensation limit for the UK (payable through the FSCS) was changed; this too was the result of European intervention – the equivalent in pounds sterling of the euro deposit compensation limit agreed for all members of the European Economic Area (EEA), which includes EU member states plus several other European countries, such as Iceland, Liechtenstein and Norway.


European law particularly affects the financial services industry. The objective is to create a single European market for financial services in which people living in one EU member country can confidently buy financial products and services from a provider in another EU member country, secure in the knowledge that providers are regulated and supervised to the same standard across the Union. The European Commission consequently plans to bring into force a huge number of laws and directives over the next few years that will affect both UK financial services businesses that deal only with people in the UK and also those businesses that want to sell to customers in other European countries – at least until the UK leaves the EU.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T3"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T3_7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Analysing Data Sources", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Many of the PESTEL factors that we have discussed are quantifiable – ie their values can be measured, and differences or changes in those values can be recorded and analysed. 

Data on interest rates, levels of inflation or unemployment, house ownership, budget deficits and debts are just some of the social and economic variables that can be measured and presented in tables, graphs, histograms, bar charts and pie charts, etc. 

3.7.2 Graphs 

Tables of raw data are necessary for detailed analysis of the figures. But to see overall trends and comparisons of data at a glance, it is better to turn the data into a graph or chart.




""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T3"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3_T4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="4.1",command=lambda: controller.show_frame("U3T4_1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="4.2",command=lambda: controller.show_frame("U3T4_2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="4.3 ",command=lambda: controller.show_frame("U3T4_3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button4= tk.Button(self, text="4.4",command=lambda: controller.show_frame("U3T4_4"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button19 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("D_Unit3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=1,padx=10,pady=10)
        button20 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)


class U3T4_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Establihing Clear, Measurable Objectives", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Main needs and wants in life

Attitude to spending money

Attitude to saving

Attitude to borrowing and in debt 

Aspirations

Attitude to risk 

Making a budget - 

Identify and list all sources of income

Identify and list all items of expenditure

Decide on the time period that you will use in the cash-flow chart, e.g week or month

Now you can calculate the total income and total expenditure for each time period. 

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T4"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T4_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Monitoring your financial plans", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Budget variance - difference between the expected and actual figures.

The key to effective monitoring is to analyse the cause of the variance.


Methods of monitoring -

keep receipts for all of your purchases and use them, together with bank account statements, to keep a written record of your income and expenditure, writing the actual figures in a column next to your forecast figures on your cash-flow forecast using a spreadsheet program.

Free online planning tools:

the free budget planner offered by the government-funded Money Advice Service

Money Dashboard

the Debt Advice Foundation budget planner

Money Saving Expert’s budget planner

Paid online planning websites:

You Need a Budget

Moneydance

Goodbudget

Keeping an accurate record of the plan -

Organised people - always keep receipts and other financial documents, and who keep records of how much they earn and spend - will not find it hard to compile detailed financial cash-flow plans, whether they use one of the financial apps listed, simpler budgeting spreadsheets, or even simply a pencil and paper.

Less organised people - may simply jot down a few figures on the back of an envelope every week or month to see how much they have spent and how much money they have left until they receive their next allowance or salary payment - not very detailed planning and leaves quite a lot to chance

People who do not forward plan may do only a few mental calculations -  simply check their current account balance when they think of it, or when they need to use their debit card to withdraw cash or pay for an item - This approach to personal financial planning is very ‘hit and miss’. There is no planning for emergencies – or even foresight that they will occur – so these people have to do a lot of ‘firefighting

The ‘envelope’ method of budgeting -

probably few people who still use cash and real envelopes, some banks and building societies and most credit unions allow you to open multiple savings accounts that can each be given a different name, eg ‘holiday fund’ or ‘emergency fund’.


Zero based budgeting -

idea adapted from business accounting, and the aim is to ensure that every penny of your income is spent purposefully and wisely.

problem with traditional personal budgeting methods is that if your forward planning consists only of making sure that you have enough income to cover your essential bills and your regular discretionary spending – with a potential surplus that is vaguely allocated to paying any unexpected bills that might crop up – it is likely that, by the end of the month  you will have spent the surplus, but have no idea on what you have spent it.

With zero-based budgets, you have to draw up a detailed cash flow forecast allocating every single penny of your expected income to a different expenditure envelope. The envelopes need to cover all of your expected spending, preferably over a period spanning the next 12 months.

The advantage of this system is that it forces you to be aware of where your money goes and to prioritise every item of expenditure.

With a zero-based budget, when you have spent all of the money that you had allocated this month, you have to decide which other envelope you are going to take the money from to pay for it.

Zero-based budgeting is more complicated and requires more effort than other budget methods, but there are spreadsheets available for free online that make it a lot easier.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T4"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T4_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Financial planning with interlocking time periods", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

financial plans should cover short-term, medium-term, long term and very long-term time periods.
There are no commonly agreed or standard definitions of how long the short, medium and long terms are because it depends on personal circumstances and the perspective of the individual.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T4"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T4_4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Adapting plans to changing circumstances", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
When something happens that significantly affects someone’s financial plan, their first course of action should be to revisit the plan to assess exactly what the impact is likely to be.

This will enable the person to change their plans to take the new circumstances into account and, where possible, to keep the planning on track to achieve their medium-term and long-term objectives.


Adapting plans in order to fulfil longer term goals - 

Different people have different approaches to setting themselves goals and achieving aspirations.

The key is to act now to make some provision for the future. Individuals do not know what will happen to them in the future, but if they have some money saved or a plan to work their way out of debt, their life choices are less constrained by their finances.

There must be a certain amount of flexibility in a budget because changes in circumstances mean that things will not go according to plan; the longer the term of your budget, the more likelihood there is that the actual outcome will be different from what you had hoped.

People’s typical long-term goals will, of course, depend on their stage in the life cycle.

Planning to achieve these aspirations will involve someone making a lot of assumptions about how secure their job is, the likelihood of pay increases and promotions, the effect of economic boom or bust, and what is going to happen to interest rates and inflation.

It is not only changes in external factors that can affect financial plans, but also changes in personal circumstances, eg changes in family circumstances.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T4"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3_T5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="5.1",command=lambda: controller.show_frame("U3T5_1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="5.2",command=lambda: controller.show_frame("U3T5_2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="5.3 ",command=lambda: controller.show_frame("U3T5_3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button4= tk.Button(self, text="5.4",command=lambda: controller.show_frame("U3T5_4"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button5= tk.Button(self, text="5.5",command=lambda: controller.show_frame("U3T5_5"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button6= tk.Button(self, text="5.6 ",command=lambda: controller.show_frame("U3T5_6"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button7= tk.Button(self, text="5.7",command=lambda: controller.show_frame("U3T5_7"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button19 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("D_Unit3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=1,padx=10,pady=10)
        button20 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)


class U3T5_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="The Benefits of Borrowing", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Borrowing can help people to smooth out differences in timing between their income and expenditure.

Someone who is always short of funds at the end of the month can use their credit card or overdraft to finance their purchases until the next salary payment arrives in their bank account.

Deficit - negative balance at the end of the month.

Borrowing money to cover this deficit is sensible if you know that you will have extra money next month to repay it. But if you have to carry the deficit over to the following month and add to it to cover that month’s deficit, you will be in danger of accumulating a rising debt.

Most people borrow money as a means of affording a substantial purchase, such as a house, a car or furniture, which they need to buy now, but which is too expensive to be funded only by current income.

Most common example is the mortgage loan: very few people are able to buy a house without taking out a mortgage loan, which they pay back while they are living in the house. Although they will pay interest on the loan, interest rates are lower for a mortgage than for other loans because it is secured on the property. 

Equity - difference between the amount owed on the mortgage and the market value of the house


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T5"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T5_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="The Costs of Borrowing", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
When someone borrows money, they agree to repay the debt from their future income. This means that they will have less left over from their future earnings until they have repaid their loans and so there is an opportunity cost.

A borrower repays not only what was borrowed, but also a percentage interest charge on top of this to recompense the lender for the use of its money over the time of the loan and for the risk that it takes.

Some types of debt (such as payday loans) are very expensive, while others (such as personal loans) are much cheaper.

Debt can also become a big problem for some people simply because they allow it to get out of control. Some people borrow more than they can afford to repay so that they can finance the purchase of goods and services that seem very attractive.

Hardcore debt - They may find themselves taking out new loans to help them to repay old ones.

Defaulting on a loan is a serious matter:

    the loan is secured on an asset, such as a mortgage secured on a home, the borrower will lose that asset.

    If the loan is unsecured, the defaulter will obtain a bad financial reputation or ‘financial footprint’.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T5"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T5_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Attitdues to Borrowing and Debt", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
Young people are more likely to have to borrow when they are starting out in adult life than older people who have been working for some years. Younger people will need loans to finance their studies, day-to-day cash flow and the larger items of expenditure.

Providers have also been guilty of irresponsible lending – of providing credit too easily and lending money to people who could not afford to pay it back.

Lenders are being more cautious when agreeing mortgages and other loans: they are accepting only customers who have a better credit history and who are more likely to be able to repay.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T5"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T5_4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Balancing the Beneifts and Costs of Debt", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

The price that the customer pays for a loan must be reasonable when compared with the purpose of the loan: are the items purchased worth the amount of interest being paid and could the money have been borrowed more cheaply.

The length of the loan should also correspond to the life of the article purchased. For example, the borrower will sensibly apply for a 25-year loan to fund the purchase of a new home – but not to finance the purchase of a computer.

To maintain sustainable personal finances, then, an individual’s borrowing decisions should not be taken in isolation, but should be both integrated into their short-term and medium-term budgeting plans and cash-flow forecasts and fully justified as part of their long-term financial plan.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T5"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class U3T5_5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Borrowing and Financial Footprints", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

When a potential borrower approaches a bank or finance company for a loan, the lender researches their credit history.

Companies compile files on consumers using information from banks, building societies and credit card companies, and also from county court judgments (CCJs), the electoral register, bankruptcy orders and house repossessions.

The details of every loan, credit card or other credit agreement that an individual has or has had are recorded in these files, which builds up a picture of how much the individual has borrowed and how good they are at making the required monthly payments.


This search leaves an electronic ‘footprint’ in the person’s personal credit history. 

‘Shopping around’ for the best loan or mortgage deal can also cause a problem, because lenders may view multiple credit searches by different credit providers as a sign that the individual is finding it hard to get a loan agreed.

A financial institution may refuse to offer credit to an applicant if it thinks that the applicant is a bad risk because they have already borrowed too much or because they have a bad history of repaying.

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T5"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T5_6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Comparing different solutions for individuals in debt", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""
When people realise that they can no longer afford to pay the necessary monthly payments on their debts, many react to the situation by applying for a consolidation loan. A consolidation loan provides enough money to pay off all of the other debts. This kind of loan is often secured on the customer’s home, assuming that the applicant is a homeowner and that there is positive equity in that property.

The first thing that people should do if they cannot repay what they owe is recognise that there is a problem and ask for help. There are many companies that offer debt management advice and services.

Informal payment plans  - If the debtor’s income is enough to leave a surplus after paying priority bills and their essential spending the debtor should then use this surplus to offer regular repayments on the remaining nonpriority, unsecured debts, negotiation.

Debt management plans - Anyone who does not feel capable of making all these arrangements by themselves can get free help to set up and maintain a more formal DMP. 

Administration and county court judgements - debtor pays the single monthly payment to the court rather than to a DMP manager. Likewise, the CCJ represents a legally binding requirement to pay what the court has decided is owing, either in full or by instalments, by a certain deadline. That payment may be made to the court or directly to the creditor.

Individual voluntary arrangements (IVA) - a formal agreement between debtor and creditors; creditors representing at least 75 per cent of the total debt value have to agree to the arrangement for it to become legally binding. If the debtor makes the monthly repayments for the full term of the IVA, their debts are then classed as ‘discharged’ and they are officially ‘debt-free’ as far as unsecured debts are concerned.

Debt relief order (DRO) - If the debtor has quite a low level of debt, low surplus income and few or no assets a DRO is an alternative to IVA or bankruptcy. Once the DRO is in place, the debts included in the order are frozen, so that the debtor no longer makes any repayments and the creditors cannot take court action to recover the debt. After 12 months, the debts are discharged.

Bankruptcy - If someone is declared bankrupt, the court will appoint the Official Receiver or a licensed IP to take over their finances. All debts, bank accounts and assets are frozen, and arrangements are made to sell most of the debtor’s assets and to use the proceeds to pay off as much of the debt as possible. The debtor will have to pay up to £700 in court fees plus legal fees if they use a solicitor


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T5"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T5_7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Cultural Perceptions of Financial Products", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Cultural factors affect a person’s approach to financial services, helping to determine which products they will buy and from which suppliers.

At the one extreme, there are groups of people who are not at all concerned about getting into debt and even going bankrupt.

At the other extreme are those who see debt as something to be avoided at all costs. These people believe that you should not borrow from financial institutions and that, if you do need to spend money, you should borrow only from members of your family group.


Perceptions in societies and cultural change -

Borrowing was seen as a risky way of buying things that you could not really afford, which frequently led people into unmanageable debt. Many looked down upon those who used hire purchase, because only low-income families needed this financial product. The only type of loan that was socially acceptable was a mortgage, because people could not own their homes without one.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T5"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3_T6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="6.1",command=lambda: controller.show_frame("U3T6_1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="6.2",command=lambda: controller.show_frame("U3T6_2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="6.3 ",command=lambda: controller.show_frame("U3T6_3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button4= tk.Button(self, text="6.4",command=lambda: controller.show_frame("U3T6_4"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button5= tk.Button(self, text="6.5",command=lambda: controller.show_frame("U3T6_5"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button6= tk.Button(self, text="6.6 ",command=lambda: controller.show_frame("U3T6_6"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button19 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("D_Unit3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=1,padx=10,pady=10)
        button20 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)


class U3T6_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Globalisation", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Travel between different countries is now easier, and it is both quick and relatively cheap.
Communication is faster now than it has ever been, and information communication technology (ICT) has made contact between people and between financial markets almost instantaneous.
Businesses frequently trade across borders because of the ease with which goods can be transported and with which people can get in touch with each other.
People from one country often migrate to live in another and, because people take a part of their culture with them when they move, many individual countries now have much more diverse local cultures.
Many businesses – particularly financial services providers – have expanded their activities to span national borders. They conduct business in more than one country and often have offices in many different places. 


Defining globalisation
the trend towards a single global economy and society
a process of increasing international networking, which means that communities and economies that used to be isolated are increasingly linked and affected by what is happening elsewhere in the world.

Criticising globalisation
They feel that it undermines the local culture in those countries and they do not like the depersonalisation that they believe results from it.
supports increased offshoring.
The key point is that what happens in one part of the world affects people in other parts much more than used to be the case. As well as being affected by our local economies, we are affected by what is happening in the world as a whole.
Has led to the emergence of very large multinational companies, which can dominate markets and be so competitive that small local businesses fail.

The effects of globalisation
Increasing globalisation means that UK providers face competition from overseas providers, which may set up operations in the UK or simply offer their products via the internet, as a comparatively low-cost way of finding and serving customers.
means that UK providers may decide to expand overseas (or may already be part of international organisations). They must decide how much of their resources to commit to the UK market in light of the opportunities elsewhere in the world.
UK providers also need to understand the cultural, regulatory and other constraints that may affect how successful they will be overseas

Outsourcing and offshoring 
Outsourcing -  process of one provider paying another to carry out certain functions that it previously performed itself.
Offshoring - the practice of moving some of a company’s operational functions to overseas locations. Companies can cut their overall operational costs by relocating operations to countries where there is a labour force with the necessary skills, but the country’s lower cost of living means that wage costs are much lower.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T6"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T6_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="The Global Economy",font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Financial providers are affected by what goes on in their local economy, eg what can happen when local interest rates change or when the job market suffers a setback. But each is also affected by what is going on in the global economy because:
Countries do a lot of trade with each other.
As a result of globalisation, banks and other financial services providers may find themselves in competition with businesses based in overseas economies, or may themselves be part of groups based overseas or with offices in other countries.

Exchange rates
Exchange rates also affect, and are affected by, what happens in the world’s financial markets. A strong and growing economy in the United States, for example, would lead to higher US interest rates.
The Bank of England’s Monetary Policy Committee (MPC) is responsible for setting Bank rate in the UK, which is used to influence the demand for and supply of the pound sterling.
an increase in UK interest rates will cause a fall in consumer spending (because borrowing to fund consumer spending has become more expensive), and this will not only reduce demand for UK goods and services, but also will have a knock-on effect on the volume of goods and services that the UK imports from foreign suppliers.

International trade organisations
World trade organisation (WTO) - only international organisation dealing with the global rules of trade between nations. Its main function is to ensure that trade flows as smoothly, predictably and freely as possible.
Other regional economic unions:
European Union (EU)
Association of South Eastern Asia Nations (ASEAN)
Carribean Community (Caricom)
Brazil, Russia, India and China (BRICs)

Measuring the performance of the global economy
gross domestic product (GDP) , a country's economic activity in terms of its total output of goods and services.
the ideal situation is steady, sustainable growth. If there is too much growth, some negative consequences can occur. An economy can become ‘overheated’, which means that businesses are unable to supply sufficient goods and services to meet the growing demand, and so will push up their prices instead – leading to higher inflation.
There is also an environmental impact when there is too much growth, eg an increase in the burning of fossil fuels, the shrinkage of green areas and increased congestion in urban environments. 
Countries should aim for sustainable growth - growth that is controlled enough to be able to continue into the medium term and long term.

Effect of changes in the global economy: saving and borrowing
Individuals tend, however, to opt for safety in times of economic uncertainty. If anything, they are more likely to sell their risky investments and move their money into savings accounts, funds that invest in safer gilt-edged securities or corporate bonds.
individuals are being more careful in their borrowing and spending, despite low interest rates and government encouragement to ‘shop for Britain’. Many are already over indebted and they are trying to pay off what they owe – a situation that is made worse by their fear of unemployment.
Effect of changes in the global economy: investing
Investment companies may find it difficult to identify good investment opportunities.
Businesses that specialise in low-priced products and services therefore tend to see an increase in sales and profits during an economic downturn.
For investors, then, it is vital to be fully aware of and up to date with companies’ market strategies, so that they can anticipate which ones are likely to be affected.

Effect of changes in the global economy: employment and earnings
Falling growth and recession generally means falling employment levels
When someone who owes money loses their job, they have an additional problem in that they no longer have an income to finance their debt repayments. 

The european economy
There is a strong interaction between different countries’ economic and financial health and the global monetary system:
Governments fund their public spending from taxation and, when that is not enough, by selling government bonds on the world financial markets. They must offer an interest rate on their bonds that is high enough to attract investors – and investors will want an interest rate that matches the risk that the government will default on the bonds and that they will not get their money back when the bond matures.
When a country’s economic problems cause the perceived risk of default to increase, the government has to offer higher interest payments to be sure that it can sell the volume of bonds that it needs to fund public spending.

The UK economy
The Bank of England is the UK’s central bank. Its Monetary Policy Committee (MPC) meets regularly to decide on whether or not to change the level of interest rates
If inflation is low, people have a sense of security and a degree of confidence in the value of their assets in the future. This makes them happy to invest, because they feel that the value of their assets will not be eroded. If inflation is rising, people will be uncertain about the future and will look for investments that will keep ahead of inflation.
When interest rates are low, borrowing is cheap and therefore people will feel able to borrow more. The demand for houses will probably be high and this will lead to rising house prices. People with savings will have low returns on their money and may look to products other than simple savings accounts in order to receive greater returns.
High personal debt has been a feature of the UK economy for several years. This causes problems when interest rates rise. People can find themselves unable to make their repayments on credit cards, overdrafts, loans and mortgages. 


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T6"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T6_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Major World Events", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


Financial crisis and recessions
Some financial institutions failed, while others were ‘bailed out’ to prevent them from failing, damaging confidence in banks and other financial institutions. The global economy was plunged into a recession from which many countries are still recovering.
If a bank fails, its creditors (ie the people to whom it owes money) are also likely to fail because it cannot pay back their money.

War
Finding the money to pay for a war generally means that taxes must rise or that the government must borrow more.
War brings with it a great deal of uncertainty – something to which the stock markets can react with falling prices

Weather patterns, climate change and natural disasters.
The price of food products on commodity markets directly affects the size of people’s supermarket bills, eg the international price of grain affects the price of bread. So the effect of bad weather on food production – and therefore also on food prices – can be directly linked to the amount that individuals and families need to allocate in their budgets to food. 
The insurance industry is being affected by more frequent and larger claims for extreme weather events, such as floods, storms, hurricanes and forest fires, and this is likely to continue.

Company collapses and financial scandals
Laws made at the European level are influencing many of the changes that are being introduced in the UK to prevent corporate collapses, and to protect investors and consumers. 

Political change
Some governments work to protect the consumers of financial services as much as they can. They are highly critical of certain aspects of the financial services industry.
Other governments are more ‘business-friendly’, and may relax regulation and reduce the taxes that financial services businesses have to pay to make it easier and cheaper for financial product providers to make their products and services available to consumers.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T6"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T6_4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Social Change", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Changing attitudes towards money and financial provision - People are becoming more aware of the importance of finding the best products and services.

Increasing ethnic and cultural diversity - Most countries are becoming more ethnically and culturally diverse. Many providers themselves are multinational organisations; even on a local basis, they employ people of different nationalities and from different cultures.

Increasing complexity - At one time, each financial product fulfilled one need; now, it is possible to buy products that fulfil many. 

Changing demographics - The UK has an ageing population, which is creating opportunities for many product providers. This ageing population is placing an ever-increasing burden on the working population, which has to pay the taxes that will finance the rising costs of pensions, medical services and residential care.

Changing attitudes to debt. - At one time, people who could not afford to buy what they wanted simply did not buy until they had saved enough to do so. In recent decades, many people were much more relaxed about debt and used credit to finance the purchase of what they wanted when they wanted it.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T6"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class U3T6_5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Ethical Considerations", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


Business ethics: environmental, product, political and animal welfare. 

Ethical investment decisions 
People who want to invest their money in ethical projects and companies are not always concerned about all of these different types of ethical behaviour. Some may be concerned only that the organisations in which they invest will carry out activities that are considered to be ‘good’

Corporate social responsibility 
It is a way in which a company can demonstrate that there is a social conscience behind its business model, setting for itself standards that it believes are ethical and complying with the way in which society expects it to behave.
A company with an active CSR policy is showing that it is trying to take responsibility for its actions and to have a positive impact on the environment, its consumers, employees, communities and all other stakeholders.
the extent to which it can reduce its carbon footprint by using recycled materials and energy, and by reducing staff travel via video-conferencing and allowing staff to work from home;
general environmental issues – eg reducing the amount of waste that it creates.
making environmentally friendly purchasing decisions, either in terms of not over ordering materials or ordering items in bulk to save on transport costs.

Ethically branded organisations and products
An ethical brand is one that does not offend and which is not targeted at unsuitable customers. For example, unethical branding might include alcoholic drinks specifically targeting teenagers.
An ethically branded financial product is one that is aimed at people who are able to afford it and for whom it is suitable. People should not be persuaded by attractive advertising and catchy brand names to commit themselves to a financial deal that they are unlikely to be able to complete.

Ethical operations
One example of ethical operations in the financial sector is the paperless bank account, aiming to save trees.
In today’s electronic world, there is no need to use paper for these purposes. Customers can be encouraged to manage their accounts online, where they will always have access to their bank account details; these must be available for several years into the past, so that customers can check old transactions.
One popular service is text alerts to customers whose accounts are about to become overdrawn;
Marketing campaigns can also be delivered electronically, either by SMS messaging or via emails.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T6"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T6_6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Sustainability in the Financial Servivces Sector", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Banks, building societies, credit unions, friendly societies and insurance companies that are sustainable will survive into the very long term: they will not fail, they will continue to provide services and they will continue to make a profit. But this will happen only if they are really operating in a way that can be maintained over the long term.

The rise of systematic failure 
financial services providers such as banks and investment funds work very closely with each other. They trade in financial markets by borrowing from and lending to each other, and by buying and selling financial securities from and to each other. These markets now form very complex networks and these networks exist on a global scale. 
This means that if a major player in the system were to fail, the other players would be badly hit and the whole system would be at risk of failing too.
The ability of financial markets to keep going is based on confidence; if that confidence is undermined, the system fails. A financial system that operates in such a way that there is a realistic chance that it might fail is therefore not sustainable.

The impact of a systemic financial failure on personal financial sustainability 
In the event of a systematic failure, the customers of the failed banks would be hit immediately because they would be unable to make any payments. They would be unable to use the money in their current accounts to back debit card and cheque payments, because nobody would have any confidence that the banks would be able to honour them. 
Businesses would also be seriously affected: they would be unable to pay their employees’ salaries, buy their raw materials, or borrow funds to meet their cash flow and investment needs. Many companies would be forced to cease trading, with huge consequences for workers now out of a job.
Those customers who held savings accounts in the failed banks would lose their money.
Those customers who had borrowed from the failed banks would be unsure about the impact on their debts.
There would almost certainly be a substantial slump in stock market prices and – if the failure were limited to UK banks – a fall in the value of the pound sterling against most other currencies.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T6"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3_T7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#2980b9")
        self.controller = controller
        button1= tk.Button(self, text="7.1",command=lambda: controller.show_frame("U3T7_1"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=0,padx=10,pady=10)
        button2= tk.Button(self, text="7.2",command=lambda: controller.show_frame("U3T7_2"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button3= tk.Button(self, text="7.3 ",command=lambda: controller.show_frame("U3T7_3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button4= tk.Button(self, text="7.4",command=lambda: controller.show_frame("U3T7_4"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=1,column=0,padx=10,pady=10)
        button5= tk.Button(self, text="7.5",command=lambda: controller.show_frame("U3T7_5"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=1,padx=10,pady=10)
        button6= tk.Button(self, text="7.6 ",command=lambda: controller.show_frame("U3T7_6"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=0,column=2,padx=10,pady=10)
        button19 = tk.Button(self, text="Go Back",command=lambda: controller.show_frame("D_Unit3"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=1,padx=10,pady=10)
        button20 = tk.Button(self, text="Homepage",command=lambda: controller.show_frame("StartPage"),fg="white",bg="#3498db",width=35,font=(None, 17, "bold")).grid(row=9,column=2,padx=10,pady=10)


class U3T7_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Sustainable Economy", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Personal financial sustainability is affected by the sustainability of the economy in which an individual lives.
In 1997, the Bank of England was made independent of the government and tasked with setting monetary policy to ensure monetary stability.
Bank rate would be a tool with which the economy could be manipulated to meet a Consumer Prices Index (CPI) inflation target of 2 per cent. The goal is to deliver stable prices that will help to create a stable, sustainable economy.
The effect of this extremely low Bank rate is low returns on savings products and low charges on borrowing products - savers wish to see Bank rate increase, while borrowers hope it will remain low.



""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T7"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T7_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Sustainable Financial Services",font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

The purpose of most of these changes, such as the new regulatory regime, is to make financial services safer for consumers, and to increase their choice of products, services and providers.
All of these changes have a positive impact on the sustainability of individual finances and help to avoid market failure.

The role of the European Union
The Union achieves this aim by means of the European System of Financial Supervision (ESFS), which includes:
 ◆ the European Systemic Risk Board, which monitors the entire financial sector to identify potential problems that could lead to future crises and to take action to prevent them (ESRB, undated); 
◆ three independent regulatory bodies:
the European Banking Authority (EBA), which ‘works to ensure effective and consistent prudential regulation and supervision across the European banking sector’ 
the European Securities and Markets Authority (ESMA), which ‘contributes to safeguarding the stability of the European Union's financial system by enhancing the protection of investors and promoting stable and orderly financial markets’.
the European Insurance and Occupational Pensions Authority (EIOPA), which aims to ‘support the stability of the financial system, transparency of markets and financial products as well as the protection of insurance policyholders, pension scheme members and beneficiaries’.

EU Gender Directive - European court judgment determined that insurance companies should be prohibited from charging different insurance premiums for men and women.
Transparency Directive - applies to storing and providing regulated information, such as the financial reports of providers, annual and half - yearly accounts, and interim management statements, and the disclosure of major shareholder transactions.
Capital Requirements Directive - amendment to an earlier version of the Directive and specifies the liquid assets that providers must hold to ensure that they will be able to meet the withdrawal needs of their customers and continue to operate during any period when external funding is not available.

Legislation in the UK
This ensures that all senior bankers and certain staff providing regulated financial advice are ‘fit and proper’ by assessing their:honesty, integrity and reputation competence and capability financial soundness.
Implementing this new legislation and complying with new regulation may have a negative impact on consumers if providers need to raise the fees on borrowing and reduce the returns on savings to pay for the changes.
This enhances personal financial sustainability because provider and product failures become less likely, transparency of provider operations, fees and charges increases, and there is more choice of products and providers.



""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T7"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T7_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Getting Information and Advice", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""


This information is available via the internet, brochures and in person, from organisations such as Citizens Advice, National Debtline and StepChange Debt Charity.
The government also provides unbiased and reliable financial information and advice online, including details on benefits, work, pensions and debt. Pension Wise offers advice on current pension rules.
The Money Advice Service (MAS) independent body in April 2010, with the aim of improving people’s money management, covers a wide range of topics, including detailed guides to life events, explanations of products, tools such as budgets and borrowing calculators, and news.
Regulatory changes have also been made to ensure that people can get reasonably priced, unbiased professional advice. Independent financial advisers (IFAs), for example, can no longer receive a commission from the provider of investment products that they sell; instead, they must be paid by means of fees. The FSA introduced this change to ensure that advisers cannot be tempted to recommend products that offer them higher commission, but which may not necessarily be the very best choices for the customers.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T7"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T7_4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Changes to Providers, and to products and services", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

New providers and switching accounts
As large competitors enter the personal banking market, consumers will find themselves with more choice.
In the past, consumers rarely changed bank accounts because of the work involved and the time it took to complete the transfer.
For these reasons, and in response to recommendations made by the government-sponsored Independent Commission on Banking, the Payments Council set up the Current Account Switch Service. This service was introduced on 16 September 2013 to ensure that people are able to switch bank accounts quickly and easily.
The service ensures that switching bank accounts will take no more than seven working days, and that providers will transfer all of the existing balance, incoming payments (such as a salary) and outgoing payments (such as direct debits and standing orders).

Changes to products and services
In recent years, the government has introduced new financial services products, such as basic bank accounts, that ensure that individuals who formerly had no bank account now have access to financial services.
Individual savings accounts (ISAs) encourage people to save by offering a tax-free return.
There are also government changes to the benefits system and to the state pension.
The government has also introduced a ‘Help to Buy’ scheme in England for people wanting to buy a home, which is its response to rising house prices and the high deposits needed to get a mortgage.


""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T7"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")

class U3T7_5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Technology-Enabled Products and Services", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""

Online and mobile banking enables individuals to get information, to apply for products and services, to operate products, to transfer funds, to make payments and to manage their money 24 hours a day, from any location with an internet connection.
Apps and calculators with which someone can budget and manage their money are common, such as budget planners, ways of recording transactions as you make them and the Money Dashboard app, which groups expenditure into categories such as food, travel and fuel.
Faster payments enable people to make payments that are credited to the recipient within a few hours, so that consumers know their bills have been paid on time, eg credit card repayments

virtual currencies such as Bitcoin - currency that is not linked to any other currency and is not backed by a government or central bank. It was created by a group of computer programmers.



""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T7"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")


class U3T7_6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#303F9F")
        label=tk.Label(self, text="Withdrawing from the European Union (Brexit)", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        mylist = ScrolledText(self)
        mylist.insert(0.0,"""



Pros 

The UK would not be required to contribute to the EU budget

Reduction in bureaucracy and regulatory burden for small and medium sized enterprises

Potential economic revitalisation for the UK as a standalone economy

Freedom to look at significant growing economies outside of the EU such as China, India and the US for business

Increased control over immigration to help govern the UK economy

Cons

Loss of free trade and increase in import tariffs resulting in a reduction in international trade and thus a fall in GDP

Loss of foreign direct investment from the EU

Uncertainty of trading terms with other countries

As a major financial centre, the UK may lose its reputation as a way for central banks to access the EU

Workers from the EU currently contribute more to the UK in fiscal terms than they cost

""")
        mylist.pack()
        button = tk.Button(self, text="Go Back",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("U3_T7"))
        button.pack(side="top")
        button1 = tk.Button(self, text="Start Page",bg="#3F51B5",fg="white",command=lambda: controller.show_frame("StartPage"))
        button1.pack(side="top")
