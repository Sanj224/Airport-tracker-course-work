import tkinter
from tkinter import *
from tkinter import messagebox
import time

##flags
entryFlag = False
UKairportEntered = False
OverseasairportEntered = False
airportsEntered = False
aircraftEntered = False
airportSubmitFlag = False
aircraftSubmitFlag = False
profitSubmitFlag = False



def mainMenu():
    global menu
    global my_image
    try:
        airports.destroy()
    except:
        print('')
    try:
        aircrafts.destroy()
    except:
        print('')
    try:
        priceplan.destroy()
    except:
        print('')
        
    menu = Tk()
    canvas = Canvas(menu, width = 600, height = 600, bg='light blue')
    canvas.pack()
    menu.title('Airports program')
    my_image = PhotoImage(file='worldimage.png')
    canvas.create_image(300, 299,image=my_image)

    menu.title('Airport profit calculator')
    firstButton = Button(menu, text='Enter Airport Details',command=AirportDetails).place(x=270, y= 200)
    secondButton = Button(menu, text='Enter Aircraft Details',command=aircraftDetails).place(x=270,y=250)
    thirdButton = Button(menu, text='Enter Price Plan and Calculate Profits',command=pricePlan).place(x=240, y=300)
    fourthButton = Button(menu, text='Clear Data',command=clear).place(x=295, y=350)
    fifthButton = Button(menu, text='Exit',command=menu.destroy).place(x=310, y =400)
    menu.resizable(False, False)
    mainloop()

def AirportDetails():
    def confirmation():
        global airportsEntered
        global OverseasairportEntered
        global UKairportEntered
        global UKairportLabelError
        global UKairport
        global OverseasAirport
        global OverseasAirportLabelError
        global distance
        global airportSubmitFlag

        UKairport = str(UKairportEntry.get())
        OverseasAirport = str(OverseasAirportEntry.get())
        if UKairport.upper() == 'LPL' or UKairport.upper() == 'BOH':
            UKairportLabel2 = Label(airports,text="airport choosen",bg='green').place(x=280,y=180)
            try:
                UKairportLabelError.destroy()
                UKairportEntered = True
            except:
                UKairportEntered = True
        else:
            UKairportLabelError = Label(airports,text="The three letter code you entered was not valid, please try again ",bg='red')
            UKairportLabelError.place(x=190,y=180)

        airportList = []
        fullAirportList = []
        distanceFromLPL = []
        distanceFromBOH = []
        search = False
        airportFile = open('Airports.txt','r')
        for row in airportFile:
            if row == '\n':
                break
            
            field = row.split(',')
            airportList.append(field[0])
            fullAirportList.append(field[1])
            distanceFromLPL.append(field[2])
            distanceFromBOH.append(field[3])

        for i in range (len(airportList)):
            if OverseasAirport.upper() == (airportList[i]):
                search = True
                airport = fullAirportList[i]
                if UKairport == 'LPL':
                    distance = int(distanceFromLPL[i])
                else:
                    distance = int(distanceFromBOH[i])
                break
        if search == True:
            OverseasAirportsLabel2 = Label (airports, text=airport, bg='green')
            OverseasAirportsLabel2.place(x=250,y=330)
            try:
                OverseasAirportLabelError.destroy()
                OverseasairportEntered = True
            except:
                OverseasairportEntered = True
        else:
            OverseasAirportLabelError = Label(airports,text='The overseas airport code was not valid, please try again', bg='red')
            OverseasAirportLabelError.place(x=200,y=330)

        if OverseasairportEntered == True and UKairportEntered == True and airportSubmitFlag==False:
            airportsEntered = True
            backtomenu = Button(airports,text='return to main menu',command=mainMenu).pack()
            airportSubmitFlag = True
            
            
                 
            
    if airportsEntered == True:
        tkinter.messagebox.showinfo(title="Error Message", message="You have already entered values for this option, clear data if you want to re-enter these values")
    else:

        menu.destroy()
        global airports
        global UKairport
        UKairport = ''
        airports = Tk()
        canvas = Canvas(airports, width = 600, height = 600, bg='black')
        canvas.pack()
        airports.title('Enter Airport Details')
        my_image = PhotoImage(file='Airport.png')
        canvas.create_image(300, 299,image=my_image)
        airports.resizable(False, False)
        UKairportLabel = Label(airports, text='Please enter the three letter code for your UK airport').place(x=200, y=100 )
        UKairportEntry = Entry(airports)
        UKairportEntry.place(x=270,y=150)
        OverseasAirportLabel = Label(airports, text='Please enter the three letter code for your Overseas airport').place(x=190,y=250 )
        OverseasAirportEntry = Entry(airports)
        OverseasAirportEntry.place(x=270,y=300)
        submitAirportButton = Button(airports, text='submit',command=confirmation).place(x=300, y=400)
        mainloop()

