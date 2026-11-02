from tkinter import *
import sqlite3
connection = sqlite3.connect("loginInfo.db")
cursor = connection.cursor()
#window initialised
global window
window = Tk()


global orderTotal
orderTotal=0


global openMenus
openMenus=[]


global isBlack
isBlack=False


def clearMenus():
    global openMenus
    global menuBox

    if len(openMenus)>0:
        for widget in menuBox.winfo_children():
            widget.destroy()
        openMenus.clear()

 
def checkout():
    global menuBox
    global openMenus

    clearMenus()
    openMenus.append(1)

    tip=0
    tipLabel= Label(menuBox, text="Would you like to give a tip?")
    tipLabel.grid(row=0, column=0)

    yesTipButton = Button(menuBox, text="Yes",command=lambda:yesTip())
    yesTipButton.grid(row=1, column=1)

    noTipButton = Button(menuBox, text="No",command=lambda:noTip())
    noTipButton.grid(row=1, column=2)


def yesTip():
    global openMenus
    global menuBox
    global orderTotal
    global tipEntry

    clearMenus()
    openMenus.append(1)

    tipEntryLabel=Label(menuBox,text="How much would you like to tip?")
    tipEntryLabel.grid(row=0,column=0)

    tipEntry=Entry(menuBox)
    tipEntry.grid(row=1,column=1)

    confirmTipButton=Button(menuBox,text="Confirm tip",command=lambda:[getTip(), noTip()])
    confirmTipButton.grid(row=2, column=1)


def getTip():
    global tipEntry
    global total
    global orderTotal
    try:
        tipAmount=float(tipEntry.get())
        orderTotal = round(orderTotal+tipAmount,3)
    except ValueError:
        invalidLabel=Label(menuBox,text="Please try again using a number")
        invalidLabel.grid(row=3,column=1)
        

def noTip():
    global openMenus
    global menuBox
    global orderTotal

    clearMenus()
    openMenus.append(1)

    endPrice=Label(menuBox,text="Your final price is £" + str(orderTotal))
    endPrice.grid(row=0,column=0)

    continueLabel=Label(menuBox,text="Do you wish to finish? (The app will close)")
    continueLabel.grid(row=1,column=0)

    finishButton=Button(menuBox,text="Yes",command=lambda:endOrder())
    finishButton.grid(row=4, column=0)

    doNotFinishButton=Button(menuBox,text="No",command=lambda:clearMenus())
    doNotFinishButton.grid(row=4, column=1)

    

def menu():
    global menuBox
    menuBox = Frame(screen2, borderwidth=3, relief="solid", bg="white", width=510, height=600, highlightbackground="black")
    menuBox.pack_propagate(FALSE)
    menuBox.grid_propagate(FALSE)
    menuBox.place(anchor="n",relx=0.505)


def cart():
    global cartBox
    global total
    global orderTotal
    cartBox = Frame(screen2, borderwidth=3, relief="solid", bg="white", width=200, height=600)
    cartBox.place(relx=1, anchor="ne")
    cartBox.pack_propagate(FALSE)

    total = Label(cartBox, text=("Total: £" + str(orderTotal)))
    total.pack(side = BOTTOM)

    checkoutButton = Button(cartBox, text="Checkout", command=lambda:checkout())
    checkoutButton.pack(side = BOTTOM)


def homeScreen():
    global screen2
    screen2 = Tk()
    screen2.geometry("700x600")
    screen2.title('Bell Point of Sale')

    whiteButton = Button(screen2, text="Light Mode", command=lambda: configBackgColourWhite())
    whiteButton.grid(row=46, columnspan=100, column=150)
    whiteButton.config(width=12, height=2)

    blackButton = Button(screen2, text="Dark Mode", command=lambda: configBackgColourBlack())
    blackButton.grid(row=54, columnspan=100,column=150)
    blackButton.config(width=12, height=2)

    breakfastButton = Button(screen2, text="Breakfast Menu", command=lambda: breakfast())
    breakfastButton.grid(row= 6, columnspan=100, column=150)
    breakfastButton.config(width= 12, height=2)

    lunchButton = Button(screen2, text="Lunch Menu", command=lambda: lunch())
    lunchButton.grid(row=14, columnspan=100, column=150)
    lunchButton.config(width=12, height=2)

    dinnerButton = Button(screen2, text="Dinner Menu", command=lambda: dinner())
    dinnerButton.grid(row=22, columnspan=100, column=150)
    dinnerButton.config(width=12, height=2)

    drinksButton = Button(screen2, text="Drinks",command=lambda:drinks())
    drinksButton.grid(row=30, columnspan=100, column=150)
    drinksButton.config(width= 12, height=2)

    dessertsButton =Button(screen2, text="Desserts",command=lambda:desserts())
    dessertsButton.grid(row=38, columnspan=100, column=150)
    dessertsButton.config(width=12, height=2)

    menu()

    cart()

    screen2.mainloop()


