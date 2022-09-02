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
window.geometry("500x500")

# ändrar titeln på fönstret
window.title("Kalender v0.01")

# skapar kalendern och sätter startdatumet
cal = Calendar(window, selectmode="day", year=today.year, month=today.month, day=today.day)
cal.pack(pady=20, fill="both", expand=True)

Text = tkinter.Canvas(window, width = 430, height = 330)

def grab_date():
    my_label.config(text= "Dagens datum är: "+cal.get_date())

    # skapar ett nytt fönster med titel och dimensioner
    NewWindow = Toplevel(window)
    NewWindow.title("Nytt fönster")
    NewWindow.geometry("200x300")

    # text för händelseruta
    NewLabel = Label(NewWindow, text="Vad vill du skriva?")
    NewLabel.pack()

    #Ruta att skriva i
    e = Entry(NewWindow)
    e.pack()

    #Vad som händer när man klickar på knappen
    def myClick():
        myLabel = Label(NewWindow, text="Den funkade!!!")
        myLabel.pack()

    #Knapp att klicka på
    myButton = Button(NewWindow, text="Klicka här", command=myClick)
    myButton.pack()

my_button = Button(window, text = "Get Date", command = grab_date)
my_button.pack(pady = 20)

my_label = Label(window, text = "")
my_label.pack(pady = 20)

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