def aircraftDetails():
    def confirmation():
        global aircraftEntered
        global FirstClass
        global standardClassSeats
        global aircraftSubmitFlag
        FirstClass = str(firstEntry.get())
        try:
            FirstClass = int(FirstClass)
            message = ''
            if FirstClass < 0:
                message="There cannot be a negative number of first class seats"
            elif FirstClass <=minFirstclass:
                message = ('The amount of first class seats must be more than ',str(minFirstclass))
            elif FirstClass > (capacity/2):
                message ='The number of first class seats must be less than half the capacity'
            else:
                standardClassSeats = capacity - (FirstClass*2)
                message = ''
                message2 = ('The number of standard class seats are', str(standardClassSeats))
                label5=Label(aircrafts,text=message2,bg='green').place(x=220,y=290)
                if aircraftSubmitFlag == False:
                    backToMenu = Button(aircrafts,text='return to main menu',command=mainMenu).pack()
                    aircraftSubmitFlag = True
                aircraftEntered = True
            errorLabel=Label(aircrafts)
            errorLabel.destroy()
            errorLabel=Label(aircrafts,text=message,bg='red')
            errorLabel.place(x=240,y=290)
            
                
        except:
            errorLabel=Label(aircrafts)
            errorLabel.destroy()
            errorLabel = Label(aircrafts,text="Please enter a number",bg='red')
            errorLabel.place(x=240,y=290)
                        
    def NextStage():
        global firstEntry
        Label2=Label(aircrafts,text="Enter in Aircraft details").place(x=240, y=150)
        Label3=Label(aircrafts,text="Enter the number of first class seats").place(x=210,y=200)
        firstEntry=Entry(aircrafts)
        firstEntry.place(x=240,y=250)
        confirmbutton=Button(aircrafts,text="confirm",command=confirmation).pack()

        
    def choice1 ():
        global aircraftChoice
        global runningCost
        global flightRange
        global capacity
        global minFirstclass
        aircraftChoice = 'Medium Narrow Body'
        runningCost = 8
        flightRange = 2650
        capacity = 180
        minFirstclass = 8
        if flightRange < distance:
            tkinter.messagebox.showinfo(title="Error message", message="The aircraft you have chosen can not travel the distance")
        else:
            NextStage()
                    
    def choice2 ():
        global aircraftChoice
        global runningCost
        global flightRange
        global capacity
        global minFirstclass
        aircraftChoice = 'Large Narrow Body'
        runningCost = 7
        flightRange = 5600
        capacity = 220
        minFirstclass = 10
        if flightRange < distance:
            tkinter.messagebox.showinfo(title="Error message", message="The aircraft you have chosen can not travel the distance")
        else:
            NextStage()  
    def choice3():
        global aircraftChoice
        global runningCost
        global flightRange
        global capacity
        global minFirstclass
        aircraftChoice = 'Medium Wide Body'
        runningCost = 5
        flightRange = 4050
        capacity = 406
        minFirstclass = 14
        if flightRange < distance:
            tkinter.messagebox.showinfo(title="Error message", message="The aircraft you have chosen can not travel the distance")
        else:
            NextStage()

    global aircraftChoice
    global runningCost
    global flightRange
    global capacity
    global minFirstclass
    global standardClassSeats
    global Firstclass
    global aircrafts
    global aircraftsEntered
                    
    if airportsEntered == True:
        if aircraftEntered == True:
            tkinter.messagebox.showinfo(title="Error Message",message="You have already entered the aircraft details, please clear the data if you want to re-enter values")
        else:
            menu.destroy()
            aircrafts = Tk()
            aircrafts.title('Enter aircraft details')
            myimage = PhotoImage(file='aircrafts.png')
            canvas = Canvas(aircrafts, width = 600, height = 600)
            myimage = myimage.zoom(2, 2)
            canvas.create_image(300,300,image=myimage)
            canvas.pack()
            aircrafts.resizable(False, False)
            label =Label(aircrafts,text="Select the aircraft you want").place(x=240,y=10)
            button1=Button(aircrafts,text='Medium Narrow Body',command=choice1).place(x=50,y=50)
            button2=Button(aircrafts,text='Large Narrow Body',command=choice2).place(x=260,y=50)
            button3=Button(aircrafts,text='Medium Wide Body',command=choice3).place(x=450,y=50)
            mainloop()
        
    else:
        tkinter.messagebox.showinfo(title="Error Message", message="Please enter your airports before choosing an aircraft")
        mainloop()
    