def configBackgColourWhite():
    cartBox.config(bg="white")
    screen2.configure(bg="white")
    menuBox.configure(bg="white")
    menuBox.configure(bg="white",highlightbackground="black",highlightthickness=1)
    cartBox.configure(bg="white",highlightbackground="black",highlightthickness=1)

    for widget in screen2.winfo_children():
        widget.configure(bg="white",fg="black")

    for widget in menuBox.winfo_children():
        widget.configure(bg="white",fg="black")
        
    for widget in cartBox.winfo_children():
        widget.configure(bg="white",fg="black")
        
    #global isBlack
    #isBlack=False


def configBackgColourBlack():
    cartBox.config(bg="black")
    screen2.configure(bg="black")
    menuBox.configure(bg="black",highlightbackground="white",highlightthickness=1)
    cartBox.configure(bg="black",highlightbackground="white",highlightthickness=1)
    
    for widget in screen2.winfo_children():
        widget.configure(bg="black",fg="white")
        
    for widget in menuBox.winfo_children():
        widget.configure(bg="black",fg="white")
        
    for widget in cartBox.winfo_children():
        widget.configure(bg="black",fg="white")
        
    #global isBlack
    #isBlack=True

    
def lunch():
    global openMenus

    clearMenus()
    openMenus.append(1)

    hamButton = Button(menuBox, text="Ham Sandwich", command=lambda:hamSandy())
    hamButton.grid(row=0, column=0, columnspan=2)
    hamButton.config(height=5, width=15, font=10)

    cheeseButton = Button(menuBox, text="Cheese Sandwich", command=lambda: cheeseSandy())
    cheeseButton.grid(row=1, column=0, columnspan=2)
    cheeseButton.config(height=5, width=15, font=10)



def hamSandy():
    global orderTotal
    global total
    global cartBox
    hamSandyPrice = 3.00
    orderTotal = orderTotal + hamSandyPrice
    orderTotal = round(orderTotal,3)
    total.config(text=("Total: £" + str(orderTotal)))
    hamSandyLabel = Label(cartBox, text="Ham sandwich")
    hamSandyLabel.pack(side="top")

    global isBlack
    if isBlack:
        hamSandyLabel.configure(bg="black",fg="white")

    
def cheeseSandy():
    global orderTotal
    global total
    global cartBox
    cheeseSandyPrice = 3.00
    orderTotal = orderTotal + cheeseSandyPrice
    orderTotal = round(orderTotal,3)
    total.config(text=("Total: £" + str(orderTotal)))
    cheeseSandyLabel = Label(cartBox, text="Cheese sandwich")
    cheeseSandyLabel.pack(side="top")

    global isBlack
    if isBlack:
        cheeseSandyLabel.configure(bg="black",fg="white")


def hashBrown():
    global orderTotal
    global total
    global cartBox
    hashBrownPrice = 0.20
    orderTotal = orderTotal + hashBrownPrice
    orderTotal = round(orderTotal,3)
    total.config(text=("Total: £" + str(orderTotal)))
    hashBrownLabel = Label(cartBox, text="Hashbrown")
    hashBrownLabel.pack(side="top")

    global isBlack
    if isBlack:
        hashBrownLabel.configure(bg="black",fg="white")

def sausageBap():
    global orderTotal
    global total
    global cartBox
    sausageBapPrice = 1.20
    orderTotal = orderTotal + sausageBapPrice
    orderTotal = round(orderTotal,3)
    total.config(text=("Total: £" + str(orderTotal)))
    sausageBapLabel=Label(cartBox, text="Sausage Bap")
    sausageBapLabel.pack(side="top")

    global isBlack
    if isBlack:
        sausageBapLabel.configure(bg="black",fg="white")


def baconRoll():
    global orderTotal
    global total
    global cartBox
    baconRollPrice = 1.20
    orderTotal = orderTotal + baconRollPrice
    orderTotal = round(orderTotal,3)
    total.config(text=("Total: £" + str(orderTotal)))
    baconRollLabel=Label(cartBox, text="Bacon Roll")
    baconRollLabel.pack(side="top")

    global isBlack
    if isBlack:
        baconRollLabel.configure(bg="black",fg="white")


def breakfast():
    global total
    global breakfasts
    global orderTotal
    global menuBox
    global openMenus

    clearMenus()
    openMenus.append(1)

    baconRollButton = Button(menuBox, text="Bacon Roll", command=lambda: baconRoll())
    baconRollButton.grid(row=0, column=0, columnspan=2)
    baconRollButton.config(height=5, width=15, font=10)

    hashBrownButton = Button(menuBox, text="Hash Brown", command=lambda: hashBrown())
    hashBrownButton.grid(row=1, column=0, columnspan=2)
    hashBrownButton.config(height=5, width=15, font=10)

    sausageBapButton = Button(menuBox, text="Sausage Bap", command=lambda: sausageBap())
    sausageBapButton.grid(row=2, column=0, columnspan=2)
    sausageBapButton.config(height=5, width=15, font=10)


    menuBox.pack_propagate(FALSE)


