from tkinter import *
import tkinter
from tkinter.ttk import *
from tkcalendar import *
import datetime
import mysql.connector

#Kollar dagens datum och sätter kalendern till det när den öppnas
today = datetime.date.today()
 
# skapar ett fönster
window = Tk()
 
# sätter storleken på fönstret
window.geometry("500x700")

# ändrar titeln på fönstret
window.title("Kalender v0.01")

inp=""

# skapar kalendern och sätter startdatumet
cal = Calendar(window, selectmode="day", year=today.year, month=today.month, day=today.day)
cal.pack(pady=20, fill="both", expand=True)

Text = tkinter.Canvas(window, width = 500, height = 700)

def grab_date():
    my_label.config(text= "Dagens datum är: "+cal.get_date())

    # skapar ett nytt fönster med titel och dimensioner
    NewWindow = Toplevel(window)
    NewWindow.title("Nytt fönster")
    NewWindow.geometry("200x300")

    # text för händelseruta
    NewLabel = Label(NewWindow, text="Händelse: ")
    NewLabel.pack()

    #Vad som händer när man klickar på knappen
    def myClick():
        myLabel = Label(NewWindow, text="Den funkade!!!")
        myLabel.pack()

    def printInput():
        global inp 
        inp = inputtxt.get(1.0, "end-1c")

        lbl = Label(NewWindow, text = "")
        lbl.pack()
        with open("event.txt", "a+") as file_object:
            data = file_object.read(10000)
            # Append text at the end of file
            file_object.write("\n" + "Time: " + cal.get_date() + " event: " + inp)
    # TextBox Creation
    inputtxt = tkinter.Text(NewWindow, height = 5, width = 20)
    inputtxt.pack()

    #Knapp att klicka på
    myButton = Button(NewWindow, text = "Print", command = printInput)
    myButton.pack()

my_button = Button(window, text = "Get Date", command = grab_date)
my_button.pack(pady = 20)

def buttonClick():
    print("test")
    with open("event.txt") as f:
        next(f)
        for line in f:
            #do something
            lines = f.readline()
            datumLabel.config(text = lines)


my_label = Label(window, text = "")
my_label.pack(pady = 20)

datumknapp = Button(window, text = "Visa händelser", command = buttonClick)
datumknapp.pack(pady = 20)

datumLabel = Label(window, text = "")
datumLabel.pack()

"""events={'2022-09-28':('London','meeting'),\
    '2022-08-15':('Paris','meeting'),\
    '2022-07-30':('New York','meeting')}


class MyCalendar(Calendar):

    def _next_month(self):
        Calendar._next_month(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _prev_month(self):
        Calendar._prev_month(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _next_year(self):
        Calendar._next_year(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _prev_year(self):
        Calendar._prev_year(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def get_displayed_month_year(self):
        return self.date.month, self.date.year


def on_change_month(event):
    # remove previously displayed events
    cal.calevent_remove('all')
    year, month = cal.get_displayed_month_year()
    # display the current month events 
    print(year, month)

cal.bind('<<CalendarMonthChanged>>', on_change_month)"""

# mainloop, runs infinitely
window.mainloop()