def pricePlan():
    def calculate ():
        global profitSubmitFlag 
        try:
            firstclassPrice = int(firstclassentry.get())
            standardclassPrice = int(standardclassentry.get())
            flightCostPerSeat = (runningCost*distance)/100
            flightCost = flightCostPerSeat*(FirstClass + standardClassSeats)
            flightIncome = (FirstClass*firstclassPrice) + (standardClassSeats*standardclassPrice)
            flightProfit = flightIncome - flightCost
            message = '\n Flight cost per seat = £', str(flightCostPerSeat), '\n Flight cost = £', str(flightCost), '\n Flight income = £', str(flightIncome), '\n Flight proft = £', str(round(flightProfit,2))
            Profitoutcome = Label(priceplan,text=message).place(x=240,y=300)
            if profitSubmitFlag == False:
                backToMenu = Button(priceplan,text="Return to menu",command=mainMenu)
                profitSubmitFlag = True
            backToMenu.pack()
        except:
            tkinter.messagebox.showinfo(title="Error message",message="Please enter a number")
        #mainloop()
        
    global firstclassentry
    global standardclassentry
    global priceplan
    
    if aircraftEntered == False or airportsEntered == False:
        tkinter.messagebox.showinfo(title="Error Message",message="Please enter the aircraft AND airport details before claculating the price plan")
        #mainloop()
    else:
        menu.destroy()
        priceplan = Tk()

        canvas = Canvas(priceplan, width = 600, height = 600, bg='light blue').pack()
        priceplan.title('Profits and Price Plan Calculator')
        priceplan.resizable(False, False)
        
        label = Label(priceplan,text="Calculating Profits").place(x=240,y=10)
        label2 = Label(priceplan,text="What is the price of a standard class seat?").place(x=240,y=50)
        standardclassentry = Entry(priceplan)
        standardclassentry.place(x=270, y=70)
        label3 = Label(priceplan,text='What is the price of a first class seat?').place(x=240,y=100)
        firstclassentry = Entry(priceplan)
        firstclassentry.place(x=270,y=120)
        calculateProfit = Button(priceplan,text="Calculate Profit",command=calculate).place(x=300,y=150)
        #mainloop()
    mainloop()

        

def clear():
    global airportsEntered 
    global aircraftEntered 
    global choice 
    global UKairport 
    global OverseasAirport 
    global airportList 
    global fullAirportList 
    global distanceFromLPL 
    global distanceFromBOH 
    global search 
    global aircraftChoice 
    global runningCost 
    global flightRange 
    global capacity 
    global minFirstclass
    global Firstclass 
    global standardClassSeats 
    global validation 
    global standardclassPrice 
    global firstclassPrice 
    global flightCostPerSeat 
    global flightCost 
    global flightIncome 
    global flightProfit 

    airportsEntered = False
    aircraftEntered = False
    choice = 0
    UKairport = ''
    OverseasAirport = ''
    airportList = []
    fullAirportList = []
    distanceFromLPL = []
    distanceFromBOH = []
    search = False
    aircraftChoice = 0
    runningCost = 0
    flightRange = 0
    capacity = 0
    minFirstclass = 0
    Firstclass = 0
    standardClassSeats = 0
    validation = False
    standardclassPrice = 0
    firstclassPrice = 0
    flightCostPerSeat = 0
    flightCost = 0
    flightIncome = 0
    flightProfit = 0
    tkinter.messagebox.showinfo(title="Message",message="All data has been cleared")
    
mainMenu()