def dinner():
    global openMenus

    clearMenus()
    openMenus.append(1)

    comingSoonLabel=Label(menuBox,text="Dinners coming soon!",font=10)
    comingSoonLabel.grid(row=0,column=0)

    global isBlack
    if isBlack:
        comingSoonLabel.configure(bg="black",fg="white")



def desserts():
    global openMenus

    clearMenus()
    openMenus.append(1)

    comingSoonLabel=Label(menuBox,text="Desserts coming soon!",font=10)
    comingSoonLabel.grid(row=0,column=0)

    global isBlack
    if isBlack:
        comingSoonLabel.configure(bg="black",fg="white")


def drinks():
    global openMenus

    clearMenus()
    openMenus.append(1)

    comingSoonLabel=Label(menuBox,text="Drinks coming soon!",font=10)
    comingSoonLabel.grid(row=0,column=0)

    global isBlack
    if isBlack:
        comingSoonLabel.configure(bg="black",fg="white")



def clearScreen():
    login.destroy()
    usernameLabel.destroy()
    usernameEntry.destroy()
    passwordLabel.destroy()
    passwordEntry.destroy()
    loginButton.destroy()



def loginAttempt():
    global usernameEntry
    global passwordEntry
    username = usernameEntry.get()
    password = passwordEntry.get()
    
    # check if the username/password pair exists
    cursor.execute("SELECT * FROM logins WHERE usernames=? AND passwords=?", (username, password))
    result = cursor.fetchone()

    if result:
        clearScreen()
        welcomeLabel = Label(window,text="WELCOME", font=("Arial", 20))
        welcomeLabel.grid(row=4, column=0, columnspan=3)
        welcomeLabel.after(2000, lambda: welcomeLabel.destroy())
        window.after(2000, lambda: homeScreen())
        window.after(2000, lambda: window.destroy())

    else:
        invalidLabel = Label(window, text="Invalid Login")
        invalidLabel.grid(row=5, column=0,columnspan=2)
        invalidLabel.after(2000, invalidLabel.destroy)


def newAccount():
    global userSetup
    userSetup = Tk()
    userSetup.title("User Setup")
    userSetup.geometry("200x110")
    userSetupTitle = Label(userSetup,text="Create Account")
    newUsernameLabel = Label(userSetup, text="Username")
    global newUsernameEntry
    newUsernameEntry = Entry(userSetup)
    newPasswordLabel = Label(userSetup,text="Password")
    global newPasswordEntry
    newPasswordEntry = Entry(userSetup)
    saveDetailsButton = Button(userSetup, text="Save Details", command=saveDetails)
    
    userSetupTitle.grid(row=0, column=0, columnspan=2)
    newUsernameLabel.grid(row=1, column=0)
    newUsernameEntry.grid(row=1, column=1)
    newPasswordLabel.grid(row=2, column=0)
    newPasswordEntry.grid(row=2, column=1)
    saveDetailsButton.grid(row=3, column=0, columnspan=2)

    userSetup.mainloop()


def saveDetails():
    global newUsernameEntry
    global newPasswordEntry
    global userSetup
    newUser = newUsernameEntry.get()
    newPassword = newPasswordEntry.get()

    cursor.execute("INSERT INTO logins VALUES (?,?)",(newUser,newPassword))
    userCreated=Label(userSetup, text="User Created").grid(row=4, column=0, columnspan=2)
    userSetup.after(2000, lambda:userSetup.destroy())

    connection.commit()


def endOrder():
    clearMenus()
    
    thankYouLabel = Label(menuBox, text="Thank you for your order!",font=10)
    thankYouLabel.grid(row=0, column=0)
    screen2.after(2000, lambda:screen2.destroy())




window.title("Login")
window.geometry("200x135")
#window.configure(background="black")
#adding widgets
login = Label(window, text="Login Page")
usernameLabel = Label(window, text="Username")
usernameEntry = Entry(window)
passwordLabel = Label(window,text="Password")
passwordEntry = Entry(window, show="*")
loginButton = Button(window, text="Login", command=loginAttempt)
newUserButton= Button(window, text="Create Account",command=newAccount)
#placing widgets
login.grid(row=0, column=0, columnspan=2)
usernameLabel.grid(row=1, column=0)
usernameEntry.grid(row=1, column=1)
passwordLabel.grid(row=2, column=0)
passwordEntry.grid(row=2, column=1)
loginButton.grid(row=3, column=0, columnspan=2)
newUserButton.grid(row=4,column=0,columnspan=2)

#run the window
window.mainloop()

connection.close()
