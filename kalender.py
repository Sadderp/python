from tkinter import *
import tkinter
from tkinter.ttk import *
from tkcalendar import *
import datetime

#Kollar dagens datum och sätter kalendern till det när den öppnas
today = datetime.date.today()
 
# skapar ett fönster
window = Tk()
 
# sätter storleken på fönstret
window.geometry("500x700")

# ändrar titeln på fönstret
window.title("Kalender v0.1")

inp=""

# skapar kalendern och sätter startdatumet
cal = Calendar(window, selectmode="day", year=today.year, month=today.month, day=today.day)
cal.pack(fill="both", expand=True)

Text = tkinter.Canvas(window, width = 500, height = 700)

#öppnar det andra förnstret
def handelse():

    # skapar ett nytt fönster med titel och dimensioner
    NewWindow = Toplevel(window)
    NewWindow.title("Nytt fönster")
    NewWindow.geometry("200x200")

    # text för händelseruta
    NewLabel = Label(NewWindow, text="Händelse: ")
    NewLabel.pack()

    #Hanterar texten som skrivs i händelserutan
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        
        lbl = Label(NewWindow, text = "")
        lbl.pack()
        with open("event.txt", "a+") as file_object:
            data = file_object.read(10000)
            file_object.write("\n" + "Date: " + cal.get_date() + " event: " + inp)           #Lägger till texten till slutet av filen
        NewWindow.destroy()
    #gör textruta att skriva händelser i
    inputtxt = tkinter.Text(NewWindow, height = 4, width = 20)
    inputtxt.pack()

    #Knapp att klicka på
    myButton = Button(NewWindow, text = "Lägg till händelse", command = printInput)
    myButton.pack()

my_button = Button(window, text = "Lägg till händelse", command = handelse)
my_button.pack(pady = 20)

#skapar och visar listan med händelser
def buttonClick():
    with open("event.txt") as f:
        for line in f:
            lines = f.readlines()[0:]
            datumLabel.config(text = ' '.join(lines))

datumknapp = Button(window, text = "Visa händelser", command = buttonClick)
datumknapp.pack(pady = 10)

datumLabel = Label(window, text = "")
datumLabel.pack(pady = 20)

# mainloop, runs infinitely
window.mainloop()