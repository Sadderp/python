from tkinter import *
from tkinter.ttk import *
import calendar
import babel.numbers
from tkcalendar import *

c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2025,1)
#print(str)
 
# skapar ett fönster
window = Tk()
 
# sätter storleken på fönstret
window.geometry("500x500")

# ändrar titeln på fönstret
window.title("Kalender v0.01")

# skapar kalendern och sätter startdatumet
cal = Calendar(window, selectmode="day", year=2022, month=8, day=31)
cal.pack(pady=20, fill="both", expand=True)

def grab_date():
    my_label.config(text= "Dagens datum är: "+cal.get_date())

    # skapar ett nytt fönster med titel och dimensioner
    NewWindow = Toplevel(window)
    NewWindow.title("Nytt fönster")
    NewWindow.geometry("200x300")

    #Ruta att skriva i
    e = Entry(NewWindow, width=50, background="Blue")
    e.pack
    e.get()

    #Vad som händer när man kickar på knappen
    def myClick():
        myLabel = Label(NewWindow, text="Den funkade!!!")
        myLabel.pack()

    #Knapp att klicka på
    myButton = Button(NewWindow, text="Kicka här", command=myClick)
    myButton.pack()

my_button = Button(window, text = "Get Date", command = grab_date)
my_button.pack(pady = 20)

my_label = Label(window, text = "")
my_label.pack(pady = 20)

# mainloop, runs infinitely
window.mainloop()